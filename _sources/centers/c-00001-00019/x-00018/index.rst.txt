:order: 18
:canonical_id: X_18
:subtitle: 2nd NAPOLEON POINT
:dependencies: X_2, X_3, X_4, X_5, X_6, X_12, X_13, X_14, X_15, X_16, X_17, X_61, X_62, X_63, X_76, X_83, X_140, X_202, X_203, X_231, X_275, X_298, X_302, X_303, X_398, X_470, X_472, X_499, X_523, X_623, X_624, X_628, X_630, X_634, X_636, X_1209, X_10641, X_14447, X_32628

.. _X_18:
.. _SecondNapoleonPoint:
.. _second_napoleon_point:

X_18
====

.. rubric:: 2nd NAPOLEON POINT

``second_napoleon_point(A, B, C) -> X_18`` • **Kiepert • Napoleon** • **Kimberling** ``X(18)`` • **Search Value** :math:`(6, 9, 13)`: :math:`- \frac{81811 \sqrt{3}}{16041} - \frac{20192 \sqrt{35}}{16041} \approx -16.280673997778`

.. enunciation::

   Let ``Nap_a``, ``Nap_b``, ``Nap_c`` be the centers of the equilateral triangles in the construction of :ref:`X_14 <X_14>`. The lines ``ANap_a``, ``BNap_b``, ``CNap_c`` concur in :ref:`X_18 <X_18>`.

.. figure:: x-00018.svg
   :alt: X_18 — 2nd NAPOLEON POINT
   :align: center

   **X_18** (*2nd NAPOLEON POINT*) constructed at :g:`X_18 <X_18>` = :math:`\left(\frac{8736 \sqrt{3}}{29635} + \frac{192941}{29635},\; \frac{23520}{5927} - \frac{189 \sqrt{3}}{29635}\right)` in exact algebraic coordinates on the Heronian reference triangle :math:`(a, b, c) = (15, 13, 14)` over :math:`\mathbb{Q}(\sqrt{3})` with vertices :g:`A <A>` = :math:`(0, 0)`, :g:`B <B>` = :math:`(14, 0)`, :g:`C <C>` = :math:`(5, 12)`, and area :math:`\Delta = 84`. Switch tabs above to inspect exact constructions on Right :math:`(3, 4, 5)`, Kepler :math:`(1, \sqrt{\phi}, \phi)`, and Kimberling :math:`(6, 9, 13)`.

.. admonition:: Constructed Elements
   :class: note

   * **Inward Equilateral Side Triangles:** :g:`△BCA'' << B C A'' >>`, :g:`△CAB'' << C A B'' >>`, :g:`△ABC'' << A B C'' >>` erected inward on sidelines with apexes :g:`A'' <A''>`, :g:`B'' <B''>`, :g:`C'' <C''>`
   * **Derived Triangle:** :term:`Inner Napoleon Triangle <inner-napoleon-triangle>` :g:`△Nap'_aNap'_bNap'_c << Nap'_a Nap'_b Nap'_c >>` — vertices :g:`Nap'_a <Nap'_a>`, :g:`Nap'_b <Nap'_b>`, :g:`Nap'_c <Nap'_c>` (Equilateral triangle formed by centers of inward side equilateral triangles)
   * **Concurrence Lines (Inner Cevians):** :g:`A–Nap'_a <[ A Nap'_a ]>`, :g:`B–Nap'_b <[ B Nap'_b ]>`, :g:`C–Nap'_c <[ C Nap'_c ]>` concurring at :g:`X_18 <X_18>`

Homogeneous Coordinates & Exact Invariants
------------------------------------------

.. figure:: 02_coordinates.svg
   :alt: X_18 — Homogeneous Trilinear Distances and Barycentric Sub-Areas
   :align: center

   **Homogeneous Coordinates of X_18** on Heronian :math:`(15, 13, 14)`: orthogonal trilinear struts :math:`(\alpha, \beta, \gamma)` and signed barycentric sub-triangles :math:`(\Delta_a, \Delta_b, \Delta_c)`.

