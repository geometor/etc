:navigation: header
:order: 20
:nav_title: About

.. _about:
.. _about-index:

About
=====

.. rubric:: Extracting Historical Semantic Knowledge & Repurposing It for Exact Symbolic Reasoning

About This Edition
------------------

``geometor.etc`` is a digital reconstruction, semantic index, and symbolic modeling framework for Clark Kimberling's monumental `Encyclopedia of Triangle Centers (ETC) <https://faculty.evansville.edu/ck6/encyclopedia/ETC.html>`_ at the University of Evansville. Spanning more than 53,000 distinct triangle centers—from antiquity's incenter :ref:`X_1 <X_1>`, centroid :ref:`X_2 <X_2>`, circumcenter :ref:`X_3 <X_3>`, and orthocenter :ref:`X_4 <X_4>` to modern central discoveries—this edition ingests archival HTML volumes and transforms unstructured mathematical prose into structured Python objects, computable dependency chains, and exact symbolic coordinates.

Every center entry is systematized into a synchronized two-track **Book Codex**: an *Overview* track equipped with formal ``.. enunciation::`` directives, ``.. signature:: center`` definitions for functional trilinear (:math:`\alpha : \beta : \gamma`) and barycentric (:math:`u : v : w`) coordinates, comprehensive cross-references to Kimberling's thematic preambles, and calibrated multi-triangle vector diagrams rendered across Acute, Right, Kepler, and Kimberling reference geometries; and a *Code* track providing standalone ``model.py`` geometric construction scripts ready for execution and algebraic inspection.

By parsing historical definitions, collineations, central lines, central triangles, and geometric transformations into explicit semantic links, ``geometor.etc`` bridges centuries of synthetic and analytic triangle geometry with modern symbolic computation. It connects directly with sister GEOMETOR repositories—including ``geometor.model`` for algebraic construction verification, ``geometor.explorer`` for dynamic SVG laboratories, and historical codices such as ``geometor.elements`` and ``geometor.pappus``—establishing a computable foundation for classical and contemporary geometry.

The GEOMETOR Mission
--------------------

The **GEOMETOR** initiative, conceived and directed by **phi ARCHITECT**, is dedicated to the systematic recovery, symbolic formalization, and creative re-articulation of humanity's geometric heritage. GEOMETOR unites classical synthesis with modern algebraic rigor across three core pillars:

Extracting Historical Semantic Knowledge
    Moving beyond passive page scans, static facsimile bitmaps, and flat optical character recognition (OCR), GEOMETOR recovers the living deductive architecture of 2,300+ years of geometric, axiomatic, and philosophical treatises. Primary sources—spanning Euclid, Apollonius, Archimedes, Pappus, Johannes Kepler, Felix Klein, and Clark Kimberling—are analyzed to elevate enunciations, deductive steps, synthetic justifications, marginal citations, primary-source folios (via ``publish folio``), and calibrated Ink-to-Vector ``.euclid-graphic`` diagrams into structured, machine-addressable semantic graphs.

Exact Symbolic Grounding (``geometor.model``)
    Geometric constructions must not depend on floating-point approximations or visual artifacts. GEOMETOR anchors geometric entities in 100% exact symbolic algebra via `SymPy <https://www.sympy.org/>`_ and the principles of Rational Trigonometry (quadrance, spread, cross-ratio). Points, lines, circles, and conic loci are evaluated over exact algebraic fields, ensuring that tangencies, incidences, harmonic conjugates, and collinearities represent absolute mathematical truths rather than numerical estimates.

Repurposing Knowledge Across Mediums
    Extracted semantic architectures and exact symbolic models are re-deployed across a unified digital ecosystem: synchronized multi-track **Book Codices** and EPUB 3 editions powered by ``photon-platform/publish``, computable deductive canons (``geometor.elements``, ``geometor.etc``, ``geometor.pappus``, ``geometor.divine``), interactive SVG exploration laboratories (``geometor.explorer``), ultra-high-definition visual broadcasts, and neuro-symbolic program synthesis (``geometor.seer``) across `geometor.com <https://geometor.com>`_.

Sources, Provenance & Methodology
---------------------------------

* **Primary Corpus**: Clark Kimberling, *Encyclopedia of Triangle Centers* (ETC), University of Evansville (established 1994, continuously expanded to 53,144+ centers).
* **Glossary & Preambles**: Kimberling's *Glossary of Terms in ETC* and catalog of 925 inter-center preambles across Parts 1–37.
* **Biographical Register**: Historical and contemporary attribution to over 150 classical and modern mathematicians curated in the :doc:`People Register </people/index>`.
* **Digital Scriptorium Methodology**: Developed and maintained by **phi ARCHITECT** using Sphinx, Python, ``geometor.model``, and ``photon-platform/publish``. Raw HTML sources are scraped, normalized, parsed into typed dataclasses, linked with the comprehensive glossary, and typeset into responsive web and codex formats.
