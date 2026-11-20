:order: 3758
:type: collection
:canonical_id: X_3758–X_3861
:subtitle: Central Triangle Combos Xcom(T) II: Parameterized T(f, g) & Euler Triangles

.. _c-03758-03861:

X_3758–X_3861
=============

.. rubric:: Central Triangle Combos Xcom(T) II: Parameterized T(f, g) & Euler Triangles

.. enunciation::

   :term:`Combo <combo>` centers X_k-com[T(f, g)] and X_k-com[Inverse(nT(f, g))] for parameterized :term:`central triangles <central-triangle>` (:ref:`X_3758 <X_3758>`\ –\ :ref:`X_3810 <X_3810>`), followed by combo centers on the 1st through 5th :term:`Euler triangles <euler-triangle>` (:ref:`X_3811 <X_3811>`\ –\ :ref:`X_3861 <X_3861>`).

.. figure:: c-03758-03861.svg
   :alt: X_3758–X_3861 — Central Triangle Combos Xcom(T) II: Parameterized T(f, g) & Euler Triangles
   :align: center

   **X_3758–X_3861** (*Central Triangle Combos Xcom(T) II: Parameterized T(f, g) & Euler Triangles*) — 16 representative centers (from 104 in collection) constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :g:`AB <[ A B ]>` = :math:`1`.

.. _preamble-0059:

