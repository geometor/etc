/**
 * GEOMETOR ETC — Universal Live Sharded Center Explorer (X_1 .. X_80000+)
 *
 * Renders the full 5-track tabular Book Codex + 7-triangle interactive SVG
 * suite client-side from compact 100-center exact symbolic JSON shards
 * (`_static/data/shards/s-XXXXX-YYYYY.json`), reusing `ETCViewer.Controller`
 * and `etc-viewer.css` for identical pan/zoom, Fit breathing padding, docked
 * footer, 8-slot anti-crowding labels, smart HUD, and Fullscreen App Mode (F).
 */
(function (window, document) {
  'use strict';

  const TRI_ORDER = [
    { key: 'heronian', tab: 'acute', short: 'Heronian', title: 'Heronian (15, 13, 14)', color: '#e8b85a', panel: 'panel-heronian' },
    { key: 'right', tab: 'right', short: '3, 4, 5', title: 'Right (5, 3, 4)', color: '#38bdf8', panel: 'panel-right' },
    { key: 'kepler', tab: 'kepler', short: 'Kepler', title: 'Kepler (φ, 1, √φ)', color: '#4ade80', panel: 'panel-kepler' },
    { key: 'kimberling', tab: 'kimberling', short: 'Kimberling', title: 'Kimberling (6, 9, 13)', color: '#a78bfa', panel: 'panel-kimberling' },
    { key: 'golden', tab: 'golden', short: 'Golden', title: 'Golden (φ, φ, 1)', color: '#fb923c', panel: 'panel-golden' },
    { key: 'gnomon', tab: 'gnomon', short: 'Gnomon', title: 'Gnomon (1, 1, φ)', color: '#f472b6', panel: 'panel-gnomon' },
    { key: 'equilateral', tab: 'equilateral', short: 'Equilateral', title: 'Equilateral (2, 2, 2)', color: '#2dd4bf', panel: 'panel-equilateral' },
  ];

  const TAB_TO_KEY = Object.fromEntries(TRI_ORDER.map((t) => [t.tab, t.key]));
  const KEY_TO_SPEC = Object.fromEntries(TRI_ORDER.map((t) => [t.key, t]));

  const LINE_PALETTE = [
    '#e8b85a',
    '#38bdf8',
    '#4ade80',
    '#f472b6',
    '#a78bfa',
    '#fb923c',
    '#2dd4bf',
    '#fb7185',
    '#facc15',
    '#60a5fa',
    '#c084fc',
    '#34d399',
  ];

  const TRACK_SPECS = [
    { key: 'overview', label: 'Overview', defaultMode: 'construction' },
    { key: 'lines', label: 'Lines', defaultMode: 'lines' },
    { key: 'relations', label: 'Relations', defaultMode: 'relations' },
    { key: 'notes', label: 'Notes', defaultMode: 'construction' },
    { key: 'code', label: 'Code', defaultMode: 'construction' },
  ];

  function esc(str) {
    return String(str == null ? '' : str)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;');
  }

  function texSpan(ltx) {
    if (!ltx) return '';
    return `<span class="math notranslate nohighlight">\\(${esc(ltx)}\\)</span>`;
  }

  function formatXLinks(text, currentNum) {
    if (!text) return '';
    // Preserve TeX \(...\) blocks inside Sphinx-compatible <span class="math"> while linking bare X_n / X(n)
    const parts = String(text).split(/(\\\([\s\S]*?\\\))/g);
    return parts
      .map((seg, idx) => {
        if (idx % 2 === 1) {
          return `<span class="math notranslate nohighlight">${esc(seg)}</span>`;
        }
        return esc(seg).replace(/(?<![A-Za-z0-9_])X(?:_(\d+)|\((\d+)\))/g, (_, d1, d2) => {
          const n = parseInt(d1 || d2, 10);
          if (n === currentNum) {
            return `<strong>X<sub>${n}</sub></strong>`;
          }
          return `<a class="etc-live-xref" href="#X_${n}" data-jump-x="${n}">X<sub>${n}</sub></a>`;
        });
      })
      .join('');
  }

  function cyclicPermuteLatex(expr, steps) {
    const s = ((steps % 3) + 3) % 3;
    if (s === 0 || !expr) return expr;
    const low = { a: 'b', b: 'c', c: 'a' };
    const up = { A: 'B', B: 'C', C: 'A' };
    const permChar = (ch) => {
      let o = ch;
      for (let i = 0; i < s; i++) {
        if (low[o]) o = low[o];
        else if (up[o]) o = up[o];
      }
      return o;
    };
    const re =
      /(\\operatorname\{[^}]+\}|\\text\{[^}]+\}|\\mathrm\{[^}]+\}|\\[A-Za-z]+|(?<![A-Za-z\\])(?:Area|area|ABC)(?![A-Za-z])|(?<![A-Za-z\\])(?:S|r)_\{?[ABCabc]\}?|(?<![A-Za-z\\])[abc]+(?![A-Za-z])|(?<![A-Za-z\\])[ABC](?![A-Za-z]))/g;
    return expr.replace(re, (tok) => {
      if (tok.startsWith('\\') || tok === 'Area' || tok === 'area' || tok === 'ABC' || tok === 'abc') {
        return tok;
      }
      if (tok.length >= 3 && (tok[0] === 'S' || tok[0] === 'r') && tok[1] === '_') {
        return tok.slice(0, 2) + tok.slice(2).split('').map(permChar).join('');
      }
      return tok.split('').map(permChar).join('');
    });
  }

  function splitTopColons(expr) {
    const parts = [];
    let buf = '';
    let depth = 0;
    for (let i = 0; i < expr.length; i++) {
      const ch = expr[i];
      if ('({['.includes(ch)) depth++;
      else if (')}]'.includes(ch)) depth = Math.max(0, depth - 1);
      if (ch === ':' && depth === 0) {
        parts.push(buf.trim());
        buf = '';
      } else {
        buf += ch;
      }
    }
    parts.push(buf.trim());
    return parts;
  }

  function extractCoordTriple(entry) {
    if (!entry) return null;
    if (entry.m) {
      const parts = splitTopColons(entry.m);
      const c1 = parts[0] || entry.m;
      const c2 = parts[1] ? parts[1] : cyclicPermuteLatex(c1, 1);
      const c3 = parts[2] ? parts[2] : cyclicPermuteLatex(c1, 2);
      return { isMath: true, c: [c1, c2, c3], note: entry.w || '' };
    }
    if (entry.t) {
      const parts = splitTopColons(entry.t);
      const c1 = parts[0] || entry.t;
      const c2 = parts[1] || c1.replace(/\bA-/g, 'B-');
      const c3 = parts[2] || c1.replace(/\bA-/g, 'C-');
      return { isMath: false, c: [c1, c2, c3], note: '' };
    }
    return null;
  }

  function footOfPerp(px, py, x1, y1, x2, y2) {
    const dx = x2 - x1;
    const dy = y2 - y1;
    const d2 = dx * dx + dy * dy;
    if (d2 < 1e-12) return { x: x1, y: y1, t: 0 };
    const t = ((px - x1) * dx + (py - y1) * dy) / d2;
    return { x: x1 + t * dx, y: y1 + t * dy, t };
  }

  function rightAnglePath(vx, vy, p1x, p1y, p2x, p2y, sz) {
    const u1x = p1x - vx;
    const u1y = p1y - vy;
    const l1 = Math.hypot(u1x, u1y) || 1;
    const u2x = p2x - vx;
    const u2y = p2y - vy;
    const l2 = Math.hypot(u2x, u2y) || 1;
    const e1x = (u1x / l1) * sz;
    const e1y = (u1y / l1) * sz;
    const e2x = (u2x / l2) * sz;
    const e2y = (u2y / l2) * sz;
    return `M ${(vx + e1x).toFixed(4)},${(vy + e1y).toFixed(4)} L ${(vx + e1x + e2x).toFixed(4)},${(vy + e1y + e2y).toFixed(4)} L ${(vx + e2x).toFixed(4)},${(vy + e2y).toFixed(4)}`;
  }

  function circumcircle(A, B, C) {
    const ax = A[0], ay = A[1], bx = B[0], by = B[1], cx = C[0], cy = C[1];
    const d = 2 * (ax * (by - cy) + bx * (cy - ay) + cx * (ay - by));
    if (Math.abs(d) < 1e-12) return null;
    const a2 = ax * ax + ay * ay;
    const b2 = bx * bx + by * by;
    const c2 = cx * cx + cy * cy;
    const ux = (a2 * (by - cy) + b2 * (cy - ay) + c2 * (ay - by)) / d;
    const uy = (a2 * (cx - bx) + b2 * (ax - cx) + c2 * (bx - ax)) / d;
    return { cx: ux, cy: uy, r: Math.hypot(ux - ax, uy - ay) };
  }

  function incircle(A, B, C, sides) {
    const [a, b, c] = sides;
    const p = a + b + c;
    const ix = (a * A[0] + b * B[0] + c * C[0]) / p;
    const iy = (a * A[1] + b * B[1] + c * C[1]) / p;
    const s = p / 2;
    const area = Math.sqrt(Math.max(0, s * (s - a) * (s - b) * (s - c)));
    return { cx: ix, cy: iy, r: area / s };
  }

  function lineIntersection(p1, p2, p3, p4) {
    const x1 = p1[0], y1 = p1[1], x2 = p2[0], y2 = p2[1];
    const x3 = p3[0], y3 = p3[1], x4 = p4[0], y4 = p4[1];
    const denom = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4);
    if (Math.abs(denom) < 1e-10) return null;
    const det1 = x1 * y2 - y1 * x2;
    const det2 = x3 * y4 - y3 * x4;
    const ix = (det1 * (x3 - x4) - (x1 - x2) * det2) / denom;
    const iy = (det1 * (y3 - y4) - (y1 - y2) * det2) / denom;
    if (!Number.isFinite(ix) || !Number.isFinite(iy)) return null;
    return [ix, iy];
  }

  function secondCircleIntersection(cc, pOn, pThru) {
    if (!cc) return null;
    const dx = pThru[0] - pOn[0];
    const dy = pThru[1] - pOn[1];
    const d2 = dx * dx + dy * dy;
    if (d2 < 1e-12) return null;
    const t = -2 * ((pOn[0] - cc.cx) * dx + (pOn[1] - cc.cy) * dy) / d2;
    if (!Number.isFinite(t) || Math.abs(t) < 1e-7) return null;
    return [pOn[0] + t * dx, pOn[1] + t * dy];
  }

  function medialTriangle(A, B, C) {
    return {
      Ma: [(B[0] + C[0]) / 2, (B[1] + C[1]) / 2],
      Mb: [(C[0] + A[0]) / 2, (C[1] + A[1]) / 2],
      Mc: [(A[0] + B[0]) / 2, (A[1] + B[1]) / 2],
    };
  }

  function orthicTriangle(A, B, C) {
    const Ha = footOfPerp(A[0], A[1], B[0], B[1], C[0], C[1]);
    const Hb = footOfPerp(B[0], B[1], C[0], C[1], A[0], A[1]);
    const Hc = footOfPerp(C[0], C[1], A[0], A[1], B[0], B[1]);
    return { Ha: [Ha.x, Ha.y], Hb: [Hb.x, Hb.y], Hc: [Hc.x, Hc.y] };
  }

  function anticomplementaryTriangle(A, B, C) {
    return {
      Ap: [B[0] + C[0] - A[0], B[1] + C[1] - A[1]],
      Bp: [C[0] + A[0] - B[0], C[1] + A[1] - B[1]],
      Cp: [A[0] + B[0] - C[0], A[1] + B[1] - C[1]],
    };
  }

  function tangentialTriangle(A, B, C, cc) {
    if (!cc) return null;
    const tangPt = (V) => [V[0] - (V[1] - cc.cy), V[1] + (V[0] - cc.cx)];
    const tA2 = tangPt(A), tB2 = tangPt(B), tC2 = tangPt(C);
    const At = lineIntersection(B, tB2, C, tC2);
    const Bt = lineIntersection(C, tC2, A, tA2);
    const Ct = lineIntersection(A, tA2, B, tB2);
    if (!At || !Bt || !Ct) return null;
    return { At, Bt, Ct };
  }

  function circummedialTriangle(A, B, C, cc) {
    if (!cc) return null;
    const med = medialTriangle(A, B, C);
    const Am = secondCircleIntersection(cc, A, med.Ma);
    const Bm = secondCircleIntersection(cc, B, med.Mb);
    const Cm = secondCircleIntersection(cc, C, med.Mc);
    if (!Am || !Bm || !Cm) return null;
    return { Am, Bm, Cm };
  }

  function intouchTriangle(A, B, C, ic) {
    if (!ic) return null;
    const Ia = footOfPerp(ic.cx, ic.cy, B[0], B[1], C[0], C[1]);
    const Ib = footOfPerp(ic.cx, ic.cy, C[0], C[1], A[0], A[1]);
    const Ic = footOfPerp(ic.cx, ic.cy, A[0], A[1], B[0], B[1]);
    return { Ia: [Ia.x, Ia.y], Ib: [Ib.x, Ib.y], Ic: [Ic.x, Ic.y] };
  }

  function cevianTraces(A, B, C, P) {
    const Da = lineIntersection(A, P, B, C);
    const Db = lineIntersection(B, P, C, A);
    const Dc = lineIntersection(C, P, A, B);
    return { Da, Db, Dc };
  }

  function excenters(A, B, C, sides) {
    const [a, b, c] = sides;
    const s = (a + b + c) / 2;
    const area = Math.sqrt(Math.max(0, s * (s - a) * (s - b) * (s - c)));
    const da = -a + b + c;
    const db = a - b + c;
    const dc = a + b - c;
    if (da <= 1e-10 || db <= 1e-10 || dc <= 1e-10) return null;
    return {
      Ja: [(-a * A[0] + b * B[0] + c * C[0]) / da, (-a * A[1] + b * B[1] + c * C[1]) / da],
      Jb: [(a * A[0] - b * B[0] + c * C[0]) / db, (a * A[1] - b * B[1] + c * C[1]) / db],
      Jc: [(a * A[0] + b * B[0] - c * C[0]) / dc, (a * A[1] + b * B[1] - c * C[1]) / dc],
      ra: area / (s - a),
      rb: area / (s - b),
      rc: area / (s - c),
    };
  }

  function extouchTriangle(A, B, C, exc) {
    if (!exc) return null;
    const Ea = footOfPerp(exc.Ja[0], exc.Ja[1], B[0], B[1], C[0], C[1]);
    const Eb = footOfPerp(exc.Jb[0], exc.Jb[1], C[0], C[1], A[0], A[1]);
    const Ec = footOfPerp(exc.Jc[0], exc.Jc[1], A[0], A[1], B[0], B[1]);
    return { Ea: [Ea.x, Ea.y], Eb: [Eb.x, Eb.y], Ec: [Ec.x, Ec.y] };
  }

  function equilateralOnSide(P1, P2, P3, outward) {
    const mx = (P1[0] + P2[0]) / 2;
    const my = (P1[1] + P2[1]) / 2;
    let nx = -(P2[1] - P1[1]);
    let ny = P2[0] - P1[0];
    const dot = (P3[0] - mx) * nx + (P3[1] - my) * ny;
    if ((outward && dot > 0) || (!outward && dot < 0)) {
      nx = -nx;
      ny = -ny;
    }
    const s3 = Math.sqrt(3);
    return {
      apex: [mx + (s3 / 2) * nx, my + (s3 / 2) * ny],
      center: [mx + (s3 / 6) * nx, my + (s3 / 6) * ny],
    };
  }

  function ninePointCircle(A, B, C, cc) {
    if (!cc) return null;
    const H = [A[0] + B[0] + C[0] - 2 * cc.cx, A[1] + B[1] + C[1] - 2 * cc.cy];
    const N = [(cc.cx + H[0]) / 2, (cc.cy + H[1]) / 2];
    const med = medialTriangle(A, B, C);
    const ort = orthicTriangle(A, B, C);
    return {
      cx: N[0],
      cy: N[1],
      r: cc.r / 2,
      H,
      ...med,
      ...ort,
      Ea: [(A[0] + H[0]) / 2, (A[1] + H[1]) / 2],
      Eb: [(B[0] + H[0]) / 2, (B[1] + H[1]) / 2],
      Ec: [(C[0] + H[0]) / 2, (C[1] + H[1]) / 2],
    };
  }

  function resolveDataBaseUrl() {
    const scripts = document.querySelectorAll('script[src*="etc-live-viewer.js"]');
    if (scripts.length > 0) {
      const src = scripts[scripts.length - 1].getAttribute('src') || '';
      const idx = src.indexOf('js/etc-live-viewer.js');
      if (idx !== -1) {
        return src.slice(0, idx) + 'data/';
      }
    }
    return '../_static/data/';
  }

  class EtcLiveExplorer {
    constructor(rootEl) {
      this.rootEl = rootEl;
      this.dataBase = resolveDataBaseUrl();
      this.manifest = null;
      this.coreCenters = {};
      this.searchIndex = [];
      this.familiesData = { collections: [], families: [] };
      this.shardCache = new Map();

      this.currentNum = 1;
      this.currentTrack = 'overview';
      this.currentTriKey = 'heronian';
      this.currentCenter = null;
      this.currentFamilyId = null;
      this.currentFamilyObj = null;
      this.currentFamilyMembers = [];
      this.familyTab = 'families';
      this.controller = null;

      this.init();
    }

    async init() {
      this.buildShell();
      this.bindHeaderControls();
      this.parseHash();

      if (window.location.protocol === 'file:') {
        this.showFatal(
          'Browser security blocks fetching JSON shards over <code>file://</code>. Preview locally with <code>python3 -m http.server -d docs 8000</code> or on GitHub Pages.'
        );
        return;
      }

      try {
        const [mResp, cResp, sResp, fResp] = await Promise.all([
          fetch(`${this.dataBase}manifest.json`),
          fetch(`${this.dataBase}core-centers.json`),
          fetch(`${this.dataBase}search-index.json`),
          fetch(`${this.dataBase}families.json`).catch(() => ({ ok: false })),
        ]);
        if (!mResp.ok) throw new Error(`manifest.json HTTP ${mResp.status}`);
        this.manifest = await mResp.json();
        this.coreCenters = cResp.ok ? await cResp.json() : {};
        this.searchIndex = sResp.ok ? await sResp.json() : [];
        if (fResp && fResp.ok) {
          this.familiesData = await fResp.json();
        }

        this.updateCorpusBadge();
        this.renderFamilyDrawer();
        if (this.currentFamilyId) {
          await this.loadAndRenderFamily(this.currentFamilyId);
        } else {
          await this.loadAndRenderCenter(this.currentNum, this.currentTrack);
        }
      } catch (err) {
        this.showFatal(`Failed to initialize ETC Live Explorer: ${esc(err.message || err)}`);
      }

      window.addEventListener('hashchange', () => {
        const prevN = this.currentNum;
        const prevT = this.currentTrack;
        const prevF = this.currentFamilyId;
        this.parseHash();
        if (this.currentFamilyId) {
          if (this.currentFamilyId !== prevF) {
            this.loadAndRenderFamily(this.currentFamilyId);
          }
        } else if (this.currentNum !== prevN || this.currentTrack !== prevT || prevF) {
          this.loadAndRenderCenter(this.currentNum, this.currentTrack);
        }
      });
    }

    parseHash() {
      const h = (window.location.hash || '').replace(/^#/, '').trim();
      if (!h) {
        this.currentFamilyId = null;
        return;
      }
      const fm = h.match(/^family\/([A-Za-z0-9_-]+)$/i);
      if (fm) {
        this.currentFamilyId = fm[1];
        return;
      }
      this.currentFamilyId = null;
      const m = h.match(/^X[_(-]?(\d+)\)?(?:\/([a-z]+))?$/i);
      if (m) {
        const n = parseInt(m[1], 10);
        if (Number.isFinite(n) && n >= 1) this.currentNum = n;
        const tr = (m[2] || 'overview').toLowerCase();
        if (TRACK_SPECS.some((s) => s.key === tr)) this.currentTrack = tr;
      } else if (/^\d+$/.test(h)) {
        this.currentNum = parseInt(h, 10);
      }
    }

    setHash(num, track) {
      const target = track === 'overview' ? `#X_${num}` : `#X_${num}/${track}`;
      if (window.location.hash !== target) {
        window.history.replaceState(null, '', target);
      }
    }

    setFamilyHash(fid) {
      const target = `#family/${fid}`;
      if (window.location.hash !== target) {
        window.history.replaceState(null, '', target);
      }
    }

    showFatal(html) {
      if (this.proseEl) {
        this.proseEl.innerHTML = `<div class="admonition warning"><p class="admonition-title">Notice</p><p>${html}</p></div>`;
      }
    }

    buildShell() {
      const article = this.rootEl.closest('article.book-reading-pane');
      if (article) article.classList.add('has-etc-stage');

      const triTabsHtml = TRI_ORDER.map(
        (t, i) =>
          `<button type="button" class="etc-tab-btn${i === 0 ? ' active' : ''}" data-tab="${t.tab}" title="${esc(t.title)}">${esc(t.short)}</button>`
      ).join('');

      const modeTabsHtml = [
        ['construction', 'Construction'],
        ['coordinates', 'Coordinates'],
        ['lines', 'Lines'],
        ['relations', 'Relations'],
        ['four_triangles', 'Triangles'],
      ]
        .map(
          ([k, lbl], i) =>
            `<button type="button" class="etc-mode-btn${i === 0 ? ' active' : ''}" data-mode="${k}">${lbl}</button>`
        )
        .join('');

      const trackBtnsHtml = TRACK_SPECS.map(
        (t) =>
          `<a href="#X_${this.currentNum}/${t.key}" class="book-track-item${t.key === this.currentTrack ? ' is-active' : ''}" data-live-track="${t.key}">${t.label}</a>`
      ).join('<span class="book-track-sep">·</span>');

      this.rootEl.innerHTML = `
        <div class="etc-live-topbar">
          <div class="etc-live-nav">
            <button type="button" class="etc-live-nav-btn" data-nav="prev" title="Previous Center (Alt+Left)">← Prev</button>
            <button type="button" class="etc-live-nav-btn" data-nav="next" title="Next Center (Alt+Right)">Next →</button>
            <button type="button" class="etc-live-nav-btn" data-nav="random" title="Jump to Random Center">🎲 Random</button>
            <button type="button" class="etc-live-nav-btn" data-nav="families" title="Browse All 925 ETC Family Groups & 62 Curated Collections">📚 Families</button>
          </div>
          <div class="etc-live-search-wrap">
            <input type="search" class="etc-live-search" placeholder="Jump to X(n), name (Euler, Spieker…), or 6-9-13 search number…" aria-label="Search triangle centers" autocomplete="off" />
            <div class="etc-live-search-results" hidden></div>
          </div>
          <div class="etc-live-corpus-badge">Loading shards…</div>
        </div>
        <div class="etc-family-drawer" hidden>
          <div class="etc-family-drawer-head">
            <button type="button" class="etc-family-tab-btn active" data-fam-tab="families">ETC Families (925)</button>
            <button type="button" class="etc-family-tab-btn" data-fam-tab="collections">Curated Collections (62)</button>
            <input type="search" class="etc-family-filter" placeholder="Filter families by name (Euler, Kiepert, Morley…), Part, or X(n)…" aria-label="Filter family groups" autocomplete="off" />
            <button type="button" class="etc-live-nav-btn" data-nav="close-families">✕</button>
          </div>
          <div class="etc-family-list"></div>
        </div>
        <div class="etc-live-header">
          <h1 class="etc-live-h1">X<sub>1</sub></h1>
          <p class="rubric etc-live-subtitle">Loading…</p>
          <div class="etc-live-tracks-bar book-tracks">${trackBtnsHtml}</div>
          <div class="etc-identity-bar etc-live-identity math"></div>
          <div class="enunciation etc-live-enunciation math" hidden></div>
        </div>
        <div class="etc-split-workspace">
          <div class="etc-stage-column">
            <div class="etc-viewer" data-etc-live="1" data-default-mode="construction" data-default-triangle="acute">
              <div class="etc-viewer-chrome">
                <div class="etc-mode-tabs">${modeTabsHtml}</div>
                <div class="etc-triangle-tabs">${triTabsHtml}</div>
              </div>
              <div class="etc-svg-stage"></div>
              <div class="etc-viewer-caption math"><p>Loading symbolic coordinates…</p></div>
            </div>
          </div>
          <div class="etc-prose-column etc-live-prose math"></div>
        </div>
      `;

      this.h1El = this.rootEl.querySelector('.etc-live-h1');
      this.subtitleEl = this.rootEl.querySelector('.etc-live-subtitle');
      this.tracksBarEl = this.rootEl.querySelector('.etc-live-tracks-bar');
      this.identityEl = this.rootEl.querySelector('.etc-live-identity');
      this.enunciationEl = this.rootEl.querySelector('.etc-live-enunciation');
      this.viewerEl = this.rootEl.querySelector('.etc-viewer');
      this.proseEl = this.rootEl.querySelector('.etc-live-prose');
      this.searchInput = this.rootEl.querySelector('.etc-live-search');
      this.searchResults = this.rootEl.querySelector('.etc-live-search-results');
      this.badgeEl = this.rootEl.querySelector('.etc-live-corpus-badge');
      this.familyDrawerEl = this.rootEl.querySelector('.etc-family-drawer');
      this.familyFilterInput = this.rootEl.querySelector('.etc-family-filter');
      this.familyListEl = this.rootEl.querySelector('.etc-family-list');
    }

    updateCorpusBadge() {
      if (!this.manifest || !this.badgeEl) return;
      const tot = this.manifest.total_centers || 0;
      const ex = this.manifest.stats?.heronian?.exact || 0;
      const pct = tot > 0 ? ((100 * ex) / tot).toFixed(1) : '0.0';
      const famCnt = this.familiesData?.families?.length || 925;
      this.badgeEl.textContent = `${tot.toLocaleString()} centers • ${famCnt} families • ${pct}% exact`;
    }

    bindHeaderControls() {
      this.rootEl.addEventListener('click', (e) => {
        const navBtn = e.target.closest('button[data-nav]');
        if (navBtn) {
          e.preventDefault();
          const act = navBtn.dataset.nav;
          const maxN = this.manifest?.max_center || 4000;
          if (act === 'prev') this.navigateTo(Math.max(1, this.currentNum - 1), this.currentTrack);
          else if (act === 'next') this.navigateTo(Math.min(maxN, this.currentNum + 1), this.currentTrack);
          else if (act === 'random') {
            const rnd = 1 + Math.floor(Math.random() * maxN);
            this.navigateTo(rnd, this.currentTrack);
          } else if (act === 'families') {
            if (this.familyDrawerEl) {
              this.familyDrawerEl.hidden = !this.familyDrawerEl.hidden;
              if (!this.familyDrawerEl.hidden) {
                this.renderFamilyDrawer();
                this.familyFilterInput?.focus();
              }
            }
          } else if (act === 'close-families') {
            if (this.familyDrawerEl) this.familyDrawerEl.hidden = true;
          }
          return;
        }
        const famTabBtn = e.target.closest('button[data-fam-tab]');
        if (famTabBtn) {
          e.preventDefault();
          this.familyTab = famTabBtn.dataset.famTab;
          this.familyDrawerEl?.querySelectorAll('button[data-fam-tab]').forEach((b) => {
            b.classList.toggle('active', b.dataset.famTab === this.familyTab);
          });
          this.renderFamilyDrawer();
          return;
        }
        const famPick = e.target.closest('[data-jump-family]');
        if (famPick) {
          e.preventDefault();
          const fid = famPick.dataset.jumpFamily;
          if (this.familyDrawerEl) this.familyDrawerEl.hidden = true;
          if (fid) this.navigateToFamily(fid);
          return;
        }
        const trackLink = e.target.closest('a[data-live-track]');
        if (trackLink) {
          e.preventDefault();
          this.navigateTo(this.currentNum, trackLink.dataset.liveTrack);
          return;
        }
        const xref = e.target.closest('a[data-jump-x]');
        if (xref) {
          e.preventDefault();
          const n = parseInt(xref.dataset.jumpX, 10);
          if (Number.isFinite(n)) this.navigateTo(n, this.currentTrack);
          return;
        }
        const resItem = e.target.closest('[data-search-pick]');
        if (resItem) {
          e.preventDefault();
          const n = parseInt(resItem.dataset.searchPick, 10);
          this.searchResults.hidden = true;
          this.searchInput.value = '';
          if (Number.isFinite(n)) this.navigateTo(n, this.currentTrack);
        }
      });

      if (this.familyFilterInput) {
        this.familyFilterInput.addEventListener('input', () => this.renderFamilyDrawer());
      }

      this.searchInput.addEventListener('input', () => this.renderSearchDropdown());
      this.searchInput.addEventListener('keydown', (e) => {
        if (e.key === 'Enter') {
          e.preventDefault();
          const q = this.searchInput.value.trim();
          const m = q.match(/^(?:X[_(-]?)?(\d+)\)?$/i);
          if (m) {
            this.searchResults.hidden = true;
            this.searchInput.value = '';
            this.navigateTo(parseInt(m[1], 10), this.currentTrack);
            return;
          }
          const first = this.searchResults.querySelector('[data-search-pick]');
          if (first) first.click();
        } else if (e.key === 'Escape') {
          this.searchResults.hidden = true;
        }
      });

      document.addEventListener('click', (e) => {
        if (!e.target.closest('.etc-live-search-wrap') && this.searchResults) {
          this.searchResults.hidden = true;
        }
      });
    }

    renderSearchDropdown() {
      const q = (this.searchInput.value || '').trim();
      if (!q || this.searchIndex.length === 0) {
        this.searchResults.hidden = true;
        return;
      }

      let matches = [];
      // 1. Direct X_n integer query
      const mInt = q.match(/^(?:X[_(-]?)?(\d+)\)?$/i);
      if (mInt) {
        const targetN = parseInt(mInt[1], 10);
        const prefix = String(targetN);
        for (let i = 0; i < this.searchIndex.length && matches.length < 14; i++) {
          const row = this.searchIndex[i];
          if (row[0] === targetN || String(row[0]).startsWith(prefix)) {
            matches.push({ row, score: row[0] === targetN ? 0 : 1 });
          }
        }
        matches.sort((a, b) => a.score - b.score || a.row[0] - b.row[0]);
      } else if (/^[+-]?\d*\.\d+$/.test(q)) {
        // 2. Kimberling (6, 9, 13) decimal search value proximity lookup!
        const targetVal = parseFloat(q);
        const scored = [];
        for (let i = 0; i < this.searchIndex.length; i++) {
          const row = this.searchIndex[i];
          if (typeof row[2] === 'number') {
            scored.push({ row, diff: Math.abs(row[2] - targetVal) });
          }
        }
        scored.sort((a, b) => a.diff - b.diff);
        matches = scored.slice(0, 14);
      } else {
        // 3. Name / title keyword search
        const ql = q.toLowerCase();
        for (let i = 0; i < this.searchIndex.length && matches.length < 18; i++) {
          const row = this.searchIndex[i];
          if ((row[1] || '').toLowerCase().includes(ql)) {
            matches.push({ row });
          }
        }
      }

      if (matches.length === 0) {
        this.searchResults.innerHTML = '<div class="etc-live-search-empty">No matching centers found.</div>';
        this.searchResults.hidden = false;
        return;
      }

      this.searchResults.innerHTML = matches
        .map(({ row }) => {
          const svStr = typeof row[2] === 'number' ? row[2].toFixed(6) : '—';
          const pBadge = row[3] === 'e' ? 'Exact' : row[3] === 'm' ? '50-dig' : '—';
          return `<button type="button" class="etc-live-search-item" data-search-pick="${row[0]}">
            <span class="etc-ls-id">X<sub>${row[0]}</sub></span>
            <span class="etc-ls-title">${esc(row[1])}</span>
            <span class="etc-ls-meta">${svStr} · ${pBadge}</span>
          </button>`;
        })
        .join('');
      this.searchResults.hidden = false;
    }

    async fetchShardFor(num) {
      const sz = this.manifest?.shard_size || 100;
      const start = Math.floor((num - 1) / sz) * sz + 1;
      const end = start + sz - 1;
      const key = `s-${String(start).padStart(5, '0')}-${String(end).padStart(5, '0')}`;
      if (this.shardCache.has(key)) return this.shardCache.get(key);
      const resp = await fetch(`${this.dataBase}shards/${key}.json`);
      if (!resp.ok) throw new Error(`Shard ${key}.json HTTP ${resp.status}`);
      const data = await resp.json();
      this.shardCache.set(key, data);
      return data;
    }

    findFamiliesForCenter(n) {
      const fams = (this.familiesData?.families || []).filter((f) => f.start <= n && n <= f.end);
      // Sort tightest range first
      fams.sort((a, b) => a.end - a.start - (b.end - b.start) || a.idx - b.idx);
      const col = (this.familiesData?.collections || []).find((c) => c.start <= n && n <= c.end) || null;
      return { families: fams, collection: col };
    }

    resolveFamilyById(fid) {
      if (!fid) return null;
      const f = (this.familiesData?.families || []).find((x) => x.id === fid);
      if (f) return { kind: 'family', id: f.id, start: f.start, end: f.end, title: f.title, part: f.part, p: f.p || [] };
      const c = (this.familiesData?.collections || []).find((x) => x.slug === fid);
      if (c) return { kind: 'collection', id: c.slug, start: c.start, end: c.end, title: c.title, part: null, p: c.summary ? [c.summary] : [] };
      return null;
    }

    renderFamilyDrawer() {
      if (!this.familyListEl) return;
      const q = (this.familyFilterInput?.value || '').trim().toLowerCase();
      const numQ = q.match(/^(?:x[_(-]?)?(\d+)\)?$/i) ? parseInt(q.replace(/\D/g, ''), 10) : null;
      const isCol = this.familyTab === 'collections';
      const src = isCol ? this.familiesData?.collections || [] : this.familiesData?.families || [];
      const matches = [];
      for (let i = 0; i < src.length && matches.length < 80; i++) {
        const item = src[i];
        if (!q) {
          matches.push(item);
          continue;
        }
        if (numQ !== null && item.start <= numQ && numQ <= item.end) {
          matches.push(item);
          continue;
        }
        const hay = `${item.title || ''} part ${item.part || ''} ${item.start}-${item.end} ${item.summary || ''}`.toLowerCase();
        if (hay.includes(q)) matches.push(item);
      }
      if (matches.length === 0) {
        this.familyListEl.innerHTML = '<div class="etc-live-search-empty">No matching family groups found.</div>';
        return;
      }
      this.familyListEl.innerHTML = matches
        .map((item) => {
          const fid = isCol ? item.slug : item.id;
          const partStr = !isCol && item.part ? ` · Part ${item.part}` : '';
          const cnt = Math.max(1, item.end - item.start + 1);
          return `<button type="button" class="etc-family-card" data-jump-family="${esc(fid)}">
            <span class="etc-family-card-range">X<sub>${item.start}</sub>–X<sub>${item.end}</sub> (${cnt})${esc(partStr)}</span>
            <span class="etc-family-card-title">${esc(item.title)}</span>
          </button>`;
        })
        .join('');
    }

    async navigateToFamily(fid) {
      this.currentFamilyId = fid;
      this.setFamilyHash(fid);
      await this.loadAndRenderFamily(fid);
    }

    async loadAndRenderFamily(fid) {
      const fam = this.resolveFamilyById(fid);
      if (!fam) {
        this.showFatal(`Family group <code>${esc(fid)}</code> not found.`);
        return;
      }
      this.currentFamilyObj = fam;
      this.currentCenter = null;

      // Load member centers (cap rendered constellation + table to 120 members cleanly)
      const capEnd = Math.min(fam.end, fam.start + 119);
      const sz = this.manifest?.shard_size || 100;
      const firstShard = Math.floor((fam.start - 1) / sz) * sz + 1;
      const lastShard = Math.floor((capEnd - 1) / sz) * sz + 1;
      const shardStarts = [];
      for (let s = firstShard; s <= lastShard; s += sz) shardStarts.push(s);
      const shards = await Promise.all(shardStarts.map((s) => this.fetchShardFor(s).catch(() => null)));

      const members = [];
      for (let num = fam.start; num <= capEnd; num++) {
        for (const sh of shards) {
          if (sh && sh.centers && sh.centers[String(num)]) {
            members.push(sh.centers[String(num)]);
            break;
          }
        }
      }
      this.currentFamilyMembers = members;

      const triTab = this.controller ? this.controller.currentTriangle : 'acute';
      this.currentTriKey = TAB_TO_KEY[triTab] || 'heronian';

      // Header
      document.title = `X_${fam.start}–X_${fam.end} — ${fam.title} • Encyclopedia of Triangle Centers`;
      this.h1El.innerHTML = `X<sub>${fam.start}</sub>–X<sub>${fam.end}</sub>`;
      this.subtitleEl.innerHTML = formatXLinks(fam.title, -1);
      if (this.tracksBarEl) this.tracksBarEl.style.display = 'none';
      const totalSpan = fam.end - fam.start + 1;
      const partMeta = fam.part ? ` • <strong>ETC Part ${fam.part}</strong>` : '';
      const staticColLink =
        fam.kind === 'collection'
          ? ` • <a href="${esc(fam.id)}/index.html">Static Chapter Page ↗</a>`
          : '';
      this.identityEl.innerHTML = `<p><span class="etc-family-badge">Family Constellation</span> • <strong>${totalSpan} centers</strong> (X<sub>${fam.start}</sub>–X<sub>${fam.end}</sub>)${partMeta} • <a class="etc-live-xref" href="#X_${fam.start}" data-jump-x="${fam.start}">Inspect X<sub>${fam.start}</sub> →</a>${staticColLink}</p>`;
      this.enunciationEl.hidden = true;

      // Right Panel: Preamble Essay + Member Centers Table
      let proseHtml = '';
      if (fam.p && fam.p.length > 0) {
        proseHtml += `<div class="etc-family-preamble-box"><h3>Group Preamble — ${esc(fam.title)}</h3>${fam.p.map((para) => `<p>${formatXLinks(para, -1)}</p>`).join('')}</div>`;
      }
      const rows = members
        .map((c, idx) => {
          const col = LINE_PALETTE[idx % LINE_PALETTE.length];
          const kRec = c.tris?.kimberling;
          const hRec = c.tris?.heronian;
          const svTxt = kRec && typeof kRec.sv === 'number' ? kRec.sv.toFixed(6) : '—';
          const fStr = hRec ? hRec.f || this.manifest?.triangles?.heronian?.field || '\\mathbb{Q}' : '';
          const pTxt = hRec?.p === 'e' ? texSpan(fStr) : hRec?.p === 'm' ? '50-dig' : '—';
          return `<tr style="--etc-el-color:${col}">
            <td><p><span class="geom-ref" data-ref="X_${c.n}"><a class="etc-live-xref" href="#X_${c.n}" data-jump-x="${c.n}">X<sub>${c.n}</sub></a></span></p></td>
            <td><p>${formatXLinks(c.t || `X_${c.n}`, c.n)}</p></td>
            <td><p><code>${svTxt}</code></p></td>
            <td><p>${pTxt}</p></td>
          </tr>`;
        })
        .join('');
      const truncNote = fam.end > capEnd ? ` (showing first ${members.length} of ${totalSpan})` : ` (${members.length})`;
      proseHtml += `
        <h2>Family Member Centers${truncNote}</h2>
        <table class="docutils align-default etc-table etc-construction-table">
          <thead><tr><th>Center</th><th>Name</th><th>Search (6,9,13)</th><th>Field</th></tr></thead>
          <tbody>${rows}</tbody>
        </table>
      `;
      this.proseEl.innerHTML = proseHtml;

      this.ensureController();
      if (this.controller) {
        const svgHtml = this.buildFamilyConstellationSvg(fam, members, this.currentTriKey);
        const svgEl = this.controller.parseSvgFromHtml(svgHtml);
        this.controller.unpin();
        this.controller.clearHover();
        this.controller.currentMode = 'construction';
        this.controller.showLines = false;
        if (svgEl) {
          this.controller.mountSvg(svgEl, { applyModeLines: false });
        }
        this.controller.buildTextIndex();
        this.controller.syncTableColorsFromSvg();
        this.controller.syncModeButtons();
        this.controller.syncToolbarButtons();
        if (typeof this.controller.syncAppBar === 'function') this.controller.syncAppBar();
        this.controller.updateCaption(
          `<strong>Family Constellation</strong>: X<sub>${fam.start}</sub>–X<sub>${fam.end}</sub> (${esc(fam.title)}) on ${esc((KEY_TO_SPEC[this.currentTriKey] || TRI_ORDER[0]).title)}. Click any center dot to open its full construction.`
        );
      }
      this.typesetMath(this.rootEl);
    }

    buildFamilyConstellationSvg(fam, members, triKey) {
      const tMeta = this.manifest.triangles[triKey] || this.manifest.triangles.heronian;
      const A = tMeta.verts.A, B = tMeta.verts.B, C = tMeta.verts.C;
      const centroid = [(A[0] + B[0] + C[0]) / 3, (A[1] + B[1] + C[1]) / 3];
      const span = Math.max(...tMeta.sides);
      const pts = [A, B, C];
      const finiteMembers = [];
      members.forEach((c, idx) => {
        const rec = c.tris?.[triKey];
        if (rec && rec.st === 'f' && Array.isArray(rec.xy)) {
          finiteMembers.push({ c, xy: rec.xy, rec, col: LINE_PALETTE[idx % LINE_PALETTE.length] });
          if (Math.hypot(rec.xy[0] - centroid[0], rec.xy[1] - centroid[1]) < span * 2.5) {
            pts.push(rec.xy);
          }
        }
      });

      const xs = pts.map((p) => p[0]);
      const ys = pts.map((p) => -p[1]);
      const minX = Math.min(...xs), maxX = Math.max(...xs);
      const minY = Math.min(...ys), maxY = Math.max(...ys);
      const w0 = Math.max(maxX - minX, span * 0.5);
      const h0 = Math.max(maxY - minY, span * 0.5);
      const pad = Math.max(w0, h0) * 0.14;
      const vbW = w0 + 2 * pad;
      const vbH = Math.max(h0 + 2 * pad, vbW * 0.72);
      const vb = [(minX + maxX) * 0.5 - vbW * 0.5, (minY + maxY) * 0.5 - vbH * 0.5, vbW, vbH];
      const vbStr = vb.map((v) => v.toFixed(6)).join(' ');

      const linesSvg = [];
      const ptsSvg = [];
      const lblSvg = [];
      const meta = {};

      const cc = circumcircle(A, B, C);
      if (cc) linesSvg.push(`<circle class="guide circumcircle" data-id="circumcircle" style="stroke:#a78bfa" cx="${cc.cx.toFixed(6)}" cy="${(-cc.cy).toFixed(6)}" r="${cc.r.toFixed(6)}" />`);
      const ic = incircle(A, B, C, tMeta.sides);
      if (ic && ic.r > 0) linesSvg.push(`<circle class="guide incircle" data-id="incircle" style="stroke:#e040fb" cx="${ic.cx.toFixed(6)}" cy="${(-ic.cy).toFixed(6)}" r="${ic.r.toFixed(6)}" />`);

      [
        ['A', A, -18, 18],
        ['B', B, 14, 18],
        ['C', C, 12, -12],
      ].forEach(([vid, vxy, ox, oy]) => {
        ptsSvg.push(`<circle class="given vertex" data-id="${vid}" cx="${vxy[0].toFixed(6)}" cy="${(-vxy[1]).toFixed(6)}" r="0.01" />`);
        lblSvg.push(`<text class="given-label" data-point-id="${vid}" data-anchor-x="${vxy[0].toFixed(6)}" data-anchor-y="${(-vxy[1]).toFixed(6)}" data-offset-x="${ox}" data-offset-y="${oy}" x="${vxy[0].toFixed(6)}" y="${(-vxy[1]).toFixed(6)}">${vid}</text>`);
      });

      finiteMembers.forEach(({ c, xy, rec, col }) => {
        const pid = `X_${c.n}`;
        const sx = xy[0], sy = -xy[1];
        ptsSvg.push(`<circle class="center" data-id="${pid}" style="fill:${col}" cx="${sx.toFixed(6)}" cy="${sy.toFixed(6)}" r="0.01" />`);
        lblSvg.push(
          `<text class="point-label" data-point-id="${pid}" data-anchor-x="${sx.toFixed(6)}" data-anchor-y="${sy.toFixed(6)}" data-offset-x="10" data-offset-y="-8" x="${sx.toFixed(6)}" y="${sy.toFixed(6)}">X<tspan class="sub" dy="0.28em" font-size="0.72em">${c.n}</tspan></text>`
        );
        meta[pid] = {
          ID: pid,
          name: c.t || pid,
          type: 'family member (click to open)',
          color: col,
          symbolic_rows: [
            ...(rec.bl ? [{ label: 'Barycentric', latex: rec.bl, pretty: rec.bl }] : []),
            ...(rec.xyl ? [{ label: 'Cartesian', latex: rec.xyl, pretty: rec.xyl }] : []),
          ],
          approx: `≈ (${xy[0].toFixed(5)}, ${xy[1].toFixed(5)})`,
        };
      });

      const polyPts = `${A[0].toFixed(6)},${(-A[1]).toFixed(6)} ${B[0].toFixed(6)},${(-B[1]).toFixed(6)} ${C[0].toFixed(6)},${(-C[1]).toFixed(6)}`;
      const subtitleText = `${tMeta.label} | Family X_${fam.start}–X_${fam.end} | ${finiteMembers.length} finite centers plotted`;
      return `<svg class="geometor-etc-drawing" xmlns="http://www.w3.org/2000/svg" viewBox="${vbStr}" data-initial-viewbox="${vbStr}" data-triangle="${triKey}" data-tri-span="${span.toFixed(6)}" preserveAspectRatio="xMidYMid meet">
        <g id="graphics"><polygon data-id="< A B C >" points="${polyPts}" /></g>
        <g id="elements">${linesSvg.join('')}</g>
        <g id="highlights"></g>
        <g id="points">${ptsSvg.join('')}</g>
        <g id="labels">
          ${lblSvg.join('')}
          <text class="subtitle-label" x="${vb[0].toFixed(4)}" y="${(vb[1] + vb[3]).toFixed(4)}" font-size="1">${esc(subtitleText)}</text>
        </g>
        <script type="application/json" class="etc-elements-meta">${JSON.stringify(meta).replace(/</g, '\\u003c')}</script>
      </svg>`;
    }

    ensureController() {
      if (this.controller || !window.ETCViewer?.Controller) return;
      this.controller = new window.ETCViewer.Controller(this.viewerEl);
      this.controller.liveSvgProvider = (mode, tab) => {
        const tKey = TAB_TO_KEY[tab] || 'heronian';
        this.currentTriKey = tKey;
        this.currentStageMode = mode;
        if (this.currentFamilyObj) {
          this.controller.updateCaption(
            `<strong>Family Constellation</strong>: X<sub>${this.currentFamilyObj.start}</sub>–X<sub>${this.currentFamilyObj.end}</sub> (${esc(this.currentFamilyObj.title)}) on ${esc((KEY_TO_SPEC[tKey] || TRI_ORDER[0]).title)}. Click any center dot to open its full construction.`
          );
          return this.buildFamilyConstellationSvg(this.currentFamilyObj, this.currentFamilyMembers, tKey);
        }
        this.controller.updateCaption(this.buildCaptionHtml(this.currentCenter, mode, tKey));
        if (this.controller.captionEl) this.typesetMath(this.controller.captionEl);
        return this.generateSvg(this.currentCenter, mode, tKey);
      };
      this.controller.onViewChange = (mode, tab) => {
        const tKey = TAB_TO_KEY[tab] || 'heronian';
        this.currentTriKey = tKey;
        this.currentStageMode = mode;
        if (!this.currentFamilyObj && this.currentTrack === 'overview' && this.currentCenter) {
          this.refreshConstructionSection(this.currentCenter, tKey);
          this.controller.buildTextIndex();
          this.controller.syncTableColorsFromSvg();
          this.typesetMath(this.proseEl);
        }
      };
      this.controller.onPointClick = (num) => {
        if (this.currentFamilyObj && Number.isFinite(num)) {
          this.navigateTo(num, 'overview');
          return true;
        }
        return false;
      };
    }

    async navigateTo(num, track) {
      this.currentFamilyId = null;
      this.currentFamilyObj = null;
      this.currentNum = num;
      this.currentTrack = track || 'overview';
      this.setHash(this.currentNum, this.currentTrack);
      await this.loadAndRenderCenter(this.currentNum, this.currentTrack);
    }

    async loadAndRenderCenter(num, track) {
      try {
        this.currentFamilyId = null;
        this.currentFamilyObj = null;
        if (this.tracksBarEl) this.tracksBarEl.style.display = '';
        const shard = await this.fetchShardFor(num);
        const center = shard.centers?.[String(num)];
        if (!center) {
          this.showFatal(`Center X<sub>${num}</sub> was not found in shard.`);
          return;
        }
        this.currentShard = shard;
        this.currentCenter = center;
        const trackSpec = TRACK_SPECS.find((t) => t.key === track) || TRACK_SPECS[0];
        const targetMode = trackSpec.defaultMode;
        const triTab = this.controller ? this.controller.currentTriangle : 'acute';
        this.currentTriKey = TAB_TO_KEY[triTab] || 'heronian';
        this.currentStageMode = targetMode;

        this.renderHeader(center, track);
        this.renderProse(center, track);

        this.ensureController();

        if (this.controller) {
          const svgHtml = this.generateSvg(center, targetMode, this.currentTriKey);
          const svgEl = this.controller.parseSvgFromHtml(svgHtml);
          this.controller.unpin();
          this.controller.clearHover();
          this.controller.currentMode = targetMode;
          this.controller.showLines = targetMode === 'lines';
          if (svgEl) {
            this.controller.mountSvg(svgEl, { applyModeLines: targetMode === 'lines' });
          }
          this.controller.buildTextIndex();
          this.controller.syncTableColorsFromSvg();
          this.controller.syncModeButtons();
          this.controller.syncToolbarButtons();
          if (typeof this.controller.syncAppBar === 'function') this.controller.syncAppBar();
          this.controller.updateCaption(this.buildCaptionHtml(center, targetMode, this.currentTriKey));
        }

        this.typesetMath(this.rootEl);
      } catch (err) {
        this.showFatal(`Unable to load X<sub>${num}</sub>: ${esc(err.message || err)}`);
      }
    }

    renderHeader(center, track) {
      const n = center.n;
      const title = center.t || `X_${n}`;
      document.title = `X_${n} — ${title} • Encyclopedia of Triangle Centers`;
      this.h1El.innerHTML = `X<sub>${n}</sub>`;
      this.subtitleEl.innerHTML = formatXLinks(title, n);

      this.tracksBarEl.querySelectorAll('a[data-live-track]').forEach((a) => {
        const tk = a.dataset.liveTrack;
        a.href = tk === 'overview' ? `#X_${n}` : `#X_${n}/${tk}`;
        a.classList.toggle('is-active', tk === track);
      });

      const hRec = center.tris?.heronian;
      const kRec = center.tris?.kimberling;
      const hField = hRec?.f || this.manifest?.triangles?.heronian?.field || '\\mathbb{Q}';
      const precBadge =
        hRec?.p === 'e'
          ? `<span class="etc-prec-badge is-exact">Exact Symbolic (${texSpan(hField)})</span>`
          : hRec?.p === 'm'
            ? `<span class="etc-prec-badge is-mp50">50-Digit Numeric</span>`
            : `<span class="etc-prec-badge">Catalog Entry</span>`;
      const svHtml =
        kRec && typeof kRec.sv === 'number'
          ? ` • <strong>Search (6,9,13)</strong>: ${texSpan(kRec.sl || kRec.sv.toFixed(12))}`
          : '';

      const { families, collection } = this.findFamiliesForCenter(n);
      let famBadgeHtml = '';
      if (families.length > 0) {
        const pf = families[0];
        const shortT = pf.title.length > 42 ? `${pf.title.slice(0, 40)}…` : pf.title;
        famBadgeHtml = ` • <a class="etc-family-badge" href="#family/${esc(pf.id)}" data-jump-family="${esc(pf.id)}" title="Open Family Constellation & Preamble: ${esc(pf.title)}">Family: ${esc(shortT)} (X<sub>${pf.start}</sub>–X<sub>${pf.end}</sub>)</a>`;
      } else if (collection) {
        const shortT = collection.title.length > 42 ? `${collection.title.slice(0, 40)}…` : collection.title;
        famBadgeHtml = ` • <a class="etc-family-badge" href="#family/${esc(collection.slug)}" data-jump-family="${esc(collection.slug)}" title="Open Collection Constellation: ${esc(collection.title)}">Collection: ${esc(shortT)}</a>`;
      } else {
        famBadgeHtml = ` • <strong>Range</strong> <code>${esc(center.col)}</code>`;
      }

      const staticLink = collection
        ? ` • <a href="${esc(collection.slug)}/index.html">Collection Chapter ↗</a>`
        : '';
      this.identityEl.innerHTML = `<p><code>X(${n})</code> • ${precBadge}${svHtml}${famBadgeHtml}${staticLink}</p>`;

      if (center.en) {
        this.enunciationEl.innerHTML = `<p>${formatXLinks(center.en, n)}</p>`;
        this.enunciationEl.hidden = false;
      } else {
        this.enunciationEl.hidden = true;
      }
    }

    buildCaptionHtml(center, mode, triKey) {
      const n = center.n;
      const spec = KEY_TO_SPEC[triKey] || TRI_ORDER[0];
      const rec = center.tris?.[triKey];
      if (mode === 'coordinates') {
        const cSpec = rec && rec.st === 'f' ? spec : TRI_ORDER[0];
        return `<strong>X<sub>${n}</sub></strong> Coordinate Decomposition on ${esc(cSpec.title)}: trilinear distances (α, β, γ) and signed barycentric sub-triangles (u, v, w) overlaid on construction elements.`;
      }
      if (mode === 'four_triangles') {
        return `<strong>X<sub>${n}</sub></strong> across all six non-degenerate canonical reference triangles. Hover any panel or row to compare coordinates.`;
      }
      if (mode === 'relations') {
        return `<strong>X<sub>${n}</sub></strong> algebraic and geometric partner centers on Heronian (15, 13, 14).`;
      }
      const prec = rec?.p === 'e' ? 'exact algebraic' : '50-digit numeric';
      const xyTxt = rec?.xyl ? texSpan(rec.xyl) : '';
      return `<strong>X<sub>${n}</sub></strong> on ${esc(spec.title)} (${prec}) ${xyTxt}. Switch modes or reference triangles above, or press <code>F</code> for Fullscreen App Mode.`;
    }

    getPartnerXY(k, triKey) {
      const ks = String(k);
      const c = this.currentCenter;
      if (this.currentShard?.centers?.[ks]?.tris?.[triKey]?.xy) {
        return this.currentShard.centers[ks].tris[triKey].xy;
      }
      if (this.currentShard?.partners?.[ks]?.xy?.[triKey]) return this.currentShard.partners[ks].xy[triKey];
      if (c?.pxy?.[ks]?.xy?.[triKey]) return c.pxy[ks].xy[triKey];
      if (this.coreCenters?.[ks]?.xy?.[triKey]) return this.coreCenters[ks].xy[triKey];
      return null;
    }

    getPartnerTitle(k) {
      const ks = String(k);
      return (
        this.currentShard?.centers?.[ks]?.t ||
        this.currentShard?.partners?.[ks]?.t ||
        this.currentCenter?.pxy?.[ks]?.t ||
        this.coreCenters?.[ks]?.t ||
        `X_${k}`
      );
    }

    // =========================================================================
    // Live Client-Side SVG Generators (Matches Collection 1 Visual Grammar)
    // =========================================================================

    generateSvg(center, mode, triKey) {
      if (mode === 'coordinates') return this.buildCoordinatesSvg(center, triKey);
      if (mode === 'four_triangles') return this.buildSixTrianglesSvg(center);
      if (mode === 'relations') return this.buildRelationsSvg(center);
      return this.buildConstructionSvg(center, triKey, mode === 'lines');
    }

    // =========================================================================
    // 4-Tier Universal Geometric Construction Plan Engine (All 73,310 Centers)
    // =========================================================================

    computeConstructionPlan(center, triKey) {
      const tMeta = this.manifest.triangles[triKey] || this.manifest.triangles.heronian;
      const rec = center.tris?.[triKey];
      const n = center.n;
      const A = tMeta.verts.A;
      const B = tMeta.verts.B;
      const C = tMeta.verts.C;
      const span = Math.max(...tMeta.sides);
      const centroid = [(A[0] + B[0] + C[0]) / 3, (A[1] + B[1] + C[1]) / 3];
      const hasFinite = rec && rec.st === 'f' && Array.isArray(rec.xy);
      const P = hasFinite ? rec.xy : null;
      const cc = circumcircle(A, B, C);
      const ic = incircle(A, B, C, tMeta.sides);

      const plan = {
        triKey,
        triLabel: tMeta.label,
        summary: '',
        polygons: [],
        circles: [],
        lines: [],
        points: [],
        steps: [],
      };

      const seenLineIds = new Set();
      const seenPtIds = new Set(['A', 'B', 'C', `X_${n}`]);
      const seenCircIds = new Set();
      const seenPolyIds = new Set();

      const addPoly = (id, name, verts, color, desc) => {
        if (!verts || verts.length !== 3 || seenPolyIds.has(id)) return;
        if (verts.some((v) => !v || !Number.isFinite(v[0]) || !Number.isFinite(v[1]))) return;
        seenPolyIds.add(id);
        plan.polygons.push({ id, name, verts, color });
        plan.steps.push({ id, label: id, role: 'Derived △', color, desc });
      };

      const addCircle = (id, name, cx, cy, r, color, desc, isGuide = false) => {
        if (!Number.isFinite(cx) || !Number.isFinite(cy) || !Number.isFinite(r) || r <= 1e-8) return;
        if (seenCircIds.has(id)) return;
        seenCircIds.add(id);
        plan.circles.push({ id, name, cx, cy, r, color, isGuide });
        plan.steps.push({ id, label: id, role: isGuide ? 'Guide Circle' : 'Circle', color, desc });
      };

      const addPt = (id, labelHtml, name, xy, color, desc, isPartner = false, pk = null) => {
        if (!xy || !Number.isFinite(xy[0]) || !Number.isFinite(xy[1])) return;
        if (seenPtIds.has(id)) return;
        seenPtIds.add(id);
        plan.points.push({ id, labelHtml, name, xy, color, isPartner, pk });
        plan.steps.push({ id, label: id, role: isPartner ? 'Anchor Center' : 'Vertex', color, desc });
      };

      const addLine = (id, name, p1, p2, color, desc, infinite = true, relatedPts = []) => {
        if (!p1 || !p2 || seenLineIds.has(id)) return;
        const len = Math.hypot(p2[0] - p1[0], p2[1] - p1[1]);
        if (!Number.isFinite(len) || len < 1e-8) return;
        seenLineIds.add(id);
        plan.lines.push({ id, name, p1, p2, color, infinite, relatedPts });
        plan.steps.push({ id, label: id, role: 'Line', color, desc });
      };

      const addPartnerPt = (pk, color = '#e2e8f0') => {
        const pxy = this.getPartnerXY(pk, triKey);
        if (!pxy) return null;
        const pid = `X_${pk}`;
        const pTitle = this.getPartnerTitle(pk);
        addPt(
          pid,
          `X<tspan class="sub" dy="0.28em" font-size="0.72em">${pk}</tspan>`,
          pTitle,
          pxy,
          color,
          `${pTitle} (${pxy[0].toFixed(3)}, ${pxy[1].toFixed(3)})`,
          true,
          pk
        );
        return pxy;
      };

      const enLow = `${center.en || ''} ${center.t || ''}`.toLowerCase();
      const allRelText = [center.en || '', center.t || '', ...(center.re || []), ...(center.co || [])].join('\n');
      let hasPrimaryConstruction = false;
      let hasCevianOrPerspector = false;

      // -----------------------------------------------------------------------
      // Tier 0: Classical Euclidean Constructions (X_1 .. X_19)
      // Complete textbook compass-and-straightedge geometry across all 7 triangles.
      // -----------------------------------------------------------------------
      if (n >= 1 && n <= 19) {
        const subLbl = (ch, s) => `${ch}<tspan class="sub" dy="0.28em" font-size="0.72em">${s}</tspan>`;
        if (n === 1 && ic) {
          const it = intouchTriangle(A, B, C, ic);
          const bis = cevianTraces(A, B, C, [ic.cx, ic.cy]);
          addCircle('incircle', 'Incircle ⊙(I, r)', ic.cx, ic.cy, ic.r, '#e040fb', `Inscribed circle tangent to all three sidelines (r = ${ic.r.toFixed(4)})`);
          if (bis.Da) {
            addLine('[ A I_a ]', 'Angle Bisector A I_a', A, bis.Da, '#ff7043', 'Interior angle bisector of ∠A meeting BC at I_a', true, ['A', 'I_a', 'X_1']);
            addPt('I_a', subLbl('I', 'a'), 'Bisector foot I_a', bis.Da, '#ff7043', 'Intersection of ∠A bisector with BC');
          }
          if (bis.Db) {
            addLine('[ B I_b ]', 'Angle Bisector B I_b', B, bis.Db, '#38bdf8', 'Interior angle bisector of ∠B meeting CA at I_b', true, ['B', 'I_b', 'X_1']);
            addPt('I_b', subLbl('I', 'b'), 'Bisector foot I_b', bis.Db, '#38bdf8', 'Intersection of ∠B bisector with CA');
          }
          if (bis.Dc) {
            addLine('[ C I_c ]', 'Angle Bisector C I_c', C, bis.Dc, '#5ec27e', 'Interior angle bisector of ∠C meeting AB at I_c', true, ['C', 'I_c', 'X_1']);
            addPt('I_c', subLbl('I', 'c'), 'Bisector foot I_c', bis.Dc, '#5ec27e', 'Intersection of ∠C bisector with AB');
          }
          if (it) {
            addPt('T_a', subLbl('T', 'a'), 'Incircle touchpoint T_a', it.Ia, '#e040fb', 'Tangency point of incircle on side BC');
            addPt('T_b', subLbl('T', 'b'), 'Incircle touchpoint T_b', it.Ib, '#e040fb', 'Tangency point of incircle on side CA');
            addPt('T_c', subLbl('T', 'c'), 'Incircle touchpoint T_c', it.Ic, '#e040fb', 'Tangency point of incircle on side AB');
          }
          plan.summary = 'Concurrence of the three interior angle bisectors of △ABC (Euclid IV.4); center of the inscribed circle ⊙(I, r).';
          hasPrimaryConstruction = true;
          hasCevianOrPerspector = true;
        } else if (n === 2) {
          const med = medialTriangle(A, B, C);
          addPoly('< M_a M_b M_c >', 'Medial Triangle', [med.Ma, med.Mb, med.Mc], '#2dd4bf', 'Triangle formed by the three side midpoints M_a, M_b, M_c');
          addPt('M_a', subLbl('M', 'a'), 'Midpoint M_a', med.Ma, '#ff7043', 'Midpoint of side BC');
          addPt('M_b', subLbl('M', 'b'), 'Midpoint M_b', med.Mb, '#38bdf8', 'Midpoint of side CA');
          addPt('M_c', subLbl('M', 'c'), 'Midpoint M_c', med.Mc, '#5ec27e', 'Midpoint of side AB');
          addLine('[ A M_a ]', 'Median A M_a', A, med.Ma, '#ff7043', 'Median from vertex A to midpoint M_a of BC', true, ['A', 'M_a', 'X_2']);
          addLine('[ B M_b ]', 'Median B M_b', B, med.Mb, '#38bdf8', 'Median from vertex B to midpoint M_b of CA', true, ['B', 'M_b', 'X_2']);
          addLine('[ C M_c ]', 'Median C M_c', C, med.Mc, '#5ec27e', 'Median from vertex C to midpoint M_c of AB', true, ['C', 'M_c', 'X_2']);
          plan.summary = 'Concurrence of the three medians A M_a, B M_b, C M_c (center of mass dividing each median 2 : 1).';
          hasPrimaryConstruction = true;
          hasCevianOrPerspector = true;
        } else if (n === 3 && cc) {
          const med = medialTriangle(A, B, C);
          addCircle('circumcircle', 'Circumcircle ⊙(O, R)', cc.cx, cc.cy, cc.r, '#a78bfa', `Circumscribed circle through A, B, C (R = ${cc.r.toFixed(4)})`);
          addPt('M_a', subLbl('M', 'a'), 'Midpoint M_a', med.Ma, '#ff7043', 'Midpoint of side BC');
          addPt('M_b', subLbl('M', 'b'), 'Midpoint M_b', med.Mb, '#38bdf8', 'Midpoint of side CA');
          addPt('M_c', subLbl('M', 'c'), 'Midpoint M_c', med.Mc, '#5ec27e', 'Midpoint of side AB');
          addLine('perp_a', 'Perp. Bisector of BC', med.Ma, [med.Ma[0] - (C[1] - B[1]), med.Ma[1] + (C[0] - B[0])], '#ff7043', 'Perpendicular bisector of side BC through M_a and X_3', true, ['M_a', 'X_3']);
          addLine('perp_b', 'Perp. Bisector of CA', med.Mb, [med.Mb[0] - (A[1] - C[1]), med.Mb[1] + (A[0] - C[0])], '#38bdf8', 'Perpendicular bisector of side CA through M_b and X_3', true, ['M_b', 'X_3']);
          addLine('perp_c', 'Perp. Bisector of AB', med.Mc, [med.Mc[0] - (B[1] - A[1]), med.Mc[1] + (B[0] - A[0])], '#5ec27e', 'Perpendicular bisector of side AB through M_c and X_3', true, ['M_c', 'X_3']);
          plan.summary = 'Concurrence of the three perpendicular bisectors of △ABC (Euclid IV.5); center of the circumcircle ⊙(O, R).';
          hasPrimaryConstruction = true;
          hasCevianOrPerspector = true;
        } else if (n === 4) {
          const ort = orthicTriangle(A, B, C);
          addPoly('< H_a H_b H_c >', 'Orthic Triangle', [ort.Ha, ort.Hb, ort.Hc], '#2dd4bf', 'Triangle formed by the three altitude feet H_a, H_b, H_c');
          addPt('H_a', subLbl('H', 'a'), 'Altitude foot H_a', ort.Ha, '#ff7043', 'Foot of altitude from A onto sideline BC');
          addPt('H_b', subLbl('H', 'b'), 'Altitude foot H_b', ort.Hb, '#38bdf8', 'Foot of altitude from B onto sideline CA');
          addPt('H_c', subLbl('H', 'c'), 'Altitude foot H_c', ort.Hc, '#5ec27e', 'Foot of altitude from C onto sideline AB');
          addLine('[ A H_a ]', 'Altitude A H_a', A, ort.Ha, '#ff7043', 'Altitude from A perpendicular to sideline BC', true, ['A', 'H_a', 'X_4']);
          addLine('[ B H_b ]', 'Altitude B H_b', B, ort.Hb, '#38bdf8', 'Altitude from B perpendicular to sideline CA', true, ['B', 'H_b', 'X_4']);
          addLine('[ C H_c ]', 'Altitude C H_c', C, ort.Hc, '#5ec27e', 'Altitude from C perpendicular to sideline AB', true, ['C', 'H_c', 'X_4']);
          plan.summary = 'Concurrence of the three altitudes A H_a, B H_b, C H_c perpendicular to opposite sidelines.';
          hasPrimaryConstruction = true;
          hasCevianOrPerspector = true;
        } else if (n === 5 && cc) {
          const npc = ninePointCircle(A, B, C, cc);
          if (npc) {
            addCircle('nine_point_circle', 'Nine-Point Circle ⊙(N, R/2)', npc.cx, npc.cy, npc.r, '#2dd4bf', `Passes through M_a, M_b, M_c, H_a, H_b, H_c, and Euler points E_a, E_b, E_c (R_9 = ${npc.r.toFixed(4)})`);
            addPoly('< M_a M_b M_c >', 'Medial Triangle', [npc.Ma, npc.Mb, npc.Mc], '#38bdf8', 'Three side midpoints on the nine-point circle');
            addPoly('< H_a H_b H_c >', 'Orthic Triangle', [npc.Ha, npc.Hb, npc.Hc], '#fb923c', 'Three altitude feet on the nine-point circle');
            addPt('M_a', subLbl('M', 'a'), 'Midpoint M_a', npc.Ma, '#38bdf8', 'Midpoint of side BC');
            addPt('M_b', subLbl('M', 'b'), 'Midpoint M_b', npc.Mb, '#38bdf8', 'Midpoint of side CA');
            addPt('M_c', subLbl('M', 'c'), 'Midpoint M_c', npc.Mc, '#38bdf8', 'Midpoint of side AB');
            addPt('H_a', subLbl('H', 'a'), 'Altitude foot H_a', npc.Ha, '#fb923c', 'Foot of altitude on BC');
            addPt('H_b', subLbl('H', 'b'), 'Altitude foot H_b', npc.Hb, '#fb923c', 'Foot of altitude on CA');
            addPt('H_c', subLbl('H', 'c'), 'Altitude foot H_c', npc.Hc, '#fb923c', 'Foot of altitude on AB');
            addPt('E_a', subLbl('E', 'a'), 'Euler point E_a', npc.Ea, '#4ade80', 'Midpoint of segment A X_4');
            addPt('E_b', subLbl('E', 'b'), 'Euler point E_b', npc.Eb, '#4ade80', 'Midpoint of segment B X_4');
            addPt('E_c', subLbl('E', 'c'), 'Euler point E_c', npc.Ec, '#4ade80', 'Midpoint of segment C X_4');
            const p3 = addPartnerPt(3, '#a78bfa');
            const p4 = addPartnerPt(4, '#f472b6');
            if (p3 && p4) {
              addLine('{ 3, 4 }', 'Euler Line X(3)X(4)', p3, p4, '#e8b85a', 'Euler line: X_5 is the exact midpoint of circumcenter X_3 and orthocenter X_4', true, ['X_3', 'X_4', 'X_5']);
            }
            plan.summary = 'Center of the Feuerbach Nine-Point Circle passing through all 3 side midpoints, 3 altitude feet, and 3 Euler points; midpoint of X_3 and X_4.';
            hasPrimaryConstruction = true;
            hasCevianOrPerspector = true;
          }
        } else if (n === 6 && cc) {
          addCircle('circumcircle', 'Circumcircle ⊙(ABC)', cc.cx, cc.cy, cc.r, '#a78bfa', `Circumcircle of △ABC (R = ${cc.r.toFixed(4)})`);
          const tan = tangentialTriangle(A, B, C, cc);
          if (tan) {
            addPoly('< A_t B_t C_t >', 'Tangential Triangle', [tan.At, tan.Bt, tan.Ct], '#38bdf8', 'Bounded by tangents to ⊙(ABC) at A, B, C');
            addPt('A_t', subLbl('A', 't'), 'Tangential vertex A_t', tan.At, '#ff7043', 'Intersection of circumcircle tangents at B and C');
            addPt('B_t', subLbl('B', 't'), 'Tangential vertex B_t', tan.Bt, '#38bdf8', 'Intersection of circumcircle tangents at C and A');
            addPt('C_t', subLbl('C', 't'), 'Tangential vertex C_t', tan.Ct, '#5ec27e', 'Intersection of circumcircle tangents at A and B');
            addLine('[ A A_t ]', 'Symmedian A A_t', A, tan.At, '#ff7043', 'A-symmedian joining A to tangential vertex A_t through X_6', true, ['A', 'A_t', 'X_6']);
            addLine('[ B B_t ]', 'Symmedian B B_t', B, tan.Bt, '#38bdf8', 'B-symmedian joining B to tangential vertex B_t through X_6', true, ['B', 'B_t', 'X_6']);
            addLine('[ C C_t ]', 'Symmedian C C_t', C, tan.Ct, '#5ec27e', 'C-symmedian joining C to tangential vertex C_t through X_6', true, ['C', 'C_t', 'X_6']);
            plan.summary = 'Concurrence of the three symmedians (perspector of △ABC and its tangential triangle △A_t B_t C_t; isogonal conjugate of centroid X_2).';
            hasPrimaryConstruction = true;
            hasCevianOrPerspector = true;
          } else if (P) {
            const med = medialTriangle(A, B, C);
            addPartnerPt(2, '#e879f9');
            addPt('M_a', subLbl('M', 'a'), 'Midpoint M_a', med.Ma, '#2dd4bf', 'Midpoint of hypotenuse BC');
            addLine('[ A X_6 ]', 'Symmedian A X_6', A, P, '#ff7043', 'A-symmedian (altitude to hypotenuse BC in right triangle)', true, ['A', 'X_6']);
            addLine('[ B X_6 ]', 'Symmedian B X_6', B, P, '#38bdf8', 'B-symmedian (reflection of median B M_b across ∠B bisector)', true, ['B', 'X_6']);
            addLine('[ C X_6 ]', 'Symmedian C X_6', C, P, '#5ec27e', 'C-symmedian (reflection of median C M_c across ∠C bisector)', true, ['C', 'X_6']);
            plan.summary = 'Concurrence of the three symmedians (isogonal conjugate of centroid X_2; midpoint of the altitude to the hypotenuse on right triangles).';
            hasPrimaryConstruction = true;
            hasCevianOrPerspector = true;
          }
        } else if (n === 7 && ic) {
          const it = intouchTriangle(A, B, C, ic);
          if (it) {
            addCircle('incircle', 'Incircle ⊙(I, r)', ic.cx, ic.cy, ic.r, '#e040fb', `Incircle of △ABC (r = ${ic.r.toFixed(4)})`);
            addPoly('< T_a T_b T_c >', 'Intouch Triangle', [it.Ia, it.Ib, it.Ic], '#f472b6', 'Contact points where incircle meets sidelines BC, CA, AB');
            addPt('T_a', subLbl('T', 'a'), 'Intouch vertex T_a', it.Ia, '#ff7043', 'Incircle touchpoint on BC');
            addPt('T_b', subLbl('T', 'b'), 'Intouch vertex T_b', it.Ib, '#38bdf8', 'Incircle touchpoint on CA');
            addPt('T_c', subLbl('T', 'c'), 'Intouch vertex T_c', it.Ic, '#5ec27e', 'Incircle touchpoint on AB');
            addLine('[ A T_a ]', 'Gergonne Cevian A T_a', A, it.Ia, '#ff7043', 'Joins vertex A to opposite incircle touchpoint T_a', true, ['A', 'T_a', 'X_7']);
            addLine('[ B T_b ]', 'Gergonne Cevian B T_b', B, it.Ib, '#38bdf8', 'Joins vertex B to opposite incircle touchpoint T_b', true, ['B', 'T_b', 'X_7']);
            addLine('[ C T_c ]', 'Gergonne Cevian C T_c', C, it.Ic, '#5ec27e', 'Joins vertex C to opposite incircle touchpoint T_c', true, ['C', 'T_c', 'X_7']);
            plan.summary = 'Perspector of △ABC and its intouch (contact) triangle △T_a T_b T_c formed by the incircle tangency points.';
            hasPrimaryConstruction = true;
            hasCevianOrPerspector = true;
          }
        } else if (n === 8) {
          const exc = excenters(A, B, C, tMeta.sides);
          const ext = extouchTriangle(A, B, C, exc);
          if (exc && ext) {
            addPoly('< E_a E_b E_c >', 'Extouch Triangle', [ext.Ea, ext.Eb, ext.Ec], '#fb923c', 'Points where the three excircles touch sides BC, CA, AB');
            addPt('E_a', subLbl('E', 'a'), 'Extouch point E_a', ext.Ea, '#ff7043', 'A-excircle tangency point on BC (perimeter splitter)');
            addPt('E_b', subLbl('E', 'b'), 'Extouch point E_b', ext.Eb, '#38bdf8', 'B-excircle tangency point on CA (perimeter splitter)');
            addPt('E_c', subLbl('E', 'c'), 'Extouch point E_c', ext.Ec, '#5ec27e', 'C-excircle tangency point on AB (perimeter splitter)');
            addLine('[ A E_a ]', 'Nagel Splitter A E_a', A, ext.Ea, '#ff7043', 'Perimeter-bisecting splitter from A to extouch point E_a', true, ['A', 'E_a', 'X_8']);
            addLine('[ B E_b ]', 'Nagel Splitter B E_b', B, ext.Eb, '#38bdf8', 'Perimeter-bisecting splitter from B to extouch point E_b', true, ['B', 'E_b', 'X_8']);
            addLine('[ C E_c ]', 'Nagel Splitter C E_c', C, ext.Ec, '#5ec27e', 'Perimeter-bisecting splitter from C to extouch point E_c', true, ['C', 'E_c', 'X_8']);
            addCircle('excircle_a', 'A-Excircle ⊙(J_a, r_a)', exc.Ja[0], exc.Ja[1], exc.ra, '#ff7043', `A-excircle tangent to BC at E_a (r_a = ${exc.ra.toFixed(3)})`, true);
            addCircle('excircle_b', 'B-Excircle ⊙(J_b, r_b)', exc.Jb[0], exc.Jb[1], exc.rb, '#38bdf8', `B-excircle tangent to CA at E_b (r_b = ${exc.rb.toFixed(3)})`, true);
            addCircle('excircle_c', 'C-Excircle ⊙(J_c, r_c)', exc.Jc[0], exc.Jc[1], exc.rc, '#5ec27e', `C-excircle tangent to AB at E_c (r_c = ${exc.rc.toFixed(3)})`, true);
            plan.summary = 'Perspector of △ABC and its extouch triangle △E_a E_b E_c (concurrence of the three perimeter splitters; isotomic conjugate of Gergonne X_7).';
            hasPrimaryConstruction = true;
            hasCevianOrPerspector = true;
          }
        } else if (n === 9) {
          const exc = excenters(A, B, C, tMeta.sides);
          const med = medialTriangle(A, B, C);
          if (exc) {
            addPoly('< J_a J_b J_c >', 'Excentral Triangle', [exc.Ja, exc.Jb, exc.Jc], '#c084fc', 'Triangle formed by the three excenters J_a, J_b, J_c');
            addPoly('< M_a M_b M_c >', 'Medial Triangle', [med.Ma, med.Mb, med.Mc], '#2dd4bf', 'Triangle formed by the side midpoints M_a, M_b, M_c');
            addPt('J_a', subLbl('J', 'a'), 'A-Excenter J_a', exc.Ja, '#ff7043', 'Center of the A-excircle');
            addPt('J_b', subLbl('J', 'b'), 'B-Excenter J_b', exc.Jb, '#38bdf8', 'Center of the B-excircle');
            addPt('J_c', subLbl('J', 'c'), 'C-Excenter J_c', exc.Jc, '#5ec27e', 'Center of the C-excircle');
            addPt('M_a', subLbl('M', 'a'), 'Midpoint M_a', med.Ma, '#ff7043', 'Midpoint of side BC');
            addPt('M_b', subLbl('M', 'b'), 'Midpoint M_b', med.Mb, '#38bdf8', 'Midpoint of side CA');
            addPt('M_c', subLbl('M', 'c'), 'Midpoint M_c', med.Mc, '#5ec27e', 'Midpoint of side AB');
            addLine('[ J_a M_a ]', 'Mittenpunkt Line J_a M_a', exc.Ja, med.Ma, '#ff7043', 'Joins A-excenter J_a to side midpoint M_a through X_9', true, ['J_a', 'M_a', 'X_9']);
            addLine('[ J_b M_b ]', 'Mittenpunkt Line J_b M_b', exc.Jb, med.Mb, '#38bdf8', 'Joins B-excenter J_b to side midpoint M_b through X_9', true, ['J_b', 'M_b', 'X_9']);
            addLine('[ J_c M_c ]', 'Mittenpunkt Line J_c M_c', exc.Jc, med.Mc, '#5ec27e', 'Joins C-excenter J_c to side midpoint M_c through X_9', true, ['J_c', 'M_c', 'X_9']);
            plan.summary = 'Perspector of the excentral triangle △J_a J_b J_c and the medial triangle △M_a M_b M_c (symmedian point of the excentral triangle).';
            hasPrimaryConstruction = true;
            hasCevianOrPerspector = true;
          }
        } else if (n === 10) {
          const med = medialTriangle(A, B, C);
          const spk = incircle(med.Ma, med.Mb, med.Mc, tMeta.sides.map((s) => s / 2));
          if (spk) {
            addPoly('< M_a M_b M_c >', 'Medial Triangle', [med.Ma, med.Mb, med.Mc], '#2dd4bf', 'Medial triangle of △ABC (perimeter center of mass)');
            addCircle('spieker_circle', 'Spieker Circle ⊙(X_10, r/2)', spk.cx, spk.cy, spk.r, '#4ade80', `Incircle of the medial triangle △M_a M_b M_c (r_s = ${spk.r.toFixed(4)})`);
            addPt('M_a', subLbl('M', 'a'), 'Midpoint M_a', med.Ma, '#ff7043', 'Midpoint of side BC');
            addPt('M_b', subLbl('M', 'b'), 'Midpoint M_b', med.Mb, '#38bdf8', 'Midpoint of side CA');
            addPt('M_c', subLbl('M', 'c'), 'Midpoint M_c', med.Mc, '#5ec27e', 'Midpoint of side AB');
            const spPt = [spk.cx, spk.cy];
            addLine('[ M_a X_10 ]', 'Medial Bisector M_a X_10', med.Ma, spPt, '#ff7043', 'Cleaver / interior angle bisector of medial vertex M_a', true, ['M_a', 'X_10']);
            addLine('[ M_b X_10 ]', 'Medial Bisector M_b X_10', med.Mb, spPt, '#38bdf8', 'Cleaver / interior angle bisector of medial vertex M_b', true, ['M_b', 'X_10']);
            addLine('[ M_c X_10 ]', 'Medial Bisector M_c X_10', med.Mc, spPt, '#5ec27e', 'Cleaver / interior angle bisector of medial vertex M_c', true, ['M_c', 'X_10']);
            plan.summary = 'Incenter of the medial triangle △M_a M_b M_c (concurrence of the three cleavers; center of mass of the perimeter wire of △ABC).';
            hasPrimaryConstruction = true;
            hasCevianOrPerspector = true;
          }
        } else if ((n === 11 || n === 12) && ic && cc) {
          const npc = ninePointCircle(A, B, C, cc);
          if (npc) {
            addCircle('incircle', 'Incircle ⊙(X_1, r)', ic.cx, ic.cy, ic.r, '#e040fb', `Incircle of △ABC (r = ${ic.r.toFixed(4)})`);
            addCircle('nine_point_circle', 'Nine-Point Circle ⊙(X_5, R/2)', npc.cx, npc.cy, npc.r, '#2dd4bf', `Nine-point circle internally tangent to incircle at X_11 (R_9 = ${npc.r.toFixed(4)})`);
            const p1 = addPartnerPt(1, '#e040fb');
            const p5 = addPartnerPt(5, '#2dd4bf');
            if (n === 12) addPartnerPt(11, '#fb923c');
            if (p1 && p5 && Math.hypot(p1[0] - p5[0], p1[1] - p5[1]) > 1e-6) {
              addLine('{ 1, 5 }', 'Feuerbach Line X(1)X(5)', p1, p5, '#e8b85a', 'Line of centers connecting incenter X_1 and nine-point center X_5 through X_11 & X_12', true, ['X_1', 'X_5', `X_${n}`]);
            }
            plan.summary =
              n === 11
                ? "Feuerbach's Theorem: exact internal tangency point of the incircle ⊙(X_1, r) and nine-point circle ⊙(X_5, R/2)."
                : 'External center of similitude of the incircle and nine-point circle; harmonic conjugate of X_11 with respect to X_1 and X_5.';
            hasPrimaryConstruction = true;
            hasCevianOrPerspector = true;
          }
        } else if (n === 13 || n === 14) {
          const out = n === 13;
          const sgn = out ? '+' : '−';
          const eqA = equilateralOnSide(B, C, A, out);
          const eqB = equilateralOnSide(C, A, B, out);
          const eqC = equilateralOnSide(A, B, C, out);
          const idA = `A_${sgn}`, idB = `B_${sgn}`, idC = `C_${sgn}`;
          addPoly(`< B C ${idA} >`, `${out ? 'Outer' : 'Inner'} Equilateral on BC`, [B, C, eqA.apex], '#ff7043', `Equilateral triangle erected ${out ? 'outward' : 'inward'} on side BC`);
          addPoly(`< C A ${idB} >`, `${out ? 'Outer' : 'Inner'} Equilateral on CA`, [C, A, eqB.apex], '#38bdf8', `Equilateral triangle erected ${out ? 'outward' : 'inward'} on side CA`);
          addPoly(`< A B ${idC} >`, `${out ? 'Outer' : 'Inner'} Equilateral on AB`, [A, B, eqC.apex], '#5ec27e', `Equilateral triangle erected ${out ? 'outward' : 'inward'} on side AB`);
          const cA = circumcircle(B, C, eqA.apex);
          const cB = circumcircle(C, A, eqB.apex);
          const cC = circumcircle(A, B, eqC.apex);
          if (cA) addCircle(`torr_a`, `Torricelli Circle ⊙(BC${idA})`, cA.cx, cA.cy, cA.r, '#ff7043', `Circumcircle of equilateral △BC${idA}`, true);
          if (cB) addCircle(`torr_b`, `Torricelli Circle ⊙(CA${idB})`, cB.cx, cB.cy, cB.r, '#38bdf8', `Circumcircle of equilateral △CA${idB}`, true);
          if (cC) addCircle(`torr_c`, `Torricelli Circle ⊙(AB${idC})`, cC.cx, cC.cy, cC.r, '#5ec27e', `Circumcircle of equilateral △AB${idC}`, true);
          addPt(idA, subLbl('A', sgn), `Equilateral apex ${idA}`, eqA.apex, '#ff7043', `Apex of ${out ? 'outward' : 'inward'} equilateral triangle on BC`);
          addPt(idB, subLbl('B', sgn), `Equilateral apex ${idB}`, eqB.apex, '#38bdf8', `Apex of ${out ? 'outward' : 'inward'} equilateral triangle on CA`);
          addPt(idC, subLbl('C', sgn), `Equilateral apex ${idC}`, eqC.apex, '#5ec27e', `Apex of ${out ? 'outward' : 'inward'} equilateral triangle on AB`);
          addLine(`[ A ${idA} ]`, `Fermat Line A ${idA}`, A, eqA.apex, '#ff7043', `Joins A to equilateral apex ${idA} through X_${n}`, true, ['A', idA, `X_${n}`]);
          addLine(`[ B ${idB} ]`, `Fermat Line B ${idB}`, B, eqB.apex, '#38bdf8', `Joins B to equilateral apex ${idB} through X_${n}`, true, ['B', idB, `X_${n}`]);
          addLine(`[ C ${idC} ]`, `Fermat Line C ${idC}`, C, eqC.apex, '#5ec27e', `Joins C to equilateral apex ${idC} through X_${n}`, true, ['C', idC, `X_${n}`]);
          plan.summary = out
            ? 'Concurrence of A A_+, B B_+, C C_+ and the three outward Torricelli circles (Fermat-Torricelli 1st isogonic center).'
            : 'Concurrence of A A_−, B B_−, C C_− and the three inward Torricelli circles (2nd isogonic / Fermat center).';
          hasPrimaryConstruction = true;
          hasCevianOrPerspector = true;
        } else if (n === 15 || n === 16) {
          const p15 = this.getPartnerXY(15, triKey);
          const p16 = this.getPartnerXY(16, triKey);
          const p3 = addPartnerPt(3, '#a78bfa');
          const p6 = addPartnerPt(6, '#fb923c');
          if (n === 15 && p16) addPartnerPt(16, '#f472b6');
          if (n === 16 && p15) addPartnerPt(15, '#f472b6');
          if (p3 && p6 && Math.hypot(p3[0] - p6[0], p3[1] - p6[1]) > 1e-6) {
            addLine('{ 3, 6 }', 'Brocard Axis X(3)X(6)', p3, p6, '#e8b85a', 'Brocard axis carrying X_3, X_6, X_15, and X_16 (radical axis of Apollonius circles)', true, ['X_3', 'X_6', `X_${n}`]);
          }
          if (p15 && p16 && Math.hypot(p15[0] - p16[0], p15[1] - p16[1]) > 1e-5) {
            const apA = circumcircle(A, p15, p16);
            const apB = circumcircle(B, p15, p16);
            const apC = circumcircle(C, p15, p16);
            if (apA) addCircle('apollonius_a', 'A-Apollonius Circle', apA.cx, apA.cy, apA.r, '#ff7043', `A-Apollonius circle through A, X_15, X_16 (R = ${apA.r.toFixed(4)})`);
            if (apB) addCircle('apollonius_b', 'B-Apollonius Circle', apB.cx, apB.cy, apB.r, '#38bdf8', `B-Apollonius circle through B, X_15, X_16 (R = ${apB.r.toFixed(4)})`);
            if (apC) addCircle('apollonius_c', 'C-Apollonius Circle', apC.cx, apC.cy, apC.r, '#5ec27e', `C-Apollonius circle through C, X_15, X_16 (R = ${apC.r.toFixed(4)})`);
            plan.summary =
              n === 15
                ? 'Common intersection inside ⊙(ABC) of the three Apollonius circles on the Brocard axis X_3 X_6 (isogonal conjugate of X_13; pedal triangle is equilateral).'
                : 'Common intersection outside ⊙(ABC) of the three Apollonius circles on the Brocard axis X_3 X_6 (inverse of X_15 in ⊙(ABC); isogonal conjugate of X_14).';
            hasPrimaryConstruction = true;
            hasCevianOrPerspector = true;
          }
        } else if (n === 17 || n === 18) {
          const out = n === 17;
          const sgn = out ? '+' : '−';
          const eqA = equilateralOnSide(B, C, A, out);
          const eqB = equilateralOnSide(C, A, B, out);
          const eqC = equilateralOnSide(A, B, C, out);
          const idA = `N_a${sgn}`, idB = `N_b${sgn}`, idC = `N_c${sgn}`;
          addPoly(`< ${idA} ${idB} ${idC} >`, `${out ? 'Outer' : 'Inner'} Napoleon Triangle`, [eqA.center, eqB.center, eqC.center], '#2dd4bf', `Equilateral triangle formed by centers of ${out ? 'outward' : 'inward'} equilateral triangles on sides`);
          addPt(idA, subLbl('N', `a${sgn}`), `Napoleon vertex ${idA}`, eqA.center, '#ff7043', `Center of ${out ? 'outward' : 'inward'} equilateral triangle on BC`);
          addPt(idB, subLbl('N', `b${sgn}`), `Napoleon vertex ${idB}`, eqB.center, '#38bdf8', `Center of ${out ? 'outward' : 'inward'} equilateral triangle on CA`);
          addPt(idC, subLbl('N', `c${sgn}`), `Napoleon vertex ${idC}`, eqC.center, '#5ec27e', `Center of ${out ? 'outward' : 'inward'} equilateral triangle on AB`);
          addLine(`[ A ${idA} ]`, `Napoleon Line A ${idA}`, A, eqA.center, '#ff7043', `Perspector ray joining A to ${idA} through X_${n}`, true, ['A', idA, `X_${n}`]);
          addLine(`[ B ${idB} ]`, `Napoleon Line B ${idB}`, B, eqB.center, '#38bdf8', `Perspector ray joining B to ${idB} through X_${n}`, true, ['B', idB, `X_${n}`]);
          addLine(`[ C ${idC} ]`, `Napoleon Line C ${idC}`, C, eqC.center, '#5ec27e', `Perspector ray joining C to ${idC} through X_${n}`, true, ['C', idC, `X_${n}`]);
          plan.summary = out
            ? 'Perspector of △ABC and its equilateral Outer Napoleon Triangle △N_a+ N_b+ N_c+.'
            : 'Perspector of △ABC and its equilateral Inner Napoleon Triangle △N_a− N_b− N_c−.';
          hasPrimaryConstruction = true;
          hasCevianOrPerspector = true;
        } else if (n === 19) {
          const ort = orthicTriangle(A, B, C);
          const exc = excenters(A, B, C, tMeta.sides);
          if (exc) {
            addPoly('< H_a H_b H_c >', 'Orthic Triangle', [ort.Ha, ort.Hb, ort.Hc], '#2dd4bf', 'Orthic triangle of △ABC');
            addPoly('< J_a J_b J_c >', 'Excentral Triangle', [exc.Ja, exc.Jb, exc.Jc], '#c084fc', 'Excentral triangle (homothetic to orthic triangle at X_19)');
            addPt('H_a', subLbl('H', 'a'), 'Orthic vertex H_a', ort.Ha, '#ff7043', 'Altitude foot on BC');
            addPt('H_b', subLbl('H', 'b'), 'Orthic vertex H_b', ort.Hb, '#38bdf8', 'Altitude foot on CA');
            addPt('H_c', subLbl('H', 'c'), 'Orthic vertex H_c', ort.Hc, '#5ec27e', 'Altitude foot on AB');
            addPt('J_a', subLbl('J', 'a'), 'A-Excenter J_a', exc.Ja, '#ff7043', 'Center of the A-excircle');
            addPt('J_b', subLbl('J', 'b'), 'B-Excenter J_b', exc.Jb, '#38bdf8', 'Center of the B-excircle');
            addPt('J_c', subLbl('J', 'c'), 'C-Excenter J_c', exc.Jc, '#5ec27e', 'Center of the C-excircle');
            addLine('[ H_a J_a ]', 'Clawson Line H_a J_a', ort.Ha, exc.Ja, '#ff7043', 'Homothety ray joining H_a and J_a through X_19', true, ['H_a', 'J_a', 'X_19']);
            addLine('[ H_b J_b ]', 'Clawson Line H_b J_b', ort.Hb, exc.Jb, '#38bdf8', 'Homothety ray joining H_b and J_b through X_19', true, ['H_b', 'J_b', 'X_19']);
            addLine('[ H_c J_c ]', 'Clawson Line H_c J_c', ort.Hc, exc.Jc, '#5ec27e', 'Homothety ray joining H_c and J_c through X_19', true, ['H_c', 'J_c', 'X_19']);
            plan.summary = 'Homothetic center of the orthic triangle △H_a H_b H_c and the excentral triangle △J_a J_b J_c.';
            hasPrimaryConstruction = true;
            hasCevianOrPerspector = true;
          }
        }
      }

      // -----------------------------------------------------------------------
      // Tier 1: Named Derived-Triangle Perspectors & Classical Constructions
      // -----------------------------------------------------------------------
      if (!hasPrimaryConstruction && enLow.includes('circummedial') && enLow.includes('tangential')) {
        const tan = tangentialTriangle(A, B, C, cc);
        const cm = circummedialTriangle(A, B, C, cc);
        if (cc && tan && cm) {
          plan.summary = 'Perspector of the circummedial triangle and the tangential triangle (classical Exeter construction).';
          addCircle('circumcircle', 'Circumcircle ⊙(ABC)', cc.cx, cc.cy, cc.r, '#c084fc', `Circumcircle of △ABC (R = ${cc.r.toFixed(4)})`);
          addPoly('< A_t B_t C_t >', 'Tangential Triangle', [tan.At, tan.Bt, tan.Ct], '#38bdf8', 'Tangents to circumcircle at A, B, C');
          addPoly('< A_m B_m C_m >', 'Circummedial Triangle', [cm.Am, cm.Bm, cm.Cm], '#4ade80', 'Medians extended to circumcircle');
          [
            ['A_t', 'A<tspan class="sub" dy="0.28em" font-size="0.72em">t</tspan>', tan.At, '#38bdf8', 'Tangential vertex opposite A'],
            ['B_t', 'B<tspan class="sub" dy="0.28em" font-size="0.72em">t</tspan>', tan.Bt, '#38bdf8', 'Tangential vertex opposite B'],
            ['C_t', 'C<tspan class="sub" dy="0.28em" font-size="0.72em">t</tspan>', tan.Ct, '#38bdf8', 'Tangential vertex opposite C'],
            ['A_m', 'A<tspan class="sub" dy="0.28em" font-size="0.72em">m</tspan>', cm.Am, '#4ade80', 'Circummedial vertex on ⊙(ABC)'],
            ['B_m', 'B<tspan class="sub" dy="0.28em" font-size="0.72em">m</tspan>', cm.Bm, '#4ade80', 'Circummedial vertex on ⊙(ABC)'],
            ['C_m', 'C<tspan class="sub" dy="0.28em" font-size="0.72em">m</tspan>', cm.Cm, '#4ade80', 'Circummedial vertex on ⊙(ABC)'],
          ].forEach(([pid, lbl, xy, col, desc]) => addPt(pid, lbl, pid, xy, col, desc));
          addLine('[ A_m A_t ]', 'Perspector line A_m A_t', cm.Am, tan.At, '#ff7043', `Joins A_m and A_t through X_${n}`, true, ['A_m', 'A_t', `X_${n}`]);
          addLine('[ B_m B_t ]', 'Perspector line B_m B_t', cm.Bm, tan.Bt, '#38bdf8', `Joins B_m and B_t through X_${n}`, true, ['B_m', 'B_t', `X_${n}`]);
          addLine('[ C_m C_t ]', 'Perspector line C_m C_t', cm.Cm, tan.Ct, '#5ec27e', `Joins C_m and C_t through X_${n}`, true, ['C_m', 'C_t', `X_${n}`]);
          hasPrimaryConstruction = true;
          hasCevianOrPerspector = true;
        }
      }

      if (!hasPrimaryConstruction && enLow.includes('tangential') && cc) {
        const tan = tangentialTriangle(A, B, C, cc);
        if (tan) {
          addCircle('circumcircle', 'Circumcircle ⊙(ABC)', cc.cx, cc.cy, cc.r, '#c084fc', `Circumcircle of △ABC (R = ${cc.r.toFixed(4)})`);
          addPoly('< A_t B_t C_t >', 'Tangential Triangle', [tan.At, tan.Bt, tan.Ct], '#38bdf8', 'Tangents to circumcircle at A, B, C');
          [
            ['A_t', 'A<tspan class="sub" dy="0.28em" font-size="0.72em">t</tspan>', tan.At, '#38bdf8', 'Tangential vertex opposite A'],
            ['B_t', 'B<tspan class="sub" dy="0.28em" font-size="0.72em">t</tspan>', tan.Bt, '#38bdf8', 'Tangential vertex opposite B'],
            ['C_t', 'C<tspan class="sub" dy="0.28em" font-size="0.72em">t</tspan>', tan.Ct, '#38bdf8', 'Tangential vertex opposite C'],
          ].forEach(([pid, lbl, xy, col, desc]) => addPt(pid, lbl, pid, xy, col, desc));
          if (P) {
            addLine('[ A_t X ]', `Ray A_t X_${n}`, tan.At, P, '#ff7043', `Constructive ray from A_t through X_${n}`, true, ['A_t', `X_${n}`]);
            addLine('[ B_t X ]', `Ray B_t X_${n}`, tan.Bt, P, '#38bdf8', `Constructive ray from B_t through X_${n}`, true, ['B_t', `X_${n}`]);
            addLine('[ C_t X ]', `Ray C_t X_${n}`, tan.Ct, P, '#5ec27e', `Constructive ray from C_t through X_${n}`, true, ['C_t', `X_${n}`]);
            plan.summary = 'Constructed via the tangential triangle △A_t B_t C_t of △ABC.';
            hasPrimaryConstruction = true;
            hasCevianOrPerspector = true;
          }
        }
      }

      if (!hasPrimaryConstruction && enLow.includes('orthic')) {
        const ort = orthicTriangle(A, B, C);
        addPoly('< H_a H_b H_c >', 'Orthic Triangle', [ort.Ha, ort.Hb, ort.Hc], '#2dd4bf', 'Feet of the altitudes of △ABC');
        if (P) {
          addLine('[ H_a X ]', `Ray H_a X_${n}`, ort.Ha, P, '#ff7043', `Ray through orthic vertex H_a and X_${n}`, true, [`X_${n}`]);
          addLine('[ H_b X ]', `Ray H_b X_${n}`, ort.Hb, P, '#38bdf8', `Ray through orthic vertex H_b and X_${n}`, true, [`X_${n}`]);
          addLine('[ H_c X ]', `Ray H_c X_${n}`, ort.Hc, P, '#5ec27e', `Ray through orthic vertex H_c and X_${n}`, true, [`X_${n}`]);
          plan.summary = 'Constructed via the orthic triangle △H_a H_b H_c of △ABC.';
          hasPrimaryConstruction = true;
          hasCevianOrPerspector = true;
        }
      }

      if (!hasPrimaryConstruction && enLow.includes('intouch') && ic) {
        const it = intouchTriangle(A, B, C, ic);
        addCircle('incircle', 'Incircle ⊙(I, r)', ic.cx, ic.cy, ic.r, '#e040fb', `Incircle of △ABC (r = ${ic.r.toFixed(4)})`);
        addPoly('< I_a I_b I_c >', 'Intouch Triangle', [it.Ia, it.Ib, it.Ic], '#f472b6', 'Incircle tangency points on sidelines');
        if (P) {
          addLine('[ I_a X ]', `Ray I_a X_${n}`, it.Ia, P, '#ff7043', `Ray through intouch vertex I_a and X_${n}`, true, [`X_${n}`]);
          addLine('[ I_b X ]', `Ray I_b X_${n}`, it.Ib, P, '#38bdf8', `Ray through intouch vertex I_b and X_${n}`, true, [`X_${n}`]);
          addLine('[ I_c X ]', `Ray I_c X_${n}`, it.Ic, P, '#5ec27e', `Ray through intouch vertex I_c and X_${n}`, true, [`X_${n}`]);
          plan.summary = 'Constructed via the intouch (contact) triangle △I_a I_b I_c.';
          hasPrimaryConstruction = true;
          hasCevianOrPerspector = true;
        }
      }

      // -----------------------------------------------------------------------
      // Tier 2: Explicit Defining Line Intersection X(i)X(j) ∩ X(k)X(l)
      // -----------------------------------------------------------------------
      if (!hasPrimaryConstruction) {
        const mInt = `${center.t || ''} ${center.en || ''}`.match(
          /X[_(\s]*(\d+)\)?\s*X[_(\s]*(\d+)\)?\s*(?:∩|\\cap)\s*X[_(\s]*(\d+)\)?\s*X[_(\s]*(\d+)\)?/i
        );
        if (mInt) {
          const i1 = parseInt(mInt[1], 10), j1 = parseInt(mInt[2], 10);
          const i2 = parseInt(mInt[3], 10), j2 = parseInt(mInt[4], 10);
          const p1 = this.getPartnerXY(i1, triKey), p2 = this.getPartnerXY(j1, triKey);
          const p3 = this.getPartnerXY(i2, triKey), p4 = this.getPartnerXY(j2, triKey);
          const l1Pts = p1 && p2 ? [p1, p2] : P && (p1 || p2) ? [p1 || p2, P] : null;
          const l2Pts = p3 && p4 ? [p3, p4] : P && (p3 || p4) ? [p3 || p4, P] : null;
          if (l1Pts && l2Pts) {
            if (p1) addPartnerPt(i1, '#38bdf8');
            if (p2) addPartnerPt(j1, '#38bdf8');
            if (p3) addPartnerPt(i2, '#f472b6');
            if (p4) addPartnerPt(j2, '#f472b6');
            addLine(`{ ${Math.min(i1, j1)}, ${Math.max(i1, j1)} }`, `Defining Line X(${i1})X(${j1})`, l1Pts[0], l1Pts[1], '#38bdf8', `First defining line through X_${i1} and X_${j1}`, true, [`X_${i1}`, `X_${j1}`, `X_${n}`]);
            addLine(`{ ${Math.min(i2, j2)}, ${Math.max(i2, j2)} }`, `Defining Line X(${i2})X(${j2})`, l2Pts[0], l2Pts[1], '#f472b6', `Second defining line through X_${i2} and X_${j2}`, true, [`X_${i2}`, `X_${j2}`, `X_${n}`]);
            plan.summary = `Exact intersection of defining lines X_${i1}X_${j1} and X_${i2}X_${j2}.`;
            hasPrimaryConstruction = true;
          }
        }
      }

      // -----------------------------------------------------------------------
      // Tier 3: Explicit Functional Relations (Reflection, Midpoint, Conjugate, Homothety, Inverse)
      // -----------------------------------------------------------------------
      if (!hasPrimaryConstruction && P) {
        const mRefl = allRelText.match(/reflection\s+of\s+X[_(\s]*(\d+)\)?\s+in\s+X[_(\s]*(\d+)\)?/i);
        const mMid = allRelText.match(/midpoint\s+of\s+X[_(\s]*(\d+)\)?\s+and\s+X[_(\s]*(\d+)\)?/i);
        const mIso = allRelText.match(/isogonal\s+conjugate\s+of\s+X[_(\s]*(\d+)\)?/i);
        const mIsot = allRelText.match(/isotomic\s+conjugate\s+of\s+X[_(\s]*(\d+)\)?/i);
        const mComp = allRelText.match(/(anti)?complement\s+of\s+X[_(\s]*(\d+)\)?/i);
        const mInv = allRelText.match(/inverse\s+of\s+X[_(\s]*(\d+)\)?\s+in\s+(?:the\s+)?circumcircle/i);

        if (mRefl) {
          const ki = parseInt(mRefl[1], 10), kj = parseInt(mRefl[2], 10);
          const pi = this.getPartnerXY(ki, triKey), pj = this.getPartnerXY(kj, triKey);
          if (pi && pj) {
            addPartnerPt(ki, '#fb923c');
            addPartnerPt(kj, '#38bdf8');
            addLine(`{ ${Math.min(ki, kj)}, ${Math.max(ki, kj)} }`, `Reflection axis X(${ki})X(${kj})`, pi, pj, '#fb923c', `Line carrying reflection X_${ki} → X_${kj} → X_${n}`, true, [`X_${ki}`, `X_${kj}`, `X_${n}`]);
            const rr = Math.hypot(pi[0] - pj[0], pi[1] - pj[1]);
            addCircle(`⊙(X_${kj})`, `Reflection circle centered at X_${kj}`, pj[0], pj[1], rr, '#38bdf8', `Equal-distance reflection circle through X_${ki} and X_${n}`);
            plan.summary = `Point reflection of X_${ki} across X_${kj}.`;
            hasPrimaryConstruction = true;
          }
        } else if (mMid) {
          const ki = parseInt(mMid[1], 10), kj = parseInt(mMid[2], 10);
          const pi = this.getPartnerXY(ki, triKey), pj = this.getPartnerXY(kj, triKey);
          if (pi && pj) {
            addPartnerPt(ki, '#38bdf8');
            addPartnerPt(kj, '#4ade80');
            addLine(`{ ${Math.min(ki, kj)}, ${Math.max(ki, kj)} }`, `Segment line X(${ki})X(${kj})`, pi, pj, '#38bdf8', `Line joining X_${ki} and X_${kj} bisected at X_${n}`, true, [`X_${ki}`, `X_${kj}`, `X_${n}`]);
            const rr = Math.hypot(P[0] - pi[0], P[1] - pi[1]);
            addCircle(`⊙(X_${n})`, `Midpoint circle ⊙(X_${n})`, P[0], P[1], rr, '#4ade80', `Circle centered at midpoint X_${n} passing through X_${ki} & X_${kj}`);
            plan.summary = `Midpoint of segment X_${ki}X_${kj}.`;
            hasPrimaryConstruction = true;
          }
        } else if (mInv && cc) {
          const kk = parseInt(mInv[1], 10);
          const pk = this.getPartnerXY(kk, triKey);
          if (pk) {
            addCircle('circumcircle', 'Circumcircle ⊙(ABC)', cc.cx, cc.cy, cc.r, '#c084fc', `Circle of inversion ⊙(O, R = ${cc.r.toFixed(4)})`);
            addPartnerPt(3, '#c084fc');
            addPartnerPt(kk, '#38bdf8');
            addLine(`{ ${Math.min(3, kk)}, ${Math.max(3, kk)} }`, `Inversion ray O X(${kk})`, [cc.cx, cc.cy], pk, '#38bdf8', `Radial inversion ray through X_3, X_${kk}, and X_${n}`, true, ['X_3', `X_${kk}`, `X_${n}`]);
            plan.summary = `Geometric inversion of X_${kk} in the circumcircle ⊙(ABC).`;
            hasPrimaryConstruction = true;
          }
        } else if (mComp) {
          const isAnti = Boolean(mComp[1]);
          const kk = parseInt(mComp[2], 10);
          const pk = this.getPartnerXY(kk, triKey);
          if (pk) {
            const med = medialTriangle(A, B, C);
            addPoly('< M_a M_b M_c >', 'Medial Triangle', [med.Ma, med.Mb, med.Mc], '#2dd4bf', 'Side midpoints of △ABC (homothety −1/2)');
            addPartnerPt(2, '#fb923c');
            addPartnerPt(kk, '#38bdf8');
            addLine(`{ ${Math.min(2, kk)}, ${Math.max(2, kk)} }`, `Homothety line X(2)X(${kk})`, centroid, pk, '#fb923c', `Centroid homothety (${isAnti ? '−2' : '−1/2'}) mapping X_${kk} → X_${n}`, true, ['X_2', `X_${kk}`, `X_${n}`]);
            plan.summary = `${isAnti ? 'Anticomplement' : 'Complement'} of X_${kk} under centroid homothety.`;
            hasPrimaryConstruction = true;
          }
        } else if (mIso) {
          const kk = parseInt(mIso[1], 10);
          const pk = this.getPartnerXY(kk, triKey);
          if (pk) {
            addPartnerPt(kk, '#e879f9');
            addLine(`[ A X_${kk} ]`, `Conjugate ray A X_${kk}`, A, pk, '#e879f9', `Source ray from A to isogonal conjugate X_${kk}`, true, ['A', `X_${kk}`]);
            addLine(`[ B X_${kk} ]`, `Conjugate ray B X_${kk}`, B, pk, '#e879f9', `Source ray from B to isogonal conjugate X_${kk}`, true, ['B', `X_${kk}`]);
            addLine(`[ C X_${kk} ]`, `Conjugate ray C X_${kk}`, C, pk, '#e879f9', `Source ray from C to isogonal conjugate X_${kk}`, true, ['C', `X_${kk}`]);
            plan.summary = `Isogonal conjugate of X_${kk} (reflected angle rays from A, B, C).`;
            hasPrimaryConstruction = true;
          }
        } else if (mIsot) {
          const kk = parseInt(mIsot[1], 10);
          const pk = this.getPartnerXY(kk, triKey);
          if (pk) {
            const med = medialTriangle(A, B, C);
            addPartnerPt(kk, '#a78bfa');
            addPt('M_a', 'M<tspan class="sub" dy="0.28em" font-size="0.72em">a</tspan>', 'Midpoint M_a', med.Ma, '#2dd4bf', 'Midpoint of side BC');
            addPt('M_b', 'M<tspan class="sub" dy="0.28em" font-size="0.72em">b</tspan>', 'Midpoint M_b', med.Mb, '#2dd4bf', 'Midpoint of side CA');
            addPt('M_c', 'M<tspan class="sub" dy="0.28em" font-size="0.72em">c</tspan>', 'Midpoint M_c', med.Mc, '#2dd4bf', 'Midpoint of side AB');
            addLine(`[ A X_${kk} ]`, `Source cevian A X_${kk}`, A, pk, '#a78bfa', `Source cevian to isotomic conjugate X_${kk}`, true, ['A', `X_${kk}`]);
            plan.summary = `Isotomic conjugate of X_${kk} (reflected cevian traces across midpoints).`;
            hasPrimaryConstruction = true;
          }
        }
      }

      // -----------------------------------------------------------------------
      // Tier 4a: Principal Intersecting Central Lines (Guarantees L_1 ∩ L_2 = X_n)
      // -----------------------------------------------------------------------
      if (!hasPrimaryConstruction && (center.li || []).length >= 2) {
        const chosen = [];
        for (const [iN, jN] of center.li) {
          const p1 = this.getPartnerXY(iN, triKey);
          const p2 = this.getPartnerXY(jN, triKey);
          if (!p1 || !p2) continue;
          const dx = p2[0] - p1[0], dy = p2[1] - p1[1], len = Math.hypot(dx, dy);
          if (len < 1e-7) continue;
          const ux = dx / len, uy = dy / len;
          // Ensure second line is genuinely transverse (not parallel to first!)
          if (chosen.length === 1) {
            const cross = Math.abs(chosen[0].ux * uy - chosen[0].uy * ux);
            if (cross < 0.08) continue;
          }
          chosen.push({ iN, jN, p1, p2, ux, uy });
          if (chosen.length >= 2) break;
        }
        if (chosen.length >= 2) {
          const cols = ['#38bdf8', '#f472b6'];
          chosen.forEach((ln, idx) => {
            addPartnerPt(ln.iN, cols[idx]);
            addPartnerPt(ln.jN, cols[idx]);
            addLine(
              `{ ${Math.min(ln.iN, ln.jN)}, ${Math.max(ln.iN, ln.jN)} }`,
              `Defining Line X(${ln.iN})X(${ln.jN})`,
              ln.p1,
              ln.p2,
              cols[idx],
              `${idx === 0 ? 'First' : 'Second'} defining central line through X_${ln.iN} and X_${ln.jN}`,
              true,
              [`X_${ln.iN}`, `X_${ln.jN}`, `X_${n}`]
            );
          });
          plan.summary = `Intersection of central lines X_${chosen[0].iN}X_${chosen[0].jN} and X_${chosen[1].iN}X_${chosen[1].jN}.`;
          hasPrimaryConstruction = true;
        }
      }

      // -----------------------------------------------------------------------
      // Tier 4b: Universal Cevian Concurrence Construction (A D_a ∩ B D_b ∩ C D_c = X_n)
      // Always added when finite and no perspector rays exist yet so every single center
      // has concrete vertex-to-sideline constructive geometry!
      // -----------------------------------------------------------------------
      if (P && !hasCevianOrPerspector) {
        const cev = cevianTraces(A, B, C, P);
        const maxDist = span * 6.0;
        const okTrace = (pt) => pt && Math.hypot(pt[0] - centroid[0], pt[1] - centroid[1]) < maxDist;
        const cevSpecs = [
          { vid: 'A', vxy: A, did: 'D_a', dlbl: 'D<tspan class="sub" dy="0.28em" font-size="0.72em">a</tspan>', trace: cev.Da, lid: '[ A D_a ]', side: 'BC', col: '#ff7043' },
          { vid: 'B', vxy: B, did: 'D_b', dlbl: 'D<tspan class="sub" dy="0.28em" font-size="0.72em">b</tspan>', trace: cev.Db, lid: '[ B D_b ]', side: 'CA', col: '#38bdf8' },
          { vid: 'C', vxy: C, did: 'D_c', dlbl: 'D<tspan class="sub" dy="0.28em" font-size="0.72em">c</tspan>', trace: cev.Dc, lid: '[ C D_c ]', side: 'AB', col: '#5ec27e' },
        ];
        let addedCev = 0;
        cevSpecs.forEach((cs) => {
          if (Math.hypot(P[0] - cs.vxy[0], P[1] - cs.vxy[1]) < 1e-6) return;
          const endPt = okTrace(cs.trace) ? cs.trace : P;
          addLine(cs.lid, `Cevian ${cs.vid} X_${n}`, cs.vxy, endPt, cs.col, `Cevian from vertex ${cs.vid} through X_${n} to sideline ${cs.side}`, true, [cs.vid, cs.did, `X_${n}`]);
          if (okTrace(cs.trace)) {
            addPt(cs.did, cs.dlbl, `Cevian trace ${cs.did}`, cs.trace, cs.col, `Trace of ${cs.vid} X_${n} on sideline ${cs.side}`);
          }
          addedCev++;
        });
        if (!plan.summary && addedCev > 0) {
          plan.summary = `Cevian concurrence A D_a ∩ B D_b ∩ C D_c = X_${n} on ${tMeta.label}.`;
        }
      }

      // Always register circumcircle & incircle as subtle guide circles if not already primary
      if (cc && !seenCircIds.has('circumcircle')) {
        addCircle('circumcircle', 'Circumcircle ⊙(ABC)', cc.cx, cc.cy, cc.r, '#a78bfa', `Reference circumcircle (R = ${cc.r.toFixed(4)})`, true);
      }
      if (ic && ic.r > 0 && !seenCircIds.has('incircle')) {
        addCircle('incircle', 'Incircle ⊙(I, r)', ic.cx, ic.cy, ic.r, '#e040fb', `Reference incircle (r = ${ic.r.toFixed(4)})`, true);
      }

      // Culminating step: Target Center X_n
      plan.steps.push({
        id: `X_${n}`,
        label: `X_${n}`,
        role: 'Target Center',
        color: '#e8b85a',
        desc: P
          ? `${center.t || `X_${n}`} • (${P[0].toFixed(4)}, ${P[1].toFixed(4)})`
          : `${center.t || `X_${n}`} • ${rec?.st === 'i' ? 'Point at infinity' : 'Indeterminate'}`,
      });

      return plan;
    }

    buildConstructionSvg(center, triKey, showLinesMode) {
      const tMeta = this.manifest.triangles[triKey] || this.manifest.triangles.heronian;
      const rec = center.tris?.[triKey];
      const n = center.n;
      const A = tMeta.verts.A;
      const B = tMeta.verts.B;
      const C = tMeta.verts.C;
      const centroid = [(A[0] + B[0] + C[0]) / 3, (A[1] + B[1] + C[1]) / 3];
      const span = Math.max(...tMeta.sides);
      const plan = this.computeConstructionPlan(center, triKey);

      const pts = [A, B, C];
      const hasFiniteTarget = rec && rec.st === 'f' && Array.isArray(rec.xy);
      const targetPt = hasFiniteTarget ? rec.xy : null;
      if (targetPt) {
        const distFromTri = Math.hypot(targetPt[0] - centroid[0], targetPt[1] - centroid[1]);
        if (distFromTri < span * 3.5) pts.push(targetPt);
      }
      // Include close construction points so derived triangles / anchor centers frame cleanly
      plan.points.forEach((pt) => {
        const d = Math.hypot(pt.xy[0] - centroid[0], pt.xy[1] - centroid[1]);
        if (d < span * 2.4) pts.push(pt.xy);
      });

      const xs = pts.map((p) => p[0]);
      const ys = pts.map((p) => -p[1]);
      const minX = Math.min(...xs), maxX = Math.max(...xs);
      const minY = Math.min(...ys), maxY = Math.max(...ys);
      const w0 = Math.max(maxX - minX, span * 0.5);
      const h0 = Math.max(maxY - minY, span * 0.5);
      const pad = Math.max(w0, h0) * 0.14;
      const vbW = w0 + 2 * pad;
      const vbH = Math.max(h0 + 2 * pad, vbW * 0.72);
      const cx0 = (minX + maxX) * 0.5;
      const cy0 = (minY + maxY) * 0.5;
      const vb = [cx0 - vbW * 0.5, cy0 - vbH * 0.5, vbW, vbH];
      const vbStr = vb.map((v) => v.toFixed(6)).join(' ');
      const lineExt = Math.max(vbW, vbH) * 1.4;

      const meta = {};
      const graphicsExtra = [];
      const linesSvg = [];
      const hlSvg = [];
      const ptsSvg = [];
      const lblSvg = [];

      // Sidelines (sparse dotted infinite)
      const sideSpecs = [
        { id: '[ B C ]', lbl: 'Side a (BC)', p1: B, p2: C },
        { id: '[ C A ]', lbl: 'Side b (CA)', p1: C, p2: A },
        { id: '[ A B ]', lbl: 'Side c (AB)', p1: A, p2: B },
      ];
      sideSpecs.forEach((sd) => {
        const x1 = sd.p1[0], y1 = -sd.p1[1], x2 = sd.p2[0], y2 = -sd.p2[1];
        const dx = x2 - x1, dy = y2 - y1, len = Math.hypot(dx, dy) || 1;
        const ux = dx / len, uy = dy / len, mx = (x1 + x2) / 2, my = (y1 + y2) / 2;
        linesSvg.push(
          `<line class="sideline" data-id="${sd.id}" data-line="${mx.toFixed(6)},${my.toFixed(6)},${ux.toFixed(8)},${uy.toFixed(8)}" x1="${(mx - ux * lineExt).toFixed(5)}" y1="${(my - uy * lineExt).toFixed(5)}" x2="${(mx + ux * lineExt).toFixed(5)}" y2="${(my + uy * lineExt).toFixed(5)}" />`
        );
        meta[sd.id] = { ID: sd.id, name: sd.lbl, type: 'sideline', color: '#94a3b8', rows: [['Triangle', tMeta.label]] };
      });

      // Construction Polygons (derived triangles like tangential / circummedial / medial / orthic)
      plan.polygons.forEach((pg) => {
        const pStr = pg.verts.map((v) => `${v[0].toFixed(6)},${(-v[1]).toFixed(6)}`).join(' ');
        graphicsExtra.push(
          `<polygon class="secondary" data-id="${esc(pg.id)}" points="${pStr}" style="stroke:${pg.color};fill:${pg.color};fill-opacity:0.06;stroke-opacity:0.65;stroke-width:2.2;stroke-dasharray:6,4" />`
        );
        meta[pg.id] = { ID: pg.id, name: pg.name, type: 'derived triangle', color: pg.color };
      });

      // Construction Circles & Guide Circles
      plan.circles.forEach((ci) => {
        const cls = ci.isGuide ? `guide ${ci.id}` : `secondary_circle`;
        linesSvg.push(
          `<circle class="${cls}" data-id="${esc(ci.id)}" style="stroke:${ci.color}" cx="${ci.cx.toFixed(6)}" cy="${(-ci.cy).toFixed(6)}" r="${ci.r.toFixed(6)}" />`
        );
        meta[ci.id] = { ID: ci.id, name: ci.name, type: ci.isGuide ? 'guide circle' : 'construction circle', color: ci.color, rows: [['Radius', ci.r.toFixed(5)]] };
      });

      // Construction Lines (sparse round dots -> solid in their own color on hover!)
      const constrLineIds = new Set();
      plan.lines.forEach((ln) => {
        constrLineIds.add(ln.id);
        const x1 = ln.p1[0], y1 = -ln.p1[1], x2 = ln.p2[0], y2 = -ln.p2[1];
        const dx = x2 - x1, dy = y2 - y1, len = Math.hypot(dx, dy) || 1;
        const ux = dx / len, uy = dy / len, mx = (x1 + x2) / 2, my = (y1 + y2) / 2;
        linesSvg.push(
          `<line class="construction_line" data-id="${esc(ln.id)}" style="stroke:${ln.color}" data-line="${mx.toFixed(6)},${my.toFixed(6)},${ux.toFixed(8)},${uy.toFixed(8)}" x1="${(mx - ux * lineExt).toFixed(5)}" y1="${(my - uy * lineExt).toFixed(5)}" x2="${(mx + ux * lineExt).toFixed(5)}" y2="${(my + uy * lineExt).toFixed(5)}" />`
        );
        hlSvg.push(
          `<line class="highlight-segment" data-highlight-for="${esc(ln.id)}" style="display:none;stroke:${ln.color}" x1="${x1.toFixed(5)}" y1="${y1.toFixed(5)}" x2="${x2.toFixed(5)}" y2="${y2.toFixed(5)}" />`
        );
        meta[ln.id] = { ID: ln.id, name: ln.name, type: 'construction line', color: ln.color, parents: ln.relatedPts };
      });

      // Construction Helper Points & Anchor Centers (always visible in Construction mode!)
      const addedPartners = new Set();
      plan.points.forEach((pt) => {
        if (pt.pk) addedPartners.add(pt.pk);
        const sx = pt.xy[0], sy = -pt.xy[1];
        ptsSvg.push(`<circle class="center construction-pt" data-id="${esc(pt.id)}" style="fill:${pt.color}" cx="${sx.toFixed(6)}" cy="${sy.toFixed(6)}" r="0.01" />`);
        lblSvg.push(
          `<text class="point-label" data-point-id="${esc(pt.id)}" data-anchor-x="${sx.toFixed(6)}" data-anchor-y="${sy.toFixed(6)}" data-offset-x="10" data-offset-y="-8" x="${sx.toFixed(6)}" y="${sy.toFixed(6)}">${pt.labelHtml}</text>`
        );
        meta[pt.id] = {
          ID: pt.id,
          name: pt.name,
          type: pt.isPartner ? 'anchor center' : 'construction vertex',
          color: pt.color,
          rows: [['Cartesian', `(${pt.xy[0].toFixed(5)}, ${pt.xy[1].toFixed(5)})`]],
        };
      });

      // Incident Central Lines + companion partner points (sparse dots -> solid on hover, shown in Lines mode)
      const rawLines = (center.li || []).slice(0, 14);
      rawLines.forEach(([iN, jN], idx) => {
        const lid = `{ ${iN}, ${jN} }`;
        if (constrLineIds.has(lid)) return;
        const p1 = this.getPartnerXY(iN, triKey);
        const p2 = this.getPartnerXY(jN, triKey);
        if (!p1 || !p2) return;
        const x1 = p1[0], y1 = -p1[1], x2 = p2[0], y2 = -p2[1];
        const dx = x2 - x1, dy = y2 - y1, len = Math.hypot(dx, dy);
        if (len < 1e-8) return;
        const ux = dx / len, uy = dy / len, mx = (x1 + x2) / 2, my = (y1 + y2) / 2;
        const col = LINE_PALETTE[idx % LINE_PALETTE.length];
        linesSvg.push(
          `<line class="central_line incident" data-id="${lid}" style="stroke:${col}" data-line="${mx.toFixed(6)},${my.toFixed(6)},${ux.toFixed(8)},${uy.toFixed(8)}" x1="${(mx - ux * lineExt).toFixed(5)}" y1="${(my - uy * lineExt).toFixed(5)}" x2="${(mx + ux * lineExt).toFixed(5)}" y2="${(my + uy * lineExt).toFixed(5)}" />`
        );
        hlSvg.push(
          `<line class="highlight-segment" data-highlight-for="${lid}" style="display:none;stroke:${col}" x1="${x1.toFixed(5)}" y1="${y1.toFixed(5)}" x2="${x2.toFixed(5)}" y2="${y2.toFixed(5)}" />`
        );
        meta[lid] = {
          ID: lid,
          name: `Line X(${iN}) X(${jN})`,
          type: 'central line',
          color: col,
          parents: [`X_${iN}`, `X_${jN}`, `X_${n}`],
          rows: [
            ['Through', `X_${iN} (${this.getPartnerTitle(iN)})`],
            ['And', `X_${jN} (${this.getPartnerTitle(jN)})`],
          ],
        };

        [
          [iN, p1],
          [jN, p2],
        ].forEach(([pk, pxy]) => {
          if (pk === n || addedPartners.has(pk)) return;
          addedPartners.add(pk);
          const pid = `X_${pk}`;
          const sx = pxy[0], sy = -pxy[1];
          ptsSvg.push(`<circle class="center incident" data-id="${pid}" cx="${sx.toFixed(6)}" cy="${sy.toFixed(6)}" r="0.01" />`);
          lblSvg.push(
            `<text class="point-label incident" data-point-id="${pid}" data-anchor-x="${sx.toFixed(6)}" data-anchor-y="${sy.toFixed(6)}" data-offset-x="10" data-offset-y="-8" x="${sx.toFixed(6)}" y="${sy.toFixed(6)}">X<tspan class="sub" dy="0.28em" font-size="0.72em">${pk}</tspan></text>`
          );
          meta[pid] = {
            ID: pid,
            name: this.getPartnerTitle(pk),
            type: 'companion center',
            color: '#e0e0e0',
            rows: [['Cartesian', `(${pxy[0].toFixed(5)}, ${pxy[1].toFixed(5)})`]],
          };
        });
      });

      // Reference triangle polygon + right-angle mark on right / kepler
      const polyPts = `${A[0].toFixed(6)},${(-A[1]).toFixed(6)} ${B[0].toFixed(6)},${(-B[1]).toFixed(6)} ${C[0].toFixed(6)},${(-C[1]).toFixed(6)}`;
      let rightMarkSvg = '';
      if (tMeta.is_right) {
        const rSz = Math.min(...tMeta.sides) * 0.085;
        rightMarkSvg = `<path class="right-angle-mark" d="${rightAnglePath(A[0], -A[1], B[0], -B[1], C[0], -C[1], rSz)}" fill="none" stroke="#94a3b8" stroke-width="1.6" vector-effect="non-scaling-stroke" />`;
      }

      // Vertices A, B, C
      [
        ['A', A, -18, 18],
        ['B', B, 14, 18],
        ['C', C, 12, -12],
      ].forEach(([vid, vxy, ox, oy]) => {
        const sx = vxy[0], sy = -vxy[1];
        ptsSvg.push(`<circle class="given vertex" data-id="${vid}" cx="${sx.toFixed(6)}" cy="${sy.toFixed(6)}" r="0.01" />`);
        lblSvg.push(
          `<text class="given-label" data-point-id="${vid}" data-anchor-x="${sx.toFixed(6)}" data-anchor-y="${sy.toFixed(6)}" data-offset-x="${ox}" data-offset-y="${oy}" x="${sx.toFixed(6)}" y="${sy.toFixed(6)}">${vid}</text>`
        );
        meta[vid] = {
          ID: vid,
          name: `Vertex ${vid}`,
          type: 'reference vertex',
          color: '#66ff66',
          rows: [['Coordinates', `(${vxy[0].toFixed(5)}, ${vxy[1].toFixed(5)})`]],
        };
      });

      // Target Center X_n (finite, ideal ray, or indeterminate)
      const tid = `X_${n}`;
      let specialGraphicSvg = '';
      if (hasFiniteTarget) {
        const sx = targetPt[0], sy = -targetPt[1];
        ptsSvg.push(`<circle class="target selected" data-id="${tid}" cx="${sx.toFixed(6)}" cy="${sy.toFixed(6)}" r="0.01" />`);
        lblSvg.push(
          `<text class="target-label selected-label" data-point-id="${tid}" data-anchor-x="${sx.toFixed(6)}" data-anchor-y="${sy.toFixed(6)}" data-offset-x="14" data-offset-y="-12" x="${sx.toFixed(6)}" y="${sy.toFixed(6)}">X<tspan class="sub" dy="0.28em" font-size="0.72em">${n}</tspan></text>`
        );
      } else if (rec && rec.st === 'i' && Array.isArray(rec.b)) {
        const gx = centroid[0], gy = centroid[1];
        const dirX = rec.b[0] * A[0] + rec.b[1] * B[0] + rec.b[2] * C[0];
        const dirY = rec.b[0] * A[1] + rec.b[1] * B[1] + rec.b[2] * C[1];
        const dl = Math.hypot(dirX, dirY) || 1;
        const rx = gx + (dirX / dl) * span * 0.65;
        const ry = gy + (dirY / dl) * span * 0.65;
        specialGraphicSvg = `<line data-id="${tid}" x1="${gx.toFixed(5)}" y1="${(-gy).toFixed(5)}" x2="${rx.toFixed(5)}" y2="${(-ry).toFixed(5)}" stroke="#e8b85a" stroke-width="2.6" stroke-dasharray="6,4" vector-effect="non-scaling-stroke" />`;
        ptsSvg.push(`<circle class="target selected" data-id="${tid}" cx="${rx.toFixed(6)}" cy="${(-ry).toFixed(6)}" r="0.01" />`);
        lblSvg.push(
          `<text class="target-label selected-label" data-point-id="${tid}" data-anchor-x="${rx.toFixed(6)}" data-anchor-y="${(-ry).toFixed(6)}" data-offset-x="12" data-offset-y="-10" x="${rx.toFixed(6)}" y="${(-ry).toFixed(6)}">X<tspan class="sub" dy="0.28em" font-size="0.72em">${n}</tspan> (∞)</text>`
        );
      }

      const symRows = [];
      if (rec?.bl) symRows.push({ label: 'Barycentric', latex: rec.bl, pretty: rec.bl });
      if (rec?.tl) symRows.push({ label: 'Trilinear', latex: rec.tl, pretty: rec.tl });
      if (rec?.xyl) symRows.push({ label: 'Cartesian', latex: rec.xyl, pretty: rec.xyl });
      if (rec?.f || tMeta.field) symRows.push({ label: 'Field', latex: rec?.f || tMeta.field, pretty: rec?.f || tMeta.field });
      meta[tid] = {
        ID: tid,
        name: center.t || tid,
        type: rec?.p === 'e' ? 'exact center' : '50-digit center',
        color: '#e8b85a',
        symbolic_rows: symRows,
        approx: hasFiniteTarget ? `≈ (${targetPt[0].toFixed(6)}, ${targetPt[1].toFixed(6)})` : rec?.sn || '',
      };

      const subParts = [tMeta.label, `Δ = ${tMeta.area_latex === '84' ? '84' : tMeta.area.toFixed(4)}`];
      if (rec?.sn) subParts.push(rec.sn);
      else if (rec?.p === 'e') subParts.push('Exact Symbolic');
      else if (rec?.p === 'm') subParts.push('50-digit Numeric');
      const subtitleText = subParts.join(' | ');

      return `<svg class="geometor-etc-drawing${showLinesMode ? ' show-lines' : ''}" xmlns="http://www.w3.org/2000/svg" viewBox="${vbStr}" data-initial-viewbox="${vbStr}" data-triangle="${triKey}" data-field="${esc(rec?.f || tMeta.field)}" data-tri-span="${span.toFixed(6)}" data-target-r-px="10.5" preserveAspectRatio="xMidYMid meet">
        <g id="graphics">
          ${graphicsExtra.join('')}
          <polygon data-id="< A B C >" points="${polyPts}" />
          ${rightMarkSvg}
          ${specialGraphicSvg}
        </g>
        <g id="elements">${linesSvg.join('')}</g>
        <g id="highlights">${hlSvg.join('')}</g>
        <g id="points">${ptsSvg.join('')}</g>
        <g id="labels">
          ${lblSvg.join('')}
          <text class="subtitle-label" x="${vb[0].toFixed(4)}" y="${(vb[1] + vb[3]).toFixed(4)}" font-size="1">${esc(subtitleText)}</text>
        </g>
        <script type="application/json" class="etc-elements-meta">${JSON.stringify(meta).replace(/</g, '\\u003c')}</script>
      </svg>`;
    }

    buildCoordinatesSvg(center, reqTriKey) {
      const useKey =
        reqTriKey && center.tris?.[reqTriKey]?.st === 'f' && Array.isArray(center.tris[reqTriKey].xy)
          ? reqTriKey
          : 'heronian';
      const tMeta = this.manifest.triangles[useKey] || this.manifest.triangles.heronian;
      const rec = center.tris?.[useKey];
      const n = center.n;
      const A = tMeta.verts.A;
      const B = tMeta.verts.B;
      const C = tMeta.verts.C;
      const hasFinite = rec && rec.st === 'f' && Array.isArray(rec.xy);
      const P = hasFinite ? rec.xy : [(A[0] + B[0] + C[0]) / 3, (A[1] + B[1] + C[1]) / 3];
      const plan = this.computeConstructionPlan(center, useKey);

      const Ta = footOfPerp(P[0], P[1], B[0], B[1], C[0], C[1]);
      const Tb = footOfPerp(P[0], P[1], C[0], C[1], A[0], A[1]);
      const Tc = footOfPerp(P[0], P[1], A[0], A[1], B[0], B[1]);

      const allPts = [A, B, C, P, [Ta.x, Ta.y], [Tb.x, Tb.y], [Tc.x, Tc.y]];
      const xs = allPts.map((p) => p[0]);
      const ys = allPts.map((p) => p[1]);
      const minX = Math.min(...xs), maxX = Math.max(...xs);
      const minY = Math.min(...ys), maxY = Math.max(...ys);
      const scale = Math.min(780 / Math.max(maxX - minX, 1), 540 / Math.max(maxY - minY, 1));
      const cxM = (minX + maxX) / 2;
      const cyM = (minY + maxY) / 2;
      const toS = (x, y) => [500 + (x - cxM) * scale, 405 - (y - cyM) * scale];

      const sA = toS(A[0], A[1]);
      const sB = toS(B[0], B[1]);
      const sC = toS(C[0], C[1]);
      const sP = toS(P[0], P[1]);
      const sTa = toS(Ta.x, Ta.y);
      const sTb = toS(Tb.x, Tb.y);
      const sTc = toS(Tc.x, Tc.y);

      const channels = [
        { k: 'a', sym: 'α', bs: 'u', col: '#ff7043', foot: sTa, footId: 'T_a', strutId: `[ X_${n} T_a /`, triId: `< X_${n} B C >`, v1: sB, v2: sC, ra: rightAnglePath(sTa[0], sTa[1], sP[0], sP[1], sB[0], sB[1], 11) },
        { k: 'b', sym: 'β', bs: 'v', col: '#38bdf8', foot: sTb, footId: 'T_b', strutId: `[ X_${n} T_b /`, triId: `< X_${n} C A >`, v1: sC, v2: sA, ra: rightAnglePath(sTb[0], sTb[1], sP[0], sP[1], sC[0], sC[1], 11) },
        { k: 'c', sym: 'γ', bs: 'w', col: '#5ec27e', foot: sTc, footId: 'T_c', strutId: `[ X_${n} T_c /`, triId: `< X_${n} A B >`, v1: sA, v2: sB, ra: rightAnglePath(sTc[0], sTc[1], sP[0], sP[1], sA[0], sA[1], 11) },
      ];

      const meta = {
        [`X_${n}`]: {
          ID: `X_${n}`,
          name: center.t || `X_${n}`,
          type: 'target center',
          color: '#e8b85a',
          symbolic_rows: [
            ...(rec?.tl ? [{ label: 'Trilinear', latex: rec.tl, pretty: rec.tl }] : []),
            ...(rec?.bl ? [{ label: 'Barycentric', latex: rec.bl, pretty: rec.bl }] : []),
            ...(rec?.xyl ? [{ label: 'Cartesian', latex: rec.xyl, pretty: rec.xyl }] : []),
          ],
        },
      };

      // Subtle Construction Evidence Layer underneath the Coordinates decomposition!
      // Preserves data-id & metadata so hovering Construction rows highlights them live right here.
      const evSvg = [];
      const evPtsSvg = [];
      plan.polygons.forEach((pg) => {
        const ptsS = pg.verts.map((v) => toS(v[0], v[1]).map((z) => z.toFixed(1)).join(',')).join(' ');
        evSvg.push(
          `<polygon class="etc-plate-poly" data-id="${esc(pg.id)}" points="${ptsS}" fill="${pg.color}" fill-opacity="0.04" stroke="${pg.color}" stroke-width="1.6" stroke-dasharray="5,4" />`
        );
        meta[pg.id] = { ID: pg.id, name: pg.name, type: 'derived triangle', color: pg.color };
      });
      plan.circles.forEach((ci) => {
        const sc = toS(ci.cx, ci.cy);
        const sr = ci.r * scale;
        if (sr > 2 && sr < 2600) {
          evSvg.push(
            `<circle class="etc-plate-circle" data-id="${esc(ci.id)}" cx="${sc[0].toFixed(1)}" cy="${sc[1].toFixed(1)}" r="${sr.toFixed(1)}" fill="none" stroke="${ci.color}" stroke-width="1.6" stroke-linecap="round" stroke-dasharray="0.1 9" />`
          );
          meta[ci.id] = { ID: ci.id, name: ci.name, type: ci.isGuide ? 'guide circle' : 'construction circle', color: ci.color };
        }
      });
      plan.lines.forEach((ln) => {
        const p1 = toS(ln.p1[0], ln.p1[1]);
        const p2 = toS(ln.p2[0], ln.p2[1]);
        const dx = p2[0] - p1[0], dy = p2[1] - p1[1], d = Math.hypot(dx, dy);
        if (d < 1e-4) return;
        const ux = dx / d, uy = dy / d, mx = (p1[0] + p2[0]) / 2, my = (p1[1] + p2[1]) / 2;
        const ext = 1600;
        evSvg.push(
          `<line class="etc-plate-line" data-id="${esc(ln.id)}" x1="${(mx - ux * ext).toFixed(1)}" y1="${(my - uy * ext).toFixed(1)}" x2="${(mx + ux * ext).toFixed(1)}" y2="${(my + uy * ext).toFixed(1)}" stroke="${ln.color}" stroke-width="2.0" stroke-linecap="round" stroke-dasharray="0.1 10" />`
        );
        meta[ln.id] = { ID: ln.id, name: ln.name, type: 'construction line', color: ln.color, parents: ln.relatedPts };
      });
      plan.points.forEach((pt) => {
        const sp = toS(pt.xy[0], pt.xy[1]);
        if (sp[0] > -60 && sp[0] < 1060 && sp[1] > -60 && sp[1] < 820) {
          evPtsSvg.push(
            `<circle class="etc-plate-pt" data-id="${esc(pt.id)}" cx="${sp[0].toFixed(1)}" cy="${sp[1].toFixed(1)}" r="4.5" fill="${pt.color}" fill-opacity="0.72" stroke="#161616" stroke-width="1.6" />`
          );
          meta[pt.id] = { ID: pt.id, name: pt.name, type: pt.isPartner ? 'anchor center' : 'construction vertex', color: pt.color };
        }
      });

      const subPolys = [];
      const struts = [];
      const feet = [];
      channels.forEach((ch) => {
        subPolys.push(
          `<polygon class="etc-plate-poly etc-sub-tri" data-id="${ch.triId}" points="${sP[0].toFixed(1)},${sP[1].toFixed(1)} ${ch.v1[0].toFixed(1)},${ch.v1[1].toFixed(1)} ${ch.v2[0].toFixed(1)},${ch.v2[1].toFixed(1)}" fill="${ch.col}" fill-opacity="0.13" stroke="${ch.col}" stroke-opacity="0.45" stroke-width="1.4" />`
        );
        struts.push(
          `<line class="etc-plate-strut etc-trilin-strut" data-id="${ch.strutId}" x1="${sP[0].toFixed(1)}" y1="${sP[1].toFixed(1)}" x2="${ch.foot[0].toFixed(1)}" y2="${ch.foot[1].toFixed(1)}" stroke="${ch.col}" stroke-width="3.2" stroke-linecap="round" />` +
            `<path d="${ch.ra}" fill="none" stroke="${ch.col}" stroke-width="1.5" opacity="0.85" />` +
            `<text x="${((sP[0] + ch.foot[0]) / 2 + 8).toFixed(1)}" y="${((sP[1] + ch.foot[1]) / 2 - 6).toFixed(1)}" fill="${ch.col}" font-family="EB Garamond, Georgia, serif" font-style="italic" font-size="22" font-weight="700">${ch.sym}</text>`
        );
        feet.push(
          `<circle class="etc-plate-pt" data-id="${ch.footId}" cx="${ch.foot[0].toFixed(1)}" cy="${ch.foot[1].toFixed(1)}" r="5.5" fill="${ch.col}" stroke="#161616" stroke-width="2" />` +
            `<text x="${(ch.foot[0] + 10).toFixed(1)}" y="${(ch.foot[1] + 5).toFixed(1)}" fill="${ch.col}" font-family="JetBrains Mono, monospace" font-size="15" font-weight="600">T<tspan dy="4" font-size="11">${ch.k}</tspan></text>`
        );
        meta[ch.strutId] = { ID: ch.sym, name: `Trilinear distance ${ch.sym} to side ${ch.k}`, type: 'trilinear strut', color: ch.col };
        meta[ch.triId] = { ID: ch.bs, name: `Signed sub-triangle ${ch.triId}`, type: 'barycentric area', color: ch.col };
        meta[ch.footId] = { ID: ch.footId, name: `Pedal foot ${ch.footId}`, type: 'pedal foot', color: ch.col };
      });

      const areaTxt = tMeta.area_latex === '84' ? '84' : tMeta.area.toFixed(4);
      const subBanner = `${tMeta.label} • ${rec?.p === 'e' ? 'Exact Symbolic' : '50-digit Numeric'} • Δ = ${areaTxt}`;
      return `<svg class="geometor-etc-drawing" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 760" data-initial-viewbox="0 0 1000 760" data-triangle="${useKey}" preserveAspectRatio="xMidYMid meet">
        <defs><clipPath id="coord-stage-clip"><rect x="0" y="76" width="1000" height="684" /></clipPath></defs>
        <rect width="1000" height="760" fill="#141416" />
        <text x="26" y="42" fill="#e8b85a" font-family="EB Garamond, Georgia, serif" font-size="24" font-weight="700">X<tspan dy="5" font-size="16">${n}</tspan><tspan dy="-5"> — Coordinate Decomposition</tspan></text>
        <text x="26" y="66" fill="#94a3b8" font-family="Fira Sans Condensed, sans-serif" font-size="14">Trilinear struts (α, β, γ) &amp; barycentric areas (u, v, w) over construction elements on ${esc(tMeta.label)}</text>
        <g id="plate-subtris" clip-path="url(#coord-stage-clip)">${subPolys.join('')}</g>
        <g id="coord-construction-evidence" class="etc-coord-evidence" clip-path="url(#coord-stage-clip)">${evSvg.join('')}</g>
        <polygon points="${sA[0].toFixed(1)},${sA[1].toFixed(1)} ${sB[0].toFixed(1)},${sB[1].toFixed(1)} ${sC[0].toFixed(1)},${sC[1].toFixed(1)}" fill="none" stroke="#60a5fa" stroke-width="3.2" stroke-linejoin="round" />
        <g id="plate-struts">${struts.join('')}</g>
        <g id="coord-construction-pts">${evPtsSvg.join('')}</g>
        <g id="plate-feet">${feet.join('')}</g>
        <circle class="etc-plate-pt given" data-id="A" cx="${sA[0].toFixed(1)}" cy="${sA[1].toFixed(1)}" r="6" fill="#4ade80" stroke="#161616" stroke-width="2" />
        <text x="${(sA[0] - 22).toFixed(1)}" y="${(sA[1] + 22).toFixed(1)}" fill="#86efac" font-family="JetBrains Mono, monospace" font-size="17" font-weight="700">A</text>
        <circle class="etc-plate-pt given" data-id="B" cx="${sB[0].toFixed(1)}" cy="${sB[1].toFixed(1)}" r="6" fill="#4ade80" stroke="#161616" stroke-width="2" />
        <text x="${(sB[0] + 12).toFixed(1)}" y="${(sB[1] + 22).toFixed(1)}" fill="#86efac" font-family="JetBrains Mono, monospace" font-size="17" font-weight="700">B</text>
        <circle class="etc-plate-pt given" data-id="C" cx="${sC[0].toFixed(1)}" cy="${sC[1].toFixed(1)}" r="6" fill="#4ade80" stroke="#161616" stroke-width="2" />
        <text x="${(sC[0] - 6).toFixed(1)}" y="${(sC[1] - 14).toFixed(1)}" fill="#86efac" font-family="JetBrains Mono, monospace" font-size="17" font-weight="700">C</text>
        <circle class="etc-plate-pt target selected" data-id="X_${n}" cx="${sP[0].toFixed(1)}" cy="${sP[1].toFixed(1)}" r="8" />
        <text x="${(sP[0] + 12).toFixed(1)}" y="${(sP[1] - 12).toFixed(1)}" fill="#ffd54f" font-family="JetBrains Mono, monospace" font-size="18" font-weight="700">X<tspan dy="4" font-size="13">${n}</tspan></text>
        <text x="976" y="742" text-anchor="end" fill="#94a3b8" font-family="JetBrains Mono, monospace" font-size="14">${esc(subBanner)}</text>
        <script type="application/json" class="etc-elements-meta">${JSON.stringify(meta).replace(/</g, '\\u003c')}</script>
      </svg>`;
    }

    buildRelationsSvg(center) {
      const tMeta = this.manifest.triangles.heronian;
      const rec = center.tris?.heronian;
      const n = center.n;
      const A = tMeta.verts.A, B = tMeta.verts.B, C = tMeta.verts.C;
      const hasFinite = rec && rec.st === 'f' && Array.isArray(rec.xy);
      const P = hasFinite ? rec.xy : null;

      // Extract distinct referenced relational partner centers
      const partners = [];
      const seen = new Set([n]);
      (center.re || []).forEach((rTxt) => {
        const re = /\bX_(\d+)/g;
        let m;
        while ((m = re.exec(rTxt)) !== null) {
          const pk = parseInt(m[1], 10);
          if (!seen.has(pk)) {
            const pxy = this.getPartnerXY(pk, 'heronian');
            if (pxy) {
              seen.add(pk);
              partners.push({ k: pk, xy: pxy, rel: rTxt });
              if (partners.length >= 14) break;
            }
          }
        }
      });

      const allPts = [A, B, C];
      if (P) allPts.push(P);
      const span = 15;
      partners.forEach((p) => {
        if (Math.hypot(p.xy[0] - 6.3, p.xy[1] - 4) < span * 3.0) allPts.push(p.xy);
      });
      const xs = allPts.map((p) => p[0]);
      const ys = allPts.map((p) => -p[1]);
      const minX = Math.min(...xs), maxX = Math.max(...xs);
      const minY = Math.min(...ys), maxY = Math.max(...ys);
      const w0 = Math.max(maxX - minX, 10), h0 = Math.max(maxY - minY, 8);
      const pad = Math.max(w0, h0) * 0.16;
      const vbW = w0 + 2 * pad, vbH = Math.max(h0 + 2 * pad, vbW * 0.72);
      const vb = [(minX + maxX) / 2 - vbW / 2, (minY + maxY) / 2 - vbH / 2, vbW, vbH];
      const vbStr = vb.map((v) => v.toFixed(6)).join(' ');

      const els = [];
      const ptsSvg = [];
      const lblSvg = [];
      const meta = {};

      partners.forEach((p, idx) => {
        const col = LINE_PALETTE[idx % LINE_PALETTE.length];
        const pid = `X_${p.k}`;
        if (P) {
          els.push(
            `<line class="central_line" data-id="rel_${p.k}" style="stroke:${col}" x1="${P[0].toFixed(5)}" y1="${(-P[1]).toFixed(5)}" x2="${p.xy[0].toFixed(5)}" y2="${(-p.xy[1]).toFixed(5)}" />`
          );
          meta[`rel_${p.k}`] = { ID: `X_${n} ↔ X_${p.k}`, name: p.rel, type: 'relation link', color: col, parents: [`X_${n}`, pid] };
        }
        ptsSvg.push(`<circle class="center" data-id="${pid}" style="fill:${col}" cx="${p.xy[0].toFixed(6)}" cy="${(-p.xy[1]).toFixed(6)}" r="0.01" />`);
        lblSvg.push(
          `<text class="point-label" data-point-id="${pid}" data-anchor-x="${p.xy[0].toFixed(6)}" data-anchor-y="${(-p.xy[1]).toFixed(6)}" data-offset-x="10" data-offset-y="-8" x="${p.xy[0].toFixed(6)}" y="${(-p.xy[1]).toFixed(6)}">X<tspan class="sub" dy="0.28em" font-size="0.72em">${p.k}</tspan></text>`
        );
        meta[pid] = { ID: pid, name: this.getPartnerTitle(p.k), type: 'relational partner', color: col, rows: [['Relation', p.rel]] };
      });

      [
        ['A', A, -18, 18],
        ['B', B, 14, 18],
        ['C', C, 12, -12],
      ].forEach(([vid, vxy, ox, oy]) => {
        ptsSvg.push(`<circle class="given vertex" data-id="${vid}" cx="${vxy[0].toFixed(6)}" cy="${(-vxy[1]).toFixed(6)}" r="0.01" />`);
        lblSvg.push(`<text class="given-label" data-point-id="${vid}" data-anchor-x="${vxy[0].toFixed(6)}" data-anchor-y="${(-vxy[1]).toFixed(6)}" data-offset-x="${ox}" data-offset-y="${oy}" x="${vxy[0].toFixed(6)}" y="${(-vxy[1]).toFixed(6)}">${vid}</text>`);
      });

      if (P) {
        const tid = `X_${n}`;
        ptsSvg.push(`<circle class="target selected" data-id="${tid}" cx="${P[0].toFixed(6)}" cy="${(-P[1]).toFixed(6)}" r="0.01" />`);
        lblSvg.push(`<text class="target-label selected-label" data-point-id="${tid}" data-anchor-x="${P[0].toFixed(6)}" data-anchor-y="${(-P[1]).toFixed(6)}" data-offset-x="14" data-offset-y="-12" x="${P[0].toFixed(6)}" y="${(-P[1]).toFixed(6)}">X<tspan class="sub" dy="0.28em" font-size="0.72em">${n}</tspan></text>`);
        meta[tid] = { ID: tid, name: center.t || tid, type: 'target center', color: '#e8b85a' };
      }

      const polyPts = `${A[0]},${-A[1]} ${B[0]},${-B[1]} ${C[0]},${-C[1]}`;
      return `<svg class="geometor-etc-drawing" xmlns="http://www.w3.org/2000/svg" viewBox="${vbStr}" data-initial-viewbox="${vbStr}" data-triangle="heronian" data-tri-span="15" preserveAspectRatio="xMidYMid meet">
        <g id="graphics"><polygon points="${polyPts}" /></g>
        <g id="elements">${els.join('')}</g>
        <g id="highlights"></g>
        <g id="points">${ptsSvg.join('')}</g>
        <g id="labels">
          ${lblSvg.join('')}
          <text class="subtitle-label" x="0" y="0" font-size="1">Heronian (15, 13, 14) | ${partners.length} mapped relational partner centers</text>
        </g>
        <script type="application/json" class="etc-elements-meta">${JSON.stringify(meta).replace(/</g, '\\u003c')}</script>
      </svg>`;
    }

    buildSixTrianglesSvg(center) {
      const n = center.n;
      const gridSpecs = TRI_ORDER.slice(0, 6);
      const pw = 372, ph = 336, gapX = 16, gapY = 16, startX = 26, startY = 64;
      const panels = [];
      const meta = {};

      gridSpecs.forEach((spec, idx) => {
        const colIdx = idx % 3;
        const rowIdx = Math.floor(idx / 3);
        const ox = startX + colIdx * (pw + gapX);
        const oy = startY + rowIdx * (ph + gapY);
        const tMeta = this.manifest.triangles[spec.key];
        const rec = center.tris?.[spec.key];
        const A = tMeta.verts.A, B = tMeta.verts.B, C = tMeta.verts.C;
        const hasFinite = rec && rec.st === 'f' && Array.isArray(rec.xy);
        const pts = [A, B, C];
        const span = Math.max(...tMeta.sides);
        if (hasFinite && Math.hypot(rec.xy[0] - (A[0] + B[0] + C[0]) / 3, rec.xy[1] - (A[1] + B[1] + C[1]) / 3) < span * 2.5) {
          pts.push(rec.xy);
        }

        const xs = pts.map((p) => p[0]);
        const ys = pts.map((p) => p[1]);
        const minX = Math.min(...xs), maxX = Math.max(...xs);
        const minY = Math.min(...ys), maxY = Math.max(...ys);
        const sc = Math.min((pw - 76) / Math.max(maxX - minX, 0.4), (ph - 122) / Math.max(maxY - minY, 0.4));
        const mx = (minX + maxX) / 2, my = (minY + maxY) / 2;
        const toP = (p) => [ox + pw / 2 + (p[0] - mx) * sc, oy + ph / 2 + 12 - (p[1] - my) * sc];
        const sA = toP(A), sB = toP(B), sC = toP(C);

        let rightMark = '';
        if (tMeta.is_right) {
          rightMark = `<path d="${rightAnglePath(sA[0], sA[1], sB[0], sB[1], sC[0], sC[1], 10)}" fill="none" stroke="#94a3b8" stroke-width="1.5" />`;
        }
        let targetEl = '';
        let footStr = rec?.sn || 'Unresolved';
        if (hasFinite) {
          const sP = toP(rec.xy);
          targetEl = `<circle class="etc-plate-pt target selected" data-id="${spec.panel}" cx="${sP[0].toFixed(1)}" cy="${sP[1].toFixed(1)}" r="6" />` +
            `<text x="${(sP[0] + 9).toFixed(1)}" y="${(sP[1] - 8).toFixed(1)}" fill="#ffd54f" font-family="JetBrains Mono, monospace" font-size="13" font-weight="700">X<tspan dy="3" font-size="9">${n}</tspan></text>`;
          footStr = `(${rec.xy[0].toFixed(4)}, ${rec.xy[1].toFixed(4)})`;
        } else if (rec?.st === 'i') {
          footStr = '∞ (line at infinity)';
        } else if (rec?.st === '0') {
          footStr = 'indeterminate (0 : 0 : 0)';
        }

        panels.push(`
          <g class="etc-plate-panel" data-id="${spec.panel}">
            <rect class="etc-panel-border" x="${ox}" y="${oy}" width="${pw}" height="${ph}" rx="8" fill="#18181c" stroke="${spec.color}" stroke-opacity="0.45" stroke-width="1.5" />
            <text x="${ox + 14}" y="${oy + 24}" fill="${spec.color}" font-family="Fira Sans Condensed, sans-serif" font-size="15" font-weight="700">${esc(spec.title)}</text>
            <text x="${ox + pw - 14}" y="${oy + 24}" text-anchor="end" fill="#94a3b8" font-family="JetBrains Mono, monospace" font-size="11.5">${rec?.p === 'e' ? 'EXACT' : rec?.p === 'm' ? '50-DIG' : '—'}</text>
            <polygon points="${sA[0].toFixed(1)},${sA[1].toFixed(1)} ${sB[0].toFixed(1)},${sB[1].toFixed(1)} ${sC[0].toFixed(1)},${sC[1].toFixed(1)}" fill="${spec.color}" fill-opacity="0.08" stroke="${spec.color}" stroke-width="2.1" stroke-linejoin="round" />
            ${rightMark}
            <circle cx="${sA[0].toFixed(1)}" cy="${sA[1].toFixed(1)}" r="3.5" fill="#4ade80" />
            <circle cx="${sB[0].toFixed(1)}" cy="${sB[1].toFixed(1)}" r="3.5" fill="#4ade80" />
            <circle cx="${sC[0].toFixed(1)}" cy="${sC[1].toFixed(1)}" r="3.5" fill="#4ade80" />
            ${targetEl}
            <text x="${ox + pw / 2}" y="${oy + ph - 14}" text-anchor="middle" fill="#cbd5e1" font-family="JetBrains Mono, monospace" font-size="11.5">${esc(footStr)}</text>
          </g>
        `);
        meta[spec.panel] = {
          ID: spec.title,
          name: `X_${n} on ${spec.title}`,
          type: rec?.p === 'e' ? 'exact triangle panel' : '50-digit panel',
          color: spec.color,
          symbolic_rows: [
            ...(rec?.bl ? [{ label: 'Barycentric', latex: rec.bl, pretty: rec.bl }] : []),
            ...(rec?.xyl ? [{ label: 'Cartesian', latex: rec.xyl, pretty: rec.xyl }] : []),
          ],
        };
      });

      return `<svg class="geometor-etc-drawing" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 760" data-initial-viewbox="0 0 1200 760" preserveAspectRatio="xMidYMid meet">
        <rect width="1200" height="760" fill="#141416" />
        <text x="26" y="40" fill="#e8b85a" font-family="EB Garamond, Georgia, serif" font-size="24" font-weight="700">X<tspan dy="5" font-size="16">${n}</tspan><tspan dy="-5"> — Six Canonical Reference Triangles</tspan></text>
        ${panels.join('')}
        <script type="application/json" class="etc-elements-meta">${JSON.stringify(meta).replace(/</g, '\\u003c')}</script>
      </svg>`;
    }

    // =========================================================================
    // 5-Track Tabular Prose Pane Renderer (Mirrors tracks.py CSS classes!)
    // =========================================================================

    renderProse(center, track) {
      if (track === 'lines') {
        this.proseEl.innerHTML = this.renderLinesTrack(center);
      } else if (track === 'relations') {
        this.proseEl.innerHTML = this.renderRelationsTrack(center);
      } else if (track === 'notes') {
        this.proseEl.innerHTML = this.renderNotesTrack(center);
      } else if (track === 'code') {
        this.proseEl.innerHTML = this.renderCodeTrack(center);
      } else {
        this.proseEl.innerHTML = this.renderOverviewTrack(center);
      }
    }

    renderConstructionSectionHtml(center, triKey) {
      const n = center.n;
      const plan = this.computeConstructionPlan(center, triKey || this.currentTriKey || 'heronian');
      if (!plan || !plan.steps || plan.steps.length === 0) return '';

      const formatElLabel = (lbl) =>
        esc(lbl).replace(/([A-Za-z])_([A-Za-z0-9]+)/g, '$1<sub>$2</sub>');

      const rows = plan.steps
        .map(
          (st) => `<tr style="--etc-el-color:${esc(st.color)}">
            <td><p><span class="geom-ref" data-ref="${esc(st.id)}">${formatElLabel(st.label)}</span></p></td>
            <td><p>${esc(st.role)}</p></td>
            <td><p>${formatXLinks(st.desc, n)}</p></td>
          </tr>`
        )
        .join('');

      const summaryHtml = plan.summary
        ? `<p class="etc-construction-summary">${formatXLinks(plan.summary, n)}</p>`
        : '';

      return `
        <h2>Geometric Construction <span style="font-size:0.74em;font-weight:500;color:#9c958a;">(${esc(plan.triLabel)})</span></h2>
        ${summaryHtml}
        <table class="docutils align-default etc-table etc-construction-table">
          <thead><tr><th>Element</th><th>Role</th><th>Definition &amp; Invariants</th></tr></thead>
          <tbody>${rows}</tbody>
        </table>
      `;
    }

    refreshConstructionSection(center, triKey) {
      const sec = this.proseEl?.querySelector('.etc-live-construction-section');
      if (sec) {
        sec.innerHTML = this.renderConstructionSectionHtml(center, triKey);
      }
    }

    renderCoordTable(title, entries, symSpecs, n) {
      if (!entries || entries.length === 0) return '';
      const prim = extractCoordTriple(entries[0]);
      if (!prim) return '';
      const alts = entries.slice(1, 5).map(extractCoordTriple).filter(Boolean);
      const hasAlts = alts.length > 0;

      const rowsHtml = symSpecs
        .map(([sym, ref], idx) => {
          const pCell = prim.isMath ? texSpan(prim.c[idx]) : formatXLinks(prim.c[idx], n);
          let altCell = '';
          if (hasAlts) {
            const altLines = alts
              .map((a) => (a.isMath ? `<p>${texSpan(a.c[idx])}</p>` : `<p>${formatXLinks(a.c[idx], n)}</p>`))
              .join('');
            altCell = `<td>${altLines}</td>`;
          }
          return `<tr>
            <td><p><span class="geom-ref" data-ref="${esc(ref)}">${sym}</span></p></td>
            <td><p>${pCell}</p></td>
            ${altCell}
          </tr>`;
        })
        .join('');

      const noteHtml = prim.note ? `<div class="etc-coord-notes"><p>${formatXLinks(prim.note, n)}</p></div>` : '';
      return `
        <table class="docutils align-default etc-table etc-mode-coordinates etc-coord-table">
          <thead><tr><th>${esc(title)}</th><th>Primary</th>${hasAlts ? '<th>Alternates</th>' : ''}</tr></thead>
          <tbody>${rowsHtml}</tbody>
        </table>
        ${noteHtml}
      `;
    }

    renderOverviewTrack(center) {
      const n = center.n;
      let html = `<div class="etc-live-construction-section">${this.renderConstructionSectionHtml(center, this.currentTriKey)}</div>`;
      html += '<h2>Homogeneous Coordinates</h2>';
      html += this.renderCoordTable(
        'Trilinears',
        center.tr,
        [
          ['α', `[ X_${n} T_a /`],
          ['β', `[ X_${n} T_b /`],
          ['γ', `[ X_${n} T_c /`],
        ],
        n
      );
      html += this.renderCoordTable(
        'Barycentrics',
        center.ba,
        [
          ['u', `< X_${n} B C >`],
          ['v', `< X_${n} C A >`],
          ['w', `< X_${n} A B >`],
        ],
        n
      );
      html += this.renderCoordTable(
        'Tripolars',
        center.tp,
        [
          ['PA', `[ X_${n} A /`],
          ['PB', `[ X_${n} B /`],
          ['PC', `[ X_${n} C /`],
        ],
        n
      );

      // 7-Triangle Symbolic Invariants Table (cols 4 & 5 align with Coral/Sky/Emerald CSS rules)
      const splitTriplePs = (ltx) => {
        if (!ltx) return '<p>—</p>';
        const parts = splitTopColons(ltx);
        if (parts.length === 3) {
          return parts.map((p) => `<p>${texSpan(p)}</p>`).join('');
        }
        return `<p>${texSpan(ltx)}</p>`;
      };
      const triRows = TRI_ORDER.map((spec) => {
        const rec = center.tris?.[spec.key];
        const refSpan =
          spec.key === 'equilateral'
            ? `<strong>${esc(spec.title)}</strong>`
            : `<span class="geom-ref" data-ref="${spec.panel}"><strong>${esc(spec.title)}</strong></span>`;
        if (!rec) {
          return `<tr><td><p>${refSpan}</p></td><td><p>—</p></td><td><p>Unresolved</p></td><td><p>—</p></td><td><p>—</p></td></tr>`;
        }
        const fStr = rec.f || this.manifest?.triangles?.[spec.key]?.field || '';
        const fldCell = texSpan(fStr);
        const xyCell = rec.xyl ? texSpan(rec.xyl) : '—';
        return `<tr>
          <td><p>${refSpan}</p></td>
          <td><p>${fldCell}</p></td>
          <td><p>${xyCell}</p></td>
          <td>${splitTriplePs(rec.bl)}</td>
          <td>${splitTriplePs(rec.tl)}</td>
        </tr>`;
      }).join('');

      html += `
        <h2>Canonical Reference Triangles</h2>
        <table class="docutils align-default etc-table etc-mode-four-triangles">
          <thead><tr><th>Triangle</th><th>Field</th><th>Cartesian (x, y)</th><th>Barycentric (u, v, w)</th><th>Trilinear (α, β, γ)</th></tr></thead>
          <tbody>${triRows}</tbody>
        </table>
      `;

      if (center.co && center.co.length > 0) {
        const lis = center.co.map((c) => `<li>${formatXLinks(c, n)}</li>`).join('');
        html += `<h2>Linear Combinations</h2><ul>${lis}</ul>`;
      }
      return html;
    }

    renderLinesTrack(center) {
      const n = center.n;
      const lines = center.li || [];
      if (lines.length === 0) {
        return `<h2>Principal Central Lines</h2><p>No incident central lines cataloged for X<sub>${n}</sub>.</p>`;
      }

      const rows = lines
        .slice(0, 24)
        .map(([iN, jN], idx) => {
          const lid = `{ ${iN}, ${jN} }`;
          const col = idx < 14 ? LINE_PALETTE[idx % LINE_PALETTE.length] : '#94a3b8';
          return `<tr class="etc-line-colored" style="--etc-line-color:${col}">
            <td><p><strong>{${iN}, ${jN}}</strong></p></td>
            <td><p><span class="geom-ref" data-ref="${lid}">X<sub>${iN}</sub>X<sub>${jN}</sub></span></p></td>
            <td><p><a class="etc-live-xref" href="#X_${iN}" data-jump-x="${iN}">X<sub>${iN}</sub></a> (${esc(this.getPartnerTitle(iN))}) · <a class="etc-live-xref" href="#X_${jN}" data-jump-x="${jN}">X<sub>${jN}</sub></a> (${esc(this.getPartnerTitle(jN))})</p></td>
          </tr>`;
        })
        .join('');

      const totalNote = center.lt ? ` (showing first ${lines.length} of ${center.lt} lines)` : ` (${lines.length} lines)`;
      const chips = lines
        .map(
          ([iN, jN]) =>
            `{<a class="etc-live-xref" href="#X_${iN}" data-jump-x="${iN}">${iN}</a>, <a class="etc-live-xref" href="#X_${jN}" data-jump-x="${jN}">${jN}</a>}`
        )
        .join(', ');

      return `
        <h2>Principal Central Lines${totalNote}</h2>
        <table class="docutils align-default etc-table etc-mode-lines">
          <thead><tr><th>Line</th><th>Ref</th><th>Collinear Partner Centers</th></tr></thead>
          <tbody>${rows}</tbody>
        </table>
        <h3>Incident Line Catalog</h3>
        <p class="etc-line-catalog">${chips}</p>
      `;
    }

    renderRelationsTrack(center) {
      const n = center.n;
      const rels = center.re || [];
      if (rels.length === 0) {
        return `<h2>Functional Relations</h2><p>No explicit functional relations cataloged for X<sub>${n}</sub>.</p>`;
      }
      const rows = rels
        .map((r) => `<tr><td><p>${formatXLinks(r, n)}</p></td></tr>`)
        .join('');
      return `
        <h2>Functional Relations (${center.rt || rels.length})</h2>
        <table class="docutils align-default etc-table etc-mode-relations">
          <thead><tr><th>Relation</th></tr></thead>
          <tbody>${rows}</tbody>
        </table>
      `;
    }

    renderNotesTrack(center) {
      const n = center.n;
      let html = `<h2>Scholarly Notes &amp; Provenance</h2>`;
      const { families, collection } = this.findFamiliesForCenter(n);
      if (families.length > 0) {
        const pf = families[0];
        const bodyPs = (pf.p || []).length > 0
          ? pf.p.map((para) => `<p>${formatXLinks(para, n)}</p>`).join('')
          : `<p>Part ${pf.part} family group spanning X<sub>${pf.start}</sub>–X<sub>${pf.end}</sub>.</p>`;
        html += `<div class="etc-family-preamble-box">
          <h3>Family Preamble: <a class="etc-live-xref" href="#family/${esc(pf.id)}" data-jump-family="${esc(pf.id)}">${esc(pf.title)} (X<sub>${pf.start}</sub>–X<sub>${pf.end}</sub>) ↗</a></h3>
          ${bodyPs}
        </div>`;
      } else if (collection) {
        html += `<div class="etc-family-preamble-box">
          <h3>Collection: <a class="etc-live-xref" href="#family/${esc(collection.slug)}" data-jump-family="${esc(collection.slug)}">${esc(collection.title)} (X<sub>${collection.start}</sub>–X<sub>${collection.end}</sub>) ↗</a></h3>
          <p>${formatXLinks(collection.summary || '', n)}</p>
        </div>`;
      }
      if (center.al && center.al.length > 0) {
        html += `<p><strong>Aliases:</strong> ${center.al.map((a) => esc(a)).join(' · ')}</p>`;
      }
      const notes = center.no || [];
      if (notes.length === 0) {
        html += `<p>No additional narrative notes in ETC source entry for X<sub>${n}</sub>.</p>`;
      } else {
        html += notes.map((p) => `<p>${formatXLinks(p, n)}</p>`).join('');
      }
      return html;
    }

    renderCodeTrack(center) {
      const n = center.n;
      const pad5 = String(n).padStart(5, '0');
      let classicalBlock = '';
      if (n >= 1 && n <= 19) {
        const clsCode = `"""Exact symbolic compass-and-straightedge Model for X_${n} (${center.t || ''})."""
from geometor.etc.models.x_${pad5} import build_model

# Construct full exact SymPy Model (zero floats) on any canonical triangle:
# "heronian", "right", "kepler", "kimberling", "golden", "gnomon", "equilateral"
model = build_model("heronian")
for el, info in model.items():
    if info.ID == "X_${n}":
        print(f"X_${n} exact SymPy Point = {el}")
`;
        classicalBlock = `
          <h2>Exact Symbolic Euclidean Construction (<code>geometor.model</code>)</h2>
          <p>Build the full ruler-and-compass symbolic dependency DAG for <strong>X<sub>${n}</sub></strong> using <code>geometor.etc.models.x_${pad5}</code>:</p>
          <pre class="literal-block"><code>${esc(clsCode)}</code></pre>
        `;
      }
      const code = `"""Exact algebraic evaluation of X_${n} across all 7 canonical triangles."""
from pathlib import Path
from geometor.etc.parser import parse_center
from geometor.etc.field_eval import ExactCorpusResolver, _CANONICAL_TRIANGLE_ORDER

# Evaluate X_${n} (${center.t || ''}) in exact algebraic number fields
html = Path("resources/split/x-${pad5}.html").read_text(encoding="utf-8")
cdata = parse_center(html)

for tri_key in _CANONICAL_TRIANGLE_ORDER:
    resolver = ExactCorpusResolver({${n}: cdata}, tri_key)
    res = resolver.resolve_all().get(${n})
    if res:
        print(f"{tri_key:11s} [{res.precision}] bary = {res.bary_latex} | xy = {res.xy_latex}")
`;
      return `
        ${classicalBlock}
        <h2>Exact Symbolic Field Evaluator API</h2>
        <p>Evaluate <strong>X<sub>${n}</sub></strong> directly in exact algebraic number fields (zero floating-point drift) across all 7 canonical reference triangles:</p>
        <pre class="literal-block"><code>${esc(code)}</code></pre>
      `;
    }

    ensureMathJax() {
      if (window.MathJax && typeof window.MathJax.typesetPromise === 'function') {
        return Promise.resolve();
      }
      if (this._mjLoading) return this._mjLoading;

      const existingScript = document.querySelector('script[src*="mathjax"]');
      if (existingScript) {
        this._mjLoading = new Promise((resolve) => {
          let tries = 0;
          const poll = () => {
            if (window.MathJax && typeof window.MathJax.typesetPromise === 'function') {
              resolve();
              return;
            }
            if (++tries > 200) {
              resolve();
              return;
            }
            window.setTimeout(poll, 50);
          };
          existingScript.addEventListener('load', poll, { once: true });
          existingScript.addEventListener('error', () => resolve(), { once: true });
          poll();
        });
        return this._mjLoading;
      }

      this._mjLoading = new Promise((resolve) => {
        window.MathJax = {
          options: {
            ignoreHtmlClass: 'etc-lazy-math|no-mathjax',
            processHtmlClass: 'math|arithmatex',
            enableComplexity: true,
            makeCollapsible: true,
          },
          output: { displayOverflow: 'linebreak', linebreaks: { inline: true } },
          startup: {
            pageReady: () =>
              window.MathJax.startup.defaultPageReady().then(() => resolve()),
          },
        };
        const sc = document.createElement('script');
        sc.defer = true;
        sc.src = 'https://cdn.jsdelivr.net/npm/mathjax@4/tex-mml-chtml.js';
        sc.onerror = () => resolve();
        document.head.appendChild(sc);
      });
      return this._mjLoading;
    }

    typesetMath(container) {
      if (!container) return;
      const run = () => {
        if (window.MathJax && typeof window.MathJax.typesetPromise === 'function') {
          if (typeof window.MathJax.typesetClear === 'function') {
            try {
              window.MathJax.typesetClear([container]);
            } catch (e) {}
          }
          window.MathJax.typesetPromise([container]).catch(() => {});
        }
      };
      this.ensureMathJax().then(() => {
        if (window.MathJax?.startup?.promise) {
          window.MathJax.startup.promise.then(run).catch(() => {});
        } else {
          run();
        }
      });
    }
  }

  function bootLiveExplorer() {
    const el = document.getElementById('etc-live-app');
    if (!el || el.dataset.etcLiveBooted === '1') return;
    el.dataset.etcLiveBooted = '1';
    window.ETCLiveExplorer = new EtcLiveExplorer(el);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', bootLiveExplorer);
  } else {
    bootLiveExplorer();
  }
})(window, document);
