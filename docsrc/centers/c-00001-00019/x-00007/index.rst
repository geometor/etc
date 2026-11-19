:order: 7
:canonical_id: X_7
:subtitle: GERGONNE POINT
:tracks: Overview: index | Lines: lines | Relations: relations | Notes: notes | Code: code
:dependencies: X_1, X_2, X_3, X_4, X_6, X_8, X_9, X_11, X_12, X_20, X_21, X_27, X_33, X_34, X_37, X_41, X_42, X_48, X_55, X_56, X_57, X_58, X_59, X_63, X_65, X_69, X_72, X_73, X_75, X_76, X_77, X_80, X_81, X_85, X_86, X_88, X_92, X_99, X_100, X_104, X_108, X_109, X_142, X_144, X_145, X_150, X_171, X_174, X_177, X_189, X_190, X_192, X_193, X_196, X_218, X_220, X_222, X_224, X_225, X_226, X_228, X_229, X_234, X_238, X_239, X_241, X_253, X_256, X_264, X_269, X_272, X_273, X_274, X_277, X_278, X_279, X_280, X_281, X_286, X_290, X_294, X_309, X_310, X_314, X_329, X_330, X_331, X_335, X_344, X_347, X_348, X_349, X_354, X_390, X_404, X_443, X_452, X_464, X_479, X_480, X_492, X_497, X_506, X_508, X_513, X_514, X_517, X_528, X_554, X_555, X_594, X_599, X_604, X_645, X_648, X_653, X_657, X_658, X_662, X_663, X_664, X_666, X_668, X_670, X_671, X_673, X_675, X_757, X_811, X_840, X_857, X_870, X_885, X_886, X_889, X_892, X_903, X_927, X_934, X_940, X_941, X_942, X_943, X_944, X_952, X_959, X_969, X_982, X_983, X_986, X_987, X_991, X_1000, X_1002, X_1004, X_1013, X_1020, X_1039, X_1041, X_1061, X_1082, X_1086, X_1101, X_1106, X_1156, X_1159, X_1210, X_1214, X_1223, X_1246, X_1253, X_1254, X_1259, X_1266, X_1267, X_1268, X_1269, X_1275, X_1354, X_1362, X_1365, X_1366, X_1367, X_1371, X_1372, X_1373, X_1374, X_1376, X_1386, X_1389, X_1407, X_1414, X_1419, X_1427, X_1429, X_1431, X_1432, X_1435, X_1445, X_1447, X_1449, X_1456, X_1467, X_1471, X_1479, X_1486, X_1602, X_1617, X_1621, X_1742, X_1765, X_1843, X_1848, X_1870, X_1901, X_2175, X_2293, X_2346, X_2475, X_2884, X_2886, X_2893, X_3064, X_3091, X_3160, X_3700, X_3818, X_4092, X_5273, X_37787

.. _X_7:
.. _GergonnePoint:
.. _gergonne_point:

X_7
====

.. rubric:: GERGONNE POINT

.. container:: etc-identity-bar

   ``gergonne_point(A, B, C) -> X_7`` • **Gergonne (1818)** • **Kimberling** ``X(7)`` • **Search** :math:`(6,9,13)`: :math:`\frac{20 \sqrt{35}}{159} \approx 0.744160979006`

.. enunciation::

   Let :g:`T_a <T_a>`, :g:`T_b <T_b>`, :g:`T_c <T_c>` denote the points in which the incircle meets the sides :g:`BC <[ B C ]>`, :g:`CA <[ C A ]>`, :g:`AB <[ A B ]>`, respectively. The lines :g:`AT_a <[ A T_a ]>`, :g:`BT_b <[ B T_b ]>`, :g:`CT_c <[ C T_c ]>` concur in :ref:`X_7 <X_7>`.

.. figure:: x-00007.svg
   :alt: X_7 — GERGONNE POINT
   :align: center

   **X_7** (*GERGONNE POINT*) constructed at :g:`X_7 <X_7>` = :math:`\left(\frac{414}{73},\; \frac{288}{73}\right)` in exact rational coordinates on Heronian :math:`(15, 13, 14)` over :math:`\mathbb{Q}` with vertices :g:`A <A>` = :math:`(0, 0)`, :g:`B <B>` = :math:`(14, 0)`, :g:`C <C>` = :math:`(5, 12)`, area :math:`\Delta = 84`. Switch view modes or reference triangles above.