.. admonition:: Group Preamble — Central Triangles and More Combos
   :class: note

   Many :term:`triangle centers <triangle-center>` can be defined (as just above) by the form Xcom(nT), where T denotes a central triangle. In order to present such centers, it is helpful to introduce the notation T(f(a,b,c), g(b,c,a)) for central triangles. Following :cite:`TCCT <tcct>`, pages 53-54, suppose that each of f(a,b,c) and g(a,b,c) is a center-function or the zero function, and that one of these three conditions holds:

   | the degree of homogeneity of g equals that of f;
   | f is the zero function and g is not the zero function;
   | g is the zero function and f is not the zero function.

   There are two cases to be considered: If :math:`g(a,b,c)=g(a`,c,b), then the central triangle T(f(a,b,c), g(b,c,a)) is defined by the following 3x3 matrix (whose rows give homogeneous coordinates for the A-, B-, C- vertices, respectively):

   | f(a,b,c) g(b,c,a) g(c,a,b)
   | g(a,b,c) f(b,c,a) g(c,a,b)
   | g(a,b,c) g(b,c,a) f(c,a,b)

   If g(a,b,c) is not equal to g(a,c,b), then the central triangle T(f(a,b,c),g(b,c,a)) is defined by the following 3x3 matrix:

   | f(a,b,c) g(b,c,a) g(c,b,a)
   | g(a,c,b) f(b,c,a) g(c,a,b)
   | g(a,b,c) g(b,a,c) f(c,a,b)

   If the homogenous coordinates are chosen to be barycentric, as they are for present purposes, then the new notation for central triangles is typified by these examples:

   | **Medial triangle** = T(1, 0)
   | **Anticomplementary triangle** = T(-1, 1)
   | **Incentral triangle** = T(a, 0)
   | **Excentral triangle** = T(-a, b)
   | **Euler triangle** = T(2(:math:`b^{4}` + :math:`c^{4}` - :math:`b^{2}`\ :math:`c^{2}` - :math:`c^{2}`\ :math:`a^{2}` - :math:`a^{2}`\ :math:`b^{2})`, (:math:`b^{2}` + :math:`c^{2}` - :math:`a^{2})`\ (:math:`a^{2}` + :math:`b^{2}` - :math:`c^{2})`)
   | **2nd Euler triangle** = :math:`T(2a^{2}(b^{4} + c^{4} - 2b^{2}c^{2} - c^{2}a^{2} - a^{2}b^{2})`, (:math:`a^{2}` - :math:`b^{2}` + :math:`c^{2})`\ (:math:`a^{4}` + :math:`b^{4}` + :math:`c^{4}` - :math:`2a^{2}`\ :math:`c^{2}` - :math:`2b^{2}`\ :math:`c^{2})`)
   | **3rd Euler triangle** = T((b - c)\ :sup:`2`, :math:`c^{2}` - :math:`a^{2}` - bc)
   | **4th Euler triangle** = T((b + c)\ :sup:`2`, :math:`c^{2}` - :math:`a^{2}` + bc)
   | **5th Euler triangle** = T(2(:math:`b^{2}` + :math:`c^{2})`, :math:`b^{2}` + :math:`c^{2}` - :math:`a^{2}` )

   The vertices of the five Euler triangles lie on the nine-point circle. (See :person:`C. Kimberling <clark-kimberling>`, "Twenty-one points on the nine-point circle," *Mathematical Gazette* 92 (2008) 29-38.) :person:`Randy Hutson <randy-hutson>` observes (January 8, 2015) that the **2nd Euler triangle** is the :term:`complement <complement>` of the circumorthic triangle, the **2nd Euler triangle** is the reflection of the :term:`orthic triangle <orthic-triangle>` in :ref:`X_5 <X_5>`; the **3rd Euler triangle** is the complement of the 1st circumperp triangle, the **4th Euler triangle** is the complement of the 2nd circumperp triangle; the **4th Euler triangle** the triangle whose sidelines are the radical axes of each of the Odehnal tritangent circles (defined at X_6176) and the corresponding excircle; the **5th Euler triangle** is the complement of the :term:`circummedial triangle <circummedial-triangle>`, and the vertices of the **5th Euler triangle** are the intersections, other than midpoints of the sides of :g:`ABC << A B C >>`, of the nine-point circle and the medians.

   The notation T(f(a,b,c),g(b,c,a)) can be used to define several more triangles; in each case, two of the perspectivities can be used to construct the triangle.

   T(bc, :math:`b^{2})` is perspective to :g:`ABC << A B C >>` with perspector :ref:`X_6 <X_6>`; other such pairs: incentral, :ref:`X_192 <X_192>`, excentral, :ref:`X_1045 <X_1045>`; tangential, :ref:`X_6 <X_6>`; anticomplementary, :ref:`X_192 <X_192>`

   T(-bc, :math:`b^{2})` is perspective to :g:`ABC << A B C >>` with perspector :ref:`X_6 <X_6>`; incentral, :ref:`X_2 <X_2>`; tangential, :ref:`X_6 <X_6>`; T(bc,\ :math:`b^{2})`, :ref:`X_6 <X_6>`

   T(bc, :math:`c^{2})` is perspective to :g:`ABC << A B C >>` with perspector :ref:`X_76 <X_76>`; anticomplementary, :ref:`X_8 <X_8>`; 4th Brocard, :ref:`X_76 <X_76>`, Fuhrmann, :ref:`X_8 <X_8>`; :term:`cevian <cevian>`(:ref:`X_350 <X_350>`),\ :ref:`X_1 <X_1>`

   T(-bc, :math:`c^{2})` is perspective to :g:`ABC << A B C >>` with perspector :ref:`X_76 <X_76>`; cevian(:ref:`X_321 <X_321>`),\ :ref:`X_75 <X_75>`; anticevian(:ref:`X_8 <X_8>`), :ref:`X_2 <X_2>`

   :math:`T(a^{2}`, :math:`a^{2}` - :math:`b^{2})` is perspective to the :term:`medial triangle <medial-triangle>` with perspector :ref:`X_3 <X_3>`; tangential , :ref:`X_3 <X_3>`; symmedial, :ref:`X_2 <X_2>`; cevian(:ref:`X_287 <X_287>`), :ref:`X_98 <X_98>`

   :math:`T(a^{2}`, :math:`a^{2}` - :math:`c^{2})` is perspective to the :term:`tangential triangle <tangential-triangle>` with perspector :ref:`X_25 <X_25>`; orthic , :ref:`X_25 <X_25>`; medial, :ref:`X_6 <X_6>`; 1st Lemoine, :ref:`X_1383 <X_1383>`; circummedial, :ref:`X_251 <X_251>`

   :math:`T(a^{2}`, :math:`a^{2}` + :math:`b^{2})` is perspective to :g:`ABC << A B C >>` with perspector :ref:`X_83 <X_83>`; medial, :ref:`X_6 <X_6>`; 1st Neuberg, :ref:`X_182 <X_182>`

   :math:`T(a^{2}`, :math:`a^{2}` + :math:`c^{2})` is perspective to :g:`ABC << A B C >>` with perspector :ref:`X_141 <X_141>`; medial, :ref:`X_3 <X_3>`; 1st Neuberg, :ref:`X_182 <X_182>`; :math:`T(a^{2}`,\ :math:`a^{2}` - :math:`c^{2})`, :ref:`X_2 <X_2>`; cevian(:ref:`X_69 <X_69>`), :ref:`X_6 <X_6>`; cevian(:ref:`X_76 <X_76>`), :ref:`X_2 <X_2>`; cevian(:ref:`X_3313 <X_3313>`),\ :ref:`X_39 <X_39>`

   The triangles :g:`IT_{1} <[ I T_1 ]>` and :g:`IT_{2} <[ I T_2 ]>` are triply perspective to :g:`ABC << A B C >>` (as are :g:`T_{1} <T_1>` and :g:`T_{3} <T_3>`). Order-label :g:`IT_{1} <[ I T_1 ]>` as :g:`A'B'C' << A' B' C' >>`. The three perspectivities are then given by

   | :g:`AA' <[ A A' ]>`\ ∩\ :g:`BB' <[ B B' ]>`\ ∩\ :g:`CC' <[ C C' ]>` = :ref:`X_3862 <X_3862>`
   | :g:`AB' <[ A B' ]>`\ ∩\ :g:`BC' <[ B C' ]>`\ ∩\ :g:`CA' <[ C A' ]>` =\ :math:`f(a,b,c) : f(b,c,a) : f(c,a,b)`, where :math:`f(a,b,c) = ab(a^{2} - bc)(c^{2} - ab)(b^{2} + bc + c^{2})`
   | :g:`AC' <[ A C' ]>`\ ∩\ :g:`BA' <[ B A' ]>`\ ∩\ :g:`CB' <[ C B' ]>` =\ :math:`f(a,c,b) : f(b,a,c) : f(c,b,a)`

   :person:`Peter Moses <peter-moses>` noted (12/23/2011) that T(bc, :math:`b^{2})` is *triply perspective* to :g:`ABC << A B C >>`. With T(bc, :math:`b^{2})` order-labeled as :g:`A'B'C' << A' B' C' >>`, the three perspectivities with perspectors are as follows:

   | :g:`AA' <[ A A' ]>`\ ∩\ :g:`BB' <[ B B' ]>`\ ∩\ :g:`CC' <[ C C' ]>` = :ref:`X_6 <X_6>`; :g:`AB' <[ A B' ]>`\ ∩\ :g:`BC' <[ B C' ]>`\ ∩\ :g:`CA' <[ C A' ]>` = P(6); :g:`AC' <[ A C' ]>`\ ∩\ :g:`BA' <[ B A' ]>`\ ∩\ :g:`CB' <[ C B' ]>` = U(6). (The notation P(k) and U(k) refers to a bicentric pair of points; see **Tables** at the top of ETC.)
   | Likewise, T(bc, :math:`c^{2})` is triply perspective to :g:`ABC << A B C >>`, with perspectors: :ref:`X_76 <X_76>`, P(10), and U(10).

   (This section was added to ETC on 12/23/2011.)

Member Centers
--------------

:ref:`Open Interactive 7-Triangle Constellation & Explorer ↗ <family-c-03758-03861>`

.. list-table::
   :class: etc-table etc-mode-relations
   :header-rows: 1
   :widths: 12 56 18 14

   * - Center
     - Name
     - Search (6,9,13)
     - Precision
   * - :ref:`X_3758 <X_3758>`
     - X\_3661com[T(bc, b²)]
     - ``1.815898``
     - Exact
   * - :ref:`X_3759 <X_3759>`
     - X\_3662com[T(-bc, b²)]
     - ``-1.098962``
     - Exact
   * - :ref:`X_3760 <X_3760>`
     - X\_2275com[T(-bc, c²)]
     - ``7.104264``
     - Exact
   * - :ref:`X_3761 <X_3761>`
     - X\_2276com[T(bc, c²)]
     - ``3.831615``
     - Exact
   * - :ref:`X_3762 <X_3762>`
     - X\_1491com[T(bc, c²)]
     - ``15.695722``
     - Exact
   * - :ref:`X_3763 <X_3763>`
     - X\_3618com[T(a², a² + c²)]
     - ``2.956661``
     - Exact
   * - :ref:`X_3764 <X_3764>`
     - X\_869com[T(bc, b²)]
     - ``1.557996``
     - Exact
   * - :ref:`X_3765 <X_3765>`
     - X\_869com[T(bc, c²)]
     - ``3.893916``
     - Exact
   * - :ref:`X_3766 <X_3766>`
     - X\_3250com[T(bc, c²)]
     - ``14.296344``
     - Exact
   * - :ref:`X_3767 <X_3767>`
     - X\_3053com[T(a², a² - c²)]
     - ``1.116358``
     - Exact
   * - :ref:`X_3768 <X_3768>`
     - X\_3250com[T(bc, b²)]
     - ``-5.539324``
     - Exact
   * - :ref:`X_3769 <X_3769>`
     - X\_3705com[T(-bc, b²)]
     - ``-3.223290``
     - Exact
   * - :ref:`X_3770 <X_3770>`
     - X\_3736com[T(bc, c²)]
     - ``3.854724``
     - Exact
   * - :ref:`X_3771 <X_3771>`
     - X\_1707com[T(a², a² - b²)]
     - ``4.065143``
     - Exact
   * - :ref:`X_3772 <X_3772>`
     - X\_1707com[T(a², a² - c²)]
     - ``0.982554``
     - Exact
   * - :ref:`X_3773 <X_3773>`
     - X\_141com[INVERSE(nT(bc, c²))]
     - ``3.976559``
     - Exact
   * - :ref:`X_3774 <X_3774>`
     - X\_39com[INVERSE(nT(bc, b²))]
     - ``1.217504``
     - Exact
   * - :ref:`X_3775 <X_3775>`
     - X\_594com[INVERSE(nT(bc, c²))]
     - ``3.285307``
     - Exact
   * - :ref:`X_3776 <X_3776>`
     - X\_3700com[INVERSE(nT(-bc, c²))]
     - ``-24.979004``
     - Exact
   * - :ref:`X_3777 <X_3777>`
     - X\_1577com[INVERSE(nT(-bc, c²))]
     - ``-10.705287``
     - Exact
   * - :ref:`X_3778 <X_3778>`
     - X\_1964com[INVERSE(nT(-bc, b²))]
     - ``1.804370``
     - Exact
   * - :ref:`X_3779 <X_3779>`
     - X\_3056com[T(-bc, b²)]
     - ``-1.024025``
     - Exact
   * - :ref:`X_3780 <X_3780>`
     - X\_3721com[T(-bc, b²)]
     - ``-0.346992``
     - Exact
   * - :ref:`X_3781 <X_3781>`
     - X\_9com[INVERSE(nT(bc, c²))]
     - ``5.352098``
     - Exact
   * - :ref:`X_3782 <X_3782>`
     - X\_2887com[T(-bc, c²)]
     - ``2.324757``
     - Exact
   * - :ref:`X_3783 <X_3783>`
     - X\_668com[T(bc, c²)]
     - ``-16.567030``
     - Exact
   * - :ref:`X_3784 <X_3784>`
     - X\_57com[INVERSE(nT(-bc, c²))]
     - ``4.627572``
     - Exact
   * - :ref:`X_3785 <X_3785>`
     - X\_2548com[INVERSE(nT(a², a² + b²))]
     - ``6.060448``
     - Exact
   * - :ref:`X_3786 <X_3786>`
     - X\_1654com[INVERSE(nT(bc, c²))]
     - ``3.900852``
     - Exact
   * - :ref:`X_3787 <X_3787>`
     - X\_1196com[INVERSE(nT(a², a² - c²))]
     - ``-1.427002``
     - Exact
   * - :ref:`X_3788 <X_3788>`
     - X\_3053com[T(a², a² - b²)]
     - ``3.385874``
     - Exact
   * - :ref:`X_3789 <X_3789>`
     - X\_3679com[INVERSE(nT(bc, c²))]
     - ``3.471599``
     - Exact
   * - :ref:`X_3790 <X_3790>`
     - X\_3662com[INVERSE(nT(bc, c²))]
     - ``5.121513``
     - Exact
   * - :ref:`X_3791 <X_3791>`
     - X\_2887com[T(-bc, b²)]
     - ``-1.694612``
     - Exact
   * - :ref:`X_3792 <X_3792>`
     - X\_190com[INVERSE(nT(bc, c²))]
     - ``-13.900044``
     - Exact
   * - :ref:`X_3793 <X_3793>`
     - X\_625com[INVERSE(nT(a², a² - c²))]
     - ``-9.153283``
     - Exact
   * - :ref:`X_3794 <X_3794>`
     - X\_2com[INVERSE(nT(-bc, c²))]
     - ``3.545674``
     - Exact
   * - :ref:`X_3795 <X_3795>`
     - X\_3097com[INVERSE(nT(bc, b²))]
     - ``0.792893``
     - Exact
   * - :ref:`X_3796 <X_3796>`
     - X\_2com[INVERSE(nT(a², a² + c²))]
     - ``12.263392``
     - Exact
   * - :ref:`X_3797 <X_3797>`
     - X\_2com[INVERSE(nT(bc, b²))]
     - ``25.452050``
     - Exact
   * - :ref:`X_3798 <X_3798>`
     - X\_3239com[INVERSE(nT(a², a² - c²))]
     - ``-13.334656``
     - Exact
   * - :ref:`X_3799 <X_3799>`
     - X\_2com[INVERSE(nT(bc, c²))]
     - ``4.681115``
     - Exact
   * - :ref:`X_3800 <X_3800>`
     - X\_512com[INVERSE(nT(a², a² + b²))]
     - —
     - Exact
   * - :ref:`X_3801 <X_3801>`
     - X\_2533com[INVERSE(nT(-bc, b²))]
     - ``-39.252720``
     - Exact
   * - :ref:`X_3802 <X_3802>`
     - X\_1909com[INVERSE(nT(bc, c²))]
     - ``2.597755``
     - Exact
   * - :ref:`X_3803 <X_3803>`
     - X\_905com[INVERSE(nT(a², a² + c²))]
     - ``14.407868``
     - Exact
   * - :ref:`X_3804 <X_3804>`
     - X\_647com[INVERSE(nT(a², a² + c²))]
     - ``8.493059``
     - Exact
   * - :ref:`X_3805 <X_3805>`
     - X\_2786com[INVERSE(nT(bc,c²))]
     - —
     - Exact
   * - :ref:`X_3806 <X_3806>`
     - X\_2525com[INVERSE(nT(a², a² + c²))]
     - ``-58.979576``
     - Exact
   * - :ref:`X_3807 <X_3807>`
     - X\_2525com[INVERSE(nT(bc, b²))]
     - ``6.681354``
     - Exact
   * - :ref:`X_3808 <X_3808>`
     - X\_2786com[INVERSE(nT(-bc, c²))]
     - —
     - Exact
   * - :ref:`X_3809 <X_3809>`
     - X\_2786com[INVERSE(nT(bc, b²))]
     - ``1.728844``
     - Exact
   * - :ref:`X_3810 <X_3810>`
     - X\_525com[INVERSE(nT(-bc, c²))]
     - —
     - Exact
   * - :ref:`X_3811 <X_3811>`
     - X\_3189com(EULER TRIANGLE)
     - ``-10.670072``
     - Exact
   * - :ref:`X_3812 <X_3812>`
     - X\_950com(4th EULER TRIANGLE)
     - ``2.104458``
     - Exact
   * - :ref:`X_3813 <X_3813>`
     - X\_2136com(4th EULER TRIANGLE)
     - ``6.733062``
     - Exact
   * - :ref:`X_3814 <X_3814>`
     - X\_2077com(EULER TRIANGLE)
     - ``5.231697``
     - Exact
   * - :ref:`X_3815 <X_3815>`
     - X\_574com(5th EULER TRIANGLE)
     - ``1.397672``
     - Exact
   * - :ref:`X_3816 <X_3816>`
     - X\_57com(3rd EULER TRIANGLE)
     - ``2.631482``
     - Exact
   * - :ref:`X_3817 <X_3817>`
     - X\_2com(3rd EULER TRIANGLE)
     - ``-0.295804``
     - Exact
   * - :ref:`X_3818 <X_3818>`
     - X\_1352com(EULER TRIANGLE)
     - ``-2.781892``
     - Exact
   * - :ref:`X_3819 <X_3819>`
     - X\_549com(2nd EULER TRIANGLE)
     - ``3.883740``
     - Exact
   * - :ref:`X_3820 <X_3820>`
     - X\_200com(4th EULER TRIANGLE)
     - ``3.426362``
     - Exact
   * - :ref:`X_3821 <X_3821>`
     - X\_3056com(4th EULER TRIANGLE)
     - ``2.569939``
     - Exact
   * - :ref:`X_3822 <X_3822>`
     - X\_2099com(3rd EULER TRIANGLE)
     - ``2.052751``
     - Exact
   * - :ref:`X_3823 <X_3823>`
     - X\_3717com(4th EULER TRIANGLE)
     - ``4.446577``
     - Exact
   * - :ref:`X_3824 <X_3824>`
     - X\_3671com(3rd EULER TRIANGLE)
     - ``2.075960``
     - Exact
   * - :ref:`X_3825 <X_3825>`
     - X\_56com(3rd EULER TRIANGLE)
     - ``2.938288``
     - Exact
   * - :ref:`X_3826 <X_3826>`
     - X\_3243com(3rd EULER TRIANGLE)
     - ``2.628483``
     - Exact
   * - :ref:`X_3827 <X_3827>`
     - X\_518com(2nd EULER TRIANGLE)
     - —
     - Exact
   * - :ref:`X_3828 <X_3828>`
     - X\_210com(4th EULER TRIANGLE)
     - ``2.864134``
     - Exact
   * - :ref:`X_3829 <X_3829>`
     - X\_3158com(3rd EULER TRIANGLE)
     - ``2.612935``
     - Exact
   * - :ref:`X_3830 <X_3830>`
     - X\_3543com(EULER TRIANGLE)
     - ``-9.829614``
     - Exact
   * - :ref:`X_3831 <X_3831>`
     - X\_3702com(4th EULER TRIANGLE)
     - ``3.384523``
     - Exact
   * - :ref:`X_3832 <X_3832>`
     - X\_3090com(EULER TRIANGLE)
     - ``-2.116910``
     - Exact
   * - :ref:`X_3833 <X_3833>`
     - X\_3058com(4th EULER TRIANGLE)
     - ``2.201173``
     - Exact
   * - :ref:`X_3834 <X_3834>`
     - X\_1266com(3rd EULER TRIANGLE)
     - ``7.141934``
     - Exact
   * - :ref:`X_3835 <X_3835>`
     - X\_693com(3rd EULER TRIANGLE)
     - ``-2.817181``
     - Exact
   * - :ref:`X_3836 <X_3836>`
     - X\_3685com(4th EULER TRIANGLE)
     - ``5.794256``
     - Exact
   * - :ref:`X_3837 <X_3837>`
     - X\_2254com(3rd EULER TRIANGLE)
     - ``7.203934``
     - Exact
   * - :ref:`X_3838 <X_3838>`
     - X\_226com(3rd EULER TRIANGLE)
     - ``1.816461``
     - Exact
   * - :ref:`X_3839 <X_3839>`
     - X\_3545com(EULER TRIANGLE)
     - ``-2.907957``
     - Exact
   * - :ref:`X_3840 <X_3840>`
     - X\_3210com(3rd EULER TRIANGLE)
     - ``3.815443``
     - Exact
   * - :ref:`X_3841 <X_3841>`
     - X\_3210com(4th EULER TRIANGLE)
     - ``2.522314``
     - Exact
   * - :ref:`X_3842 <X_3842>`
     - X\_3688com(4th EULER TRIANGLE)
     - ``2.594861``
     - Exact
   * - :ref:`X_3843 <X_3843>`
     - X\_3091com(EULER TRIANGLE)
     - ``-3.184823``
     - Exact
   * - :ref:`X_3844 <X_3844>`
     - X\_2321com(4th EULER TRIANGLE)
     - ``3.273249``
     - Exact
   * - :ref:`X_3845 <X_3845>`
     - X\_381com(EULER TRIANGLE)
     - ``-3.600122``
     - Exact
   * - :ref:`X_3846 <X_3846>`
     - X\_1999com(3rd EULER TRIANGLE)
     - ``3.254144``
     - Exact
   * - :ref:`X_3847 <X_3847>`
     - X\_1420com(3rd EULER TRIANGLE)
     - ``3.351348``
     - Exact
   * - :ref:`X_3848 <X_3848>`
     - X\_553com(3rd EULER TRIANGLE)
     - ``2.297889``
     - Exact
   * - :ref:`X_3849 <X_3849>`
     - X\_524com(5th EULER TRIANGLE)
     - —
     - Exact
   * - :ref:`X_3850 <X_3850>`
     - X\_140com(EULER TRIANGLE)
     - ``-1.004501``
     - Exact
   * - :ref:`X_3851 <X_3851>`
     - X\_3523com(EULER TRIANGLE)
     - ``-0.337056``
     - Exact
   * - :ref:`X_3852 <X_3852>`
     - X\_732com(2nd EULER TRIANGLE)
     - —
     - Exact
   * - :ref:`X_3853 <X_3853>`
     - X\_3627com(EULER TRIANGLE)
     - ``-8.791365``
     - Exact
   * - :ref:`X_3854 <X_3854>`
     - X\_3533com(EULER TRIANGLE)
     - ``-1.279332``
     - Exact
   * - :ref:`X_3855 <X_3855>`
     - X\_3525com(EULER TRIANGLE)
     - ``-1.146080``
     - Exact
   * - :ref:`X_3856 <X_3856>`
     - X\_3628com(EULER TRIANGLE)
     - ``-1.783187``
     - Exact
   * - :ref:`X_3857 <X_3857>`
     - X\_3526com(EULER TRIANGLE)
     - ``-1.226983``
     - Exact
   * - :ref:`X_3858 <X_3858>`
     - X\_1656com(EULER TRIANGLE)
     - ``-1.938925``
     - Exact
   * - :ref:`X_3859 <X_3859>`
     - X\_632com(EULER TRIANGLE)
     - ``-1.315976``
     - Exact
   * - :ref:`X_3860 <X_3860>`
     - X\_547com(EULER TRIANGLE)
     - ``-2.042750``
     - Exact
   * - :ref:`X_3861 <X_3861>`
     - X\_546com(EULER TRIANGLE)
     - ``-4.119247``
     - Exact
