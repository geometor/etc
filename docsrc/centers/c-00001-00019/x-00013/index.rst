:order: 13
:canonical_id: X_13
:subtitle: 1st ISOGONIC CENTER (FERMAT POINT, TORRICELLI POINT)
:tracks: Overview: index | Lines: lines | Relations: relations | Notes: notes | Code: code
:aliases: FERMAT POINT, TORRICELLI POINT
:dependencies: X_1, X_2, X_3, X_4, X_5, X_6, X_11, X_14, X_15, X_16, X_17, X_18, X_30, X_48, X_61, X_62, X_76, X_80, X_98, X_99, X_115, X_125, X_148, X_202, X_203, X_226, X_262, X_265, X_275, X_298, X_299, X_303, X_381, X_383, X_395, X_396, X_470, X_472, X_484, X_523, X_531, X_532, X_533, X_616, X_617, X_618, X_619, X_621, X_623, X_634, X_635, X_671, X_1080, X_1081, X_1116, X_1251, X_1277, X_1478, X_1637, X_1640, X_1989, X_2394, X_6104, X_8371, X_9200, X_9201, X_9202, X_14446, X_14447, X_30574, X_34317, X_42730, X_42731, X_42732, X_42733, X_42734, X_42735, X_42736, X_42737, X_42738, X_42740

.. _X_13:
.. _FirstIsogonicCenter:
.. _fermat_point:

X_13
====

.. rubric:: 1st ISOGONIC CENTER (FERMAT POINT, TORRICELLI POINT)

.. container:: etc-identity-bar

   ``fermat_point(A, B, C) -> X_13`` • **Fermat • Torricelli (c. 1640)** • **Kimberling** ``X(13)`` • **Search** :math:`(6,9,13)`: :math:`- \frac{153287 \sqrt{3}}{123561} + \frac{15488 \sqrt{35}}{41187} \approx 0.075945151805`

.. enunciation::

   Construct the equilateral triangle :g:`BA'C << B C A' >>` having base :g:`BC <[ B C ]>` and vertex :g:`A' <A'>` on the negative side of :g:`BC <[ B C ]>`; similarly construct equilateral triangles :g:`CB'A << C A B' >>` and :g:`AC'B << A B C' >>` based on the other two sides. The lines :g:`AA' <[ A A' ]>`, :g:`BB' <[ B B' ]>`, :g:`CC' <[ C C' ]>` concur in :ref:`X_13 <X_13>`. If each of the angles :g:`A <A>`, :g:`B <B>`, :g:`C <C>` is < 2π/3, then :ref:`X_13 <X_13>` is the only center X for which the angles ``BXC``, ``CXA``, ``AXB`` are equal, and :ref:`X_13 <X_13>` minimizes the sum \|\ ``AX``\ \| + \|\ ``BX``\ \| + \|\ ``CX``\ \|. The :term:`antipedal triangle <antipedal-triangle>` of :ref:`X_13 <X_13>` is equilateral.

.. figure:: x-00013.svg
   :alt: X_13 — 1st ISOGONIC CENTER (FERMAT POINT, TORRICELLI POINT)
   :align: center

   **X_13** (*1st ISOGONIC CENTER (FERMAT POINT, TORRICELLI POINT)*) constructed at :g:`X_13 <X_13>` = :math:`\left(\frac{13727}{2353} - \frac{224 \sqrt{3}}{2353},\; \frac{18816}{2353} - \frac{5523 \sqrt{3}}{2353}\right)` in exact algebraic coordinates on Heronian :math:`(15, 13, 14)` over :math:`\mathbb{Q}(\sqrt{3})` with vertices :g:`A <A>` = :math:`(0, 0)`, :g:`B <B>` = :math:`(14, 0)`, :g:`C <C>` = :math:`(5, 12)`, area :math:`\Delta = 84`. Switch view modes or reference triangles above.

Homogeneous Coordinates
-----------------------

