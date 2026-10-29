:order: 827
:type: center
:canonical_id: X(827)
:dependencies: X(1), X(2), X(5), X(6), X(22), X(23), X(31), X(32), X(39), X(76), X(82), X(83), X(110), X(111), X(163), X(249), X(250), X(251), X(385), X(560), X(662), X(719), X(733), X(741), X(745), X(755), X(759), X(805), X(813), X(826), X(831), X(849), X(850), X(935), X(1577), X(23285)

.. _X(827):

X(827) = o-(0, 4) CIRCUMCIRCLE POINT
====================================

.. figure:: x-00827.svg
   :alt: X(827) = o-(0, 4) CIRCUMCIRCLE POINT
   :align: center

   **X(827) = o-(0, 4) CIRCUMCIRCLE POINT** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`1/[a^{-1}(b^{4} - c^{4}) + a^{3}(b^{0} - c^{0})] : :`

* **Kimberling (6, 9, 13) Search Value:** :math:`0.419571248227`

Notes
-----

.. container:: note-item

   Let A', B', C' be the intersections of line :ref:`X(23) <X(23)>`\ \ :ref:`X(385) <X(385)>` and lines BC, CA, AB, resp. The circumcircles of AB'C', BC'A', CA'B' concur in :ref:`X(827) <X(827)>`. Note: the line :ref:`X(23) <X(23)>`\ \ :ref:`X(385) <X(385)>` is the polar of :ref:`X(2) <X(2)>` wrt the circumcircle. (:person:`Randy Hutson <randy-hutson>`, December 10, 2016)

Incidence
---------

:ref:`X(827) <X(827)>` lies on the circumcircle and on these lines:

{:ref:`5 <X(5)>`, :ref:`83 <X(83)>`}, {:ref:`6 <X(6)>`, :ref:`755 <X(755)>`}, {:ref:`31 <X(31)>`, :ref:`745 <X(745)>`}, {:ref:`32 <X(32)>`, :ref:`733 <X(733)>`}, {:ref:`82 <X(82)>`, :ref:`759 <X(759)>`}, {:ref:`111 <X(111)>`, :ref:`251 <X(251)>`}, {:ref:`163 <X(163)>`, :ref:`813 <X(813)>`}, {:ref:`249 <X(249)>`, :ref:`805 <X(805)>`}, {:ref:`250 <X(250)>`, :ref:`935 <X(935)>`}, {:ref:`560 <X(560)>`, :ref:`719 <X(719)>`}, {:ref:`662 <X(662)>`, :ref:`831 <X(831)>`}, {:ref:`741 <X(741)>`, :ref:`849 <X(849)>`}

Relations
---------

* :ref:`X(827) <X(827)>` = :term:`isogonal conjugate <isogonal-conjugate>` of :ref:`X(826) <X(826)>`
* :ref:`X(827) <X(827)>` = X(i)-:term:`cross conjugate <cross-conjugate>` of X(j) for these (i,j): (:ref:`2 <X(2)>`, :ref:`250 <X(250)>`), (:ref:`32 <X(32)>`, :ref:`249 <X(249)>`)
* :ref:`X(827) <X(827)>` = :term:`trilinear pole <trilinear-pole>` of line :ref:`X(6) <X(6)>`\ \ :ref:`X(22) <X(22)>`
* :ref:`X(827) <X(827)>` = Ψ(:ref:`X(1) <X(1)>`, :ref:`X(82) <X(82)>`)
* :ref:`X(827) <X(827)>` = Ψ(:ref:`X(2) <X(2)>`, :ref:`X(32) <X(32)>`)
* :ref:`X(827) <X(827)>` = Ψ(:ref:`X(6) <X(6)>`, :ref:`X(22) <X(22)>`)
* :ref:`X(827) <X(827)>` = Ψ(:ref:`X(76) <X(76)>`, :ref:`X(6) <X(6)>`)
* :ref:`X(827) <X(827)>` = center of bianticevian conic of :ref:`X(1) <X(1)>` and :ref:`X(31) <X(31)>`
* :ref:`X(827) <X(827)>` = X(1577)-:term:`isoconjugate <isoconjugate>` of :ref:`X(39) <X(39)>`
* :ref:`X(827) <X(827)>` = perspector of circumcevian triangle of :ref:`X(23) <X(23)>` and cross-triangle of ABC and circummedial triangle
* :ref:`X(827) <X(827)>` = :term:`isotomic conjugate <isotomic-conjugate>` of X(23285)
* :ref:`X(827) <X(827)>` = barycentric product :ref:`X(83) <X(83)>`\ \*\ :ref:`X(110) <X(110)>`
* :ref:`X(827) <X(827)>` = barycentric quotient :ref:`X(83) <X(83)>`/:ref:`X(850) <X(850)>`
* :ref:`X(827) <X(827)>` = barycentric product of circumcircle intercepts of line :ref:`X(2) <X(2)>`\ \ :ref:`X(32) <X(32)>`

Construction
------------

.. literalinclude:: model.py
   :language: python
