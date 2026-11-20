/**
 * GEOMETOR ETC — Unified Single-Stage Graphic Viewer & Euclid/Elements Two-Way Hover Engine
 *
 * Replaces 4–8 duplicate per-SVG inline scripts with one cached controller:
 *  - Strictly 1 active <svg> in the DOM (zero duplicate IDs, zero multi-controller overhead)
 *  - Analytical Liang-Barsky slab clipping of infinite <line> endpoints to 2.2x active viewBox
 *    (eliminates ~165k-1.6M dashed-line Bezier cap tessellations per line!)
 *  - rAF-coalesced pan/zoom/resize with cached canvas geometry (zero mousemove layout thrashing)
 *  - Lazy fetch() + in-memory cache for secondary modes and reference triangles
 *  - Euclid/Elements-style O(1) canonical bidirectional Text <-> SVG Gold hover + table row sync
 *  - Cached MathJax v4 HUD rendering (with instant zero-dependency fallback)
 */
(function (window, document) {
  'use strict';

  const VIEW_CACHE = new Map();       // url -> { svgElHTML, meta }
  const MATH_HTML_CACHE = new Map();  // latex -> HTML string (rendered via MathJax.tex2chtml)

  function escapeHtml(str) {
    return String(str || '')
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;');
  }

  function formatIdHtml(idStr) {
    const s = escapeHtml(idStr);
    return s
      .replace(/_\{([^}]+)\}/g, '<sub>$1</sub>')
      .replace(/_([A-Za-z0-9']+)/g, '<sub>$1</sub>');
  }

  function extractBraced(src, startIdx) {
    if (src[startIdx] !== '{') return null;
    let depth = 0;
    for (let i = startIdx; i < src.length; i++) {
      if (src[i] === '{') depth++;
      else if (src[i] === '}') {
        depth--;
        if (depth === 0) {
          return { content: src.slice(startIdx + 1, i), next: i + 1 };
        }
      }
    }
    return null;
  }

  function convertLatexFallback(tex) {
    let s = String(tex || '');
    s = s.replace(/\\left\s*([(\[{|])/g, '$1').replace(/\\right\s*([)\]}|])/g, '$1');
    s = s.replace(/\\;/g, ' ').replace(/\\,/g, '\u2009').replace(/\\quad/g, '  ');
    s = s
      .replace(/\\varphi|\\phi/g, 'φ')
      .replace(/\\Delta/g, 'Δ')
      .replace(/\\alpha/g, 'α')
      .replace(/\\beta/g, 'β')
      .replace(/\\gamma/g, 'γ')
      .replace(/\\cdot/g, '·')
      .replace(/\\approx/g, '≈')
      .replace(/\\infty/g, '∞');

    let out = '';
    let i = 0;
    while (i < s.length) {
      if (s.startsWith('\\frac', i)) {
        let k = i + 5;
        while (k < s.length && s[k] === ' ') k++;
        const numB = extractBraced(s, k);
        if (numB) {
          let k2 = numB.next;
          while (k2 < s.length && s[k2] === ' ') k2++;
          const denB = extractBraced(s, k2);
          if (denB) {
            out +=
              '<span class="etc-math-frac"><span class="etc-math-num">' +
              convertLatexFallback(numB.content) +
              '</span><span class="etc-math-den">' +
              convertLatexFallback(denB.content) +
              '</span></span>';
            i = denB.next;
            continue;
          }
        }
      }
      if (s.startsWith('\\sqrt', i)) {
        let k = i + 5;
        while (k < s.length && s[k] === ' ') k++;
        const radB = extractBraced(s, k);
        if (radB) {
          out += '√<span class="etc-math-rad">' + convertLatexFallback(radB.content) + '</span>';
          i = radB.next;
          continue;
        }
      }
      if ((s[i] === '_' || s[i] === '^') && i + 1 < s.length) {
        const tag = s[i] === '_' ? 'sub' : 'sup';
        if (s[i + 1] === '{') {
          const subB = extractBraced(s, i + 1);
          if (subB) {
            out += `<${tag}>` + convertLatexFallback(subB.content) + `</${tag}>`;
            i = subB.next;
            continue;
          }
        } else {
          out += `<${tag}>` + escapeHtml(s[i + 1]) + `</${tag}>`;
          i += 2;
          continue;
        }
      }
      out += escapeHtml(s[i]);
      i++;
    }
    return out;
  }

  function renderMathHtml(latexStr, prettyStr) {
    if (!latexStr) return escapeHtml(prettyStr || '');
    if (MATH_HTML_CACHE.has(latexStr)) {
      return MATH_HTML_CACHE.get(latexStr);
    }
    if (window.MathJax && typeof window.MathJax.tex2chtml === 'function') {
      try {
        const node = window.MathJax.tex2chtml(latexStr, { display: false });
        if (node && node.outerHTML) {
          MATH_HTML_CACHE.set(latexStr, node.outerHTML);
          return node.outerHTML;
        }
      } catch (e) {}
    }
    return '<span class="etc-math-fallback">' + convertLatexFallback(latexStr) + '</span>';
  }

  /**
   * Canonicalize any GEOMETOR reference string into one or more normalized keys
   * so Text <-> SVG matching succeeds regardless of vertex order or notation.
   */
  function canonicalKeys(rawRef) {
    if (!rawRef) return [];
    const keys = new Set();
    const parts = String(rawRef)
      .split(';')
      .map((s) => s.trim())
      .filter(Boolean);

    parts.forEach((raw) => {
      const clean = raw.includes(':') ? raw.split(':').pop().trim() : raw;
      if (!clean) return;
      keys.add(clean);

      // Line [ A B ] or Segment / A B /
      const lineOrSeg = clean.match(/^([\[/])\s*(\S+)\s+(\S+)\s*([\]/])$/);
      if (lineOrSeg) {
        const a = lineOrSeg[2];
        const b = lineOrSeg[3];
        const pair = [a, b].sort().join('|');
        keys.add(`edge:${pair}`);
        keys.add(`[ ${a} ${b} ]`);
        keys.add(`[ ${b} ${a} ]`);
        keys.add(`/ ${a} ${b} /`);
        keys.add(`/ ${b} ${a} /`);
        return;
      }

      // Central line index set: { 2, 8 } or { 1, 2, 8, 10 }
      const braceM = clean.match(/^\{\s*([\d,\s]+)\s*\}$/);
      if (braceM) {
        const nums = Array.from(
          new Set(
            braceM[1]
              .split(',')
              .map((s) => s.trim())
              .filter(Boolean)
          )
        ).sort((a, b) => Number(a) - Number(b));
        if (nums.length >= 2) {
          keys.add(`cl:${nums.join(',')}`);
          // Emit pairwise keys so { 2, 8 } matches { 1, 2, 8, 10 } in BOTH directions
          for (let i = 0; i < nums.length; i++) {
            for (let j = i + 1; j < nums.length; j++) {
              keys.add(`clpair:${nums[i]},${nums[j]}`);
            }
          }
        }
        return;
      }

      // Triangle / Polygon < A B C >
      const polyM = clean.match(/^<\s*([^>]+?)\s*>$/);
      if (polyM) {
        const verts = polyM[1].trim().split(/[\s,]+/).filter(Boolean);
        if (verts.length >= 3) {
          keys.add(`poly:${[...verts].sort().join('|')}`);
        }
        return;
      }

      // Center shorthand X(n) or X_n
      const xm = clean.match(/^X(?:_|\()(\d+)\)?$/);
      if (xm) {
        keys.add(`X_${xm[1]}`);
      }
    });

    return Array.from(keys);
  }

  /**
   * Extract constituent point IDs from a canonical element ID (for secondary point/label highlighting).
   */
  function inferRelatedPoints(id, info) {
    if (info && Array.isArray(info.related_points) && info.related_points.length > 0) {
      return info.related_points;
    }
    if (!id) return [];
    const sm = id.match(/^[\[/]\s*(\S+)\s+(\S+)\s*[\]/]$/);
    if (sm) return [sm[1], sm[2]];
    const tm = id.match(/^<\s*([^>]+?)\s*>$/);
    if (tm) return tm[1].trim().split(/[\s,]+/).filter(Boolean);
    const bm = id.match(/^\{\s*([\d,\s]+)\s*\}$/);
    if (bm) {
      return bm[1]
        .split(',')
        .map((s) => s.trim())
        .filter(Boolean)
        .map((n) => `X_${n}`);
    }
    return [id];
  }

  /**
   * Analytical Liang-Barsky intersection of infinite line P(t) = (x0, y0) + t*(ux, uy)
   * with axis-aligned rectangle [xmin, xmax] x [ymin, ymax].
   */
  function clipInfiniteLineToBox(x0, y0, ux, uy, xmin, ymin, xmax, ymax) {
    let tMin = -Infinity;
    let tMax = Infinity;
    const eps = 1e-12;

    if (Math.abs(ux) < eps) {
      if (x0 < xmin || x0 > xmax) return null;
    } else {
      let t1 = (xmin - x0) / ux;
      let t2 = (xmax - x0) / ux;
      if (t1 > t2) [t1, t2] = [t2, t1];
      tMin = Math.max(tMin, t1);
      tMax = Math.min(tMax, t2);
    }

    if (Math.abs(uy) < eps) {
      if (y0 < ymin || y0 > ymax) return null;
    } else {
      let t1 = (ymin - y0) / uy;
      let t2 = (ymax - y0) / uy;
      if (t1 > t2) [t1, t2] = [t2, t1];
      tMin = Math.max(tMin, t1);
      tMax = Math.min(tMax, t2);
    }

    if (tMin > tMax || !Number.isFinite(tMin) || !Number.isFinite(tMax)) {
      return null;
    }
    return [x0 + tMin * ux, y0 + tMin * uy, x0 + tMax * ux, y0 + tMax * uy];
  }

  class EtcViewerController {
    constructor(viewerEl) {
      this.viewerEl = viewerEl;
      this.stageEl = viewerEl.querySelector('.etc-svg-stage');
      this.captionEl = viewerEl.querySelector('.etc-viewer-caption');
      this.modeBar = viewerEl.querySelector('.etc-mode-tabs');
      this.triBar = viewerEl.querySelector('.etc-triangle-tabs');

      this.currentMode = viewerEl.getAttribute('data-default-mode') || 'construction';
      this.currentTriangle = viewerEl.getAttribute('data-default-triangle') || 'acute';

      this.svg = null;
      this.initialViewBox = [0, 0, 100, 100];
      this.linesViewBox = null;
      this.currentViewBox = [0, 0, 100, 100];
      this.elementsCatalog = {};

      // Cached SVG element references (rebuilt on view switch)
      this.pointsGroup = null;
      this.labelsGroup = null;
      this.highlightsGroup = null;
      this.pointEls = [];
      this.labelEls = [];
      this.subtitleEl = null;
      this.infiniteLines = []; // { el, x0, y0, ux, uy }
      this.svgIndex = new Map(); // canonicalKey -> Set<SVGElement>
      this.pointById = new Map();
      this.labelByPtId = new Map();
      this.hlByFor = new Map();

      // View state flags preserved across triangle switches
      this.hideLabels = false;
      this.hideGuides = false;
      this.showLines = this.currentMode === 'lines';

      // Canvas size cache + rAF scheduling
      this.cachedRect = { width: 800, height: 600, left: 0, top: 0 };
      this.rafPending = false;
      this.isPanning = false;
      this.didDrag = false;
      this.startClient = { x: 0, y: 0 };

      // Hover & pin state
      this.activeKey = null;
      this.pinnedKey = null;
      this.activeEls = new Set();

      // Bidirectional text index (page-wide, built once)
      this.textIndex = new Map(); // canonicalKey -> Set<HTMLElement>
      this.textRowsIndex = new Map(); // canonicalKey -> Set<HTMLTableRowElement>

      // Store initial inline SVG HTML in cache so switching back is instant
      const initialSvg = this.stageEl ? this.stageEl.querySelector('svg.geometor-etc-drawing') : null;
      const initialKey = this.cacheKeyFor(
        this.currentMode === 'lines' ? 'construction' : this.currentMode,
        this.currentTriangle
      );
      if (initialSvg) {
        VIEW_CACHE.set(initialKey, initialSvg.outerHTML);
      }

      this.footerEl = this.ensureStageFooter();
      this.statusEl = this.ensureStatusBar();
      this.toolbarEl = this.ensureToolbar();
      this.hudEl = this.ensureHud();
      this.noticeEl = null;

      this.initLayoutPreference();
      this.buildTextIndex();
      this.bindChrome();
      this.bindTextDelegation();

      if (initialSvg) {
        this.mountSvg(initialSvg, { applyModeLines: this.currentMode === 'lines' });
      }
    }

    cacheKeyFor(mode, triangle) {
      if (mode === 'construction' || mode === 'lines') {
        return `inline:construction:${triangle}`;
      }
      return `inline:${mode}`;
    }

    ensureStageFooter() {
      let footer = this.viewerEl.querySelector(':scope > .etc-stage-footer');
      if (footer) return footer;
      footer = document.createElement('div');
      footer.className = 'etc-stage-footer';
      if (this.stageEl.nextSibling) {
        this.viewerEl.insertBefore(footer, this.stageEl.nextSibling);
      } else {
        this.viewerEl.appendChild(footer);
      }
      return footer;
    }

    ensureStatusBar() {
      const footer = this.footerEl || this.ensureStageFooter();
      let st = footer.querySelector(':scope > .etc-stage-status');
      if (st) return st;
      st = document.createElement('div');
      st.className = 'etc-stage-status';
      footer.insertBefore(st, footer.firstChild);
      return st;
    }

    ensureToolbar() {
      const footer = this.footerEl || this.ensureStageFooter();
      let bar = footer.querySelector(':scope > .etc-svg-toolbar');
      if (bar) return bar;
      bar = document.createElement('div');
      bar.className = 'etc-svg-toolbar';
      const specs = [
        { key: 'zoom-in', label: '+', title: 'Zoom In (+ / scroll wheel)' },
        { key: 'zoom-out', label: '−', title: 'Zoom Out (− / scroll wheel)' },
        { key: 'reset', label: '⟲ Fit', title: 'Reset View (0 or double-click canvas)' },
        { key: 'lines', label: 'Lines', title: 'Toggle Incident Central Lines', toggle: true },
        { key: 'labels', label: 'Labels', title: 'Toggle Point Labels (L)', toggle: true },
        { key: 'guides', label: 'Guides', title: 'Toggle Construction Guides (G)', toggle: true },
        { key: 'layout', label: 'Split', title: 'Toggle Wide Split-Stage / Stacked Layout', toggle: true },
        { key: 'fullscreen', label: '⛶', title: 'Fullscreen Geometry App Mode (F)', toggle: true },
      ];
      specs.forEach((s) => {
        const btn = document.createElement('button');
        btn.type = 'button';
        btn.className = 'etc-svg-btn';
        btn.dataset.action = s.key;
        btn.textContent = s.label;
        btn.title = s.title;
        bar.appendChild(btn);
      });
      bar.addEventListener('click', (e) => {
        const btn = e.target.closest('button[data-action]');
        if (!btn) return;
        e.preventDefault();
        e.stopPropagation();
        this.handleToolbarAction(btn.dataset.action);
      });
      footer.appendChild(bar);
      return bar;
    }

    updateStatusFromSvg(svgEl) {
      if (!this.statusEl) this.statusEl = this.ensureStatusBar();
      if (!this.statusEl) return;
      let rawText = '';
      if (this.subtitleEl) {
        rawText = (this.subtitleEl.textContent || '').trim();
      } else if (svgEl) {
        // Coordinates plate bottom-right status text (y="742", text-anchor="end")
        const coordSub = svgEl.querySelector('text[y="742"][text-anchor="end"]');
        if (coordSub) {
          rawText = (coordSub.textContent || '').trim();
          coordSub.style.display = 'none';
        }
      }
      if (!rawText) {
        this.statusEl.innerHTML = '';
        this.statusEl.removeAttribute('title');
        return;
      }
      const formatted = escapeHtml(rawText).replace(/([A-Za-z])_([A-Za-z0-9]+)/g, '$1<sub>$2</sub>');
      this.statusEl.innerHTML = `<span>${formatted}</span>`;
      this.statusEl.setAttribute('title', rawText);
    }

    ensureHud() {
      let hud = this.stageEl.querySelector('.etc-symbolic-hud');
      if (hud) return hud;
      hud = document.createElement('div');
      hud.className = 'etc-symbolic-hud';
      hud.setAttribute('aria-live', 'polite');
      hud.addEventListener('click', (e) => {
        if (e.target.closest('.etc-hud-pin-hint')) {
          this.unpin();
        }
      });
      this.stageEl.appendChild(hud);
      return hud;
    }

    showNotice(msg) {
      if (!this.noticeEl) {
        this.noticeEl = document.createElement('div');
        this.noticeEl.className = 'etc-viewer-notice';
        this.stageEl.appendChild(this.noticeEl);
      }
      this.noticeEl.textContent = msg;
      this.noticeEl.style.display = 'block';
      clearTimeout(this._noticeTimer);
      this._noticeTimer = setTimeout(() => {
        if (this.noticeEl) this.noticeEl.style.display = 'none';
      }, 4200);
    }

    ensureAppBar(article) {
      if (!article) return null;
      let bar = article.querySelector(':scope > .etc-app-bar');
      if (bar) return bar;

      bar = document.createElement('div');
      bar.className = 'etc-app-bar';
      bar.setAttribute('role', 'banner');

      const left = document.createElement('div');
      left.className = 'etc-app-bar-left';

      const prevSrc = article.querySelector('.book-nav-prev a.book-nav-btn');
      if (prevSrc) {
        const prevBtn = document.createElement('a');
        prevBtn.className = 'etc-app-nav-btn';
        prevBtn.href = prevSrc.getAttribute('href') || '#';
        prevBtn.title = prevSrc.getAttribute('title') || 'Previous';
        prevBtn.innerHTML = '&larr;';
        left.appendChild(prevBtn);
      }

      const brand = document.createElement('div');
      brand.className = 'etc-app-brand';
      const h1 = article.querySelector('.etc-live-h1') || article.querySelector('.book-content > section > h1');
      const rubric = article.querySelector('.etc-live-subtitle') || article.querySelector('.book-content > section > p.rubric');
      const idSpan = document.createElement('span');
      idSpan.className = 'etc-app-brand-id';
      if (h1) {
        const clone = h1.cloneNode(true);
        clone.querySelectorAll('a.headerlink').forEach((a) => a.remove());
        idSpan.innerHTML = clone.innerHTML.trim();
      } else {
        idSpan.textContent = article.getAttribute('data-canonical-id') || 'ETC';
      }
      brand.appendChild(idSpan);

      const titleSpan = document.createElement('span');
      titleSpan.className = 'etc-app-brand-title';
      if (rubric && rubric.textContent.trim()) {
        titleSpan.innerHTML = rubric.innerHTML.trim();
      }
      brand.appendChild(titleSpan);
      left.appendChild(brand);

      const nextSrc = article.querySelector('.book-nav-next a.book-nav-btn');
      if (nextSrc) {
        const nextBtn = document.createElement('a');
        nextBtn.className = 'etc-app-nav-btn';
        nextBtn.href = nextSrc.getAttribute('href') || '#';
        nextBtn.title = nextSrc.getAttribute('title') || 'Next';
        nextBtn.innerHTML = '&rarr;';
        left.appendChild(nextBtn);
      }

      const center = document.createElement('div');
      center.className = 'etc-app-bar-center';
      const tracksSrc = article.querySelector('.book-tracks-nav');
      if (tracksSrc) {
        const tracksClone = tracksSrc.cloneNode(true);
        tracksClone.className = 'etc-app-tracks';
        center.appendChild(tracksClone);
      }

      const right = document.createElement('div');
      right.className = 'etc-app-bar-right';
      const hint = document.createElement('span');
      hint.className = 'etc-app-keys-hint';
      hint.textContent = 'F app · L labels · G guides · 0 fit · Esc exit';
      right.appendChild(hint);

      const exitBtn = document.createElement('button');
      exitBtn.type = 'button';
      exitBtn.className = 'etc-app-exit-btn';
      exitBtn.title = 'Exit Fullscreen App Mode (F or Esc)';
      exitBtn.textContent = '✕ Exit';
      exitBtn.addEventListener('click', (e) => {
        e.preventDefault();
        this.setFullscreen(false);
      });
      right.appendChild(exitBtn);

      bar.appendChild(left);
      bar.appendChild(center);
      bar.appendChild(right);

      // Delegate live track and X_n link clicks inside fullscreen app bar back to Live Explorer
      bar.addEventListener('click', (e) => {
        const liveApp = article.querySelector('#etc-live-app');
        if (!liveApp) return;
        const trLink = e.target.closest('a[data-live-track]');
        if (trLink) {
          e.preventDefault();
          const real = liveApp.querySelector(`.etc-live-tracks-bar a[data-live-track="${trLink.dataset.liveTrack}"]`);
          if (real) real.click();
          return;
        }
        const xLink = e.target.closest('a[data-jump-x]');
        if (xLink && window.ETCLiveExplorer) {
          e.preventDefault();
          const num = parseInt(xLink.dataset.jumpX, 10);
          if (Number.isFinite(num)) {
            window.ETCLiveExplorer.navigateTo(num, window.ETCLiveExplorer.currentTrack);
          }
        }
      });

      article.insertBefore(bar, article.firstChild);
      this.syncAppBar(article);
      return bar;
    }

    syncAppBar(articleEl) {
      const article = articleEl || this.viewerEl.closest('article.book-reading-pane');
      if (!article) return;
      const bar = article.querySelector(':scope > .etc-app-bar');
      if (!bar) return;

      const liveH1 = article.querySelector('.etc-live-h1');
      const liveSub = article.querySelector('.etc-live-subtitle');
      const liveTracks = article.querySelector('.etc-live-tracks-bar');
      if (!liveH1) return;

      const idSpan = bar.querySelector('.etc-app-brand-id');
      if (idSpan) {
        idSpan.innerHTML = liveH1.innerHTML.trim();
      }
      const titleSpan = bar.querySelector('.etc-app-brand-title');
      if (titleSpan) {
        titleSpan.innerHTML = liveSub ? liveSub.innerHTML.trim() : '';
        titleSpan.title = liveSub ? liveSub.textContent.trim() : '';
      }
      const center = bar.querySelector('.etc-app-bar-center');
      if (center && liveTracks) {
        if (liveTracks.style.display === 'none') {
          center.innerHTML = '';
        } else {
          const clone = liveTracks.cloneNode(true);
          clone.className = 'etc-app-tracks';
          clone.style.display = '';
          center.innerHTML = '';
          center.appendChild(clone);
        }
      }
    }

    ensureAppSplitter(article) {
      if (!article) return null;
      const ws = article.querySelector('.etc-split-workspace');
      const stageCol = ws ? ws.querySelector(':scope > .etc-stage-column') : null;
      const proseCol = ws ? ws.querySelector(':scope > .etc-prose-column') : null;
      if (!ws || !stageCol || !proseCol) return null;

      let splitter = ws.querySelector(':scope > .etc-app-splitter');
      if (splitter) return splitter;

      splitter = document.createElement('div');
      splitter.className = 'etc-app-splitter';
      splitter.setAttribute('role', 'separator');
      splitter.setAttribute('aria-orientation', 'vertical');
      splitter.title = 'Drag to resize graphic and data panes';
      ws.insertBefore(splitter, proseCol);

      try {
        const savedPct = parseFloat(window.localStorage.getItem('etc-app-split-pct') || '');
        if (Number.isFinite(savedPct) && savedPct >= 34 && savedPct <= 78) {
          ws.style.setProperty('--etc-app-left', `${savedPct.toFixed(1)}%`);
        }
      } catch (e) {}

      let dragging = false;
      splitter.addEventListener('pointerdown', (e) => {
        if (!this.isFullscreen) return;
        e.preventDefault();
        dragging = true;
        splitter.classList.add('is-dragging');
        if (splitter.setPointerCapture) {
          try {
            splitter.setPointerCapture(e.pointerId);
          } catch (err) {}
        }
      });

      splitter.addEventListener('pointermove', (e) => {
        if (!dragging) return;
        const rect = ws.getBoundingClientRect();
        if (rect.width <= 0) return;
        const pct = Math.max(34, Math.min(78, ((e.clientX - rect.left) / rect.width) * 100));
        ws.style.setProperty('--etc-app-left', `${pct.toFixed(1)}%`);
        try {
          window.localStorage.setItem('etc-app-split-pct', pct.toFixed(1));
        } catch (err) {}
        this.refreshCanvasMetricsAndRender();
      });

      const endDrag = () => {
        if (!dragging) return;
        dragging = false;
        splitter.classList.remove('is-dragging');
        this.refreshCanvasMetricsAndRender();
      };
      splitter.addEventListener('pointerup', endDrag);
      splitter.addEventListener('pointercancel', endDrag);
      return splitter;
    }

    setFullscreen(active, { persist = true } = {}) {
      const article = this.viewerEl.closest('article.book-reading-pane');
      if (!article || !article.querySelector('.etc-split-workspace')) return false;
      const want = Boolean(active);
      if (want) {
        this.ensureAppBar(article);
        this.syncAppBar(article);
        this.ensureAppSplitter(article);
      }
      this.isFullscreen = want;
      document.documentElement.classList.toggle('etc-app-fullscreen', want);
      document.body.classList.toggle('etc-app-fullscreen', want);
      article.classList.toggle('etc-app-fullscreen', want);
      if (persist) {
        try {
          if (want) {
            window.sessionStorage.setItem('etc-app-fullscreen', '1');
          } else {
            window.sessionStorage.removeItem('etc-app-fullscreen');
          }
        } catch (e) {}
      }
      this.syncToolbarButtons();
      requestAnimationFrame(() => {
        this.refreshCanvasMetricsAndRender();
        requestAnimationFrame(() => this.refreshCanvasMetricsAndRender());
      });
      return true;
    }

    toggleFullscreen() {
      return this.setFullscreen(!this.isFullscreen);
    }

    initLayoutPreference() {
      this.isFullscreen = false;
      const article = this.viewerEl.closest('article.book-reading-pane');
      if (!article || !article.querySelector('.etc-split-workspace')) return;
      article.classList.add('has-etc-stage');
      try {
        const pref = window.localStorage.getItem('etc-stage-layout');
        if (pref === 'stacked') {
          article.classList.add('etc-layout-stacked');
        }
        if (window.sessionStorage.getItem('etc-app-fullscreen') === '1') {
          this.setFullscreen(true, { persist: false });
        }
      } catch (e) {}
      this.syncToolbarButtons();
    }

    handleToolbarAction(action) {
      if (action === 'zoom-in') {
        this.zoomBy(1 / 1.25);
      } else if (action === 'zoom-out') {
        this.zoomBy(1.25);
      } else if (action === 'reset') {
        this.resetView();
      } else if (action === 'lines') {
        this.showLines = !this.showLines;
        if (this.svg) {
          this.svg.classList.toggle('show-lines', this.showLines);
          if (this.showLines && this.linesViewBox) {
            this.setViewBox([...this.linesViewBox]);
          } else if (!this.showLines) {
            this.setViewBox([...this.initialViewBox]);
          } else {
            this.scheduleRender();
          }
        }
        // Keep mode button synced if Lines mode tab exists
        if (this.modeBar) {
          const targetMode = this.showLines ? 'lines' : 'construction';
          if (this.modeBar.querySelector(`[data-mode="${targetMode}"]`)) {
            this.currentMode = targetMode;
            this.syncModeButtons();
          }
        }
        this.syncToolbarButtons();
      } else if (action === 'labels') {
        this.hideLabels = !this.hideLabels;
        if (this.svg) this.svg.classList.toggle('hide-labels', this.hideLabels);
        this.syncToolbarButtons();
        this.scheduleRender();
      } else if (action === 'guides') {
        this.hideGuides = !this.hideGuides;
        if (this.svg) this.svg.classList.toggle('hide-guides', this.hideGuides);
        this.syncToolbarButtons();
        this.scheduleRender();
      } else if (action === 'layout') {
        const article = this.viewerEl.closest('article.book-reading-pane.has-etc-stage');
        if (article) {
          const stacked = article.classList.toggle('etc-layout-stacked');
          try {
            window.localStorage.setItem('etc-stage-layout', stacked ? 'stacked' : 'split');
          } catch (e) {}
          this.syncToolbarButtons();
          requestAnimationFrame(() => this.refreshCanvasMetricsAndRender());
        }
      } else if (action === 'fullscreen') {
        this.toggleFullscreen();
      }
    }

    syncToolbarButtons() {
      if (!this.toolbarEl) return;
      const linesBtn = this.toolbarEl.querySelector('[data-action="lines"]');
      const labelsBtn = this.toolbarEl.querySelector('[data-action="labels"]');
      const guidesBtn = this.toolbarEl.querySelector('[data-action="guides"]');
      const layoutBtn = this.toolbarEl.querySelector('[data-action="layout"]');
      const fsBtn = this.toolbarEl.querySelector('[data-action="fullscreen"]');

      const allowLines = this.viewerEl.getAttribute('data-allow-lines') !== 'false';
      const hasIncident = Boolean(this.svg && this.svg.querySelector('.incident'));
      const hasLabels = this.labelEls.length > 0;
      const hasGuides = Boolean(this.svg && this.svg.querySelector('.guide'));
      const article = this.viewerEl.closest('article.book-reading-pane.has-etc-stage');

      if (linesBtn) {
        linesBtn.style.display = allowLines && hasIncident ? '' : 'none';
        linesBtn.classList.toggle('active', this.showLines);
      }
      if (labelsBtn) {
        labelsBtn.style.display = hasLabels ? '' : 'none';
        labelsBtn.classList.toggle('active', !this.hideLabels);
      }
      if (guidesBtn) {
        guidesBtn.style.display = hasGuides ? '' : 'none';
        guidesBtn.classList.toggle('active', !this.hideGuides);
      }
      if (layoutBtn) {
        const wideEnough = window.innerWidth >= 1280 && Boolean(article) && !this.isFullscreen;
        layoutBtn.style.display = wideEnough ? '' : 'none';
        const isSplit = Boolean(article && !article.classList.contains('etc-layout-stacked'));
        layoutBtn.classList.toggle('active', isSplit);
        layoutBtn.textContent = isSplit ? 'Split' : 'Stack';
      }
      if (fsBtn) {
        fsBtn.style.display = article ? '' : 'none';
        fsBtn.classList.toggle('active', Boolean(this.isFullscreen));
        fsBtn.textContent = this.isFullscreen ? '✕' : '⛶';
        fsBtn.title = this.isFullscreen ? 'Exit Fullscreen App Mode (F or Esc)' : 'Fullscreen Geometry App Mode (F)';
      }
    }

    syncModeButtons() {
      if (this.modeBar) {
        this.modeBar.querySelectorAll('.etc-mode-btn').forEach((btn) => {
          const active = btn.getAttribute('data-mode') === this.currentMode;
          btn.classList.toggle('active', active);
          btn.setAttribute('aria-selected', active ? 'true' : 'false');
        });
      }
      if (this.triBar) {
        const supportsTri =
          this.currentMode === 'construction' ||
          this.currentMode === 'lines' ||
          (typeof this.liveSvgProvider === 'function' && this.currentMode === 'coordinates');
        this.triBar.classList.toggle('is-disabled', !supportsTri);
        this.triBar.querySelectorAll('.etc-tab-btn').forEach((btn) => {
          const active = btn.getAttribute('data-tab') === this.currentTriangle;
          btn.classList.toggle('active', active);
          btn.setAttribute('aria-selected', active ? 'true' : 'false');
        });
      }
    }

    bindChrome() {
      if (this.modeBar) {
        this.modeBar.addEventListener('click', (e) => {
          const btn = e.target.closest('.etc-mode-btn');
          if (!btn) return;
          e.preventDefault();
          const mode = btn.getAttribute('data-mode');
          if (mode) this.switchMode(mode);
        });
      }
      if (this.triBar) {
        this.triBar.addEventListener('click', (e) => {
          const btn = e.target.closest('.etc-tab-btn');
          if (!btn) return;
          e.preventDefault();
          const tab = btn.getAttribute('data-tab');
          if (tab) this.switchTriangle(tab);
        });
      }

      // Inline section mode/triangle trigger pills anywhere in the reading pane
      document.addEventListener('click', (e) => {
        const trig = e.target.closest('[data-etc-switch-mode], [data-etc-switch-triangle]');
        if (!trig) return;
        e.preventDefault();
        const mode = trig.getAttribute('data-etc-switch-mode');
        const tri = trig.getAttribute('data-etc-switch-triangle');
        if (tri && (!mode || mode === 'construction' || mode === 'lines')) {
          if (mode && mode !== this.currentMode) {
            this.switchMode(mode).then(() => this.switchTriangle(tri));
          } else {
            this.switchTriangle(tri);
          }
        } else if (mode) {
          this.switchMode(mode);
        }
        // Scroll stage into view on narrow stacked screens
        if (window.innerWidth < 1280 && !this.isFullscreen) {
          this.viewerEl.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
        }
      });

      window.addEventListener('keydown', (e) => {
        if (e.ctrlKey || e.metaKey || e.altKey) return;
        const t = e.target;
        if (
          t &&
          (t.tagName === 'INPUT' ||
            t.tagName === 'TEXTAREA' ||
            t.tagName === 'SELECT' ||
            t.isContentEditable)
        ) {
          return;
        }
        if (e.key === 'Escape') {
          if (this.pinnedKey) {
            this.unpin();
          } else if (this.isFullscreen) {
            this.setFullscreen(false);
          }
        } else if (e.key === 'f' || e.key === 'F') {
          if (this.toggleFullscreen()) {
            e.preventDefault();
          }
        } else if (e.key === '0' || e.key === 'r' || e.key === 'R') {
          this.resetView();
        } else if (e.key === 'l' || e.key === 'L') {
          if (this.labelEls.length > 0) this.handleToolbarAction('labels');
        } else if (e.key === 'g' || e.key === 'G') {
          if (this.svg && this.svg.querySelector('.guide')) this.handleToolbarAction('guides');
        } else if (e.key === '+' || e.key === '=') {
          this.zoomBy(1 / 1.25);
        } else if (e.key === '-' || e.key === '_') {
          this.zoomBy(1.25);
        }
      });

      window.addEventListener(
        'resize',
        () => {
          this.syncToolbarButtons();
          this.refreshCanvasMetricsAndRender();
        },
        { passive: true }
      );
    }

    async loadViewSvgHtml(url, fallbackCacheKey) {
      if (fallbackCacheKey && VIEW_CACHE.has(fallbackCacheKey)) {
        return VIEW_CACHE.get(fallbackCacheKey);
      }
      if (url && VIEW_CACHE.has(url)) {
        return VIEW_CACHE.get(url);
      }
      if (!url) return null;

      if (window.location.protocol === 'file:') {
        this.showNotice('Local file:// blocks view fetch — preview via `python3 -m http.server` or GitHub Pages.');
        return null;
      }

      this.stageEl.classList.add('is-loading');
      try {
        const resp = await fetch(url);
        if (!resp.ok) throw new Error(`HTTP ${resp.status}`);
        const text = await resp.text();
        VIEW_CACHE.set(url, text);
        if (fallbackCacheKey) VIEW_CACHE.set(fallbackCacheKey, text);
        return text;
      } catch (err) {
        this.showNotice(`Unable to load view (${url}).`);
        return null;
      } finally {
        this.stageEl.classList.remove('is-loading');
      }
    }

    parseSvgFromHtml(svgHtml) {
      const tpl = document.createElement('template');
      tpl.innerHTML = svgHtml.trim();
      const svgEl = tpl.content.querySelector('svg');
      return svgEl;
    }

    updateCaption(captionHtml) {
      if (!this.captionEl) return;
      if (!this.captionEl.dataset.origHtml) {
        this.captionEl.dataset.origHtml = this.captionEl.innerHTML;
      }
      if (captionHtml === '__ORIG__') {
        this.captionEl.innerHTML = this.captionEl.dataset.origHtml;
      } else if (captionHtml) {
        this.captionEl.innerHTML = `<p>${captionHtml}</p>`;
      }
    }

    async switchMode(targetMode) {
      if (!targetMode) return false;
      const prevMode = this.currentMode;

      // Fast path: switching between Construction <-> Central Lines reuses the active SVG!
      if (
        (prevMode === 'construction' || prevMode === 'lines') &&
        (targetMode === 'construction' || targetMode === 'lines') &&
        this.svg
      ) {
        this.currentMode = targetMode;
        this.showLines = targetMode === 'lines';
        this.svg.classList.toggle('show-lines', this.showLines);
        this.setViewBox(
          this.showLines && this.linesViewBox ? [...this.linesViewBox] : [...this.initialViewBox]
        );
        this.syncModeButtons();
        this.syncToolbarButtons();
        const modeBtn = this.modeBar?.querySelector(`.etc-mode-btn[data-mode="${targetMode}"]`);
        if (modeBtn?.dataset.captionHtml) {
          this.updateCaption(modeBtn.dataset.captionHtml);
        }
        if (typeof this.onViewChange === 'function') {
          this.onViewChange(this.currentMode, this.currentTriangle);
        }
        return true;
      }

      // Determine source URL
      let url = null;
      let cacheKey = null;
      let capHtml = null;

      if (targetMode === 'construction' || targetMode === 'lines') {
        const triBtn = this.triBar?.querySelector(`.etc-tab-btn[data-tab="${this.currentTriangle}"]`);
        url = triBtn ? triBtn.getAttribute('data-src') : null;
        cacheKey = this.cacheKeyFor('construction', this.currentTriangle);
        capHtml =
          this.currentTriangle === (this.viewerEl.getAttribute('data-default-triangle') || 'acute') &&
          targetMode === (this.viewerEl.getAttribute('data-default-mode') || 'construction')
            ? '__ORIG__'
            : triBtn?.dataset.captionHtml || null;
      } else {
        const modeBtn = this.modeBar?.querySelector(`.etc-mode-btn[data-mode="${targetMode}"]`);
        if (!modeBtn) return false;
        url = modeBtn.getAttribute('data-src');
        cacheKey = this.cacheKeyFor(targetMode, this.currentTriangle);
        capHtml = modeBtn.dataset.captionHtml || null;
      }

      const svgHtml =
        typeof this.liveSvgProvider === 'function'
          ? this.liveSvgProvider(targetMode, this.currentTriangle)
          : await this.loadViewSvgHtml(url, cacheKey);
      if (!svgHtml) return false;
      const newSvg = this.parseSvgFromHtml(svgHtml);
      if (!newSvg) return false;

      this.unpin();
      this.clearHover();
      this.currentMode = targetMode;
      this.showLines = targetMode === 'lines';
      this.mountSvg(newSvg, { applyModeLines: this.showLines });
      this.syncModeButtons();
      if (capHtml) this.updateCaption(capHtml);
      if (typeof this.onViewChange === 'function') {
        this.onViewChange(this.currentMode, this.currentTriangle);
      }
      return true;
    }

    async switchTriangle(targetTab) {
      if (!targetTab) return false;
      const triBtn = this.triBar?.querySelector(`.etc-tab-btn[data-tab="${targetTab}"]`);
      if (!triBtn) return false;

      if (this.currentMode !== 'construction' && this.currentMode !== 'lines') {
        if (!(typeof this.liveSvgProvider === 'function' && this.currentMode === 'coordinates')) {
          this.currentMode = 'construction';
        }
      }

      const url = triBtn.getAttribute('data-src');
      const cacheKey = this.cacheKeyFor('construction', targetTab);
      const svgHtml =
        typeof this.liveSvgProvider === 'function'
          ? this.liveSvgProvider(this.currentMode, targetTab)
          : await this.loadViewSvgHtml(url, cacheKey);
      if (!svgHtml) return false;
      const newSvg = this.parseSvgFromHtml(svgHtml);
      if (!newSvg) return false;

      this.unpin();
      this.clearHover();
      this.currentTriangle = targetTab;
      this.mountSvg(newSvg, { applyModeLines: this.showLines });
      this.syncModeButtons();

      const defaultTri = this.viewerEl.getAttribute('data-default-triangle') || 'acute';
      if (targetTab === defaultTri && this.currentMode === (this.viewerEl.getAttribute('data-default-mode') || 'construction')) {
        this.updateCaption('__ORIG__');
      } else if (triBtn.dataset.captionHtml) {
        this.updateCaption(triBtn.dataset.captionHtml);
      }
      if (typeof this.onViewChange === 'function') {
        this.onViewChange(this.currentMode, this.currentTriangle);
      }
      return true;
    }

    mountSvg(svgEl, opts = {}) {
      // Remove previous <svg> strictly keeping 1 <svg> in DOM
      const oldSvg = this.stageEl.querySelector('svg.geometor-etc-drawing');
      if (oldSvg && oldSvg !== svgEl) {
        oldSvg.replaceWith(svgEl);
      } else if (!oldSvg) {
        this.stageEl.insertBefore(svgEl, this.stageEl.firstChild);
      }
      this.svg = svgEl;

      // Remove native browser <title> tooltips (superseded by symbolic HUD)
      svgEl.querySelectorAll('title').forEach((t) => t.remove());

      // Parse metadata catalog once
      this.elementsCatalog = {};
      const metaEl = svgEl.querySelector('script.etc-elements-meta');
      if (metaEl) {
        try {
          this.elementsCatalog = JSON.parse(metaEl.textContent || '{}');
        } catch (e) {}
      }

      // ViewBox setup (add clean breathing margin around point-labeled geometry SVGs)
      const hasPointsLayer = Boolean(svgEl.querySelector('#points'));
      const padViewBox = (vb) => {
        if (!Array.isArray(vb) || vb.length !== 4 || !vb.every(Number.isFinite)) return vb;
        const px = vb[2] * 0.04;
        const py = vb[3] * 0.07;
        return [vb[0] - px, vb[1] - py, vb[2] + 2 * px, vb[3] + 2 * py];
      };
      const initAttr = svgEl.getAttribute('data-initial-viewbox') || svgEl.getAttribute('viewBox') || '0 0 100 100';
      const rawInitVb = initAttr.trim().split(/\s+/).map(Number);
      this.initialViewBox = hasPointsLayer ? padViewBox(rawInitVb) : rawInitVb;
      const linesVbAttr = svgEl.getAttribute('data-lines-viewbox');
      const rawLinesVb = linesVbAttr ? linesVbAttr.trim().split(/\s+/).map(Number) : null;
      this.linesViewBox = rawLinesVb ? (hasPointsLayer ? padViewBox(rawLinesVb) : rawLinesVb) : null;

      // Apply preserved visibility flags
      svgEl.classList.toggle('hide-labels', this.hideLabels);
      svgEl.classList.toggle('hide-guides', this.hideGuides);
      if (opts.applyModeLines) {
        svgEl.classList.add('show-lines');
      } else {
        svgEl.classList.toggle('show-lines', this.showLines);
      }

      this.currentViewBox =
        this.showLines && this.linesViewBox ? [...this.linesViewBox] : [...this.initialViewBox];
      svgEl.setAttribute('viewBox', this.currentViewBox.map((n) => n.toFixed(6)).join(' '));

      // Cache SVG groups & elements
      this.pointsGroup = svgEl.querySelector('#points');
      this.labelsGroup = svgEl.querySelector('#labels');
      this.highlightsGroup = svgEl.querySelector('#highlights');
      this.activeRingSpecs = [];
      let ringsGrp = svgEl.querySelector('#etc-point-rings');
      if (!ringsGrp) {
        ringsGrp = document.createElementNS('http://www.w3.org/2000/svg', 'g');
        ringsGrp.setAttribute('id', 'etc-point-rings');
        ringsGrp.setAttribute('pointer-events', 'none');
        if (this.labelsGroup && this.labelsGroup.parentNode === svgEl) {
          svgEl.insertBefore(ringsGrp, this.labelsGroup);
        } else {
          svgEl.appendChild(ringsGrp);
        }
      }
      this.pointRingsGroup = ringsGrp;
      this.pointEls = this.pointsGroup ? Array.from(this.pointsGroup.querySelectorAll('circle')) : [];
      this.platePtEls = Array.from(svgEl.querySelectorAll('circle.etc-plate-pt'));
      this.labelEls = this.labelsGroup ? Array.from(this.labelsGroup.querySelectorAll('text[data-point-id]')) : [];
      this.subtitleEl = this.labelsGroup ? this.labelsGroup.querySelector('text.subtitle-label') : null;
      this.updateStatusFromSvg(svgEl);

      // Pre-sort labels by visual priority for fast screen-space anti-crowding
      const targetPtEl = this.pointsGroup ? this.pointsGroup.querySelector('circle.target, circle.selected') : null;
      const targetPtId = targetPtEl ? targetPtEl.getAttribute('data-id') : null;
      this.sortedLabelEls = this.labelEls
        .map((lbl) => {
          const pid = lbl.getAttribute('data-point-id') || '';
          const isTarget =
            lbl.classList.contains('target') ||
            lbl.classList.contains('selected-label') ||
            (targetPtId && pid === targetPtId);
          const isVertex = pid === 'A' || pid === 'B' || pid === 'C';
          const isGuide = lbl.classList.contains('guide-label') || lbl.classList.contains('guide');
          const isIncident = lbl.classList.contains('incident');
          const xm = pid.match(/^X_(\d+)$/);
          const num = xm ? parseInt(xm[1], 10) : 999999;
          let priority = 3;
          if (isTarget) priority = 0;
          else if (isVertex) priority = 1;
          else if (xm && !isGuide) priority = 2;
          return {
            el: lbl,
            pid,
            priority,
            num,
            isGuide,
            isIncident,
            cx: parseFloat(lbl.getAttribute('data-anchor-x') || '0'),
            cy: parseFloat(lbl.getAttribute('data-anchor-y') || '0'),
            oxPx: parseFloat(lbl.getAttribute('data-offset-x') || '12'),
            oyPx: parseFloat(lbl.getAttribute('data-offset-y') || '-10.5'),
            textLen: Math.max(1, (lbl.textContent || '').trim().length),
          };
        })
        .sort((a, b) => a.priority - b.priority || a.num - b.num);
      // Promote static dense-label hints to dynamic zoom-adaptive de-crowding
      this.sortedLabelEls.forEach((item) => {
        if (item.el.classList.contains('dense-label')) {
          item.el.classList.remove('dense-label');
        }
      });

      // Index infinite lines for dynamic Liang-Barsky viewport clipping
      this.infiniteLines = [];
      svgEl.querySelectorAll('#elements line').forEach((ln) => {
        const dl = ln.getAttribute('data-line');
        if (dl) {
          const parts = dl.split(',').map(Number);
          if (parts.length === 4 && parts.every(Number.isFinite)) {
            this.infiniteLines.push({ el: ln, x0: parts[0], y0: parts[1], ux: parts[2], uy: parts[3] });
            return;
          }
        }
        // Fallback: derive unit vector from x1,y1,x2,y2 for any un-tagged infinite line
        const x1 = parseFloat(ln.getAttribute('x1'));
        const y1 = parseFloat(ln.getAttribute('y1'));
        const x2 = parseFloat(ln.getAttribute('x2'));
        const y2 = parseFloat(ln.getAttribute('y2'));
        if ([x1, y1, x2, y2].every(Number.isFinite)) {
          const dx = x2 - x1;
          const dy = y2 - y1;
          const len = Math.hypot(dx, dy);
          if (len > this.initialViewBox[2] * 2.5) {
            this.infiniteLines.push({
              el: ln,
              x0: (x1 + x2) * 0.5,
              y0: (y1 + y2) * 0.5,
              ux: dx / len,
              uy: dy / len,
            });
          }
        }
      });

      this.buildSvgIndex();
      this.syncTableColorsFromSvg();
      this.bindSvgInteraction(svgEl);
      this.syncModeButtons();
      this.syncToolbarButtons();

      // Observe canvas resize once
      if (this._resizeObserver) this._resizeObserver.disconnect();
      if (typeof ResizeObserver !== 'undefined') {
        this._resizeObserver = new ResizeObserver(() => this.refreshCanvasMetricsAndRender());
        this._resizeObserver.observe(svgEl);
      }
      this.refreshCanvasMetricsAndRender();
    }

    buildSvgIndex() {
      this.svgIndex.clear();
      this.pointById.clear();
      this.labelByPtId.clear();
      this.hlByFor.clear();
      if (!this.svg) return;

      this.svg.querySelectorAll('[data-id], [data-ref]').forEach((el) => {
        if (el.closest('defs') || el.closest('#highlights')) return;
        const rawId = (el.getAttribute('data-id') || el.getAttribute('data-ref') || '').trim();
        if (!rawId) return;
        canonicalKeys(rawId).forEach((k) => {
          if (!this.svgIndex.has(k)) this.svgIndex.set(k, new Set());
          this.svgIndex.get(k).add(el);
        });
      });

      this.pointEls.forEach((pt) => {
        const pid = pt.getAttribute('data-id');
        if (pid) this.pointById.set(pid, pt);
      });
      this.platePtEls.forEach((pt) => {
        const pid = pt.getAttribute('data-id');
        if (pid && !this.pointById.has(pid)) this.pointById.set(pid, pt);
      });
      this.labelEls.forEach((lbl) => {
        const pid = lbl.getAttribute('data-point-id');
        if (pid) this.labelByPtId.set(pid, lbl);
      });
      if (this.highlightsGroup) {
        this.highlightsGroup.querySelectorAll('[data-highlight-for], [data-for]').forEach((hl) => {
          const key = hl.getAttribute('data-highlight-for') || hl.getAttribute('data-for');
          if (key) {
            canonicalKeys(key).forEach((ck) => this.hlByFor.set(ck, hl));
          }
        });
      }
    }

    syncTableColorsFromSvg() {
      const root =
        this.viewerEl.closest('article.book-reading-pane') ||
        document.querySelector('.book-content') ||
        document.body;
      if (!root || !this.svg) return;

      const resolveElementColor = (rawRef) => {
        if (!rawRef) return null;
        const { matchedEls, primaryInfo } = this.resolveSvgMatches(rawRef);
        if (primaryInfo && primaryInfo.color) {
          const c = String(primaryInfo.color).trim();
          if (c && c.toLowerCase() !== 'none') return c;
        }
        for (const el of matchedEls) {
          const stroke = (el.getAttribute('stroke') || '').trim();
          if (stroke && stroke.toLowerCase() !== 'none') return stroke;
          if (window.getComputedStyle) {
            const comp = window.getComputedStyle(el).stroke;
            if (comp && comp !== 'none' && comp !== 'rgb(0, 0, 0)') return comp;
          }
        }
        return null;
      };

      // 1. Principal Central Lines table: match line name, indices & row accent bar to SVG stroke
      root.querySelectorAll('table.etc-mode-lines tbody tr').forEach((tr) => {
        const lineRefEl =
          tr.querySelector('td:nth-child(2) .geom-ref[data-ref]') ||
          tr.querySelector('.geom-ref[data-ref^="{"]');
        if (!lineRefEl) return;
        const color = resolveElementColor(lineRefEl.getAttribute('data-ref'));
        if (color) {
          tr.style.setProperty('--etc-line-color', color);
          tr.classList.add('etc-line-colored');
        }
      });

      // 2. Central-line and circle .geom-ref badges in Lines & Relations tables
      root
        .querySelectorAll(
          'table.etc-mode-relations tbody .geom-ref[data-ref], table.etc-mode-lines tbody .geom-ref[data-ref]'
        )
        .forEach((span) => {
          const raw = (span.getAttribute('data-ref') || '').trim();
          if (!raw) return;
          const isLineOrCircle =
            raw.startsWith('{') || /(?:circle|incircle|circumcircle|excircle)/i.test(raw);
          if (!isLineOrCircle) return;
          const color = resolveElementColor(raw);
          if (color) {
            span.style.setProperty('--etc-ref-color', color);
            span.classList.add('etc-ref-colored');
          }
        });
    }

    buildTextIndex() {
      this.textIndex.clear();
      this.textRowsIndex.clear();
      const root =
        this.viewerEl.closest('article.book-reading-pane') ||
        document.querySelector('.book-content') ||
        document.body;
      if (!root) return;

      const register = (rawRef, el) => {
        const row = el.closest('table.etc-table tbody tr');
        canonicalKeys(rawRef).forEach((k) => {
          if (!this.textIndex.has(k)) this.textIndex.set(k, new Set());
          this.textIndex.get(k).add(el);
          if (row) {
            if (!this.textRowsIndex.has(k)) this.textRowsIndex.set(k, new Set());
            this.textRowsIndex.get(k).add(row);
          }
        });
      };

      root.querySelectorAll('.geom-ref[data-ref]').forEach((span) => {
        if (span.closest('svg')) return;
        register(span.getAttribute('data-ref'), span);
      });

      // Also index explicit center links (X_n) outside closed huge catalogs
      root.querySelectorAll('a.reference.internal').forEach((link) => {
        if (link.closest('details:not([open])')) return;
        const txt = (link.textContent || '').trim();
        const xm = txt.match(/^X(?:_|\()?(\d+)\)?$/);
        if (xm) {
          register(`X_${xm[1]}`, link);
        }
      });
    }

    refreshCanvasMetricsAndRender() {
      if (!this.svg) return;
      const rect = this.svg.getBoundingClientRect();
      if (rect.width > 0 && rect.height > 0) {
        this.cachedRect = rect;
      }
      this.scheduleRender();
    }

    scheduleRender() {
      if (this.rafPending || !this.svg) return;
      this.rafPending = true;
      requestAnimationFrame(() => {
        this.rafPending = false;
        this.renderViewBoxNow();
      });
    }

    setViewBox(vb) {
      this.currentViewBox = vb;
      this.scheduleRender();
    }

    renderViewBoxNow() {
      if (!this.svg) return;
      const vb = this.currentViewBox;
      this.svg.setAttribute('viewBox', `${vb[0].toFixed(6)} ${vb[1].toFixed(6)} ${vb[2].toFixed(6)} ${vb[3].toFixed(6)}`);

      const widthPx = this.cachedRect.width || 800;
      const heightPx = this.cachedRect.height || 600;
      const unitsPerPx = Math.max(vb[2] / widthPx, vb[3] / heightPx);

      // 1. Scale all points uniformly (compact geometor.explorer scale, slightly tighter on dense plates)
      const activeShowLines = this.showLines || this.svg.classList.contains('show-lines');
      const visiblePtAnchors = [];
      if (this.pointEls.length > 0) {
        const denseCount = this.pointEls.length >= 12 && activeShowLines;
        const ptPx = denseCount ? 4.2 : 4.6;
        const uniformR = (ptPx * unitsPerPx).toFixed(6);
        for (let i = 0; i < this.pointEls.length; i++) {
          const pt = this.pointEls[i];
          pt.setAttribute('r', uniformR);
          if (!activeShowLines && pt.classList.contains('incident')) continue;
          if (this.hideGuides && pt.classList.contains('guide')) continue;
          const px = parseFloat(pt.getAttribute('cx') || 'NaN');
          const py = parseFloat(pt.getAttribute('cy') || 'NaN');
          if (Number.isFinite(px) && Number.isFinite(py)) {
            visiblePtAnchors.push({
              pid: pt.getAttribute('data-id') || '',
              sx: (px - vb[0]) / unitsPerPx,
              sy: (py - vb[1]) / unitsPerPx,
            });
          }
        }
      }
      if (this.platePtEls && this.platePtEls.length > 0) {
        const plateR = (4.4 * unitsPerPx).toFixed(6);
        for (let i = 0; i < this.platePtEls.length; i++) {
          this.platePtEls[i].setAttribute('r', plateR);
        }
      }
      if (this.activeRingSpecs && this.activeRingSpecs.length > 0) {
        for (let i = 0; i < this.activeRingSpecs.length; i++) {
          const rs = this.activeRingSpecs[i];
          rs.el.setAttribute('r', ((rs.primary ? 11.5 : 9.2) * unitsPerPx).toFixed(6));
        }
      }

      // 1b. Screen-space 8-slot anti-crowding label placement (blossoms cleanly on zoom-in or hover)
      if (this.sortedLabelEls && this.sortedLabelEls.length > 0) {
        const baseFontPx = this.isFullscreen ? 21.0 : 20.0;
        const guideFontPx = this.isFullscreen ? 18.0 : 17.0;
        const fontSize = (baseFontPx * unitsPerPx).toFixed(6);
        const guideFontSize = (guideFontPx * unitsPerPx).toFixed(6);
        const placedBoxes = [];
        const pad = 3.5;
        const dotR = 6.5;

        const boxesOverlap = (a, b) =>
          a.l < b.r + pad && a.r + pad > b.l && a.t < b.b + pad && a.b + pad > b.t;

        for (let i = 0; i < this.sortedLabelEls.length; i++) {
          const item = this.sortedLabelEls[i];
          const lbl = item.el;
          if ((!activeShowLines && item.isIncident) || (this.hideGuides && item.isGuide)) {
            lbl.classList.remove('etc-label-crowded');
            continue;
          }

          const fPx = item.isGuide ? guideFontPx : baseFontPx;
          const boxW = Math.max(18, item.textLen * fPx * 0.62) + 4;
          const boxH = fPx * 1.05;
          const axPx = (item.cx - vb[0]) / unitsPerPx;
          const ayPx = (item.cy - vb[1]) / unitsPerPx;

          // 9 candidates: authored preferred offset first, then 8 radial slots around point
          const candidates = [
            [item.oxPx, item.oyPx],
            [11, -10],
            [-11 - boxW, -10],
            [11, 10 + fPx * 0.72],
            [-11 - boxW, 10 + fPx * 0.72],
            [-boxW * 0.5, -13],
            [-boxW * 0.5, 13 + fPx * 0.78],
            [14, fPx * 0.3],
            [-14 - boxW, fPx * 0.3],
          ];

          let bestSlot = candidates[0];
          let bestBox = null;
          let bestPenalty = Infinity;
          let bestLabelCollision = true;

          for (let c = 0; c < candidates.length; c++) {
            const dx = candidates[c][0];
            const dy = candidates[c][1];
            const lx = axPx + dx;
            const ly = ayPx + dy;
            const box = {
              l: lx,
              t: ly - fPx * 0.84,
              r: lx + boxW,
              b: ly + fPx * 0.2,
            };

            let labelHits = 0;
            for (let p = 0; p < placedBoxes.length; p++) {
              if (boxesOverlap(box, placedBoxes[p])) {
                labelHits++;
              }
            }

            let dotHits = 0;
            for (let d = 0; d < visiblePtAnchors.length; d++) {
              const pt = visiblePtAnchors[d];
              if (pt.pid === item.pid) continue;
              if (
                pt.sx + dotR > box.l &&
                pt.sx - dotR < box.r &&
                pt.sy + dotR > box.t &&
                pt.sy - dotR < box.b
              ) {
                dotHits++;
              }
            }

            const penalty = labelHits * 1000 + dotHits * 45 + c * 2;
            if (penalty < bestPenalty) {
              bestPenalty = penalty;
              bestSlot = candidates[c];
              bestBox = box;
              bestLabelCollision = labelHits > 0;
              if (labelHits === 0 && dotHits === 0) break;
            }
          }

          lbl.setAttribute('x', (item.cx + bestSlot[0] * unitsPerPx).toFixed(6));
          lbl.setAttribute('y', (item.cy + bestSlot[1] * unitsPerPx).toFixed(6));
          lbl.setAttribute('font-size', item.isGuide ? guideFontSize : fontSize);

          if (bestLabelCollision && item.priority >= 2) {
            lbl.classList.add('etc-label-crowded');
          } else {
            lbl.classList.remove('etc-label-crowded');
            if (bestBox) placedBoxes.push(bestBox);
          }
        }
      }

      if (this.subtitleEl) {
        this.subtitleEl.setAttribute('x', (vb[0] + 14.0 * unitsPerPx).toFixed(6));
        this.subtitleEl.setAttribute('y', (vb[1] + vb[3] - 10.0 * unitsPerPx).toFixed(6));
        this.subtitleEl.setAttribute('font-size', (13.5 * unitsPerPx).toFixed(6));
      }

      // 2. Dynamically clip every infinite dashed line to 2.2x active viewBox!
      if (this.infiniteLines.length > 0) {
        const padX = vb[2] * 0.6;
        const padY = vb[3] * 0.6;
        const xmin = vb[0] - padX;
        const ymin = vb[1] - padY;
        const xmax = vb[0] + vb[2] + padX;
        const ymax = vb[1] + vb[3] + padY;

        for (let i = 0; i < this.infiniteLines.length; i++) {
          const ln = this.infiniteLines[i];
          const seg = clipInfiniteLineToBox(ln.x0, ln.y0, ln.ux, ln.uy, xmin, ymin, xmax, ymax);
          if (seg) {
            ln.el.setAttribute('x1', seg[0].toFixed(5));
            ln.el.setAttribute('y1', seg[1].toFixed(5));
            ln.el.setAttribute('x2', seg[2].toFixed(5));
            ln.el.setAttribute('y2', seg[3].toFixed(5));
          }
        }
      }

      // 3. Keep visible HUD positioned clear of the active object during pan/zoom/resize
      if (this._hudAnchorEls && this.hudEl && this.hudEl.classList.contains('is-visible')) {
        this.positionHud(this._hudAnchorEls);
      }
    }

    zoomBy(factor, clientX, clientY) {
      if (!this.svg) return;
      const vb = this.currentViewBox;
      const rect = this.svg.getBoundingClientRect();
      this.cachedRect = rect;
      const relX = clientX !== undefined && rect.width > 0 ? (clientX - rect.left) / rect.width : 0.5;
      const relY = clientY !== undefined && rect.height > 0 ? (clientY - rect.top) / rect.height : 0.5;
      const focusX = vb[0] + relX * vb[2];
      const focusY = vb[1] + relY * vb[3];
      const baseW = Math.max(this.initialViewBox[2] || 1.0, 0.2);
      const baseH = Math.max(this.initialViewBox[3] || 1.0, 0.2);
      const newW = Math.min(Math.max(vb[2] * factor, baseW * 0.002), baseW * 30.0);
      const newH = Math.min(Math.max(vb[3] * factor, baseH * 0.002), baseH * 30.0);
      this.setViewBox([focusX - relX * newW, focusY - relY * newH, newW, newH]);
    }

    resetView() {
      const base = this.showLines && this.linesViewBox ? this.linesViewBox : this.initialViewBox;
      this.setViewBox([...base]);
    }

    updateHud(info, fallbackId, pinned = false, anchorEls = null) {
      if (!this.hudEl) return;
      if (!info) {
        this.hudEl.classList.remove('is-visible', 'is-pinned');
        this._hudAnchorEls = null;
        return;
      }
      this._hudAnchorEls = anchorEls ? Array.from(anchorEls) : null;
      const dotColor = info.color || '#e8b85a';
      const idHtml = formatIdHtml(info.ID || fallbackId || '');
      const titleHtml = escapeHtml(info.name || fallbackId || '');
      const kindHtml = escapeHtml(info.type || '');
      const symRows = Array.isArray(info.symbolic_rows) ? info.symbolic_rows : [];
      let rowsHtml = '';
      if (symRows.length > 0) {
        symRows.forEach((r) => {
          rowsHtml +=
            '<div class="etc-hud-key">' +
            escapeHtml(r.label) +
            '</div><div class="etc-hud-val">' +
            renderMathHtml(r.latex, r.pretty) +
            '</div>';
        });
      } else if (Array.isArray(info.rows)) {
        info.rows.forEach((pair) => {
          rowsHtml +=
            '<div class="etc-hud-key">' +
            escapeHtml(pair[0]) +
            '</div><div class="etc-hud-val">' +
            escapeHtml(pair[1]) +
            '</div>';
        });
      }
      const approxHtml = info.approx
        ? '<div class="etc-hud-approx">' + escapeHtml(info.approx) + '</div>'
        : '';
      const pinChip = pinned
        ? '<span class="etc-hud-pin-hint" title="Click or press Esc to unpin">Pinned ×</span>'
        : '';
      this.hudEl.innerHTML =
        '<div class="etc-hud-head">' +
        '<span class="etc-hud-dot" style="background:' +
        escapeHtml(dotColor) +
        '"></span>' +
        '<span class="etc-hud-id">' +
        idHtml +
        '</span>' +
        '<span class="etc-hud-title">' +
        titleHtml +
        '</span>' +
        '<span class="etc-hud-kind">' +
        kindHtml +
        '</span>' +
        pinChip +
        '</div>' +
        '<div class="etc-hud-rows">' +
        rowsHtml +
        '</div>' +
        approxHtml;
      this.hudEl.classList.add('is-visible');
      this.hudEl.classList.toggle('is-pinned', pinned);
      this.positionHud(this._hudAnchorEls);
    }

    positionHud(anchorEls) {
      if (!this.hudEl || !this.stageEl || !this.svg) return;
      const stageRect = this.stageEl.getBoundingClientRect();
      if (stageRect.width < 40 || stageRect.height < 40) return;

      const hudW = this.hudEl.offsetWidth || 260;
      const hudH = this.hudEl.offsetHeight || 96;
      const margin = 10;
      const gap = 16;

      // Collect tight screen-space bounding box & obstacle sample points for the hovered object(s)
      let tLeft = Infinity;
      let tTop = Infinity;
      let tRight = -Infinity;
      let tBottom = -Infinity;
      const samplePts = [];
      const ctm = typeof this.svg.getScreenCTM === 'function' ? this.svg.getScreenCTM() : null;

      const toStagePt = (sx, sy) => {
        if (!ctm) return null;
        return {
          x: ctm.a * sx + ctm.c * sy + ctm.e - stageRect.left,
          y: ctm.b * sx + ctm.d * sy + ctm.f - stageRect.top,
        };
      };

      const addBox = (r) => {
        if (!r || (r.width === 0 && r.height === 0)) return;
        const l = Math.max(0, r.left - stageRect.left);
        const t = Math.max(0, r.top - stageRect.top);
        const ri = Math.min(stageRect.width, r.right - stageRect.left);
        const b = Math.min(stageRect.height, r.bottom - stageRect.top);
        if (ri < l || b < t) return;
        if (l < tLeft) tLeft = l;
        if (t < tTop) tTop = t;
        if (ri > tRight) tRight = ri;
        if (b > tBottom) tBottom = b;
      };

      const els = Array.isArray(anchorEls) ? anchorEls : [];
      els.forEach((el) => {
        if (!el || !this.svg.contains(el)) return;
        const tag = el.tagName ? el.tagName.toLowerCase() : '';
        const isInfLine = tag === 'line' && el.hasAttribute('data-line');

        if (isInfLine) {
          // Focus around the finite highlight segment (defining points) if present,
          // while still sampling the visible clipped span so the card avoids the line itself
          const did = el.getAttribute('data-id') || el.getAttribute('data-ref') || '';
          const hl = did ? this.hlByFor.get(did) : null;
          if (hl) {
            addBox(hl.getBoundingClientRect());
          }
          const x1 = parseFloat(el.getAttribute('x1'));
          const y1 = parseFloat(el.getAttribute('y1'));
          const x2 = parseFloat(el.getAttribute('x2'));
          const y2 = parseFloat(el.getAttribute('y2'));
          if (ctm && [x1, y1, x2, y2].every(Number.isFinite)) {
            for (let k = 0; k <= 12; k++) {
              const p = toStagePt(x1 + ((x2 - x1) * k) / 12, y1 + ((y2 - y1) * k) / 12);
              if (p && p.x >= 0 && p.x <= stageRect.width && p.y >= 0 && p.y <= stageRect.height) {
                samplePts.push(p);
              }
            }
          }
          if (!Number.isFinite(tLeft) && samplePts.length > 0) {
            const mid = samplePts[Math.floor(samplePts.length / 2)];
            tLeft = mid.x - 16;
            tRight = mid.x + 16;
            tTop = mid.y - 16;
            tBottom = mid.y + 16;
          }
          return;
        }

        const r = el.getBoundingClientRect();
        addBox(r);

        if (tag === 'line' && ctm) {
          const x1 = parseFloat(el.getAttribute('x1'));
          const y1 = parseFloat(el.getAttribute('y1'));
          const x2 = parseFloat(el.getAttribute('x2'));
          const y2 = parseFloat(el.getAttribute('y2'));
          if ([x1, y1, x2, y2].every(Number.isFinite)) {
            for (let k = 0; k <= 8; k++) {
              const p = toStagePt(x1 + ((x2 - x1) * k) / 8, y1 + ((y2 - y1) * k) / 8);
              if (p) samplePts.push(p);
            }
          }
        } else if (tag === 'polygon' && ctm) {
          const ptsAttr = (el.getAttribute('points') || '').trim();
          const verts = ptsAttr
            .split(/\s+/)
            .map((pair) => pair.split(',').map(Number))
            .filter((xy) => xy.length === 2 && xy.every(Number.isFinite))
            .map(([vx, vy]) => toStagePt(vx, vy))
            .filter(Boolean);
          if (verts.length > 0) {
            let cx = 0;
            let cy = 0;
            verts.forEach((v, idx) => {
              cx += v.x;
              cy += v.y;
              samplePts.push(v);
              const nxt = verts[(idx + 1) % verts.length];
              samplePts.push({ x: (v.x + nxt.x) * 0.5, y: (v.y + nxt.y) * 0.5 });
            });
            samplePts.push({ x: cx / verts.length, y: cy / verts.length });
          }
        } else if (tag === 'circle' && ctm && !el.closest('#points') && !el.classList.contains('etc-plate-pt')) {
          const ccx = parseFloat(el.getAttribute('cx'));
          const ccy = parseFloat(el.getAttribute('cy'));
          const cr = parseFloat(el.getAttribute('r'));
          if ([ccx, ccy, cr].every(Number.isFinite)) {
            for (let k = 0; k < 12; k++) {
              const ang = (k / 12) * Math.PI * 2;
              const p = toStagePt(ccx + cr * Math.cos(ang), ccy + cr * Math.sin(ang));
              if (p) samplePts.push(p);
            }
          }
        } else if (r && (r.width > 0 || r.height > 0)) {
          samplePts.push({
            x: (r.left + r.right) * 0.5 - stageRect.left,
            y: (r.top + r.bottom) * 0.5 - stageRect.top,
          });
        }
      });

      if (!Number.isFinite(tLeft)) {
        this.hudEl.style.left = `${margin}px`;
        this.hudEl.style.top = `${Math.max(margin, stageRect.height - hudH - margin)}px`;
        return;
      }

      const tCx = (tLeft + tRight) * 0.5;
      const tCy = (tTop + tBottom) * 0.5;
      const maxL = Math.max(margin, stageRect.width - hudW - margin);
      const maxT = Math.max(margin, stageRect.height - hudH - margin);
      const clamp = (v, lo, hi) => Math.max(lo, Math.min(hi, v));

      // Toolbar obstacle box (only if toolbar floats inside the stage)
      let tbBox = null;
      if (this.toolbarEl && this.stageEl.contains(this.toolbarEl)) {
        const tr = this.toolbarEl.getBoundingClientRect();
        if (tr.width > 0 && tr.height > 0) {
          tbBox = {
            l: tr.left - stageRect.left - 6,
            t: tr.top - stageRect.top - 6,
            r: tr.right - stageRect.left + 6,
            b: tr.bottom - stageRect.top + 6,
          };
        }
      }

      // Target box padded with breathing room
      const pad = 12;
      const objBox = {
        l: tLeft - pad,
        t: tTop - pad,
        r: tRight + pad,
        b: tBottom + pad,
      };
      const isLargeObj = (tRight - tLeft) > stageRect.width * 0.45 && (tBottom - tTop) > stageRect.height * 0.45;

      // Candidate positions: 8 near-object orbit slots + 4 clean stage corners
      const rawCandidates = [
        { x: tRight + gap, y: tCy - hudH * 0.5 },
        { x: tLeft - hudW - gap, y: tCy - hudH * 0.5 },
        { x: tCx - hudW * 0.5, y: tTop - hudH - gap },
        { x: tCx - hudW * 0.5, y: tBottom + gap },
        { x: tRight + gap, y: tTop - hudH - gap * 0.5 },
        { x: tLeft - hudW - gap, y: tTop - hudH - gap * 0.5 },
        { x: tRight + gap, y: tBottom + gap * 0.5 },
        { x: tLeft - hudW - gap, y: tBottom + gap * 0.5 },
        { x: margin, y: margin },
        { x: maxL, y: maxT },
        { x: margin, y: maxT },
        { x: maxL, y: tbBox ? Math.min(maxT, tbBox.b + 8) : margin },
      ];

      const overlapArea = (ax1, ay1, ax2, ay2, bx1, by1, bx2, by2) => {
        const ow = Math.max(0, Math.min(ax2, bx2) - Math.max(ax1, bx1));
        const oh = Math.max(0, Math.min(ay2, by2) - Math.max(ay1, by1));
        return ow * oh;
      };

      let best = { x: margin, y: margin, score: Infinity };
      rawCandidates.forEach((cand) => {
        const x = clamp(cand.x, margin, maxL);
        const y = clamp(cand.y, margin, maxT);
        const x2 = x + hudW;
        const y2 = y + hudH;

        let score = 0;
        // Heavy penalty for overlapping sample points of the object (handles lines, struts, polygons, circles)
        for (let i = 0; i < samplePts.length; i++) {
          const p = samplePts[i];
          if (p.x >= x - 8 && p.x <= x2 + 8 && p.y >= y - 8 && p.y <= y2 + 8) {
            score += 45000;
          }
        }
        // Bounding-box overlap penalty (lighter weight for huge enclosing circles/triangles so corners still win)
        const boxOv = overlapArea(x, y, x2, y2, objBox.l, objBox.t, objBox.r, objBox.b);
        score += boxOv * (isLargeObj ? 0.6 : 12.0);

        // Avoid covering the floating toolbar
        if (tbBox) {
          score += overlapArea(x, y, x2, y2, tbBox.l, tbBox.t, tbBox.r, tbBox.b) * 80.0;
        }

        // Prefer positions near the hovered object (tie-breaker among non-overlapping candidates)
        const dist = Math.hypot((x + x2) * 0.5 - tCx, (y + y2) * 0.5 - tCy);
        score += dist * 0.35;

        if (score < best.score) {
          best = { x, y, score };
        }
      });

      this.hudEl.style.left = `${Math.round(best.x)}px`;
      this.hudEl.style.top = `${Math.round(best.y)}px`;
    }

    hasCanonicalKey(rawRef) {
      return canonicalKeys(rawRef).some((k) => this.svgIndex.has(k));
    }

    resolveSvgMatches(rawRef) {
      const keys = canonicalKeys(rawRef);
      const matchedEls = new Set();
      let primaryId = null;
      let primaryInfo = null;

      keys.forEach((k) => {
        const set = this.svgIndex.get(k);
        if (set) {
          set.forEach((el) => {
            matchedEls.add(el);
            const did = el.getAttribute('data-id') || el.getAttribute('data-ref');
            if (!primaryId && did) primaryId = did;
            if (!primaryInfo && did && this.elementsCatalog[did]) {
              primaryInfo = this.elementsCatalog[did];
              primaryId = did;
            }
          });
        }
      });

      if (!primaryInfo && primaryId && this.elementsCatalog[primaryId]) {
        primaryInfo = this.elementsCatalog[primaryId];
      }
      return { keys, matchedEls, primaryId, primaryInfo };
    }

    clearPointRings() {
      this.activeRingSpecs = [];
      if (this.pointRingsGroup) {
        this.pointRingsGroup.innerHTML = '';
      }
    }

    addPointRing(ptEl, primary, color) {
      if (!this.pointRingsGroup || !ptEl) return;
      const cx = parseFloat(ptEl.getAttribute('cx'));
      const cy = parseFloat(ptEl.getAttribute('cy'));
      if (!Number.isFinite(cx) || !Number.isFinite(cy)) return;
      const vb = this.currentViewBox || this.initialViewBox || [0, 0, 100, 100];
      const wPx = this.cachedRect?.width || 800;
      const hPx = this.cachedRect?.height || 600;
      const unitsPerPx = Math.max(vb[2] / wPx, vb[3] / hPx);
      const ring = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
      ring.setAttribute('class', `etc-point-ring ${primary ? 'is-primary' : 'is-secondary'}`);
      ring.setAttribute('cx', cx.toFixed(6));
      ring.setAttribute('cy', cy.toFixed(6));
      ring.setAttribute('r', ((primary ? 11.5 : 9.2) * unitsPerPx).toFixed(6));
      if (color && color !== 'none') {
        ring.style.stroke = color;
      }
      this.pointRingsGroup.appendChild(ring);
      this.activeRingSpecs.push({ el: ring, primary: Boolean(primary) });
    }

    clearHover(force = false) {
      if (this.pinnedKey && !force) return;
      this.clearPointRings();
      if (this.activeEls.size === 0 && !this.activeKey) return;
      this.activeKey = null;
      this.activeEls.forEach((el) => {
        el.classList.remove(
          'hover',
          'hover-label',
          'geom-highlight-active',
          'geom-highlight-secondary',
          'geom-highlight-text',
          'etc-row-highlight',
          'is-pinned'
        );
        if (el.classList.contains('highlight-segment')) {
          el.style.display = 'none';
        }
      });
      this.activeEls.clear();
      if (this.hudEl) {
        this.hudEl.classList.remove('is-visible', 'is-pinned');
      }
    }

    unpin() {
      this.pinnedKey = null;
      this.clearHover(true);
    }

    activateHover(rawRef, opts = {}) {
      if (!rawRef || !this.svg) return false;
      const { fromSvg = false, pin = false, sourceEl = null } = opts;
      if (this.pinnedKey && !pin) return false;

      const { keys, matchedEls, primaryId, primaryInfo } = this.resolveSvgMatches(rawRef);
      if (matchedEls.size === 0) return false;

      const dedupKey = primaryId || keys[0];
      if (!pin && this.activeKey === dedupKey) return true;

      this.clearHover(true);
      this.activeKey = dedupKey;
      if (pin) this.pinnedKey = dedupKey;

      // Determine semantic stroke/accent color of primary element (keeps line highlights in their own color!)
      let primaryColor = primaryInfo?.color || null;
      if (!primaryColor) {
        for (const el of matchedEls) {
          const st = el.style?.stroke || el.getAttribute('stroke');
          if (st && st !== 'none') {
            primaryColor = st;
            break;
          }
          if (window.getComputedStyle && el.tagName.toLowerCase() !== 'circle') {
            const comp = window.getComputedStyle(el).stroke;
            if (comp && comp !== 'none' && comp !== 'rgb(0, 0, 0)') {
              primaryColor = comp;
              break;
            }
          }
        }
      }

      // 1. Highlight matched SVG elements + highlight overlays + constituent points/labels + point rings
      const allCanonicalForText = new Set(keys);
      const ringedPts = new Set();
      matchedEls.forEach((el) => {
        el.classList.add('hover', 'geom-highlight-active');
        if (pin) el.classList.add('is-pinned');
        this.activeEls.add(el);
        const tag = el.tagName.toLowerCase();
        if (tag === 'circle' && (el.closest('#points') || el.classList.contains('etc-plate-pt'))) {
          const ptCol = primaryColor && primaryColor !== '#e0e0e0' ? primaryColor : '#ffd54f';
          this.addPointRing(el, true, ptCol);
          ringedPts.add(el);
        }
        const did = el.getAttribute('data-id') || el.getAttribute('data-ref');
        if (did) {
          canonicalKeys(did).forEach((k) => allCanonicalForText.add(k));
        }
      });

      allCanonicalForText.forEach((ck) => {
        const hl = this.hlByFor.get(ck);
        if (hl) {
          hl.style.display = 'inline';
          if (primaryColor && !hl.style.stroke) {
            hl.style.stroke = primaryColor;
          }
          this.activeEls.add(hl);
        }
      });

      const relPts = inferRelatedPoints(primaryId, primaryInfo);
      relPts.forEach((pid) => {
        const ptEl = this.pointById.get(pid);
        if (ptEl && !matchedEls.has(ptEl)) {
          ptEl.classList.add('geom-highlight-secondary');
          this.activeEls.add(ptEl);
          if (!ringedPts.has(ptEl)) {
            this.addPointRing(ptEl, false, primaryColor || '#f6d38b');
            ringedPts.add(ptEl);
          }
        }
        const lblEl = this.labelByPtId.get(pid);
        if (lblEl) {
          lblEl.classList.add('hover-label', 'geom-highlight-secondary');
          this.activeEls.add(lblEl);
        }
      });

      // 2. Highlight matching text references & enclosing table rows (Two-Way Sync!)
      if (sourceEl) {
        sourceEl.classList.add('geom-highlight-text');
        this.activeEls.add(sourceEl);
        const coordRow = sourceEl.closest('table.etc-coord-table tbody tr');
        const constrRow = sourceEl.closest('table.etc-construction-table tbody tr');
        const lineRow =
          String(rawRef).trim().startsWith('{')
            ? sourceEl.closest('table.etc-mode-lines tbody tr')
            : null;
        const srcRow = coordRow || constrRow || lineRow;
        if (srcRow) {
          srcRow.classList.add('etc-row-highlight');
          this.activeEls.add(srcRow);
        }
      }
      allCanonicalForText.forEach((ck) => {
        const textSet = this.textIndex.get(ck);
        if (textSet) {
          textSet.forEach((txtEl) => {
            txtEl.classList.add('geom-highlight-text');
            this.activeEls.add(txtEl);
          });
        }
        if (fromSvg) {
          const rowSet = this.textRowsIndex.get(ck);
          if (rowSet) {
            rowSet.forEach((tr) => {
              tr.classList.add('etc-row-highlight');
              this.activeEls.add(tr);
            });
          }
        }
      });

      // 3. Show symbolic MathJax HUD placed near (never over) the highlighted element
      this.updateHud(primaryInfo, primaryId, Boolean(this.pinnedKey), matchedEls);
      return true;
    }

    bindSvgInteraction(svgEl) {
      svgEl.addEventListener('mouseover', (event) => {
        if (this.isPanning || this.pinnedKey) return;
        const target = event.target.closest('[data-id], [data-ref]');
        if (target && svgEl.contains(target) && !target.closest('#highlights')) {
          const ref = target.getAttribute('data-id') || target.getAttribute('data-ref');
          this.activateHover(ref, { fromSvg: true });
        } else {
          this.clearHover();
        }
      });

      svgEl.addEventListener('mouseout', (event) => {
        if (this.isPanning || this.pinnedKey) return;
        const rel = event.relatedTarget ? event.relatedTarget.closest?.('[data-id], [data-ref]') : null;
        if (!rel || !svgEl.contains(rel)) {
          this.clearHover();
        }
      });

      svgEl.addEventListener(
        'wheel',
        (event) => {
          event.preventDefault();
          const factor = event.deltaY > 0 ? 1.12 : 1 / 1.12;
          this.zoomBy(factor, event.clientX, event.clientY);
        },
        { passive: false }
      );

      svgEl.addEventListener('mousedown', (event) => {
        if (event.button !== 0) return;
        this.isPanning = true;
        this.didDrag = false;
        this.cachedRect = svgEl.getBoundingClientRect();
        this.startClient = { x: event.clientX, y: event.clientY };
        svgEl.classList.add('is-panning');
      });

      svgEl.addEventListener('mousemove', (event) => {
        if (!this.isPanning) return;
        const dxPx = event.clientX - this.startClient.x;
        const dyPx = event.clientY - this.startClient.y;
        if (Math.hypot(dxPx, dyPx) > 2) this.didDrag = true;
        const rect = this.cachedRect;
        if (rect.width > 0 && rect.height > 0) {
          const vb = this.currentViewBox;
          const dx = dxPx * (vb[2] / rect.width);
          const dy = dyPx * (vb[3] / rect.height);
          this.setViewBox([vb[0] - dx, vb[1] - dy, vb[2], vb[3]]);
        }
        this.startClient = { x: event.clientX, y: event.clientY };
      });

      svgEl.addEventListener('mouseleave', () => {
        if (this.isPanning) {
          this.isPanning = false;
          svgEl.classList.remove('is-panning');
        }
        this.clearHover();
      });

      svgEl.addEventListener('click', (event) => {
        if (this.didDrag) return;
        const target = event.target.closest('[data-id], [data-ref]');
        if (!target || !svgEl.contains(target)) {
          if (this.pinnedKey) this.unpin();
          return;
        }
        // On collection constellation pages (or live family constellations), clicking a center dot navigates to that center
        const pid = target.getAttribute('data-id') || target.getAttribute('data-ref') || '';
        const cm = pid.match(/^X_(\d+)$/);
        if (cm && target.tagName.toLowerCase() === 'circle') {
          const num = parseInt(cm[1], 10);
          if (typeof this.onPointClick === 'function' && this.onPointClick(num, target) === true) {
            return;
          }
          if (window.location.pathname.includes('/c-') && !window.location.pathname.includes('/x-')) {
            window.location.href = `../explore.html#X_${num}`;
            return;
          }
        }
        // Otherwise toggle pin on clicked element so user can copy/zoom HUD MathJax
        if (this.pinnedKey && this.pinnedKey === pid) {
          this.unpin();
        } else {
          this.activateHover(pid, { fromSvg: true, pin: true });
        }
      });

      svgEl.addEventListener('dblclick', (event) => {
        event.preventDefault();
        this.resetView();
      });
    }

    inferTargetModeForElement(el) {
      if (!el || !this.modeBar) return null;
      let candidate = null;
      const explicit = el.closest('[data-viewer-mode]');
      if (explicit) {
        candidate = explicit.getAttribute('data-viewer-mode');
      } else if (el.closest('.etc-mode-coordinates')) {
        candidate = 'coordinates';
      } else if (el.closest('.etc-mode-four-triangles')) {
        candidate = 'four_triangles';
      } else if (el.closest('.etc-mode-lines')) {
        candidate = 'lines';
      } else if (el.closest('.etc-mode-relations')) {
        candidate = 'relations';
      } else if (this.currentMode !== 'construction' && this.modeBar.querySelector('[data-mode="construction"]')) {
        candidate = 'construction';
      }
      if (!candidate) return null;
      return this.modeBar.querySelector(`[data-mode="${candidate}"]`) ? candidate : null;
    }

    injectTableModeTriggers(root) {
      const specs = [
        ['.etc-mode-coordinates', 'coordinates', 'Show Coordinates'],
        ['.etc-mode-four-triangles', 'four_triangles', 'Show Triangles'],
        ['.etc-mode-lines', 'lines', 'Show Central Lines'],
        ['.etc-mode-relations', 'relations', 'Show Relations'],
      ];
      specs.forEach(([sel, mode, label]) => {
        if (!this.modeBar || !this.modeBar.querySelector(`[data-mode="${mode}"]`)) return;
        root.querySelectorAll(`table${sel}`).forEach((tbl) => {
          const cap = tbl.querySelector('caption');
          if (!cap || cap.querySelector('.etc-view-trigger')) return;
          const btn = document.createElement('button');
          btn.type = 'button';
          btn.className = 'etc-view-trigger';
          btn.style.margin = '0 0 0 0.65rem';
          btn.setAttribute('data-etc-switch-mode', mode);
          btn.textContent = `${label} ↗`;
          cap.appendChild(btn);
        });
      });
    }

    bindTextDelegation() {
      const root =
        this.viewerEl.closest('article.book-reading-pane') ||
        document.querySelector('.book-content') ||
        document.body;
      if (!root || root.dataset.etcTextHoverBound === '1') return;
      root.dataset.etcTextHoverBound = '1';

      this.injectTableModeTriggers(root);

      window.addEventListener('mouseup', () => {
        if (this.isPanning && this.svg) {
          this.isPanning = false;
          this.svg.classList.remove('is-panning');
        }
      });

      root.addEventListener('mouseover', (e) => {
        if (this.pinnedKey) return;
        if (e.target.closest('.etc-viewer')) return;

        let refStr = null;
        let sourceEl = e.target.closest('.geom-ref[data-ref]');
        if (sourceEl) {
          refStr = sourceEl.getAttribute('data-ref');
        } else {
          const refLink = e.target.closest('a.reference.internal');
          if (refLink) {
            const txt = (refLink.textContent || '').trim();
            const xm = txt.match(/^X(?:_|\()?(\d+)\)?$/);
            if (xm) {
              sourceEl = refLink;
              refStr = `X_${xm[1]}`;
            }
          }
        }
        // Whole-row hover on Homogeneous Coordinate, Construction Elements & Central Lines tables
        if (!refStr && !e.target.closest('a')) {
          const coordRow = e.target.closest('table.etc-coord-table tbody tr, table.etc-construction-table tbody tr');
          if (coordRow) {
            const rowGeom = coordRow.querySelector('.geom-ref[data-ref]');
            if (rowGeom) {
              sourceEl = rowGeom;
              refStr = rowGeom.getAttribute('data-ref');
            }
          } else {
            const lineRow = e.target.closest('table.etc-mode-lines tbody tr');
            if (lineRow) {
              const lineGeom =
                lineRow.querySelector('td:nth-child(2) .geom-ref[data-ref]') ||
                lineRow.querySelector('.geom-ref[data-ref^="{"]');
              if (lineGeom) {
                sourceEl = lineGeom;
                refStr = lineGeom.getAttribute('data-ref');
              }
            }
          }
        }
        if (!refStr) return;

        // Highlight matching elements in the active SVG ONLY — never hijack/swap view modes on hover
        if (this.hasCanonicalKey(refStr)) {
          this.activateHover(refStr, { fromSvg: false, sourceEl });
        }
      });

      root.addEventListener('mouseout', (e) => {
        if (this.pinnedKey) return;
        if (e.target.closest('.etc-viewer')) return;
        const rowSel = 'table.etc-coord-table tbody tr, table.etc-construction-table tbody tr, table.etc-mode-lines tbody tr';
        const fromRow = e.target.closest(rowSel);
        if (fromRow) {
          const toRow = e.relatedTarget ? e.relatedTarget.closest?.(rowSel) : null;
          if (toRow === fromRow) return;
          this.clearHover();
          return;
        }
        const fromRef = e.target.closest('.geom-ref[data-ref], a.reference.internal');
        if (!fromRef) return;
        const toRef = e.relatedTarget ? e.relatedTarget.closest?.('.geom-ref[data-ref], a.reference.internal') : null;
        if (toRef !== fromRef) {
          this.clearHover();
        }
      });

      // Clicking a non-link .geom-ref (or coordinate/construction/line table row) pins highlight & HUD
      root.addEventListener('click', (e) => {
        if (e.target.closest('.etc-viewer') || e.target.closest('a')) return;
        let span = e.target.closest('.geom-ref[data-ref]');
        if (!span && !e.target.closest('mjx-container')) {
          const coordRow = e.target.closest('table.etc-coord-table tbody tr, table.etc-construction-table tbody tr');
          if (coordRow) {
            span = coordRow.querySelector('.geom-ref[data-ref]');
          } else {
            const lineRow = e.target.closest('table.etc-mode-lines tbody tr');
            if (lineRow) {
              span =
                lineRow.querySelector('td:nth-child(2) .geom-ref[data-ref]') ||
                lineRow.querySelector('.geom-ref[data-ref^="{"]');
            }
          }
        }
        if (!span) return;
        const refStr = span.getAttribute('data-ref');
        if (!refStr) return;

        const doPin = () => {
          const { primaryId } = this.resolveSvgMatches(refStr);
          if (this.pinnedKey && primaryId && this.pinnedKey === primaryId) {
            this.unpin();
          } else {
            this.activateHover(refStr, { fromSvg: false, pin: true, sourceEl: span });
          }
        };

        if (this.hasCanonicalKey(refStr)) {
          doPin();
        } else {
          const wantMode = this.inferTargetModeForElement(span);
          if (wantMode && wantMode !== this.currentMode) {
            this.switchMode(wantMode).then((ok) => {
              if (ok) doPin();
            });
          }
        }
      });
    }
  }

  function initLazyDetailsMath() {
    const hydrate = (det) => {
      if (!det.open) return;
      const lazyBody = det.querySelector('.etc-lazy-math');
      if (!lazyBody) return;
      lazyBody.classList.remove('etc-lazy-math');
      const runTypeset = () => {
        if (window.MathJax && typeof window.MathJax.typesetPromise === 'function') {
          window.MathJax.typesetPromise([lazyBody]).catch(() => {});
        }
      };
      if (window.MathJax && window.MathJax.startup && window.MathJax.startup.promise) {
        window.MathJax.startup.promise.then(runTypeset).catch(() => {});
      } else {
        runTypeset();
      }
    };
    document.querySelectorAll('details.book-collapse').forEach((det) => {
      if (det.open) hydrate(det);
      det.addEventListener('toggle', () => hydrate(det));
    });
  }

  function initAllViewers() {
    const controllers = [];
    document.querySelectorAll('.etc-viewer').forEach((el) => {
      if (el.dataset.etcViewerInit === '1' || el.dataset.etcLive === '1') return;
      el.dataset.etcViewerInit = '1';
      controllers.push(new EtcViewerController(el));
    });
    initLazyDetailsMath();
    window.ETCViewers = controllers;
  }

  window.ETCViewer = {
    init: initAllViewers,
    Controller: EtcViewerController,
    canonicalKeys,
    clipInfiniteLineToBox,
  };

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initAllViewers);
  } else {
    initAllViewers();
  }
})(window, document);
