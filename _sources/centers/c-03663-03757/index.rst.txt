:order: 3663
:type: collection
:canonical_id: X_3663–X_3757
:subtitle: Central Triangle Combos Xcom(T) I: Intouch, Extouch, Incentral & Hexyl Triangles

.. _c-03663-03757:

X_3663–X_3757
=============

.. rubric:: Central Triangle Combos Xcom(T) I: Intouch, Extouch, Incentral & Hexyl Triangles

.. enunciation::

   :term:`Combo <combo>` centers X_k-com(T) evaluated on the intouch (:ref:`X_3663 <X_3663>`\ –\ :ref:`X_3677 <X_3677>`), extouch (:ref:`X_3678 <X_3678>`\ –\ :ref:`X_3719 <X_3719>`), incentral (:ref:`X_3720 <X_3720>`\ –\ :ref:`X_3728 <X_3728>`), excentral, tangential, 1st Brocard, and :term:`hexyl triangles <hexyl-triangle>` (:ref:`X_3729 <X_3729>`\ –\ :ref:`X_3738 <X_3738>`), plus matrix-product combos n(incentral)*n(medial) and inverse-triangle combos (:ref:`X_3739 <X_3739>`\ –\ :ref:`X_3757 <X_3757>`).

.. figure:: c-03663-03757.svg
   :alt: X_3663–X_3757 — Central Triangle Combos Xcom(T) I: Intouch, Extouch, Incentral & Hexyl Triangles
   :align: center

   **X_3663–X_3757** (*Central Triangle Combos Xcom(T) I: Intouch, Extouch, Incentral & Hexyl Triangles*) — 16 representative centers (from 95 in collection) constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :g:`AB <[ A B ]>` = :math:`1`.

.. _preamble-0057:

.. admonition:: Group Preamble — Combos Using Central Triangles (Central Triangles and More Combos)
   :class: note

   The discussion of combos near the beginning of ETC is continued here. Suppose that T is a :term:`central triangle <central-triangle>`, and let nT its normalization, so that the triangle nT is essentially a 3x3 matrix with row sums equal to 1, and the rows of nT are normalized barycentrics for the A-, B-, C- vertices of :g:`T <T>`.

   Let :g:`X <X>` be a :term:`triangle center <triangle-center>`, given by barycentrics :math:`x : y : z`, not necessarily normalized. The point whose rows are the matrix product :g:`X* <X*>`\ (nT) is then a triangle center, denoted by Xcom(T).

   Among central triangles :g:`T <T>` are :term:`cevian <cevian>` and :term:`anticevian triangles <anticevian-triangle>` and others described at MathWorld. A brief list follows, with A-vertices given in barycentrics (not normalized):

   | :term:`Intouch triangle <intouch-triangle>` = :term:`cevian triangle <cevian-triangle>` of :ref:`X_7 <X_7>`
   | :g:`A <A>`-vertex = 0 : 1/(c + a - b) : 1/(a + b - c)

   | :term:`Extouch triangle <extouch-triangle>` = cevian triangle of :ref:`X_8 <X_8>`
   | :g:`A <A>`-vertex = 0 : c + a - b : a + b - c

   | :term:`Incentral triangle <incentral-triangle>` = cevian triangle of :ref:`X_1 <X_1>`
   | :g:`A <A>`-vertex =\ :math:`0 : b : c`

   | :term:`Excentral triangle <excentral-triangle>` = anticevian triangle of :ref:`X_1 <X_1>`
   | :g:`A <A>`-vertex = :math:`-a : b : c`

   | Hexyl triangle
   | :g:`A <A>`-vertex =\ :math:`a(1 + a_{1} + b_{1} + c_{1}) : b(-1 + a_{1} + b_{1} - c_{1}) : c(1 + a_{1} - b_{1} + c_{1})`, where :math:`a_{1}` = cos A, :math:`b_{1}` = cos B, :math:`c_{1}` = cos C

   | :term:`Tangential triangle <tangential-triangle>` = anticevian triangle of :ref:`X_6 <X_6>`
   | :g:`A <A>`-vertex = :math:`-a^{2} : b^{2} : c^{2}`

   | :term:`1st Brocard triangle <1st-brocard-triangle>`
   | :g:`A <A>`-vertex =\ :math:`a^{2} : c^{2} : b^{2}`