* **Trilinear Coordinates** (:math:`\alpha : \beta : \gamma = 10023 - 3900 \sqrt{3} : 10905 - 3380 \sqrt{3} : 10335 - 3640 \sqrt{3}`): Dropping orthogonal perpendiculars :g:`X_18T_a </ X_18 T_a />`, :g:`X_18T_b </ X_18 T_b />`, and :g:`X_18T_c </ X_18 T_c />` from :g:`X_18 <X_18>` to sidelines :g:`BC <[ B C ]>`, :g:`CA <[ C A ]>`, and :g:`AB <[ A B ]>` meets the sides at right-spread pedal feet :g:`T_a <T_a>` = :math:`\left(\frac{80892 \sqrt{3}}{740875} + \frac{6963509}{740875},\; \frac{4544988}{740875} - \frac{107856 \sqrt{3}}{740875}\right)`, :g:`T_b <T_b>` = :math:`\left(\frac{41412 \sqrt{3}}{1001663} + \frac{2375905}{1001663},\; \frac{496944 \sqrt{3}}{5008315} + \frac{5702172}{1001663}\right)`, and :g:`T_c <T_c>` = :math:`\left(\frac{8736 \sqrt{3}}{29635} + \frac{192941}{29635},\; 0\right)`. The orthogonal strut lengths on :math:`(15, 13, 14)` are :math:`d_a = \frac{534996}{148175} - \frac{34377 \sqrt{3}}{148175}`, :math:`d_b = \frac{105777 \sqrt{3}}{385255} + \frac{1727292}{385255}`, and :math:`d_c = \frac{23520}{5927} - \frac{189 \sqrt{3}}{29635}`, reducing to homogeneous trilinears :math:`\alpha : \beta : \gamma = 10023 - 3900 \sqrt{3} : 10905 - 3380 \sqrt{3} : 10335 - 3640 \sqrt{3}`.
* **Barycentric Coordinates** (:math:`u : v : w = 2313 - 900 \sqrt{3} : 2181 - 676 \sqrt{3} : 2226 - 784 \sqrt{3}`): Joining :g:`X_18 <X_18>` to the vertices along :g:`X_18A </ X_18 A />`, :g:`X_18B </ X_18 B />`, and :g:`X_18C </ X_18 C />` forms signed sub-triangles :g:`△X_18BC << X_18 B C >>`, :g:`△X_18CA << X_18 C A >>`, and :g:`△X_18AB << X_18 A B >>` of exact signed areas :math:`\Delta_a = \frac{802494}{29635} - \frac{103131 \sqrt{3}}{59270}`, :math:`\Delta_b = \frac{105777 \sqrt{3}}{59270} + \frac{863646}{29635}`, and :math:`\Delta_c = \frac{164640}{5927} - \frac{1323 \sqrt{3}}{29635}` (summing to :math:`\Delta_a + \Delta_b + \Delta_c = 84 = \Delta`), in homogeneous ratio :math:`u : v : w = 2313 - 900 \sqrt{3} : 2181 - 676 \sqrt{3} : 2226 - 784 \sqrt{3}`.