Homogeneous Coordinates
-----------------------

.. list-table::
   :header-rows: 1
   :class: etc-table etc-coord-table etc-mode-coordinates
   :widths: 18 41 41

   * - Trilinears
     - Canonical
     - Alternates
   * - :g:`α </ X_7 T_a />`
     - :math:`bc/(b + c - a)`
     - :math:`\sec^{2}(A/2)`

       :math:`1/(\tan(B/2) + \tan(C/2))`

       :math:`(bc - S_{A})/a`

       :math:`(1 - \cos A)a^{-2}`
   * - :g:`β </ X_7 T_b />`
     - :math:`ca/(c + a - b)`
     - :math:`\sec^{2}(B/2)`

       :math:`1/(\tan(C/2) + \tan(A/2))`

       :math:`(ca - S_{B})/b`

       :math:`(1 - \cos B)b^{-2}`
   * - :g:`γ </ X_7 T_c />`
     - :math:`ab/(a + b - c)`
     - :math:`\sec^{2}(C/2)`

       :math:`1/(\tan(A/2) + \tan(B/2))`

       :math:`(ab - S_{C})/c`

       :math:`(1 - \cos C)c^{-2}`

.. list-table::
   :header-rows: 1
   :class: etc-table etc-coord-table etc-mode-coordinates
   :widths: 18 41 41

   * - Barycentrics
     - Canonical
     - Alternates
   * - :g:`u << X_7 B C >>`
     - :math:`1/(b + c - a)`
     - :math:`\tan A/2`

       :math:`bc - S_{A}`

       :math:`r_{a}`
   * - :g:`v << X_7 C A >>`
     - :math:`1/(c + a - b)`
     - :math:`\tan B/2`

       :math:`ca - S_{B}`

       :math:`r_{b}`
   * - :g:`w << X_7 A B >>`
     - :math:`1/(a + b - c)`
     - :math:`\tan C/2`

       :math:`ab - S_{C}`

       :math:`r_{c}`

.. container:: etc-coord-notes

   *Note:* where :math:`r_{a}`, :math:`r_{b}`, :math:`r_{c}` are the exradii