.. list-table::
   :header-rows: 1
   :class: etc-table etc-coord-table etc-mode-coordinates
   :widths: 18 41 41

   * - Trilinears
     - Canonical
     - Alternates
   * - :g:`α </ X_13 T_a />`
     - :math:`\csc(A + \pi /3)`
     - :math:`\sec(A - \pi /6)`
   * - :g:`β </ X_13 T_b />`
     - :math:`\csc(B + \pi /3)`
     - :math:`\sec(B - \pi /6)`
   * - :g:`γ </ X_13 T_c />`
     - :math:`\csc(C + \pi /3)`
     - :math:`\sec(C - \pi /6)`

.. list-table::
   :header-rows: 1
   :class: etc-table etc-coord-table etc-mode-coordinates
   :widths: 18 41 41

   * - Barycentrics
     - Canonical
     - Alternates
   * - :g:`u << X_13 B C >>`
     - :math:`a^{4} - 2(b^{2} - c^{2})^{2} + a^{2}(b^{2} + c^{2} + 4 \sqrt{3} \operatorname{area}(ABC))`
     - :math:`(S_{A} + \sqrt{3} S) (S_{B} + S_{C}) + 4 S_{B} S_{C}`
   * - :g:`v << X_13 C A >>`
     - :math:`b^{4} - 2(c^{2} - a^{2})^{2} + b^{2}(c^{2} + a^{2} + 4 \sqrt{3} \operatorname{area}(ABC))`
     - :math:`(S_{B} + \sqrt{3} S) (S_{C} + S_{A}) + 4 S_{C} S_{A}`
   * - :g:`w << X_13 A B >>`
     - :math:`c^{4} - 2(a^{2} - b^{2})^{2} + c^{2}(a^{2} + b^{2} + 4 \sqrt{3} \operatorname{area}(ABC))`
     - :math:`(S_{C} + \sqrt{3} S) (S_{A} + S_{B}) + 4 S_{A} S_{B}`

.. list-table::
   :header-rows: 1
   :class: etc-table etc-coord-table etc-mode-coordinates
   :widths: 18 41 41

   * - Tripolars
     - Canonical
     - Alternates
   * - :g:`PA </ X_13 A />`
     - :math:`1/(a^{4}+a^{2} b^{2}-2 b^{4}+a^{2} c^{2}+4 b^{2} c^{2}-2 c^{4}+2 \sqrt{3} a^{2} S)`
     - —
   * - :g:`PB </ X_13 B />`
     - :math:`1/(b^{4}+b^{2} c^{2}-2 c^{4}+b^{2} a^{2}+4 c^{2} a^{2}-2 a^{4}+2 \sqrt{3} b^{2} S)`
     - —
   * - :g:`PC </ X_13 C />`
     - :math:`1/(c^{4}+c^{2} a^{2}-2 a^{4}+c^{2} b^{2}+4 a^{2} b^{2}-2 b^{4}+2 \sqrt{3} c^{2} S)`
     - —

