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

  On the acute reference triangle :math:`(a, b, c) = (5, 6, 7)`, :ref:`X_1 <X_1>` partitions the area in the exact ratio :math:`5 : 6 : 7` (:math:`27.8\% : 33.3\% : 38.9\%`).

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
     - :math:`a : b : c` (:math:`5 : 6 : 7`)
   * - :ref:`X_2 <X_2>` (**Centroid**)
     - Equal sub-triangle areas (:math:`\frac{1}{3}\Delta`)
     - :math:`\frac{1}{a} : \frac{1}{b} : \frac{1}{c}` (:math:`42 : 35 : 30`)
     - :math:`1 : 1 : 1`
   * - :ref:`X_6 <X_6>` (**Symmedian Point**)
     - Distances proportional to side lengths
     - :math:`a : b : c` (:math:`5 : 6 : 7`)
     - :math:`a^2 : b^2 : c^2` (:math:`25 : 36 : 49`)

Notice how :ref:`X_2 <X_2>` and :ref:`X_6 <X_6>` are :term:`isogonal conjugates <isogonal conjugate>` (their trilinear coordinates are reciprocals :math:`1/a : 1/b : 1/c` and :math:`a : b : c`), while :ref:`X_1 <X_1>` is self-isogonal (:math:`1 : 1 : 1`).

.. raw:: html

   <div style="margin: 1.5rem 0; background: #0d111a; border: 1px solid rgba(94, 194, 126, 0.35); border-radius: 12px; padding: 12px;">
     <img src="_static/coordinates/coordinate_trio.svg" alt="Coordinate Trio: X_1, X_2, and X_6" style="width: 100%; height: auto; display: block;" />
   </div>