.. list-table::
   :header-rows: 1
   :class: etc-table etc-coord-table etc-mode-coordinates
   :widths: 18 41 41

   * - Tripolars
     - Canonical
     - Alternates
   * - :g:`PA </ X_7 A />`
     - :math:`(b+c-a) \sqrt{a (a-b-c) (a^{2}+a b-2 b^{2}+a c+4 b c-2 c^{2})}`
     - —
   * - :g:`PB </ X_7 B />`
     - :math:`(c+a-b) \sqrt{b (b-c-a) (b^{2}+b c-2 c^{2}+b a+4 c a-2 a^{2})}`
     - —
   * - :g:`PC </ X_7 C />`
     - :math:`(a+b-c) \sqrt{c (c-a-b) (c^{2}+c a-2 a^{2}+c b+4 a b-2 b^{2})}`
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
     - :math:`\mathbb{Q}`
     - :math:`x = \frac{414}{73}`

       :math:`y = \frac{288}{73}`
     - :math:`\alpha = 2548`

       :math:`\beta = 2205`

       :math:`\gamma = 2340`
     - :math:`u = 28`

       :math:`v = 21`

       :math:`w = 24`
     - :math:`\Delta_a = \frac{2352}{73}`

       :math:`\Delta_b = \frac{1764}{73}`

       :math:`\Delta_c = \frac{2016}{73}`
     - :math:`d_a = \frac{1568}{365}`

       :math:`Q_a = \frac{2458624}{133225}`
   * - :g:`Right (3, 4, 5) <panel-right>`
     - :math:`\mathbb{Q}`
     - :math:`x = \frac{8}{11}`

       :math:`y = \frac{9}{11}`
     - :math:`\alpha = 72`

       :math:`\beta = 40`

       :math:`\gamma = 45`
     - :math:`u = 6`

       :math:`v = 2`

       :math:`w = 3`
     - :math:`\Delta_a = \frac{36}{11}`

       :math:`\Delta_b = \frac{12}{11}`

       :math:`\Delta_c = \frac{18}{11}`
     - :math:`d_a = \frac{72}{55}`

       :math:`Q_a = \frac{5184}{3025}`
   * - :g:`Kepler (1, √φ, φ) <panel-kepler>`
     - :math:`\mathbb{Q}(\sqrt{\phi})`
     - :math:`x = \frac{6 \phi \sqrt{\phi}}{11} - \frac{4 \sqrt{\phi}}{11} - \frac{\phi}{11} - \frac{3}{11}`

       :math:`y = - \frac{2 \phi \sqrt{\phi}}{11} + \frac{5 \sqrt{\phi}}{11} - \frac{7 \phi}{11} + \frac{12}{11}`
     - :math:`\alpha = \sqrt{\phi} \left(\phi - 1\right)`

       :math:`\beta = \phi \sqrt{\phi} - \phi`

       :math:`\gamma = \sqrt{\phi} \left(2 - \phi\right)`
     - :math:`u = \sqrt{\phi}`

       :math:`v = \phi \sqrt{\phi} - \phi`

       :math:`w = \phi - 1`
     - :math:`\Delta_a = \frac{\phi \sqrt{\phi}}{22} + \frac{3 \sqrt{\phi}}{22} - \frac{\phi}{11} + \frac{5}{22}`

       :math:`\Delta_b = \frac{3 \phi \sqrt{\phi}}{11} - \frac{2 \sqrt{\phi}}{11} - \frac{\phi}{22} - \frac{3}{22}`

       :math:`\Delta_c = - \frac{7 \phi \sqrt{\phi}}{22} + \frac{6 \sqrt{\phi}}{11} + \frac{3 \phi}{22} - \frac{1}{11}`
     - :math:`d_a = \frac{3 \phi \sqrt{\phi}}{11} - \frac{2 \sqrt{\phi}}{11} + \frac{5 \phi}{11} - \frac{7}{11}`

       :math:`Q_a = - \frac{32 \phi \sqrt{\phi}}{121} + \frac{58 \sqrt{\phi}}{121} - \frac{35 \phi}{121} + \frac{71}{121}`
   * - :g:`Kimberling (6, 9, 13) <panel-kimberling>`
     - :math:`\mathbb{Q}(\sqrt{35})`
     - :math:`x = \frac{5632}{689}`

       :math:`y = \frac{320 \sqrt{35}}{689}`
     - :math:`\alpha = 195`

       :math:`\beta = 208`

       :math:`\gamma = 720`
     - :math:`u = 5`

       :math:`v = 8`

       :math:`w = 40`
     - :math:`\Delta_a = \frac{20 \sqrt{35}}{53}`

       :math:`\Delta_b = \frac{32 \sqrt{35}}{53}`

       :math:`\Delta_c = \frac{160 \sqrt{35}}{53}`
     - :math:`d_a = \frac{20 \sqrt{35}}{159}`

       :math:`Q_a = \frac{14000}{25281}`
   * - :g:`Golden (φ, φ, 1) <panel-golden>`
     - :math:`\mathbb{Q}(\sqrt{5 + 2\sqrt{5}})`
     - :math:`x = \frac{1}{2}`

       :math:`y = - \frac{\sqrt{2 \sqrt{5} + 5}}{38} + \frac{\sqrt{5} \sqrt{2 \sqrt{5} + 5}}{19}`
     - :math:`\alpha = 5 - \sqrt{5}`

       :math:`\beta = 5 - \sqrt{5}`

       :math:`\gamma = 2`
     - :math:`u = \sqrt{5}`

       :math:`v = \sqrt{5}`

       :math:`w = 1`
     - :math:`\Delta_a = - \frac{\sqrt{5} \sqrt{2 \sqrt{5} + 5}}{76} + \frac{5 \sqrt{2 \sqrt{5} + 5}}{38}`

       :math:`\Delta_b = - \frac{\sqrt{5} \sqrt{2 \sqrt{5} + 5}}{76} + \frac{5 \sqrt{2 \sqrt{5} + 5}}{38}`

       :math:`\Delta_c = - \frac{\sqrt{2 \sqrt{5} + 5}}{76} + \frac{\sqrt{5} \sqrt{2 \sqrt{5} + 5}}{38}`
     - :math:`d_a = - \frac{15 \sqrt{2 \sqrt{5} + 5}}{76} + \frac{11 \sqrt{5} \sqrt{2 \sqrt{5} + 5}}{76}`

       :math:`Q_a = \frac{5 \sqrt{5}}{2888} + \frac{425}{2888}`
   * - :g:`Gnomon (1, 1, φ) <panel-gnomon>`
     - :math:`\mathbb{Q}(\sqrt{5 + 2\sqrt{5}})`
     - :math:`x = \frac{1}{4} + \frac{\sqrt{5}}{4}`

       :math:`y = - \frac{\sqrt{2 \sqrt{5} + 5}}{44} + \frac{3 \sqrt{5} \sqrt{2 \sqrt{5} + 5}}{44}`
     - :math:`\alpha = -1 + \sqrt{5}`

       :math:`\beta = -1 + \sqrt{5}`

       :math:`\gamma = 1 + \sqrt{5}`
     - :math:`u = -1 + \sqrt{5}`

       :math:`v = -1 + \sqrt{5}`

       :math:`w = \sqrt{5} + 3`
     - :math:`\Delta_a = - \frac{9 \sqrt{2 \sqrt{5} + 5}}{88} + \frac{5 \sqrt{5} \sqrt{2 \sqrt{5} + 5}}{88}`

       :math:`\Delta_b = - \frac{9 \sqrt{2 \sqrt{5} + 5}}{88} + \frac{5 \sqrt{5} \sqrt{2 \sqrt{5} + 5}}{88}`

       :math:`\Delta_c = \frac{\sqrt{5} \sqrt{2 \sqrt{5} + 5}}{88} + \frac{7 \sqrt{2 \sqrt{5} + 5}}{88}`
     - :math:`d_a = - \frac{9 \sqrt{2 \sqrt{5} + 5}}{44} + \frac{5 \sqrt{5} \sqrt{2 \sqrt{5} + 5}}{44}`

       :math:`Q_a = \frac{65}{968} - \frac{19 \sqrt{5}}{968}`
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

   Across the canonical algebraic number fields — :g:`Heronian (15, 13, 14) <heronian-X_7>` over :math:`\mathbb{Q}` (:math:`X_{7} = \left(\frac{414}{73},\; \frac{288}{73}\right)`), :g:`Right (3, 4, 5) <right-X_7>` over :math:`\mathbb{Q}` (:math:`X_{7} = \left(\frac{8}{11},\; \frac{9}{11}\right)`), :g:`Kepler (1, √φ, φ) <kepler-X_7>` over :math:`\mathbb{Q}(\sqrt{\phi})`, :g:`Kimberling (6, 9, 13) <kimberling-X_7>` over :math:`\mathbb{Q}(\sqrt{35})` (:math:`X_{7} = \left(\frac{5632}{689},\; \frac{320 \sqrt{35}}{689}\right)`), :g:`Golden (φ, φ, 1) <golden-X_7>` over :math:`\mathbb{Q}(\sqrt{5 + 2\sqrt{5}})`, and :g:`Gnomon (1, 1, φ) <gnomon-X_7>` over :math:`\mathbb{Q}(\sqrt{5 + 2\sqrt{5}})` — **X_7** remains strictly interior (:math:`\Delta_a, \Delta_b, \Delta_c > 0`) across all six non-degenerate canonical triangles (scalene, right, and pentagon isosceles), preserving its exact homogeneous law :math:`u : v : w` without floating-point approximation. On the **Equilateral (2, 2, 2)** limit over :math:`\mathbb{Q}(\sqrt{3})`, **X_7** coalesces to the symmetry center :math:`O = \left(1,\; \frac{\sqrt{3}}{3}\right)`.