.. list-table:: Canonical Triangle Symbolic Invariants
   :header-rows: 1
   :class: etc-table etc-mode-four-triangles

   * - Triangle
     - Field
     - Cartesian
     - Trilinears
     - Barycentrics
     - Sub-Areas
     - Directed Trilinear :math:`(d_a,\, Q_a)`
   * - :g:`Heronian (15, 13, 14) <panel-heronian>`
     - :math:`\mathbb{Q}(\sqrt{3})`
     - :math:`x = \frac{13727}{2353} - \frac{224 \sqrt{3}}{2353}`

       :math:`y = \frac{18816}{2353} - \frac{5523 \sqrt{3}}{2353}`
     - :math:`\alpha = 3900 \sqrt{3} + 6773`

       :math:`\beta = 5835 + 3380 \sqrt{3}`

       :math:`\gamma = 6045 + 3640 \sqrt{3}`
     - :math:`u = 900 \sqrt{3} + 1563`

       :math:`v = 1167 + 676 \sqrt{3}`

       :math:`w = 1302 + 784 \sqrt{3}`
     - :math:`\Delta_a = \frac{30618}{2353} + \frac{52395 \sqrt{3}}{4706}`

       :math:`\Delta_b = \frac{24927 \sqrt{3}}{4706} + \frac{35322}{2353}`

       :math:`\Delta_c = \frac{131712}{2353} - \frac{38661 \sqrt{3}}{2353}`
     - :math:`d_a = \frac{20412}{11765} + \frac{3493 \sqrt{3}}{2353}`

       :math:`Q_a = \frac{142598232 \sqrt{3}}{27683045} + \frac{1331728419}{138415225}`
   * - :g:`Right (3, 4, 5) <panel-right>`
     - :math:`\mathbb{Q}(\sqrt{3})`
     - :math:`x = \frac{162}{193} - \frac{16 \sqrt{3}}{193}`

       :math:`y = \frac{384}{193} - \frac{138 \sqrt{3}}{193}`
     - :math:`\alpha = 25 \sqrt{3} + 48`

       :math:`\beta = 20 + 15 \sqrt{3}`

       :math:`\gamma = 15 + 20 \sqrt{3}`
     - :math:`u = 25 \sqrt{3} + 48`

       :math:`v = 12 + 9 \sqrt{3}`

       :math:`w = 12 + 16 \sqrt{3}`
     - :math:`\Delta_a = \frac{147}{193} + \frac{300 \sqrt{3}}{193}`

       :math:`\Delta_b = \frac{243}{193} - \frac{24 \sqrt{3}}{193}`

       :math:`\Delta_c = \frac{768}{193} - \frac{276 \sqrt{3}}{193}`
     - :math:`d_a = \frac{294}{965} + \frac{120 \sqrt{3}}{193}`

       :math:`Q_a = \frac{14112 \sqrt{3}}{37249} + \frac{1166436}{931225}`
   * - :g:`Kepler (1, √φ, φ) <panel-kepler>`
     - :math:`\mathbb{Q}(\sqrt{\phi}, \sqrt{3})`
     - :math:`x = \sqrt{3} \left(\frac{1}{24} - \frac{\sqrt{5}}{24}\right) + \frac{\sqrt{2} \sqrt{1 + \sqrt{5}}}{8}`

       :math:`y = - \frac{\sqrt{30} \sqrt{1 + \sqrt{5}}}{24} + \frac{\sqrt{5}}{8} + \frac{3}{8}`
     - :math:`\alpha = \frac{\sqrt{3} \left(\sqrt{2} \sqrt{1 + \sqrt{5}} + \sqrt{10} \sqrt{1 + \sqrt{5}}\right)}{4} + 4`

       :math:`\beta = \phi + \frac{\sqrt{6} \sqrt{1 + \sqrt{5}}}{2}`

       :math:`\gamma = \sqrt{3} \phi + \frac{\sqrt{2} \sqrt{1 + \sqrt{5}}}{2}`
     - :math:`u = 2 + 2 \sqrt{5} + \frac{\sqrt{3} \left(\sqrt{10} \sqrt{1 + \sqrt{5}} + 3 \sqrt{2} \sqrt{1 + \sqrt{5}}\right)}{4}`

       :math:`v = \phi + \frac{\sqrt{6} \sqrt{1 + \sqrt{5}}}{2}`

       :math:`w = \phi + \frac{\sqrt{3} \left(\sqrt{2} \sqrt{1 + \sqrt{5}} + \sqrt{10} \sqrt{1 + \sqrt{5}}\right)}{4}`
     - :math:`\Delta_a = - \frac{\sqrt{10} \sqrt{1 + \sqrt{5}}}{32} + \frac{3 \sqrt{2} \sqrt{1 + \sqrt{5}}}{32} + \sqrt{3} \left(\frac{1}{12} + \frac{\sqrt{5}}{24}\right)`

       :math:`\Delta_b = \sqrt{3} \left(\frac{1}{48} - \frac{\sqrt{5}}{48}\right) + \frac{\sqrt{2} \sqrt{1 + \sqrt{5}}}{16}`

       :math:`\Delta_c = \sqrt{3} \left(- \frac{5}{48} - \frac{\sqrt{5}}{48}\right) + \frac{\sqrt{10} \sqrt{1 + \sqrt{5}}}{32} + \frac{3 \sqrt{2} \sqrt{1 + \sqrt{5}}}{32}`
     - :math:`d_a = - \frac{\sqrt{2} \sqrt{1 + \sqrt{5}}}{4} + \sqrt{3} \left(\frac{\sqrt{5}}{24} + \frac{1}{8}\right) + \frac{\sqrt{10} \sqrt{1 + \sqrt{5}}}{8}`

       :math:`Q_a = - \frac{13}{48} + \frac{\sqrt{3} \left(- \sqrt{2} \sqrt{1 + \sqrt{5}} + \sqrt{10} \sqrt{1 + \sqrt{5}}\right)}{96} + \frac{3 \sqrt{5}}{16}`
   * - :g:`Kimberling (6, 9, 13) <panel-kimberling>`
     - :math:`\mathbb{Q}(\sqrt{3}, \sqrt{35})`
     - :math:`x = \frac{1603058}{178477} - \frac{1020 \sqrt{105}}{13729}`

       :math:`y = \frac{8100 \sqrt{35}}{178477} + \frac{78101 \sqrt{3}}{41187}`
     - :math:`\alpha = -25311 + 2808 \sqrt{105}`

       :math:`\beta = -39689 + 4212 \sqrt{105}`

       :math:`\gamma = 6084 \sqrt{105} + 99639`
     - :math:`u = -1298 + 144 \sqrt{105}`

       :math:`v = -3053 + 324 \sqrt{105}`

       :math:`w = 676 \sqrt{105} + 11071`
     - :math:`\Delta_a = - \frac{153287 \sqrt{3}}{41187} + \frac{15488 \sqrt{35}}{13729}`

       :math:`\Delta_b = - \frac{708739 \sqrt{3}}{82374} + \frac{35378 \sqrt{35}}{13729}`

       :math:`\Delta_c = \frac{4050 \sqrt{35}}{13729} + \frac{1015313 \sqrt{3}}{82374}`
     - :math:`d_a = - \frac{153287 \sqrt{3}}{123561} + \frac{15488 \sqrt{35}}{41187}`

       :math:`Q_a = \frac{48684109489}{5089106907} - \frac{4748218112 \sqrt{105}}{5089106907}`
   * - :g:`Golden (φ, φ, 1) <panel-golden>`
     - :math:`\mathbb{Q}(\sqrt{5 + 2\sqrt{5}}, \sqrt{3})`
     - :math:`x = \frac{1}{2}`

       :math:`y = \frac{\sqrt{3}}{6}`
     - :math:`\alpha = 3 \sqrt{5} + 7 + \sqrt{3} \left(\sqrt{2 \sqrt{5} + 5} + \sqrt{5} \sqrt{2 \sqrt{5} + 5}\right)`

       :math:`\beta = 3 \sqrt{5} + 7 + \sqrt{3} \left(\sqrt{2 \sqrt{5} + 5} + \sqrt{5} \sqrt{2 \sqrt{5} + 5}\right)`

       :math:`\gamma = 2 \sqrt{5} + 8 + 2 \sqrt{3} \sqrt{2 \sqrt{5} + 5}`
     - :math:`u = 11 + 5 \sqrt{5} + \sqrt{3} \left(\sqrt{5} \sqrt{2 \sqrt{5} + 5} + 3 \sqrt{2 \sqrt{5} + 5}\right)`

       :math:`v = 11 + 5 \sqrt{5} + \sqrt{3} \left(\sqrt{5} \sqrt{2 \sqrt{5} + 5} + 3 \sqrt{2 \sqrt{5} + 5}\right)`

       :math:`w = 2 \sqrt{5} + 8 + 2 \sqrt{3} \sqrt{2 \sqrt{5} + 5}`
     - :math:`\Delta_a = - \frac{\sqrt{3}}{24} + \frac{\sqrt{2 \sqrt{5} + 5}}{8}`

       :math:`\Delta_b = - \frac{\sqrt{3}}{24} + \frac{\sqrt{2 \sqrt{5} + 5}}{8}`

       :math:`\Delta_c = \frac{\sqrt{3}}{12}`
     - :math:`d_a = - \frac{\sqrt{2 \sqrt{5} + 5}}{8} + \sqrt{3} \left(\frac{1}{24} - \frac{\sqrt{5}}{24}\right) + \frac{\sqrt{5} \sqrt{2 \sqrt{5} + 5}}{8}`

       :math:`Q_a = \sqrt{3} \left(- \frac{\sqrt{2 \sqrt{5} + 5}}{16} + \frac{\sqrt{5} \sqrt{2 \sqrt{5} + 5}}{48}\right) + \frac{\sqrt{5}}{48} + \frac{3}{16}`
   * - :g:`Gnomon (1, 1, φ) <panel-gnomon>`
     - :math:`\mathbb{Q}(\sqrt{5 + 2\sqrt{5}}, \sqrt{3})`
     - :math:`x = \frac{1}{4} + \frac{\sqrt{5}}{4}`

       :math:`y = \sqrt{3} \left(\frac{1}{12} + \frac{\sqrt{5}}{12}\right)`
     - :math:`\alpha = - \sqrt{5} + 1 + \sqrt{3} \left(- \sqrt{2 \sqrt{5} + 5} + \sqrt{5} \sqrt{2 \sqrt{5} + 5}\right)`

       :math:`\beta = - \sqrt{5} + 1 + \sqrt{3} \left(- \sqrt{2 \sqrt{5} + 5} + \sqrt{5} \sqrt{2 \sqrt{5} + 5}\right)`

       :math:`\gamma = 6 + 4 \sqrt{5} + 2 \sqrt{3} \sqrt{2 \sqrt{5} + 5}`
     - :math:`u = - \sqrt{5} + 1 + \sqrt{3} \left(- \sqrt{2 \sqrt{5} + 5} + \sqrt{5} \sqrt{2 \sqrt{5} + 5}\right)`

       :math:`v = - \sqrt{5} + 1 + \sqrt{3} \left(- \sqrt{2 \sqrt{5} + 5} + \sqrt{5} \sqrt{2 \sqrt{5} + 5}\right)`

       :math:`w = 5 \sqrt{5} + 13 + \sqrt{3} \left(\sqrt{2 \sqrt{5} + 5} + \sqrt{5} \sqrt{2 \sqrt{5} + 5}\right)`
     - :math:`\Delta_a = - \frac{\sqrt{2 \sqrt{5} + 5}}{16} + \sqrt{3} \left(- \frac{1}{16} - \frac{\sqrt{5}}{48}\right) + \frac{\sqrt{5} \sqrt{2 \sqrt{5} + 5}}{16}`

       :math:`\Delta_b = - \frac{\sqrt{2 \sqrt{5} + 5}}{16} + \sqrt{3} \left(- \frac{1}{16} - \frac{\sqrt{5}}{48}\right) + \frac{\sqrt{5} \sqrt{2 \sqrt{5} + 5}}{16}`

       :math:`\Delta_c = \sqrt{3} \left(\frac{\sqrt{5}}{24} + \frac{1}{8}\right)`
     - :math:`d_a = - \frac{\sqrt{2 \sqrt{5} + 5}}{8} + \sqrt{3} \left(- \frac{1}{8} - \frac{\sqrt{5}}{24}\right) + \frac{\sqrt{5} \sqrt{2 \sqrt{5} + 5}}{8}`

       :math:`Q_a = \sqrt{3} \left(- \frac{\sqrt{5} \sqrt{2 \sqrt{5} + 5}}{48} - \frac{\sqrt{2 \sqrt{5} + 5}}{48}\right) + \frac{\sqrt{5}}{16} + \frac{11}{48}`
   * - **Equilateral (2, 2, 2)**
     - :math:`\mathbb{Q}(\sqrt{3})`
     - :math:`x = 1`

       :math:`y = \frac{\sqrt{3}}{3}`
     - :math:`\alpha = 1`

       :math:`\beta = 1`

       :math:`\gamma = 1`
     - :math:`u = 1`

       :math:`v = 1`

       :math:`w = 1`
     - :math:`\Delta_a = \frac{\sqrt{3}}{3}`

       :math:`\Delta_b = \frac{\sqrt{3}}{3}`

       :math:`\Delta_c = \frac{\sqrt{3}}{3}`
     - :math:`d_a = \frac{\sqrt{3}}{3}`

       :math:`Q_a = \frac{1}{3}`

