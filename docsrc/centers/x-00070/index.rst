:order: 70
:type: center
:canonical_id: X(70)
:dependencies: X(1), X(2), X(3), X(6), X(26), X(54), X(63), X(64), X(66), X(71), X(74), X(125), X(161), X(265), X(525), X(571), X(924), X(1176), X(1177), X(1288), X(1352), X(1594), X(1899), X(2072), X(2158), X(3448), X(3527), X(3542), X(4846), X(5504), X(6145), X(6152), X(6240), X(6241), X(6243), X(6403), X(7507), X(8553), X(8746), X(8907), X(34116), X(38534)

.. _X(70):

X(70) = ISOGONAL CONJUGATE OF X(26)
===================================

.. figure:: x-00070.svg
   :alt: X(70) = ISOGONAL CONJUGATE OF X(26)
   :align: center

   **X(70) = ISOGONAL CONJUGATE OF X(26)** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`bc/[b^{2} \cos 2B + c^{2} \cos 2C - a^{2} \cos 2A] : :`

Barycentrics
~~~~~~~~~~~~

* :math:`1/(a^8 - 2 a^6 (b^2 + c^2) + 2 a^2 (b^6 + c^6) - (b^2 - c^2)^2 (b^4 + c^4)) : :`

* **Kimberling (6, 9, 13) Search Value:** :math:`5.721069014472`

Linear Combinations
-------------------

* :ref:`X(70) <X(70)>` = (S cot ω- 2R\ :sup:`2`)/(S cot ω-3 R\ :sup:`2`)\*\ :ref:`X(3) <X(3)>` - X(8907) (:person:`Peter Moses <peter-moses>`, December 28, 2015)

Incidence
---------

:ref:`X(70) <X(70)>` lies on the Jerabek circumhyperbola and on these lines:

{:ref:`3 <X(3)>`, 8907}, {:ref:`6 <X(6)>`, 1594}, {:ref:`54 <X(54)>`, 1899}, {:ref:`64 <X(64)>`, 6240}, {:ref:`66 <X(66)>`, 6403}, {:ref:`71 <X(71)>`, 2158}, {:ref:`74 <X(74)>`, 1288}, {265, 6243}, {1176, 1352}, {1177, 3542}, {3448, 5504}, {3527, 7507}, {4846, 6241}, {6145, 6152}

Relations
---------

* :ref:`X(70) <X(70)>` = :term:`isogonal conjugate <isogonal-conjugate>` of :ref:`X(26) <X(26)>`
* :ref:`X(70) <X(70)>` = :term:`anticomplement <anticomplement>` of X(34116)
* :ref:`X(70) <X(70)>` = antigonal conjugate of X(38534)
* :ref:`X(70) <X(70)>` = X(571)-crossconjugate of :ref:`X(2) <X(2)>`
* :ref:`X(70) <X(70)>` = X(i)-:term:`isoconjugate <isoconjugate>` of X(j) for these {i,j}: {:ref:`1 <X(1)>`, :ref:`26 <X(26)>`}, {:ref:`63 <X(63)>`, 8746}
* :ref:`X(70) <X(70)>` = reflection of the isogonal conjugate of X(2072) in X(125)
* :ref:`X(70) <X(70)>` = X(125)-:term:`cevapoint <cevapoint>` of X(924)
* :ref:`X(70) <X(70)>` = X(161)-:term:`crosssum <crosssum>` of X(8553)
* :ref:`X(70) <X(70)>` = barycentric product X(525) X(1288)

Construction
------------

.. literalinclude:: model.py
   :language: python
