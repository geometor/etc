:order: 572
:type: center
:canonical_id: X(572)
:dependencies: X(1), X(3), X(6), X(9), X(11), X(48), X(51), X(54), X(58), X(71), X(103), X(165), X(169), X(184), X(199), X(219), X(261), X(517), X(573), X(594), X(604), X(610), X(631), X(661), X(662), X(825), X(947), X(952), X(966), X(1011), X(1051), X(1100), X(1687), X(1688), X(2051), X(4279)

.. _X(572):

X(572) = ORTHOGONAL OF X(58)
============================

.. figure:: x-00572.svg
   :alt: X(572) = ORTHOGONAL OF X(58)
   :align: center

   **X(572) = ORTHOGONAL OF X(58)** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`f(A,B,C) : f(B,C,A) : f(C,A,B)`, where f(A,B,C) = cos(A - U), where cot U = cot(A/2) cot(B/2) cot(C/2) (Joe Goggins, 11/26/08)
* :math:`g(A,B,C) : g(B,C,A) : g(C,A,B)`, where g(A,B,C) = sin A + cot D/2 cos A,, cot D/2 = (a + b + c)\ :sup:`2`/(4\*area)
* :math:`s \cos A + r \sin A : :`
* :math:`a (a^3 - a (b^2 - b c + c^2) - b c (b + c)) : :`

* **Kimberling (6, 9, 13) Search Value:** :math:`5.234901251064`

Linear Combinations
-------------------

* :ref:`X(572) <X(572)>` = s\*\ :ref:`X(3) <X(3)>` + r\*cot(ω)\*\ :ref:`X(6) <X(6)>`

Notes
-----

.. container:: note-item

   :ref:`X(572) <X(572)>` is the intersection of the Brocard axes of ABC, the Feuerbach triangle, and the Apollonius triangle. (:person:`Randy Hutson <randy-hutson>`, March 21, 2019)

Incidence
---------

:ref:`X(572) <X(572)>` lies and on these lines:

{:ref:`1 <X(1)>`, :ref:`604 <X(604)>`}, {:ref:`3 <X(3)>`, :ref:`6 <X(6)>`}, {:ref:`9 <X(9)>`, :ref:`48 <X(48)>`}, {:ref:`51 <X(51)>`, :ref:`199 <X(199)>`}, {:ref:`54 <X(54)>`, :ref:`71 <X(71)>`}, {:ref:`103 <X(103)>`, :ref:`825 <X(825)>`}, {:ref:`165 <X(165)>`, 1051}, {:ref:`169 <X(169)>`, :ref:`610 <X(610)>`}, {:ref:`184 <X(184)>`, 1011}, {:ref:`219 <X(219)>`, :ref:`947 <X(947)>`}, {:ref:`261 <X(261)>`, :ref:`662 <X(662)>`}, {:ref:`517 <X(517)>`, 1100}, {:ref:`594 <X(594)>`, :ref:`952 <X(952)>`}, {:ref:`631 <X(631)>`, :ref:`966 <X(966)>`}

Relations
---------

* :ref:`X(572) <X(572)>` = :term:`isogonal conjugate <isogonal-conjugate>` of X(2051)
* :ref:`X(572) <X(572)>` = {X(1687),X(1688)}-harmonic conjugate of X(4279)
* :ref:`X(572) <X(572)>` = inverse-in-Brocard-circle of :ref:`X(573) <X(573)>`
* :ref:`X(572) <X(572)>` = :term:`crosssum <crosssum>` of :ref:`X(11) <X(11)>` and :ref:`X(661) <X(661)>`

Construction
------------

.. literalinclude:: model.py
   :language: python
