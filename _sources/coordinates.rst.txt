.. _coordinates:

Coordinates in Pictures
=======================

.. toctree::
   :hidden:

Every center :math:`X_n` in the *Encyclopedia of Triangle Centers* is specified by two homogeneous coordinate triples relative to a reference triangle :math:`ABC` with side lengths :math:`(a, b, c)`:

1. **Trilinear Coordinates** :math:`\alpha : \beta : \gamma` — the directed perpendicular distances from :math:`X_n` to sidelines :math:`BC, CA, AB`.
2. **Barycentric Coordinates** :math:`u : v : w` — the signed areas of the three sub-triangles :math:`\triangle X_n BC, \triangle X_n CA, \triangle X_n AB` (or equivalently, the center-of-mass weights placed at vertices :math:`A, B, C` so that their balance point is :math:`X_n`).

Because the area of each sub-triangle is :math:`\frac{1}{2} \times \text{base} \times \text{height}`, the two coordinate systems are connected by the fundamental **Bridge Identity**:

.. math::

   u : v : w \;=\; a\alpha : b\beta : c\gamma
   \qquad\Longleftrightarrow\qquad
   \alpha : \beta : \gamma \;=\; \frac{u}{a} : \frac{v}{b} : \frac{w}{c}

----

1. Trilinear Coordinates in Pictures (:math:`\alpha : \beta : \gamma`)
----------------------------------------------------------------------

Drop perpendiculars from a point :math:`P` to the three sidelines :math:`BC` (side :math:`a`), :math:`CA` (side :math:`b`), and :math:`AB` (side :math:`c`) at pedal feet :math:`P_a, P_b, P_c`.

* The **actual trilinear distances** :math:`(\alpha_{\text{act}}, \beta_{\text{act}}, \gamma_{\text{act}})` are the signed lengths of the three perpendicular struts :math:`PP_a, PP_b, PP_c` (positive when :math:`P` lies on the same side of the sideline as the opposite vertex).
* Since the three sub-triangles have areas :math:`\frac{1}{2}a\alpha_{\text{act}}`, :math:`\frac{1}{2}b\beta_{\text{act}}`, and :math:`\frac{1}{2}c\gamma_{\text{act}}`, the actual perpendicular distances always satisfy the linear constraint:

  .. math::

     a\alpha_{\text{act}} + b\beta_{\text{act}} + c\gamma_{\text{act}} \;=\; 2\Delta

  where :math:`\Delta = \operatorname{Area}(\triangle ABC)`.
* **Homogeneous Trilinear Coordinates** :math:`\alpha : \beta : \gamma` record only the *proportion* among these three perpendicular distances: for any non-zero scalar :math:`k \neq 0`, :math:`(k\alpha : k\beta : k\gamma)` represents the same point.
* **Canonical Example — Incenter** :ref:`X_1 <X_1>`: Because :ref:`X_1 <X_1>` is equidistant from all three sides by the inradius :math:`r = \Delta / s`, its three perpendicular struts have identical length :math:`(r, r, r)`, giving the simplest trilinear ratio:

  .. math::

     X_1 \text{ Trilinears:} \quad \alpha : \beta : \gamma \;=\; 1 : 1 : 1

.. raw:: html

   <div style="margin: 1.5rem 0; background: #0d111a; border: 1px solid rgba(232, 184, 90, 0.35); border-radius: 12px; padding: 12px;">
     <img src="_static/coordinates/trilinear_picture.svg" alt="Trilinear Coordinates in Pictures" style="width: 100%; height: auto; display: block;" />
   </div>

----

2. Barycentric Coordinates in Pictures (:math:`u : v : w`)
----------------------------------------------------------

Join :math:`P` to the three vertices :math:`A, B, C`, partitioning :math:`\triangle ABC` into three shaded sub-triangles opposite each vertex:

* :math:`u \propto \operatorname{Area}(\triangle PBC)` (the gold sub-triangle opposite vertex :math:`A`, with base :math:`a = BC` and height :math:`\alpha_{\text{act}}`).
* :math:`v \propto \operatorname{Area}(\triangle PCA)` (the cyan sub-triangle opposite vertex :math:`B`, with base :math:`b = CA` and height :math:`\beta_{\text{act}}`).
* :math:`w \propto \operatorname{Area}(\triangle PAB)` (the emerald sub-triangle opposite vertex :math:`C`, with base :math:`c = AB` and height :math:`\gamma_{\text{act}}`).

Equivalently, in Archimedes' and Möbius's statics interpretation, if point masses :math:`u, v, w` are placed at vertices :math:`A, B, C`, then :math:`P` is their **center of mass**:

.. math::

   P \;=\; \frac{uA + vB + wC}{u + v + w}

* **Canonical Example — Incenter** :ref:`X_1 <X_1>`: Since all three sub-triangles :math:`\triangle X_1 BC, \triangle X_1 CA, \triangle X_1 AB` share the same height :math:`r`, their areas are proportional to their bases :math:`a, b, c`:

  .. math::

     X_1 \text{ Barycentrics:} \quad u : v : w \;=\; a : b : c

  On the primary Heronian reference triangle :math:`(a, b, c) = (15, 13, 14)` (:math:`\Delta = 84`, :math:`r = 4`), :ref:`X_1 <X_1>` partitions the area into exact integer sub-areas :math:`(30, 26, 28)` in ratio :math:`15 : 13 : 14` (and :math:`5 : 6 : 7` on the acute picture triangle :math:`(5, 6, 7)` shown below).

.. raw:: html

   <div style="margin: 1.5rem 0; background: #0d111a; border: 1px solid rgba(56, 189, 248, 0.35); border-radius: 12px; padding: 12px;">
     <img src="_static/coordinates/barycentric_picture.svg" alt="Barycentric Coordinates in Pictures" style="width: 100%; height: auto; display: block;" />
   </div>

----

3. The Classic Coordinate Trio: :math:`X_1`, :math:`X_2`, and :math:`X_6`
-------------------------------------------------------------------------

Comparing the **Incenter** :ref:`X_1 <X_1>`, the **Centroid** :ref:`X_2 <X_2>`, and the **Symmedian Point** :ref:`X_6 <X_6>` side by side makes the duality between perpendicular distances (:math:`\alpha : \beta : \gamma`) and sub-triangle areas (:math:`u : v : w = a\alpha : b\beta : c\gamma`) immediately visible:

.. list-table::
   :header-rows: 1
   :widths: 22 26 26 26

   * - Center
     - Geometric Criterion
     - Trilinear Distances (:math:`\alpha : \beta : \gamma`)
     - Barycentric Sub-Areas (:math:`u : v : w`)
   * - :ref:`X_1 <X_1>` (**Incenter**)
     - Equal perpendicular distances (:math:`r`) to sidelines
     - :math:`1 : 1 : 1`
     - :math:`a : b : c` (:math:`15 : 13 : 14` on Heronian; :math:`5 : 6 : 7` below)
   * - :ref:`X_2 <X_2>` (**Centroid**)
     - Equal sub-triangle areas (:math:`\frac{1}{3}\Delta`)
     - :math:`\frac{1}{a} : \frac{1}{b} : \frac{1}{c}` (:math:`182 : 210 : 195` on Heronian; :math:`42 : 35 : 30` below)
     - :math:`1 : 1 : 1`
   * - :ref:`X_6 <X_6>` (**Symmedian Point**)
     - Distances proportional to side lengths
     - :math:`a : b : c` (:math:`15 : 13 : 14` on Heronian; :math:`5 : 6 : 7` below)
     - :math:`a^2 : b^2 : c^2` (:math:`225 : 169 : 196` on Heronian; :math:`25 : 36 : 49` below)