.. list-table:: Exact Symbolic Coordinates & Invariants Across the Four Reference Triangles
   :header-rows: 1
   :widths: 18 10 18 14 16 14 14

   * - Reference Triangle
     - Field
     - Cartesian :math:`(x, y)`
     - Trilinears :math:`\alpha : \beta : \gamma`
     - Barycentrics :math:`u : v : w`
     - Sub-Areas :math:`(\Delta_a, \Delta_b, \Delta_c)`
     - Directed Trilinear :math:`(d_a,\, Q_a)`
   * - **Heronian** :math:`(15, 13, 14)`
     - :math:`\mathbb{Q}(\sqrt{3})`
     - :math:`\left(\frac{8736 \sqrt{3}}{29635} + \frac{192941}{29635},\; \frac{23520}{5927} - \frac{189 \sqrt{3}}{29635}\right)`
     - :math:`10023 - 3900 \sqrt{3} : 10905 - 3380 \sqrt{3} : 10335 - 3640 \sqrt{3}`
     - :math:`2313 - 900 \sqrt{3} : 2181 - 676 \sqrt{3} : 2226 - 784 \sqrt{3}`
     - :math:`\left(\frac{802494}{29635} - \frac{103131 \sqrt{3}}{59270},\; \frac{105777 \sqrt{3}}{59270} + \frac{863646}{29635},\; \frac{164640}{5927} - \frac{1323 \sqrt{3}}{29635}\right)`
     - :math:`\frac{534996}{148175} - \frac{34377 \sqrt{3}}{148175}\; (Q_a = \frac{289766054403}{21955830625} - \frac{36783114984 \sqrt{3}}{21955830625})`
   * - **Right** :math:`(3, 4, 5)`
     - :math:`\mathbb{Q}(\sqrt{3})`
     - :math:`\left(\frac{1336}{575} - \frac{42 \sqrt{3}}{115},\; \frac{402}{575} - \frac{24 \sqrt{3}}{115}\right)`
     - :math:`60 - 15 \sqrt{3} : 45 - 20 \sqrt{3} : 48 - 25 \sqrt{3}`
     - :math:`36 - 9 \sqrt{3} : 36 - 16 \sqrt{3} : 48 - 25 \sqrt{3}`
     - :math:`\left(\frac{72 \sqrt{3}}{115} + \frac{297}{115},\; \frac{192}{115} - \frac{12 \sqrt{3}}{115},\; \frac{201}{115} - \frac{12 \sqrt{3}}{23}\right)`
     - :math:`\frac{48 \sqrt{3}}{115} + \frac{198}{115}\; (Q_a = \frac{19008 \sqrt{3}}{13225} + \frac{46116}{13225})`
   * - **Kepler** :math:`(1, \sqrt{\phi}, \phi)`
     - :math:`\mathbb{Q}(\sqrt{\phi}, \sqrt{3})`
     - :math:`\left(\frac{\sqrt{3} \left(- 12 \sqrt{10} \sqrt{1 + \sqrt{5}} + 3 \sqrt{2} \sqrt{1 + \sqrt{5}}\right)}{632} + \frac{75 \sqrt{5}}{632} + \frac{317}{632},\; - \frac{37 \sqrt{2} \sqrt{1 + \sqrt{5}}}{316} + \sqrt{3} \left(- \frac{11 \sqrt{5}}{632} - \frac{17}{632}\right) + \frac{59 \sqrt{10} \sqrt{1 + \sqrt{5}}}{632}\right)`
     - :math:`- \frac{\sqrt{6} \sqrt{1 + \sqrt{5}}}{2} + \frac{3}{2} + \frac{3 \sqrt{5}}{2} : - \sqrt{3} \phi + \frac{3 \sqrt{2} \sqrt{1 + \sqrt{5}}}{2} : \frac{\sqrt{3} \left(- \sqrt{10} \sqrt{1 + \sqrt{5}} - \sqrt{2} \sqrt{1 + \sqrt{5}}\right)}{4} + 4`
     - :math:`- \frac{\sqrt{6} \sqrt{1 + \sqrt{5}}}{2} + \frac{3}{2} + \frac{3 \sqrt{5}}{2} : \frac{\sqrt{3} \left(- \sqrt{10} \sqrt{1 + \sqrt{5}} - \sqrt{2} \sqrt{1 + \sqrt{5}}\right)}{4} + \frac{3}{2} + \frac{3 \sqrt{5}}{2} : \frac{\sqrt{3} \left(- 3 \sqrt{2} \sqrt{1 + \sqrt{5}} - \sqrt{10} \sqrt{1 + \sqrt{5}}\right)}{4} + 2 + 2 \sqrt{5}`
     - :math:`\left(\frac{3 \sqrt{10} \sqrt{1 + \sqrt{5}}}{632} + \sqrt{3} \left(\frac{13}{1264} + \frac{27 \sqrt{5}}{1264}\right) + \frac{117 \sqrt{2} \sqrt{1 + \sqrt{5}}}{1264},\; \sqrt{3} \left(\frac{23}{1264} - \frac{13 \sqrt{5}}{1264}\right) + \frac{3 \sqrt{10} \sqrt{1 + \sqrt{5}}}{2528} + \frac{177 \sqrt{2} \sqrt{1 + \sqrt{5}}}{2528},\; \sqrt{3} \left(- \frac{9}{316} - \frac{7 \sqrt{5}}{632}\right) - \frac{15 \sqrt{10} \sqrt{1 + \sqrt{5}}}{2528} + \frac{221 \sqrt{2} \sqrt{1 + \sqrt{5}}}{2528}\right)`
     - :math:`\frac{3 \sqrt{10} \sqrt{1 + \sqrt{5}}}{316} + \sqrt{3} \left(\frac{13}{632} + \frac{27 \sqrt{5}}{632}\right) + \frac{117 \sqrt{2} \sqrt{1 + \sqrt{5}}}{632}\; (Q_a = \frac{13305}{99856} + \frac{8163 \sqrt{5}}{99856} + \frac{\sqrt{3} \left(2331 \sqrt{2} \sqrt{1 + \sqrt{5}} + 3237 \sqrt{10} \sqrt{1 + \sqrt{5}}\right)}{199712})`
   * - **Kimberling** :math:`(6, 9, 13)`
     - :math:`\mathbb{Q}(\sqrt{3}, \sqrt{35})`
     - :math:`\left(\frac{7740 \sqrt{105}}{5347} + \frac{1579094}{69511},\; - \frac{647 \sqrt{3}}{5347} + \frac{22924 \sqrt{35}}{69511}\right)`
     - :math:`49803 - 2808 \sqrt{105} : 25597 - 4212 \sqrt{105} : 60093 - 6084 \sqrt{105}`
     - :math:`-2554 + 144 \sqrt{105} : -1969 + 324 \sqrt{105} : -6677 + 676 \sqrt{105}`
     - :math:`\left(- \frac{81811 \sqrt{3}}{5347} - \frac{20192 \sqrt{35}}{5347},\; \frac{172033 \sqrt{3}}{10694} + \frac{30118 \sqrt{35}}{5347},\; - \frac{8411 \sqrt{3}}{10694} + \frac{11462 \sqrt{35}}{5347}\right)`
     - :math:`- \frac{81811 \sqrt{3}}{16041} - \frac{20192 \sqrt{35}}{16041}\; (Q_a = \frac{3303855424 \sqrt{105}}{257313681} + \frac{34349209403}{257313681})`