.. container:: etc-mode-four-triangles

   Across the canonical algebraic number fields — :g:`Heronian (15, 13, 14) <heronian-X_13>` over :math:`\mathbb{Q}(\sqrt{3})` (:math:`X_{13} = \left(\frac{13727}{2353} - \frac{224 \sqrt{3}}{2353},\; \frac{18816}{2353} - \frac{5523 \sqrt{3}}{2353}\right)`), :g:`Right (3, 4, 5) <right-X_13>` over :math:`\mathbb{Q}(\sqrt{3})` (:math:`X_{13} = \left(\frac{162}{193} - \frac{16 \sqrt{3}}{193},\; \frac{384}{193} - \frac{138 \sqrt{3}}{193}\right)`), :g:`Kepler (1, √φ, φ) <kepler-X_13>` over :math:`\mathbb{Q}(\sqrt{\phi}, \sqrt{3})`, :g:`Kimberling (6, 9, 13) <kimberling-X_13>` over :math:`\mathbb{Q}(\sqrt{3}, \sqrt{35})` (:math:`X_{13} = \left(\frac{1603058}{178477} - \frac{1020 \sqrt{105}}{13729},\; \frac{8100 \sqrt{35}}{178477} + \frac{78101 \sqrt{3}}{41187}\right)`), :g:`Golden (φ, φ, 1) <golden-X_13>` over :math:`\mathbb{Q}(\sqrt{5 + 2\sqrt{5}}, \sqrt{3})` (:math:`X_{13} = \left(\frac{1}{2},\; \frac{\sqrt{3}}{6}\right)`), and :g:`Gnomon (1, 1, φ) <gnomon-X_13>` over :math:`\mathbb{Q}(\sqrt{5 + 2\sqrt{5}}, \sqrt{3})` — **X_13** remains strictly interior (:math:`\Delta_a, \Delta_b, \Delta_c > 0`) across all six non-degenerate canonical triangles (scalene, right, and pentagon isosceles), preserving its exact homogeneous law :math:`u : v : w` without floating-point approximation. On the **Equilateral (2, 2, 2)** limit over :math:`\mathbb{Q}(\sqrt{3})`, **X_13** coalesces to the symmetry center :math:`O = \left(1,\; \frac{\sqrt{3}}{3}\right)`.

