:order: 78
:type: center
:canonical_id: X(78)
:dependencies: X(1), X(2), X(3), X(4), X(8), X(9), X(20), X(21), X(25), X(29), X(33), X(34), X(37), X(38), X(40), X(46), X(55), X(56), X(57), X(63), X(69), X(72), X(73), X(77), X(92), X(100), X(101), X(145), X(205), X(207), X(210), X(212), X(219), X(220), X(226), X(271), X(273), X(280), X(282), X(283), X(312), X(322), X(329), X(332), X(345), X(377), X(392), X(394), X(404), X(474), X(480), X(517), X(521), X(604), X(608), X(643), X(644), X(652), X(653), X(728), X(758), X(908), X(938), X(942), X(945), X(949), X(958), X(960), X(965), X(988), X(999), X(1040), X(1042), X(1043), X(1057), X(1059), X(1395), X(1406), X(1426), X(3872)

.. _X(78):

X(78) = ISOGONAL CONJUGATE OF X(34)
===================================

.. figure:: x-00078.svg
   :alt: X(78) = ISOGONAL CONJUGATE OF X(34)
   :align: center

   **X(78) = ISOGONAL CONJUGATE OF X(34)** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`1/(1 - \sec A) : 1/(1 - \sec B) : 1/(1 - \sec C)`
* :math:`\cos A \csc^{2}(A/2) : :`
* :math:`(b + c - a)(b^{2} + c^{2} - a^{2}) : :`
* :math:`S_{A}(S_{A} + bc) : :`
* :math:`(b + c - a) \cot A : :`
* :math:`\cot A \cot(A/2) : :`

Barycentrics
~~~~~~~~~~~~

* :math:`a/(1 - \sec A) : b/(1 - \sec B) : c/(1 - \sec C)`

* **Kimberling (6, 9, 13) Search Value:** :math:`5.339129461606`

Incidence
---------

:ref:`X(78) <X(78)>` lies and on these lines:

{:ref:`1 <X(1)>`, :ref:`2 <X(2)>`}, {:ref:`3 <X(3)>`, :ref:`63 <X(63)>`}, {:ref:`4 <X(4)>`, 908}, {:ref:`9 <X(9)>`, :ref:`21 <X(21)>`}, {:ref:`20 <X(20)>`, 329}, {:ref:`29 <X(29)>`, :ref:`33 <X(33)>`}, {:ref:`37 <X(37)>`, 965}, {:ref:`38 <X(38)>`, 988}, {:ref:`40 <X(40)>`, :ref:`100 <X(100)>`}, {:ref:`46 <X(46)>`, 758}, {:ref:`55 <X(55)>`, 960}, {:ref:`56 <X(56)>`, 480}, {:ref:`57 <X(57)>`, 404}, {:ref:`69 <X(69)>`, :ref:`73 <X(73)>`}, {101, 205}, {207, 653}, {210, 958}, {212, 283}, {220, 949}, {226, 377}, {271, 394}, {273, 322}, {280, 282}, {345, 1040}, {392, 1057}, {474, 942}, {517, 945}, {644, 728}, {999, 1059}

Relations
---------

* :ref:`X(78) <X(78)>` = :term:`isogonal conjugate <isogonal-conjugate>` of :ref:`X(34) <X(34)>`
* :ref:`X(78) <X(78)>` = :term:`isotomic conjugate <isotomic-conjugate>` of X(273)
* :ref:`X(78) <X(78)>` = X(i)-:term:`Ceva conjugate <ceva-conjugate>` of X(j) for these (i,j): (:ref:`69 <X(69)>`, :ref:`63 <X(63)>`), (312, :ref:`9 <X(9)>`), (332, 345)
* :ref:`X(78) <X(78)>` = X(i)-:term:`cross conjugate <cross-conjugate>` of X(j) for these (i,j): (:ref:`3 <X(3)>`, 271), (:ref:`72 <X(72)>`, :ref:`8 <X(8)>`), (212, :ref:`9 <X(9)>`), (219, :ref:`63 <X(63)>`)
* :ref:`X(78) <X(78)>` = :term:`crosspoint <crosspoint>` of :ref:`X(69) <X(69)>` and X(345)
* :ref:`X(78) <X(78)>` = :term:`crosssum <crosssum>` of X(i) and X(j) for these (i,j): (:ref:`25 <X(25)>`, 608), (:ref:`56 <X(56)>`, 1406), (604, 1395), (1042, 1426)
* :ref:`X(78) <X(78)>` = X(i)-:term:`beth conjugate <beth-conjugate>` of X(j) for these (i,j): (:ref:`78 <X(78)>`, :ref:`3 <X(3)>`), (643, :ref:`40 <X(40)>`), (1043, :ref:`1 <X(1)>`)
* :ref:`X(78) <X(78)>` = :term:`trilinear pole <trilinear-pole>` of line X(521)X(652)
* :ref:`X(78) <X(78)>` = {:ref:`X(1) <X(1)>`,\ :ref:`X(8) <X(8)>`}-harmonic conjugate of X(3872)
* :ref:`X(78) <X(78)>` = {:ref:`X(2) <X(2)>`,X(145)}-harmonic conjugate of X(938)
* :ref:`X(78) <X(78)>` = :ref:`X(92) <X(92)>`-:term:`isoconjugate <isoconjugate>` of X(604)
* :ref:`X(78) <X(78)>` = homothetic center of :term:`anticomplementary triangle <anticomplementary-triangle>` and :term:`tangential triangle <tangential-triangle>` of the hexyl triangle
* :ref:`X(78) <X(78)>` = perspector of ABC and extraversion triangle of :ref:`X(77) <X(77)>`

Construction
------------

.. literalinclude:: model.py
   :language: python