.. signature:: center

   | **Trilinears:** :math:`\csc(A - \pi /6) : \csc(B - \pi /6) : \csc(C - \pi /6)`
   | **Barycentrics:** :math:`a \csc(A - \pi /6) : b \csc(B - \pi /6) : c \csc(C - \pi /6)`
   | **Tripolars:** :math:`(a^{2}-b^{2}-c^{2}+2 \sqrt{3} S) \sqrt{(a^{2}-3 b^{2}-3 c^{2}+2 \sqrt{3} S)} : :`
   | **Search Value (6, 9, 13):** :math:`- \frac{81811 \sqrt{3}}{16041} - \frac{20192 \sqrt{35}}{16041} \approx -16.280673997778`

.. collapse:: Alternate Coordinates
   :badge: 1 form

   * **Trilinears:** :math:`\sec(A + \pi /3) : \sec(B + \pi /3) : \sec(C + \pi /3)`

Incident Central Lines
----------------------

.. figure:: 03_central_lines.svg
   :alt: X_18 — Incident Central Lines
   :align: center

   **Principal Central Lines Through X_18** on Heronian :math:`(15, 13, 14)`.

* **Circumcenter–2nd ISOGONIC CENTER Central Line** :g:`{3, 14, 18} <{ 3, 14 }>` — collinear axis through :g:`X_3 <X_3>` (:ref:`Circumcenter <X_3>`, :math:`\left(7,\; \frac{33}{8}\right)`), :g:`X_14 <X_14>` (:ref:`2nd ISOGONIC CENTER <X_14>`, :math:`\left(\frac{224 \sqrt{3}}{2353} + \frac{13727}{2353},\; \frac{5523 \sqrt{3}}{2353} + \frac{18816}{2353}\right)`), :g:`X_18 <X_18>`, with exact Cartesian equation :math:`x \left(\frac{72879}{18824} + \frac{5523 \sqrt{3}}{2353}\right) + y \left(\frac{2744}{2353} - \frac{224 \sqrt{3}}{2353}\right) - \frac{600705}{18824} - \frac{37737 \sqrt{3}}{2353} = 0` (spread :math:`\frac{730438926336 \sqrt{3}}{2626018592353} + \frac{1319724365409}{2626018592353}` relative to :g:`AB <[ A B ]>`).
* **Nine-Point Center–1st ISOGONIC CENTER Central Line** :g:`{5, 13, 18} <{ 5, 13 }>` — collinear axis through :g:`X_5 <X_5>` (:ref:`Nine-Point Center <X_5>`, :math:`\left(6,\; \frac{63}{16}\right)`), :g:`X_13 <X_13>` (:ref:`1st ISOGONIC CENTER <X_13>`, :math:`\left(\frac{13727}{2353} - \frac{224 \sqrt{3}}{2353},\; \frac{18816}{2353} - \frac{5523 \sqrt{3}}{2353}\right)`), :g:`X_18 <X_18>`, with exact Cartesian equation :math:`x \left(- \frac{152817}{37648} + \frac{5523 \sqrt{3}}{2353}\right) + y \left(- \frac{391}{2353} - \frac{224 \sqrt{3}}{2353}\right) - \frac{32256 \sqrt{3}}{2353} + \frac{941535}{37648} = 0` (spread :math:`\frac{1313499452769}{2626018592353} - \frac{757783240704 \sqrt{3}}{2626018592353}` relative to :g:`AB <[ A B ]>`).
* **Orthocenter–2nd ISODYNAMIC POINT Central Line** :g:`{4, 16, 18} <{ 4, 16 }>` — collinear axis through :g:`X_4 <X_4>` (:ref:`Orthocenter <X_4>`, :math:`\left(5,\; \frac{15}{4}\right)`), :g:`X_16 <X_16>` (:ref:`2nd ISODYNAMIC POINT <X_16>`, :math:`\left(- \frac{65856 \sqrt{3}}{2353} - \frac{99169}{2353},\; - \frac{6867 \sqrt{3}}{2353} - \frac{2352}{2353}\right)`), :g:`X_18 <X_18>`, with exact Cartesian equation :math:`x \left(\frac{44703}{9412} + \frac{6867 \sqrt{3}}{2353}\right) + y \left(- \frac{65856 \sqrt{3}}{2353} - \frac{110934}{2353}\right) + \frac{1440495}{9412} + \frac{212625 \sqrt{3}}{2353} = 0` (spread :math:`\frac{1011192681}{33501282217} - \frac{382588416 \sqrt{3}}{33501282217}` relative to :g:`AB <[ A B ]>`).
* **Napoleon Line** :g:`{6, 17, 18} <{ 6, 17 }>` — collinear axis through :g:`X_6 <X_6>` (:ref:`Symmedian Point <X_6>`, :math:`\left(\frac{1673}{295},\; \frac{1176}{295}\right)`), :g:`X_17 <X_17>` (:ref:`1st NAPOLEON POINT <X_17>`, :math:`\left(\frac{192941}{29635} - \frac{8736 \sqrt{3}}{29635},\; \frac{189 \sqrt{3}}{29635} + \frac{23520}{5927}\right)`), :g:`X_18 <X_18>`, with exact Cartesian equation :math:`x \left(\frac{31752}{1748465} - \frac{189 \sqrt{3}}{29635}\right) + y \left(\frac{1467648}{1748465} - \frac{8736 \sqrt{3}}{29635}\right) - \frac{30153816}{8742325} + \frac{179487 \sqrt{3}}{148175} = 0` (spread :math:`\frac{81}{173137}` relative to :g:`AB <[ A B ]>`).

