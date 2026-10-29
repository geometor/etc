:order: 136
:type: center
:canonical_id: X(136)
:dependencies: X(2), X(3), X(4), X(5), X(25), X(49), X(68), X(93), X(109), X(110), X(114), X(117), X(118), X(119), X(125), X(127), X(131), X(132), X(133), X(235), X(254), X(338), X(407), X(427), X(429), X(430), X(523), X(868), X(924), X(925), X(2501), X(3563), X(18879), X(34844), X(36472), X(38970), X(39240), X(39241)

.. _X(136):

X(136) = INTERSECTION OF LINE X(4)X(110) AND X(25)X(132)
========================================================

.. figure:: x-00136.svg
   :alt: X(136) = INTERSECTION OF LINE X(4)X(110) AND X(25)X(132)
   :align: center

   **X(136) = INTERSECTION OF LINE X(4)X(110) AND X(25)X(132)** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`f(A,B,C) : f(B,C,A) : f(C,A,B)`, where, f(A,B,C) = (sec A)[(sin 2B - sin 2C)\ :sup:`2`](sin 2B + sin 2C - sin 2A) u(A,B,C),, u(A,B,C) = [sin\ :sup:`2`\ (2B) + sin\ :sup:`2`\ (2C) - sin\ :sup:`2`\ (2A)]

Barycentrics
~~~~~~~~~~~~

* :math:`(b^2 - c^2)^2 (a^4 + b^4 + c^4 - 2 a^2 b^2 - 2 a^2 c^2)/(a^2 - b^2 - c^2) : :`

* **Kimberling (6, 9, 13) Search Value:** :math:`4.219605641607`

Notes
-----

.. container:: note-item

   Barycentrics af(A,B,C) : bf(B,C,A) : cf(C,A,B)

Incidence
---------

:ref:`X(136) <X(136)>` lies on the nine-point circle

:ref:`X(136) <X(136)>` lies and on these lines:

{:ref:`2 <X(2)>`, :ref:`925 <X(925)>`}, {:ref:`4 <X(4)>`, :ref:`110 <X(110)>`}, {:ref:`5 <X(5)>`, :ref:`131 <X(131)>`}, {:ref:`25 <X(25)>`, :ref:`132 <X(132)>`}, {:ref:`68 <X(68)>`, :ref:`254 <X(254)>`}, {:ref:`114 <X(114)>`, :ref:`427 <X(427)>`}, {:ref:`117 <X(117)>`, :ref:`407 <X(407)>`}, {:ref:`118 <X(118)>`, :ref:`430 <X(430)>`}, {:ref:`119 <X(119)>`, :ref:`429 <X(429)>`}, {:ref:`125 <X(125)>`, :ref:`338 <X(338)>`}, {:ref:`127 <X(127)>`, :ref:`868 <X(868)>`}, {:ref:`133 <X(133)>`, :ref:`235 <X(235)>`}

Relations
---------

* :ref:`X(136) <X(136)>` =\ :ref:`X(109) <X(109)>`-of-:term:`orthic triangle <orthic-triangle>` if ABC is acute
* :ref:`X(136) <X(136)>` = center of the rectangular hyperbola that passes through A, B, C, and :ref:`X(93) <X(93)>`
* :ref:`X(136) <X(136)>` = reflection of :ref:`X(131) <X(131)>` in :ref:`X(5) <X(5)>`
* :ref:`X(136) <X(136)>` = :term:`complement <complement>` of :ref:`X(925) <X(925)>`
* :ref:`X(136) <X(136)>` = :term:`anticomplement <anticomplement>` of X(34844)
* :ref:`X(136) <X(136)>` = :term:`crosssum <crosssum>` of circumcircle intercepts of line :ref:`X(3) <X(3)>`\ \ :ref:`X(49) <X(49)>`
* :ref:`X(136) <X(136)>` = :term:`complementary conjugate <complementary-conjugate>` of :ref:`X(924) <X(924)>`
* :ref:`X(136) <X(136)>` = :ref:`X(254) <X(254)>`-:term:`Ceva conjugate <ceva-conjugate>` of :ref:`X(523) <X(523)>`
* :ref:`X(136) <X(136)>` = perspector of circumconic centered at X(2501)
* :ref:`X(136) <X(136)>` = center of circumconic that is locus of :term:`trilinear poles <trilinear-pole>` of lines passing through X(2501) (hyperbola {A,B,C,\ :ref:`X(4) <X(4)>`,\ :ref:`X(93) <X(93)>`}})
* :ref:`X(136) <X(136)>` = :ref:`X(2) <X(2)>`-Ceva conjugate of X(2501)
* :ref:`X(136) <X(136)>` = inverse-in-polar-circle of :ref:`X(110) <X(110)>`
* :ref:`X(136) <X(136)>` = inverse-in-orthoptic-circle-of-Steiner-inellipse of X(3563)
* :ref:`X(136) <X(136)>` = orthopole of line :ref:`X(3) <X(3)>`\ \ :ref:`X(49) <X(49)>`
* :ref:`X(136) <X(136)>` = Kirikami-six-circles image of :ref:`X(93) <X(93)>`
* :ref:`X(136) <X(136)>` = Dou-circles-radical-circle-inverse of X(36472)
* :ref:`X(136) <X(136)>` = Moses-radical-circle-inverse of X(38970)
* :ref:`X(136) <X(136)>` = {X(39240),X(39241)}-harmonic conjugate of polar conjugate of X(18879)

Construction
------------

.. literalinclude:: model.py
   :language: python
