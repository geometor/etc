:order: 952
:type: center
:canonical_id: X(952)
:dependencies: X(1), X(3), X(4), X(5), X(6), X(8), X(10), X(30), X(40), X(140), X(145), X(150), X(182), X(355), X(390), X(511), X(517), X(546), X(547), X(550), X(551), X(572), X(594), X(654), X(664), X(946), X(953), X(996), X(1000), X(5663), X(14260), X(33645)

.. _X(952):

X(952) = INTERSECTION OF X(1)X(5) AND X(3)X(8)
==============================================

.. figure:: x-00952.svg
   :alt: X(952) = INTERSECTION OF X(1)X(5) AND X(3)X(8)
   :align: center

   **X(952) = INTERSECTION OF X(1)X(5) AND X(3)X(8)** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`bc[2a^{4} - 2a^{3}(b + c) - a^{2}(b^{2} - 4bc + c^{2}) + (2a - b - c)(b - c)(b^{2} - c^{2})] : :`

Notes
-----

.. container:: note-item

   As the :term:`isogonal conjugate <isogonal-conjugate>` of a point on the circumcircle, :ref:`X(952) <X(952)>` lies on the line at infinity.

.. container:: note-item

   Let Ia be the reflection of :ref:`X(1) <X(1)>` in the perpendicular bisector of BC, and define Ib and Ic cyclically. :ref:`X(952) <X(952)>` = :ref:`X(517) <X(517)>` of IaIbIc, which is the inner Garcia triangle.. (:person:`Randy Hutson <randy-hutson>`, September 14, 2016)

.. container:: note-item

   Let A'B'C' be the outer Garcia triangle and A″B″C″ the inner Garcia triangle. Let A\* be the isogonal conjugate, wrt A″B″C″, of A', and define B\* and C\* cyclically. The lines A″A\*, B″B\*, C″C\* concur in :ref:`X(952) <X(952)>`; see also :ref:`X(355) <X(355)>`. (Randy Hutson, December 2, 2017)

Incidence
---------

:ref:`X(952) <X(952)>` lies and on these lines:

{:ref:`1 <X(1)>`, :ref:`5 <X(5)>`}, {:ref:`3 <X(3)>`, :ref:`8 <X(8)>`}, {:ref:`4 <X(4)>`, :ref:`145 <X(145)>`}, {:ref:`10 <X(10)>`, :ref:`140 <X(140)>`}, {:ref:`30 <X(30)>`, :ref:`511 <X(511)>`}, {:ref:`40 <X(40)>`, :ref:`550 <X(550)>`}, {:ref:`150 <X(150)>`, :ref:`664 <X(664)>`}, {:ref:`182 <X(182)>`, :ref:`996 <X(996)>`}, {:ref:`390 <X(390)>`, :ref:`1000 <X(1000)>`}, {:ref:`546 <X(546)>`, :ref:`946 <X(946)>`}, {:ref:`547 <X(547)>`, :ref:`551 <X(551)>`}, {:ref:`572 <X(572)>`, :ref:`594 <X(594)>`}

Relations
---------

* :ref:`X(952) <X(952)>` = isogonal conjugate of :ref:`X(953) <X(953)>`
* :ref:`X(952) <X(952)>` = :term:`crossdifference <crossdifference>` of every pair of points on line :ref:`X(6) <X(6)>`\ \ :ref:`X(654) <X(654)>`
* :ref:`X(952) <X(952)>` = :ref:`X(30) <X(30)>`-of-Fuhrmann-triangle
* :ref:`X(952) <X(952)>` = inner-Garcia-isogonal conjugate of :ref:`X(40) <X(40)>`
* :ref:`X(952) <X(952)>` = X(5663)-of-excentral-triangle
* :ref:`X(952) <X(952)>` = (inverse-in-incircle)-isogonal conjugate of X(33645)
* :ref:`X(952) <X(952)>` = Cundy-Parry Psi transform of X(14260)

Construction
------------

.. literalinclude:: model.py
   :language: python
