:order: 3310
:type: collection
:canonical_id: X_3310–X_3414
:subtitle: Incircle Transforms T(U), Trigonometric Offset Points & Kiepert Cusps

.. _c-03310-03414:

X_3310–X_3414
=============

.. rubric:: Incircle Transforms T(U), Trigonometric Offset Points & Kiepert Cusps

.. enunciation::

   Barycentric products of perpendicular directions (:ref:`X_3310 <X_3310>`), incircle transforms T(U) lying on the incircle (:ref:`X_3318 <X_3318>`\ –\ :ref:`X_3328 <X_3328>`), Darboux-cubic reflections and conjugates (:ref:`X_3341 <X_3341>`\ –\ :ref:`X_3358 <X_3358>`), trigonometric phase-shifted centers cos/sin/sec/csc/tan/cot(A ± θ) (:ref:`X_3364 <X_3364>`\ –\ :ref:`X_3409 <X_3409>`), and the Brocard-Kiepert-Fermat cusps (:ref:`X_3411 <X_3411>`\ –\ :ref:`X_3414 <X_3414>`).

.. figure:: c-03310-03414.svg
   :alt: X_3310–X_3414 — Incircle Transforms T(U), Trigonometric Offset Points & Kiepert Cusps
   :align: center

   **X_3310–X_3414** (*Incircle Transforms T(U), Trigonometric Offset Points & Kiepert Cusps*) — 16 representative centers (from 105 in collection) constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :g:`AB <[ A B ]>` = :math:`1`.

.. _preamble-0051:

.. admonition:: Group Preamble — Barycentric Products of Perpendicular Directions
   :class: note

   Suppose P and U are points on the line at infinity, given in barycentric coordinates by :g:`P <P>` =\ :math:`p : q : r` and :g:`U <U>` =\ :math:`u : v : w`. We call P and U *perpendicular directions* if for every point X not in the line at infinity, the lines XP and XU are perpendicular. (It is well known that if P and U are an antipodal pair on the circumcircle, then their :term:`isogonal conjugates <isogonal-conjugate>` are perpendicular directions.)

   Theorem: If P and U are perpendicular directions, then their barycentric product lies on the orthic axis.

   An outline of a proof follows. For given P on the line at infinity, the direction perpendicular to :g:`P <P>` is given by

   | a/:math:`d_{1}` : b/:math:`d_{2}` : c/:math:`d_{3}`,
   | where

   | :math:`d_{1}` = :math:`a^{2}`\ qr cos B cos C - :math:`p(b_{2}`\ r + :math:`c_{2}`\ q) cos A
   | :math:`d_{2}` = :math:`b^{2}`\ rp cos C cos A - :math:`q(c_{2}`\ p + :math:`a_{2}`\ r) cos B
   | :math:`d_{3}` = :math:`c^{2}`\ pq cos A cos B - :math:`r(a_{2}`\ q + :math:`b_{2}`\ p) cos C,

   and the barycentric product :g:`P*U <[ P* U ]>` is the point :math:`x : y : z` given by

   ap/:math:`d_{1}` : bq/:math:`d_{2}` : cr/:math:`d_{3}`.

   For P to lie on the line at infinity means that r = - p - q. Substitution for r, a computer quickly shows that

   x cot A + y cot B + z cot :g:`C <C>` = 0,

   as desired.

   The orthic axis is perpendicular to the Euler line. For this and other properties, visit MathWorld. The appearance of (I, J, K) in the following list means that X(K) is the barycentric product of perpendicular directions X_i and X_j.

   | (30,1511,1637)
   | (511,523,2491)
   | (514,516,676)
   | (2574,2575,647)
   | (513,517,3310)

.. _preamble-0052:

.. admonition:: Group Preamble — Points on the Incircle (Incircle transforms)
   :class: note

   Suppose that :g:`U <U>` =\ :math:`u : v : w` (trilinears) is a point other than the symmedian point, :ref:`X_6 <X_6>`. Then the *incircle transform of :g:`U* <U*>` is the point.

   T(U) = a (a - b + c) (a + b - c) (c v - b w)^2 : : ,

   which lies on the incircle. Geometrically, T(U) is the Brisse transform of the psi transform of :ref:`X_6 <X_6>` and U. (Brisse transform is described just before :ref:`X_1254 <X_1254>`, and psi transform, also called the "Psi mapping" elsewhere in ETC, and :cite:`TCCT <tcct>`, p. 80, is defined in the preamble just before :ref:`X_98 <X_98>`.

.. collection::
   :sort: order