.. container:: note-item

   :ref:`X_18 <X_18>` lies on the Napoleon cubic.

.. collapse:: Full Incident Central Line Catalog
   :badge: 13 lines
   :class: line-catalog

   {:ref:`2 <X_2>`, :ref:`61 <X_61>`}, {:ref:`3 <X_3>`, :ref:`14 <X_14>`}, {:ref:`4 <X_4>`, :ref:`16 <X_16>`}, {:ref:`5 <X_5>`, :ref:`13 <X_13>`}, {:ref:`6 <X_6>`, :ref:`17 <X_17>`}, {:ref:`12 <X_12>`, :ref:`202 <X_202>`}, {:ref:`15 <X_15>`, :ref:`140 <X_140>`}, {:ref:`76 <X_76>`, :ref:`302 <X_302>`}, {:ref:`83 <X_83>`, :ref:`623 <X_623>`}, {:ref:`203 <X_203>`, :ref:`499 <X_499>`}, {:ref:`275 <X_275>`, :ref:`470 <X_470>`}, {:ref:`298 <X_298>`, :ref:`636 <X_636>`}, {:ref:`624 <X_624>`, :ref:`634 <X_634>`}

Functional Relations & Conjugates
---------------------------------

.. figure:: 04_relations.svg
   :alt: X_18 — Functional Relations and Conjugates
   :align: center

   **Conjugate & Homothetic Partners of X_18** on Heronian :math:`(15, 13, 14)`.