.. list-table:: Coordinate Decomposition of X_7 on Heronian (15, 13, 14)
   :header-rows: 1
   :class: etc-table etc-mode-coordinates

   * - Sideline
     - Pedal Foot
     - Trilinear Strut
     - Sub-Triangle
     - Signed Area
   * - :g:`BC <[ B C ]>` (:math:`a = 15`)
     - :g:`T_a <T_a>` = :math:`\left(\frac{16622}{1825},\; \frac{11904}{1825}\right)`
     - :g:`X_7T_a </ X_7 T_a />` (:math:`d_a = \frac{1568}{365},\; Q = \frac{2458624}{133225}`)
     - :g:`△X_7BC << X_7 B C >>`
     - :math:`\Delta_a = \frac{2352}{73}`
   * - :g:`CA <[ C A ]>` (:math:`b = 13`)
     - :g:`T_b <T_b>` = :math:`\left(\frac{27630}{12337},\; \frac{66312}{12337}\right)`
     - :g:`X_7T_b </ X_7 T_b />` (:math:`d_b = \frac{3528}{949},\; Q = \frac{12446784}{900601}`)
     - :g:`△X_7CA << X_7 C A >>`
     - :math:`\Delta_b = \frac{1764}{73}`
   * - :g:`AB <[ A B ]>` (:math:`c = 14`)
     - :g:`T_c <T_c>` = :math:`\left(\frac{414}{73},\; 0\right)`
     - :g:`X_7T_c </ X_7 T_c />` (:math:`d_c = \frac{288}{73},\; Q = \frac{82944}{5329}`)
     - :g:`△X_7AB << X_7 A B >>`
     - :math:`\Delta_c = \frac{2016}{73}`