Notice how :ref:`X_2 <X_2>` and :ref:`X_6 <X_6>` are :term:`isogonal conjugates <isogonal conjugate>` (their trilinear coordinates are reciprocals :math:`1/a : 1/b : 1/c` and :math:`a : b : c`), while :ref:`X_1 <X_1>` is self-isogonal (:math:`1 : 1 : 1`).

.. raw:: html

   <div style="margin: 1.5rem 0; background: #0d111a; border: 1px solid rgba(94, 194, 126, 0.35); border-radius: 12px; padding: 12px;">
     <img src="_static/coordinates/coordinate_trio.svg" alt="Coordinate Trio: X_1, X_2, and X_6" style="width: 100%; height: auto; display: block;" />
   </div>

----

.. _canonical-triangles:

4. The Four Canonical Symbolic Reference Triangles
--------------------------------------------------

Every constructive model and center profile in GEOMETOR's *Encyclopedia of Triangle Centers* is evaluated in **100% exact symbolic arithmetic** across four canonical reference triangles spanning four algebraic number fields — with side :math:`c = AB` placed along the positive horizontal axis from :math:`A = (0, 0)` to :math:`B = (c, 0)`:

.. list-table::
   :header-rows: 1
   :widths: 16 10 14 22 14 24

   * - Preset
     - Field
     - Sides :math:`(a, b, c)`
     - Exact Vertices :math:`(A, B, C)`
     - :math:`\Delta,\; r,\; R`
     - Role in the Codex
   * - **Heronian** ``heronian``
     - :math:`\mathbb{Q}`
     - :math:`(15, 13, 14)`
     - :math:`A=(0,0),\; B=(14,0),\; C=(5,12)`
     - :math:`\Delta = 84`, :math:`r = 4`, :math:`R = \frac{65}{8}`
     - **Primary acute scalene plate** — integer vertices, integer area, integer inradius, and rational-coordinate centers (:math:`X_1 = (6, 4)`).
   * - **Right** ``right``
     - :math:`\mathbb{Q}`
     - :math:`(3, 4, 5)`
     - :math:`A=(0,0),\; B=(5,0),\; C=\left(\frac{16}{5}, \frac{12}{5}\right)`
     - :math:`\Delta = 6`, :math:`r = 1`, :math:`R = \frac{5}{2}`
     - **Pythagorean right boundary** (:math:`\angle C = 90^\circ`) — tests orthic/circumcenter collapses (:math:`X_4 = C`, :math:`X_3 = \text{mid}(AB)`).
   * - **Kepler** ``kepler``
     - :math:`\mathbb{Q}(\sqrt{\phi})`
     - :math:`(1, \sqrt{\phi}, \phi)`
     - :math:`A=(0,0),\; B=(\phi,0),\; C=\left(1, \frac{1}{\sqrt{\phi}}\right)`
     - :math:`\Delta = \frac{\sqrt{\phi}}{2}`, :math:`r = \frac{\sqrt{\phi} - \phi + 1}{2}`, :math:`R = \frac{\phi}{2}`
     - **Golden geometric-progression right triangle** (:math:`1 : \sqrt{\phi} : \phi`, :math:`\phi^2 = \phi + 1`) — bridges triangle geometry to the divine proportion.
   * - **Kimberling** ``kimberling``
     - :math:`\mathbb{Q}(\sqrt{35})`
     - :math:`(6, 9, 13)`
     - :math:`A=(0,0),\; B=(13,0),\; C=\left(\frac{107}{13}, \frac{8\sqrt{35}}{13}\right)`
     - :math:`\Delta = 4\sqrt{35}`, :math:`r = \frac{2\sqrt{35}}{7}`, :math:`R = \frac{351\sqrt{35}}{280}`
     - **Obtuse scalene ETC search standard** — exact directed distance :math:`h_a` from :math:`X_n` to sideline :math:`BC` reproduces Clark Kimberling's 12-decimal search key (:math:`h_a(X_1) = \frac{2\sqrt{35}}{7} \approx 1.690308509457`).