.. list-table:: Coordinate Decomposition of X_13 on Heronian (15, 13, 14)
   :header-rows: 1
   :class: etc-table etc-mode-coordinates

   * - Sideline
     - Pedal Foot
     - Trilinear Strut
     - Sub-Triangle
     - Signed Area
   * - :g:`BC <[ B C ]>` (:math:`a = 15`)
     - :g:`T_a <T_a>` = :math:`\left(\frac{12852 \sqrt{3}}{11765} + \frac{424823}{58825},\; \frac{531636}{58825} - \frac{17136 \sqrt{3}}{11765}\right)`
     - :g:`X_13T_a </ X_13 T_a />` (:math:`d_a = \frac{20412}{11765} + \frac{3493 \sqrt{3}}{2353},\; Q = \frac{142598232 \sqrt{3}}{27683045} + \frac{1331728419}{138415225}`)
     - :g:`△X_13BC << X_13 B C >>`
     - :math:`\Delta_a = \frac{30618}{2353} + \frac{52395 \sqrt{3}}{4706}`
   * - :g:`CA <[ C A ]>` (:math:`b = 13`)
     - :g:`T_b <T_b>` = :math:`\left(\frac{1472135}{397657} - \frac{336980 \sqrt{3}}{397657},\; \frac{3533124}{397657} - \frac{808752 \sqrt{3}}{397657}\right)`
     - :g:`X_13T_b </ X_13 T_b />` (:math:`d_b = \frac{24927 \sqrt{3}}{30589} + \frac{70644}{30589},\; Q = \frac{3521885976 \sqrt{3}}{935686921} + \frac{6854640723}{935686921}`)
     - :g:`△X_13CA << X_13 C A >>`
     - :math:`\Delta_b = \frac{24927 \sqrt{3}}{4706} + \frac{35322}{2353}`
   * - :g:`AB <[ A B ]>` (:math:`c = 14`)
     - :g:`T_c <T_c>` = :math:`\left(\frac{13727}{2353} - \frac{224 \sqrt{3}}{2353},\; 0\right)`
     - :g:`X_13T_c </ X_13 T_c />` (:math:`d_c = \frac{18816}{2353} - \frac{5523 \sqrt{3}}{2353},\; Q = \frac{445552443}{5536609} - \frac{207841536 \sqrt{3}}{5536609}`)
     - :g:`△X_13AB << X_13 A B >>`
     - :math:`\Delta_c = \frac{131712}{2353} - \frac{38661 \sqrt{3}}{2353}`

