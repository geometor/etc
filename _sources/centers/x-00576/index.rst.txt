:order: 576
:type: center
:canonical_id: X(576)
:dependencies: X(1), X(3), X(4), X(5), X(6), X(23), X(32), X(61), X(62), X(140), X(182), X(184), X(187), X(262), X(371), X(372), X(385), X(524), X(542), X(575), X(597), X(671), X(1691), X(7607), X(38225)

.. _X(576):

X(576) = ORTHOHARMONIC OF X(187)
================================

.. figure:: x-00576.svg
   :alt: X(576) = ORTHOHARMONIC OF X(187)
   :align: center

   **X(576) = ORTHOHARMONIC OF X(187)** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`\sin A + \cot(D/2) \cos A`, where cot(D/2) = - (a\ :sup:`2` + b\ :sup:`2` + c\ :sup:`2`)/(12\*area)
* 3 sin A - cos A cot ω : : (Peter J. C. Moses, 7/20/03)
* cos A - 3 sin A tan ω : : (Peter J. C. Moses, 8/22/03)
* :math:`2 \cos(A + 2\omega ) - \cos(A - 2\omega ) + \cos A : :`

Barycentrics
~~~~~~~~~~~~

* :math:`a^2(a^4 + 2b^4 + 2c^4 - 3a^2b^2 - 3a^2c^2 - 2b^2c^2) : :`

* **Kimberling (6, 9, 13) Search Value:** :math:`-1.901818704500`

Linear Combinations
-------------------

* :ref:`X(576) <X(576)>` = :ref:`X(3) <X(3)>` - 3\ :ref:`X(6) <X(6)>`

Incidence
---------

:ref:`X(576) <X(576)>` lies and on these lines:

{:ref:`3 <X(3)>`, :ref:`6 <X(6)>`}, {:ref:`4 <X(4)>`, :ref:`542 <X(542)>`}, {:ref:`5 <X(5)>`, :ref:`524 <X(524)>`}, {:ref:`23 <X(23)>`, :ref:`184 <X(184)>`}, {:ref:`140 <X(140)>`, :ref:`597 <X(597)>`}, {:ref:`262 <X(262)>`, :ref:`385 <X(385)>`}

Relations
---------

* :ref:`X(576) <X(576)>` = reflection of X(i) in X(j) for these (i,j): (:ref:`3 <X(3)>`, :ref:`575 <X(575)>`), (:ref:`182 <X(182)>`, :ref:`6 <X(6)>`)
* :ref:`X(576) <X(576)>` = circumcircle-inverse of X(38225)
* :ref:`X(576) <X(576)>` = Brocard-circle-inverse of :ref:`X(575) <X(575)>`
* :ref:`X(576) <X(576)>` = 2nd-Lemoine-circle-nverse of X(1691)
* :ref:`X(576) <X(576)>` = :term:`isogonal conjugate <isogonal-conjugate>` of X(7607)
* :ref:`X(576) <X(576)>` = {:ref:`X(61) <X(61)>`,\ :ref:`X(62) <X(62)>`}-harmonic conjugate of :ref:`X(32) <X(32)>`
* :ref:`X(576) <X(576)>` = pole of Lemoine axis wrt circle {:ref:`X(371) <X(371)>`,\ :ref:`X(372) <X(372)>`,PU(1),PU(39)}
* :ref:`X(576) <X(576)>` = center of Ehrmann circle
* :ref:`X(576) <X(576)>` = :ref:`X(1) <X(1)>` of 2nd Ehrmann triangle if ABC is acute
* :ref:`X(576) <X(576)>` = Cundy-Parry Phi transform of :ref:`X(187) <X(187)>`
* :ref:`X(576) <X(576)>` = Cundy-Parry Psi transform of :ref:`X(671) <X(671)>`

Construction
------------

.. literalinclude:: model.py
   :language: python
