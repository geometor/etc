:order: 579
:type: center
:canonical_id: X(579)
:dependencies: X(1), X(2), X(3), X(6), X(7), X(11), X(19), X(27), X(36), X(37), X(40), X(46), X(48), X(56), X(71), X(109), X(165), X(198), X(218), X(219), X(284), X(380), X(387), X(443), X(474), X(517), X(523), X(608), X(652), X(663), X(942), X(965), X(966), X(1108), X(1751)

.. _X(579):

X(579) = HARMONIC OF X(284)
===========================

.. figure:: x-00579.svg
   :alt: X(579) = HARMONIC OF X(284)
   :align: center

   **X(579) = HARMONIC OF X(284)** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`f(a,b,c) : f(b,c,a) : f(c,a,b)`, where f(a,b,c) = a(a\ :sup:`2`\ b + a\ :sup:`2`\ c + abc - b\ :sup:`3` - c\ :sup:`3`) (M.Iliev, 5/13/07)

* **Kimberling (6, 9, 13) Search Value:** :math:`-1.263414547670`

Linear Combinations
-------------------

* :ref:`X(579) <X(579)>` = s\*\ :ref:`X(3) <X(3)>` - (r + 2R)\*cot(ω)\*\ :ref:`X(6) <X(6)>`

Notes
-----

.. container:: note-item

   Barycentrics af(a,b,c) : bf(b,c,a) : cf(c,a,b)

Incidence
---------

:ref:`X(579) <X(579)>` lies and on these lines:

{:ref:`1 <X(1)>`, :ref:`71 <X(71)>`}, {:ref:`2 <X(2)>`, :ref:`7 <X(7)>`}, {:ref:`3 <X(3)>`, :ref:`6 <X(6)>`}, {:ref:`19 <X(19)>`, :ref:`46 <X(46)>`}, {:ref:`36 <X(36)>`, :ref:`48 <X(48)>`}, {:ref:`37 <X(37)>`, :ref:`942 <X(942)>`}, {:ref:`40 <X(40)>`, :ref:`387 <X(387)>`}, {:ref:`56 <X(56)>`, :ref:`219 <X(219)>`}, {:ref:`109 <X(109)>`, :ref:`608 <X(608)>`}, {:ref:`165 <X(165)>`, :ref:`380 <X(380)>`}, {:ref:`198 <X(198)>`, :ref:`218 <X(218)>`}, {:ref:`443 <X(443)>`, :ref:`966 <X(966)>`}, {:ref:`474 <X(474)>`, :ref:`965 <X(965)>`}, {:ref:`517 <X(517)>`, 1108}

Relations
---------

* :ref:`X(579) <X(579)>` = :term:`isogonal conjugate <isogonal-conjugate>` of X(1751)
* :ref:`X(579) <X(579)>` = :ref:`X(27) <X(27)>`-:term:`Ceva conjugate <ceva-conjugate>` of :ref:`X(1) <X(1)>`
* :ref:`X(579) <X(579)>` = :term:`crosssum <crosssum>` of :ref:`X(11) <X(11)>` and :ref:`X(652) <X(652)>`
* :ref:`X(579) <X(579)>` = :term:`crossdifference <crossdifference>` of every pair of points on line :ref:`X(523) <X(523)>`\ \ :ref:`X(663) <X(663)>`
* :ref:`X(579) <X(579)>` = inverse-in-Brocard-circle of :ref:`X(284) <X(284)>`

Construction
------------

.. literalinclude:: model.py
   :language: python