.. container:: etc-mode-coordinates

   Barycentric sum :math:`\Delta_a + \Delta_b + \Delta_c = 84 = \Delta` (:math:`u : v : w = 900 \sqrt{3} + 1563 : 1167 + 676 \sqrt{3} : 1302 + 784 \sqrt{3}`); trilinear ratio :math:`\alpha : \beta : \gamma = 3900 \sqrt{3} + 6773 : 5835 + 3380 \sqrt{3} : 6045 + 3640 \sqrt{3}`.

Constructed Elements
--------------------

.. list-table:: Constructed Geometric Elements
   :header-rows: 1
   :class: etc-table
   :widths: 24 38 38

   * - Role
     - Elements
     - Property
   * - **Outward Equilateral Side Triangles**
     - :g:`△BCA' << B C A' >>`, :g:`△CAB' << C A B' >>`, :g:`△ABC' << A B C' >>` erected outward on sidelines with apexes :g:`A' <A'>`, :g:`B' <B'>`, :g:`C' <C'>`
     - —
   * - **Concurrence Lines (Outer Cevians)**
     - :g:`A–A' <[ A A' ]>`, :g:`B–B' <[ B B' ]>`, :g:`C–C' <[ C C' ]>` concurring at :g:`X_13 <X_13>`
     - —

