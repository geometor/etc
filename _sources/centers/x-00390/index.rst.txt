:order: 390
:type: center
:canonical_id: X(390)
:dependencies: X(1), X(2), X(3), X(4), X(7), X(8), X(9), X(11), X(20), X(30), X(40), X(55), X(144), X(145), X(175), X(176), X(279), X(376), X(387), X(495), X(496), X(595), X(631), X(657), X(665), X(938), X(944), X(952), X(971), X(999), X(1000), X(1056), X(1058), X(2550), X(3600)

.. _X(390):

X(390) = REFLECTION OF GERGONNE POINT IN INCENTER
=================================================

.. figure:: x-00390.svg
   :alt: X(390) = REFLECTION OF GERGONNE POINT IN INCENTER
   :align: center

   **X(390) = REFLECTION OF GERGONNE POINT IN INCENTER** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`bc(b + c - a)[3a^{2} + (b - c)^{2}]`

Barycentrics
~~~~~~~~~~~~

* :math:`(b + c - a)[3a^{2} + (b - c)^{2}]`

* **Kimberling (6, 9, 13) Search Value:** :math:`2.636456039908`

Linear Combinations
-------------------

* :ref:`X(390) <X(390)>` = 4(R/r)\*\ :ref:`X(1) <X(1)>` - 3\ :ref:`X(2) <X(2)>` + 4\ :ref:`X(3) <X(3)>`

Notes
-----

.. container:: note-item

   :ref:`X(390) <X(390)>` is the point in whIch the extended legs :ref:`X(1) <X(1)>`\ \ :ref:`X(7) <X(7)>` and :ref:`X(8) <X(8)>`\ \ :ref:`X(9) <X(9)>` of the trapezoid :ref:`X(1) <X(1)>`\ \ :ref:`X(7) <X(7)>`\ \ :ref:`X(8) <X(8)>`\ \ :ref:`X(9) <X(9)>` meet. (:person:`Randy Hutson <randy-hutson>`, February 10, 2016)

.. container:: note-item

   Let A'B'C' be the extangents-to-intangents :term:`similarity image <similarity-image>` of ABC. A'B'C' is homothetic to ABC at :ref:`X(55) <X(55)>` and to the :term:`anticomplementary triangle <anticomplementary-triangle>` at :ref:`X(390) <X(390)>`. (Randy Hutson, June 7, 2019)

Incidence
---------

:ref:`X(390) <X(390)>` lies and on these lines:

{:ref:`1 <X(1)>`, :ref:`7 <X(7)>`}, {:ref:`2 <X(2)>`, :ref:`11 <X(11)>`}, {:ref:`3 <X(3)>`, 1058}, {:ref:`4 <X(4)>`, :ref:`495 <X(495)>`}, {:ref:`8 <X(8)>`, :ref:`9 <X(9)>`}, {:ref:`30 <X(30)>`, 1056}, {:ref:`40 <X(40)>`, :ref:`938 <X(938)>`}, {:ref:`144 <X(144)>`, :ref:`145 <X(145)>`}, {:ref:`376 <X(376)>`, :ref:`999 <X(999)>`}, {:ref:`387 <X(387)>`, :ref:`595 <X(595)>`}, {:ref:`496 <X(496)>`, :ref:`631 <X(631)>`}, {:ref:`944 <X(944)>`, :ref:`971 <X(971)>`}, {:ref:`952 <X(952)>`, :ref:`1000 <X(1000)>`}

Relations
---------

* :ref:`X(390) <X(390)>` = midpoint of :ref:`X(144) <X(144)>` and :ref:`X(145) <X(145)>`
* :ref:`X(390) <X(390)>` = reflection of X(i) in X(j) for these (i,j): (:ref:`7 <X(7)>`, :ref:`1 <X(1)>`), (:ref:`8 <X(8)>`, :ref:`9 <X(9)>`)
* :ref:`X(390) <X(390)>` = :term:`anticomplement <anticomplement>` of X(2550)
* :ref:`X(390) <X(390)>` = :term:`crossdifference <crossdifference>` of every pair of points on line :ref:`X(657) <X(657)>`\ \ :ref:`X(665) <X(665)>`
* :ref:`X(390) <X(390)>` = inverse-in-Feuerbach-hyperbola of :ref:`X(2) <X(2)>`
* :ref:`X(390) <X(390)>` = {:ref:`X(1) <X(1)>`,\ :ref:`X(20) <X(20)>`}-harmonic conjugate of X(3600)
* :ref:`X(390) <X(390)>` = {:ref:`X(175) <X(175)>`,\ :ref:`X(176) <X(176)>`}-harmonic conjugate of :ref:`X(279) <X(279)>`
* :ref:`X(390) <X(390)>` = bicentric sum of PU(122)

Construction
------------

.. literalinclude:: model.py
   :language: python