.. container:: etc-mode-coordinates

   Barycentric sum :math:`\Delta_a + \Delta_b + \Delta_c = 84 = \Delta` (:math:`u : v : w = 28 : 21 : 24`); trilinear ratio :math:`\alpha : \beta : \gamma = 2548 : 2205 : 2340`.

Constructed Elements
--------------------

.. list-table:: Constructed Geometric Elements
   :header-rows: 1
   :class: etc-table
   :widths: 24 38 38

   * - Role
     - Elements
     - Property
   * - **Derived Triangle**
     - :term:`Intouch (Contact) Triangle <intouch-triangle>` :g:`△T_aT_bT_c << T_a T_b T_c >>`
     - vertices :g:`T_a <T_a>`, :g:`T_b <T_b>`, :g:`T_c <T_c>` (Contact triangle of Incircle touchpoints on BC, CA, AB)
   * - **Circle**
     - **Incircle** (:g:`incircle <incircle>`)
     - Inscribed circle tangent to sidelines at T_a, T_b, T_c; centered at X_1 INCENTER
   * - **Concurrence Lines (Gergonne Cevians)**
     - :g:`A–T_a <[ A T_a ]>`, :g:`B–T_b <[ B T_b ]>`, :g:`C–T_c <[ C T_c ]>` concurring at :g:`X_7 <X_7>`
     - —

.. collapse:: Linear Combinations
   :badge: 2 combinations

   .. list-table:: Barycentric & Vector Linear Combinations of X_7
      :header-rows: 1
      :class: etc-table
      :widths: 55 45

      * - Expression
        - Definitions
      * - :ref:`X_7 <X_7>` = :math:`(2r + 4R)` :ref:`X_1 <X_1>` + :math:`3r` :ref:`X_2 <X_2>` - :math:`4r` :ref:`X_3 <X_3>`
        - —
      * - :ref:`X_7 <X_7>` = :g:`A <A>` / :math:`R_{a}` + :g:`B <B>` / :math:`R_{b}` + :g:`C <C>` / :math:`R_{c}`
        - where :math:`R_{a}`, :math:`R_{b}`, :math:`R_{c}` = radii of Soddy circles


.. admonition:: Related Collection 1 Topic Guides
   :class: tip

   :doc:`T_2: Isotomic Conjugate <../../../topics/isotomic-conjugate/index>` • :doc:`T_11: The Soddy Line <../../../topics/soddy-line/index>` • :doc:`T_12: The Fuhrmann & Spieker Central Lines <../../../topics/fuhrmann-and-spieker-lines/index>` • :doc:`T_14: The Incircle & Excircles <../../../topics/incircle-and-excircles/index>` • :doc:`T_22: Intouch (Contact) & Extouch Triangles <../../../topics/intouch-and-extouch-triangles/index>`

.. toctree::
   :hidden:

   lines
   relations
   notes
   code