.. collapse:: Linear Combinations
   :badge: 1 combination

   .. list-table:: Barycentric & Vector Linear Combinations of X_13
      :header-rows: 1
      :class: etc-table
      :widths: 55 45

      * - Expression
        - Definitions
      * - :ref:`X_13 <X_13>` = :math:`3^{1/2}(r^{2} + 2rR + s^{2})` :ref:`X_1 <X_1>` - :math:`6r(3^{1/2}R - 2s)` :ref:`X_2 <X_2>` - :math:`2r(3^{1/2}r + 3s)` :ref:`X_3 <X_3>` (:person:`Peter Moses <peter-moses>`, April 2, 2013)
        - —


.. admonition:: Related Collection 1 Topic Guides
   :class: tip

   :doc:`T_1: Isogonal Conjugate <../../../topics/isogonal-conjugate/index>` • :doc:`T_13: The Isogonic & Napoleon Central Lines <../../../topics/isogonic-and-napoleon-lines/index>` • :doc:`T_18: The Apollonian Circles <../../../topics/apollonian-circles/index>` • :doc:`T_24: Equilateral, Isogonic & Napoleon Triangles <../../../topics/isogonic-and-napoleon-triangles/index>`

.. toctree::
   :hidden:

   lines
   relations
   notes
   code