* **Isogonal Conjugate:** :g:`X_62 <X_62>` (:ref:`Isogonal Conjugate Of X_18 <X_62>`, homogeneous barycentrics :math:`-375 + 900 \sqrt{3} : -507 + 676 \sqrt{3} : -462 + 784 \sqrt{3}`) at :math:`\left(\frac{427679}{77617} - \frac{21952 \sqrt{3}}{77617},\; \frac{308112}{77617} - \frac{2289 \sqrt{3}}{77617}\right)`, joined along :g:`{18, 62} <{ 18, 62 }>` (:term:`isogonal conjugate <isogonal-conjugate>` via :math:`a^2 vw : b^2 wu : c^2 uv`).
* **Isotomic Conjugate:** :g:`X_303 <X_303>` (:ref:`ISOTOMIC CONJUGATE OF 2nd NAPOLEON POINT <X_303>`, homogeneous barycentrics :math:`-70 + 168 \sqrt{3} : -126 + 168 \sqrt{3} : -99 + 168 \sqrt{3}`) at :math:`\left(\frac{4159899}{675023} - \frac{196896 \sqrt{3}}{675023},\; \frac{2697732}{675023} - \frac{4032 \sqrt{3}}{675023}\right)`, joined along :g:`{18, 303} <{ 18, 303 }>` (:term:`isotomic conjugate <isotomic-conjugate>` via :math:`vw : wu : uv`).
* **Complement:** exact algebraic point at :math:`\left(\frac{185062}{29635} - \frac{4368 \sqrt{3}}{29635},\; \frac{189 \sqrt{3}}{59270} + \frac{23802}{5927}\right)` (homogeneous barycentrics :math:`4407 - 1460 \sqrt{3} : 4539 - 1684 \sqrt{3} : 4494 - 1576 \sqrt{3}`)  — :term:`complement <complement>` of :g:`X_18 <X_18>` dilated from :ref:`X_2 <X_2>` by factor :math:`-\frac{1}{2}`.
* **Anticomplement:** exact algebraic point at :math:`\left(\frac{177183}{29635} - \frac{17472 \sqrt{3}}{29635},\; \frac{378 \sqrt{3}}{29635} + \frac{24084}{5927}\right)` (homogeneous barycentrics :math:`1047 - 280 \sqrt{3} : 1179 - 504 \sqrt{3} : 1134 - 396 \sqrt{3}`)  — :term:`anticomplement <anticomplement>` of :g:`X_18 <X_18>` dilated from :ref:`X_2 <X_2>` by factor :math:`-2`.
* **Circumcircle Inverse:** Inversion in :g:`circumcircle <circumcircle>` centered at :g:`X_3 <X_3>` = :math:`\left(7, \frac{33}{8}\right)` (:math:`Q_R = \frac{4225}{64}`) maps :g:`X_18 <X_18>` along :g:`{3, 18} <{ 3, 18 }>` (:math:`Q(X_18, X_3) = \frac{29503775113}{56206926400} - \frac{1006633257 \sqrt{3}}{3512932900}`, scale :math:`Q_R / Q = \frac{130862323410000 \sqrt{3}}{202001430181} + \frac{239718172793125}{202001430181}`) to exact algebraic point at :math:`\left(- \frac{179801571733}{202001430181} + \frac{6618890460000 \sqrt{3}}{202001430181},\; - \frac{39238956894144}{202001430181} - \frac{22037470489125 \sqrt{3}}{202001430181}\right)` (homogeneous barycentrics :math:`5662407089625 \sqrt{3} + 18535451008500 : 9239865029044 + 9029239903125 \sqrt{3} : -26159304596096 - 14691646992750 \sqrt{3}`) .
* **Quadratic :math:`\sqrt{3}` Conjugate:** Conjugation :math:`\sqrt{3} \mapsto -\sqrt{3}` over :math:`\mathbb{Q}(\sqrt{3})` maps :g:`X_18 <X_18>` (outward/inward equilateral orientation reversal) directly to :g:`X_17 <X_17>` (:ref:`1st NAPOLEON POINT <X_17>`) at :math:`\left(\frac{192941}{29635} - \frac{8736 \sqrt{3}}{29635},\; \frac{189 \sqrt{3}}{29635} + \frac{23520}{5927}\right)`, joined along :g:`{17, 18} <{ 17, 18 }>`.