.. _preamble-0058:

.. admonition:: Group Preamble — More Combos (More Combos. Continuing the discussion of points Xcom(T))
   :class: note

   Continuing the discussion of points Xcom(T), suppose that T is an arbitrary triangle, and let nT denote the normalization of T. Let NT denote the set of these triangles, as matrices, and let \* denote matrix multiplication. Then NT is closed under \*. Also, NT is closed under matrix inversion. Consequently, (NT, \*) is a group, comparable to the group of stochastic matrices.

   Suppose that :g:`T_{1} <T_1>` and :g:`T_{2} <T_2>` are triangles. In many cases, the product :g:`T_{1} <T_1>`\ \*\ :g:`T_{2} <T_2>` is well-defined (e.g., :cite:`TCCT <tcct>`, page 175). However, n(:g:`T_{1} <T_1>`\ \*\ :g:`T_{2} <T_2>`) may not be n(:g:`T_{1} <T_1>`)\*n(:g:`T_{2} <T_2>`) if :g:`T_{1} <T_1>` and :g:`T_{2} <T_2>` are not normalized. Therefore, it is important, when dealing with products, to include the "n" if it is intended.

   As a class of examples of triangles defined by matrix products, suppose that :g:`T_{1} <T_1>` is the cevian triangle of a triangle center :math:`f : g : h` (barycentrics) and that :g:`T_{2} <T_2>` is the cevian triangle of a triangle center :math:`u : v : w`. The :g:`A <A>`-vertex of the triangle :g:`T_{3} <T_3>` = (:math:`nT_{1})`\ \*(:math:`nT_{2})` is given by

   :math:`u(gu + hu + gv +hw) : hv(u + w) : gw(u + v)`,

   from which it can be shown that :g:`T_{3} <T_3>` is perspective to the triangle :g:`ABC << A B C >>`, with perspector

   :g:`P <P>` =\ :math:`ghu(v + w) : hfv(w + u) : fgw(u + v)`.

   Also, :g:`T_{3} <T_3>` is perspective to :g:`T_{2} <T_2>`, with perspector

   :g:`Q <Q>` = u(v + w)(gu + hu + gv + hw) : v(w + u)(hv + fv + hw + fu) : w(u + v)(fw + gw + fu + gv).

   Thus, :g:`T_{3} <T_3>` can be constructed directly from the pairs {P, :g:`ABC << A B C >>`} and {Q, :g:`T_{2} <T_2>`}. Regarding the possibility that :g:`T_{3} <T_3>` is also perspective to :g:`T_{1} <T_1>`, the concurrence determinant for this condition factors as :g:`F_{1}F_{2}F_{3} << F_1 F_2 F_3 >>`, where

   | :g:`F_{1} <F_1>` = u + v + w,
   | :g:`F_{2} <F_2>` = fu(g + h) + gv(h + f) + hw(f + g),
   | :g:`F_{3} <F_3>` = (fghuvw)\ :sup:`2`\ [(gu)\ :sup:`-2` - (hu)\ :sup:`-2` + (hv)\ :sup:`-2` - (fv)\ :sup:`-2` + (fw)\ :sup:`-2` - (gw)\ :sup:`-2`].

   Consequently, the perspectivity holds if and only if one of the three factors is 0, and from this result, various geometric results can be obtained.

   **Example:** The Incentral and :term:`Medial triangles <medial-triangle>` result by taking :math:`f : g : h` =\ :math:`a : b : c` and :math:`u : v : w` =\ :math:`1 : 1: 1`. The product n(Incentral)\*n(Medial) has vertices

   :g:`A' <A'>` = b +\ :math:`c : c : b` :g:`B' <B'>` = c : c + a : a :g:`C' <C'>` =\ :math:`b : a : a` + b

   and its inverse has :g:`A <A>`-vertex :g:`A″ <A″>` = bc + ca + ab : -bc - ca + ab : -bc + ca - ab, from which :g:`B″ <B″>` and :g:`C″ <C″>` are obtained cyclically.

   The product n(Medial)\*n(Incentral) has :g:`A <A>`-vertex :math:`a(2a + b + c) : b(c + a) : c(a + b)`, and the inverse of this product has :g:`A <A>`-vertex (a + b + c)(b + c) : -c(a + c) : -b(a + b).

   Having considered the group NT of normalized triangles, we turn next to 3-point combos based on product triangles and inverse triangles. Recall that such a combo, denoted by Xcom(T), is defined, as in the preamble to :ref:`X_3663 <X_3663>`, by the matrix product (x y z)\*(nT), where nT is the normalization of :g:`T <T>`.

Member Centers
--------------

:ref:`Open Interactive 7-Triangle Constellation & Explorer ↗ <family-c-03663-03757>`

.. list-table::
   :class: etc-table etc-mode-relations
   :header-rows: 1
   :widths: 12 56 18 14

   * - Center
     - Name
     - Search (6,9,13)
     - Precision
   * - :ref:`X_3663 <X_3663>`
     - X\_6com(INTOUCH TRIANGLE)
     - ``2.040979``
     - Exact
   * - :ref:`X_3664 <X_3664>`
     - X\_37com(INTOUCH TRIANGLE)
     - ``1.488920``
     - Exact
   * - :ref:`X_3665 <X_3665>`
     - X\_41com(INTOUCH TRIANGLE)
     - ``1.302527``
     - Exact
   * - :ref:`X_3666 <X_3666>`
     - X\_42com(INTOUCH TRIANGLE)
     - ``1.857741``
     - Exact
   * - :ref:`X_3667 <X_3667>`
     - X\_513com(INTOUCH TRIANGLE)
     - —
     - Exact
   * - :ref:`X_3668 <X_3668>`
     - X\_219com(INTOUCH TRIANGLE)
     - ``0.168379``
     - Exact
   * - :ref:`X_3669 <X_3669>`
     - X\_663com(INTOUCH TRIANGLE)
     - ``0.804909``
     - Exact
   * - :ref:`X_3670 <X_3670>`
     - X\_3293com(INTOUCH TRIANGLE)
     - ``2.160978``
     - Exact
   * - :ref:`X_3671 <X_3671>`
     - X\_958com(INTOUCH TRIANGLE)
     - ``0.792557``
     - Exact
   * - :ref:`X_3672 <X_3672>`
     - X\_1449com(INTOUCH TRIANGLE)
     - ``1.838231``
     - Exact
   * - :ref:`X_3673 <X_3673>`
     - X\_3501com(INTOUCH TRIANGLE)
     - ``1.857534``
     - Exact
   * - :ref:`X_3674 <X_3674>`
     - X\_2329com(INTOUCH TRIANGLE)
     - ``0.865978``
     - Exact
   * - :ref:`X_3675 <X_3675>`
     - X\_1026com(INTOUCH TRIANGLE)
     - ``5.196352``
     - Exact
   * - :ref:`X_3676 <X_3676>`
     - X\_650com(INTOUCH TRIANGLE)
     - ``1.878121``
     - Exact
   * - :ref:`X_3677 <X_3677>`
     - X\_2999com(INTOUCH TRIANGLE)
     - ``1.931210``
     - Exact
   * - :ref:`X_3678 <X_3678>`
     - X\_5com(EXTOUCH TRIANGLE)
     - ``4.383485``
     - Exact
   * - :ref:`X_3679 <X_3679>`
     - X\_3576com(EXTOUCH TRIANGLE)
     - ``3.568429``
     - Exact
   * - :ref:`X_3680 <X_3680>`
     - X\_2136com(EXTOUCH TRIANGLE)
     - ``16.226962``
     - Exact
   * - :ref:`X_3681 <X_3681>`
     - X\_1699com(EXTOUCH TRIANGLE)
     - ``5.281211``
     - Exact
   * - :ref:`X_3682 <X_3682>`
     - X\_1715com(EXTOUCH TRIANGLE)
     - ``4.283732``
     - Exact
   * - :ref:`X_3683 <X_3683>`
     - X\_3219com(EXTOUCH TRIANGLE)
     - ``3.361198``
     - Exact
   * - :ref:`X_3684 <X_3684>`
     - X\_3509com(EXTOUCH TRIANGLE)
     - ``13.582355``
     - Exact
   * - :ref:`X_3685 <X_3685>`
     - X\_1757com(EXTOUCH TRIANGLE)
     - ``9.867747``
     - Exact
   * - :ref:`X_3686 <X_3686>`
     - X\_37com(EXTOUCH TRIANGLE)
     - ``4.308363``
     - Exact
   * - :ref:`X_3687 <X_3687>`
     - X\_171com(EXTOUCH TRIANGLE)
     - ``4.593379``
     - Exact
   * - :ref:`X_3688 <X_3688>`
     - X\_75com(EXTOUCH TRIANGLE)
     - ``3.249143``
     - Exact
   * - :ref:`X_3689 <X_3689>`
     - X\_3218com(EXTOUCH TRIANGLE)
     - ``9.911757``
     - Exact
   * - :ref:`X_3690 <X_3690>`
     - X\_1746com(EXTOUCH TRIANGLE)
     - ``5.469763``
     - Exact
   * - :ref:`X_3691 <X_3691>`
     - X\_3294com(EXTOUCH TRIANGLE)
     - ``3.825803``
     - Exact
   * - :ref:`X_3692 <X_3692>`
     - X\_1723com(EXTOUCH TRIANGLE)
     - ``5.925165``
     - Exact
   * - :ref:`X_3693 <X_3693>`
     - X\_672com(EXTOUCH TRIANGLE)
     - ``7.229488``
     - Exact
   * - :ref:`X_3694 <X_3694>`
     - X\_579com(EXTOUCH TRIANGLE)
     - ``5.538320``
     - Exact
   * - :ref:`X_3695 <X_3695>`
     - X\_580com(EXTOUCH TRIANGLE)
     - ``5.979351``
     - Exact
   * - :ref:`X_3696 <X_3696>`
     - X\_991com(EXTOUCH TRIANGLE)
     - ``4.106974``
     - Exact
   * - :ref:`X_3697 <X_3697>`
     - X\_631com(EXTOUCH TRIANGLE)
     - ``3.612733``
     - Exact
   * - :ref:`X_3698 <X_3698>`
     - X\_3522com(EXTOUCH TRIANGLE)
     - ``2.585064``
     - Exact
   * - :ref:`X_3699 <X_3699>`
     - X\_1054com(EXTOUCH TRIANGLE)
     - ``9.744131``
     - Exact
   * - :ref:`X_3700 <X_3700>`
     - X\_661com(EXTOUCH TRIANGLE)
     - ``66.109844``
     - Exact
   * - :ref:`X_3701 <X_3701>`
     - X\_3216com(EXTOUCH TRIANGLE)
     - ``5.637647``
     - Exact
   * - :ref:`X_3702 <X_3702>`
     - X\_3293com(EXTOUCH TRIANGLE)
     - ``5.179316``
     - Exact
   * - :ref:`X_3703 <X_3703>`
     - X\_31com(EXTOUCH TRIANGLE)
     - ``5.021073``
     - Exact
   * - :ref:`X_3704 <X_3704>`
     - X\_58com(EXTOUCH TRIANGLE)
     - ``4.927282``
     - Exact
   * - :ref:`X_3705 <X_3705>`
     - X\_3550com(EXTOUCH TRIANGLE)
     - ``4.763306``
     - Exact
   * - :ref:`X_3706 <X_3706>`
     - X\_42com(EXTOUCH TRIANGLE)
     - ``4.746481``
     - Exact
   * - :ref:`X_3707 <X_3707>`
     - X\_45com(EXTOUCH TRIANGLE)
     - ``4.088483``
     - Exact
   * - :ref:`X_3708 <X_3708>`
     - X\_150com(EXTOUCH TRIANGLE)
     - ``2.770012``
     - Exact
   * - :ref:`X_3709 <X_3709>`
     - X\_798com(EXTOUCH TRIANGLE)
     - ``-9.558050``
     - Exact
   * - :ref:`X_3710 <X_3710>`
     - X\_1724com(EXTOUCH TRIANGLE)
     - ``6.105081``
     - Exact
   * - :ref:`X_3711 <X_3711>`
     - X\_3306com(EXTOUCH TRIANGLE)
     - ``4.294897``
     - Exact
   * - :ref:`X_3712 <X_3712>`
     - X\_896com(EXTOUCH TRIANGLE)
     - ``7.921483``
     - Exact
   * - :ref:`X_3713 <X_3713>`
     - X\_2285com(EXTOUCH TRIANGLE)
     - ``4.826207``
     - Exact
   * - :ref:`X_3714 <X_3714>`
     - X\_386com(EXTOUCH TRIANGLE)
     - ``4.786772``
     - Exact
   * - :ref:`X_3715 <X_3715>`
     - X\_3305com(EXTOUCH TRIANGLE)
     - ``3.731071``
     - Exact
   * - :ref:`X_3716 <X_3716>`
     - X\_659com(EXTOUCH TRIANGLE)
     - ``8.693015``
     - Exact
   * - :ref:`X_3717 <X_3717>`
     - X\_238com(EXTOUCH TRIANGLE)
     - ``7.187618``
     - Exact
   * - :ref:`X_3718 <X_3718>`
     - X\_1716com(EXTOUCH TRIANGLE)
     - ``6.426604``
     - Exact
   * - :ref:`X_3719 <X_3719>`
     - X\_1711com(EXTOUCH TRIANGLE)
     - ``5.927535``
     - Exact
   * - :ref:`X_3720 <X_3720>`
     - X\_756com(INCENTRAL TRIANGLE)
     - ``1.908161``
     - Exact
   * - :ref:`X_3721 <X_3721>`
     - X\_213com(INCENTRAL TRIANGLE)
     - ``2.685977``
     - Exact
   * - :ref:`X_3722 <X_3722>`
     - X\_3120com(INCENTRAL TRIANGLE)
     - ``1.935868``
     - Exact
   * - :ref:`X_3723 <X_3723>`
     - X\_1213com(INCENTRAL TRIANGLE)
     - ``1.786851``
     - Exact
   * - :ref:`X_3724 <X_3724>`
     - X\_908com(INCENTRAL TRIANGLE)
     - ``-1.518064``
     - Exact
   * - :ref:`X_3725 <X_3725>`
     - X\_312com(INCENTRAL TRIANGLE)
     - ``0.827439``
     - Exact
   * - :ref:`X_3726 <X_3726>`
     - X\_2238com(INCENTRAL TRIANGLE)
     - ``5.882263``
     - Exact
   * - :ref:`X_3727 <X_3727>`
     - X\_2295com(INCENTRAL TRIANGLE)
     - ``2.255233``
     - Exact
   * - :ref:`X_3728 <X_3728>`
     - X\_192com(INCENTRAL TRIANGLE)
     - ``2.717070``
     - Exact
   * - :ref:`X_3729 <X_3729>`
     - X\_3056com(EXCENTRAL TRIANGLE)
     - ``3.806149``
     - Exact
   * - :ref:`X_3730 <X_3730>`
     - X\_1212com(EXCENTRAL TRIANGLE)
     - ``4.952017``
     - Exact
   * - :ref:`X_3731 <X_3731>`
     - X\_391com(EXCENTRAL TRIANGLE)
     - ``2.350760``
     - Exact
   * - :ref:`X_3732 <X_3732>`
     - X\_3022com(EXCENTRAL TRIANGLE)
     - ``1.907399``
     - Exact
   * - :ref:`X_3733 <X_3733>`
     - X\_656com(TANGENTIAL TRIANGLE)
     - ``4.915693``
     - Exact
   * - :ref:`X_3734 <X_3734>`
     - X\_6com(1st BROCARD TRIANGLE)
     - ``2.765215``
     - Exact
   * - :ref:`X_3735 <X_3735>`
     - X\_75com(1st BROCARD TRIANGLE)
     - ``2.411159``
     - Exact
   * - :ref:`X_3736 <X_3736>`
     - X\_2092com(HEXYL TRIANGLE)
     - ``1.268787``
     - Exact
   * - :ref:`X_3737 <X_3737>`
     - X\_656com(HEXYL TRIANGLE)
     - ``-13.108515``
     - Exact
   * - :ref:`X_3738 <X_3738>`
     - X\_2804com(HEXYL TRIANGLE)
     - —
     - Exact
   * - :ref:`X_3739 <X_3739>`
     - X\_37com[n(INCENTRAL)\*n(MEDIAL)]
     - ``2.898642``
     - Exact
   * - :ref:`X_3740 <X_3740>`
     - X\_210com[n(INCENTRAL)\*n(MEDIAL)]
     - ``3.292329``
     - Exact
   * - :ref:`X_3741 <X_3741>`
     - X\_321com[n(INCENTRAL)\*n(MEDIAL)]
     - ``3.302111``
     - Exact
   * - :ref:`X_3742 <X_3742>`
     - X\_3175com[n(INCENTRAL)\*n(MEDIAL)]
     - ``1.966408``
     - Exact
   * - :ref:`X_3743 <X_3743>`
     - X\_10com[n(MEDIAL)\*n(INCENTRAL)]
     - ``1.977958``
     - Exact
   * - :ref:`X_3744 <X_3744>`
     - X\_31com[n(MEDIAL)\*n(INCENTRAL)]
     - ``1.431006``
     - Exact
   * - :ref:`X_3745 <X_3745>`
     - X\_81com[n(MEDIAL)\*n(INCENTRAL)]
     - ``1.609754``
     - Exact
   * - :ref:`X_3746 <X_3746>`
     - X\_191com[n(MEDIAL)\*n(INCENTRAL)]
     - ``2.361973``
     - Exact
   * - :ref:`X_3747 <X_3747>`
     - X\_239com[n(MEDIAL)\*n(INCENTRAL)]
     - ``-2.181291``
     - Exact
   * - :ref:`X_3748 <X_3748>`
     - X\_1621com[n(MEDIAL)\*n(INCENTRAL)]
     - ``1.903031``
     - Exact
   * - :ref:`X_3749 <X_3749>`
     - X\_1707com[n(MEDIAL)\*n(INCENTRAL)]
     - ``0.975634``
     - Exact
   * - :ref:`X_3750 <X_3750>`
     - X\_846com[n(MEDIAL)\*n(INCENTRAL)]
     - ``1.877689``
     - Exact
   * - :ref:`X_3751 <X_3751>`
     - X\_1721com[INVERSE(n(HEXYL TRIANGLE))]
     - ``0.295508``
     - Exact
   * - :ref:`X_3752 <X_3752>`
     - X\_995com[INVERSE(n(HEXYL TRIANGLE))]
     - ``1.268956``
     - Exact
   * - :ref:`X_3753 <X_3753>`
     - X\_2com[INVERSE(n(HEXYL TRIANGLE))]
     - ``2.242508``
     - Exact
   * - :ref:`X_3754 <X_3754>`
     - X\_5com[INVERSE(n(HEXYL TRIANGLE))]
     - ``1.814313``
     - Exact
   * - :ref:`X_3755 <X_3755>`
     - X\_6com[INVERSE(n(HEXYL TRIANGLE))]
     - ``1.343579``
     - Exact
   * - :ref:`X_3756 <X_3756>`
     - X\_106com[INVERSE(n(HEXYL TRIANGLE))]
     - ``-0.928013``
     - Exact
   * - :ref:`X_3757 <X_3757>`
     - X\_846com[INVERSE(n(1st BROCARD TRIANGLE))]
     - ``3.494134``
     - Exact
