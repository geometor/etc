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

.. collection::
   :sort: order
