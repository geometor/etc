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

.. collection::
   :sort: order