.. collapse:: Full Functional Relations Catalog
   :badge: 14 relations

   * :ref:`X_18 <X_18>` = reflection of :ref:`X_628 <X_628>` in :ref:`X_630 <X_630>`
   * :ref:`X_18 <X_18>` = :term:`isogonal conjugate <isogonal-conjugate>` of :ref:`X_62 <X_62>`
   * :ref:`X_18 <X_18>` = :term:`isotomic conjugate <isotomic-conjugate>` of :ref:`X_303 <X_303>`
   * :ref:`X_18 <X_18>` = :term:`complement <complement>` of :ref:`X_628 <X_628>`
   * :ref:`X_18 <X_18>` = :term:`anticomplement <anticomplement>` of :ref:`X_630 <X_630>`
   * :ref:`X_18 <X_18>` = circumcircle-inverse of X_32628
   * :ref:`X_18 <X_18>` = X_i-:term:`cross conjugate <cross-conjugate>` of X_j for these (i,j): (:ref:`15 <X_15>`, :ref:`13 <X_13>`), (:ref:`140 <X_140>`, :ref:`17 <X_17>`), (:ref:`398 <X_398>`, :ref:`4 <X_4>`)
   * :ref:`X_18 <X_18>` = polar conjugate of :ref:`X_472 <X_472>`
   * :ref:`X_18 <X_18>` = trilinear product of vertices of :term:`inner Napoleon triangle <inner-napoleon-triangle>`
   * :ref:`X_18 <X_18>` = Kosnita(:ref:`X_14 <X_14>`,\ :ref:`X_3 <X_3>`) point
   * :ref:`X_18 <X_18>` = Cundy-Parry Phi transform of :ref:`X_14 <X_14>`
   * :ref:`X_18 <X_18>` = Cundy-Parry Psi transform of :ref:`X_16 <X_16>`
   * :ref:`X_18 <X_18>` = :term:`trilinear pole <trilinear-pole>` of line :ref:`X_523 <X_523>`\ X_14447
   * :ref:`X_18 <X_18>` = :ref:`X_63 <X_63>`-:term:`isoconjugate <isoconjugate>` of X_10641

Four-Triangle Symbolic Invariance
---------------------------------

.. figure:: 05_four_triangles.svg
   :alt: X_18 — Invariance Across Four Canonical Symbolic Reference Triangles
   :align: center

   **Four-Triangle Invariance of X_18** across :g:`Heronian (15, 13, 14) <panel-heronian>`, :g:`Right (3, 4, 5) <panel-right>`, :g:`Kepler (1, √φ, φ) <panel-kepler>`, and :g:`Kimberling (6, 9, 13) <panel-kimberling>`.

Across the four canonical algebraic number fields — :g:`Heronian (15, 13, 14) <heronian-X_18>` over :math:`\mathbb{Q}(\sqrt{3})` (:math:`X_18 = \left(\frac{8736 \sqrt{3}}{29635} + \frac{192941}{29635},\; \frac{23520}{5927} - \frac{189 \sqrt{3}}{29635}\right)`), :g:`Right (3, 4, 5) <right-X_18>` over :math:`\mathbb{Q}(\sqrt{3})` (:math:`X_18 = \left(\frac{1336}{575} - \frac{42 \sqrt{3}}{115},\; \frac{402}{575} - \frac{24 \sqrt{3}}{115}\right)`), :g:`Kepler (1, √φ, φ) <kepler-X_18>` over :math:`\mathbb{Q}(\sqrt{\phi}, \sqrt{3})`, and :g:`Kimberling (6, 9, 13) <kimberling-X_18>` over :math:`\mathbb{Q}(\sqrt{3}, \sqrt{35})` (:math:`X_18 = \left(\frac{7740 \sqrt{105}}{5347} + \frac{1579094}{69511},\; - \frac{647 \sqrt{3}}{5347} + \frac{22924 \sqrt{35}}{69511}\right)`) — **X_18** lies strictly interior on Heronian, Right, Kepler while crossing outside :math:`\triangle ABC` on Kimberling (where signed sub-areas change sign across the sidelines while still summing algebraically to :math:`\Delta`).

.. admonition:: Related Collection 1 Topic Guides
   :class: tip

   :doc:`T_13: The Isogonic & Napoleon Central Lines <../../../topics/isogonic-and-napoleon-lines/index>` • :doc:`T_24: Equilateral, Isogonic & Napoleon Triangles <../../../topics/isogonic-and-napoleon-triangles/index>`

Notes
-----

.. container:: note-item

   :ref:`X_18 <X_18>` is the {:ref:`X_231 <X_231>`,\ :ref:`X_1209 <X_1209>`}-harmonic conjugate of :ref:`X_17 <X_17>`.

.. toctree::
   :hidden:

   code
