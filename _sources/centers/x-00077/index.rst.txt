:order: 77
:type: center
:canonical_id: X(77)
:dependencies: X(1), X(2), X(3), X(6), X(7), X(9), X(21), X(29), X(33), X(34), X(40), X(41), X(55), X(56), X(57), X(63), X(65), X(69), X(73), X(75), X(78), X(81), X(85), X(86), X(92), X(99), X(102), X(175), X(176), X(189), X(219), X(222), X(223), X(241), X(269), X(283), X(309), X(318), X(326), X(332), X(336), X(348), X(603), X(651), X(652), X(662), X(664), X(738), X(811), X(905), X(934), X(947), X(951), X(962), X(969), X(988), X(990), X(999), X(1036), X(1037), X(1057), X(1106)

.. _X(77):

X(77) = ISOGONAL CONJUGATE OF X(33)
===================================

.. figure:: x-00077.svg
   :alt: X(77) = ISOGONAL CONJUGATE OF X(33)
   :align: center

   **X(77) = ISOGONAL CONJUGATE OF X(33)** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`1/(1 + \sec A) : 1/(1 + \sec B) : 1/(1 + \sec C)`
* :math:`\cos A \sec^{2}(A/2) : \cos B \sec^{2}(B/2) : \cos C \sec^{2}(C/2)`
* :math:`(b^{2} + c^{2} - a^{2})/(b + c - a) : :`
* :math:`S_{A}(S_{A} - bc) : :`

Barycentrics
~~~~~~~~~~~~

* :math:`a/(1 + \sec A) : b/(1 + \sec B) : c/(1 + \sec C)`
* :math:`\cot A (1 - \cos A) : :`

* **Kimberling (6, 9, 13) Search Value:** :math:`-4.331307128236`

Notes
-----

.. container:: note-item

   In the plane of a triangle ABC, let

      * Ia = line through :ref:`X(7) <X(7)>` parallel to BC, and define Ib and Ic cyclically.
      * Ac = Ia∩AB, and define Ba and Cb cyclically.
      * Ab = Ia∩AC, and define Bc and Ca cyclically.
      * Oa = circumcircle of A, Bc, Cb, and define Ob and Oc cyclically.

   Then :ref:`X(77) <X(77)>` = radical center of Oa, Ob, Oc. See also :ref:`X(77) <X(77)>`. (Ivan Pavlov, April 1, 2022)

Incidence
---------

:ref:`X(77) <X(77)>` lies and on these lines:

{:ref:`1 <X(1)>`, :ref:`7 <X(7)>`}, {:ref:`2 <X(2)>`, 189}, {:ref:`6 <X(6)>`, 241}, {:ref:`9 <X(9)>`, 651}, {:ref:`29 <X(29)>`, :ref:`34 <X(34)>`}, {:ref:`40 <X(40)>`, 947}, {:ref:`55 <X(55)>`, 1037}, {:ref:`56 <X(56)>`, 1036}, {:ref:`57 <X(57)>`, :ref:`81 <X(81)>`}, {:ref:`63 <X(63)>`, 219}, {:ref:`65 <X(65)>`, 969}, {:ref:`69 <X(69)>`, :ref:`73 <X(73)>`}, {:ref:`75 <X(75)>`, 664}, {102, 934}, {283, 603}, {309, 318}, {738, 951}, {988, 1106}, {999, 1057}

Relations
---------

* :ref:`X(77) <X(77)>` = :term:`isogonal conjugate <isogonal-conjugate>` of :ref:`X(33) <X(33)>`
* :ref:`X(77) <X(77)>` = :term:`isotomic conjugate <isotomic-conjugate>` of X(318)
* :ref:`X(77) <X(77)>` = X(i)-:term:`Ceva conjugate <ceva-conjugate>` of X(j) for these (i,j): (:ref:`85 <X(85)>`, :ref:`57 <X(57)>`), (:ref:`86 <X(86)>`, :ref:`7 <X(7)>`), (348, :ref:`63 <X(63)>`)
* :ref:`X(77) <X(77)>` = :term:`cevapoint <cevapoint>` of X(i) and X(j) for these (i,j): (:ref:`1 <X(1)>`, 223), (:ref:`3 <X(3)>`, 222)
* :ref:`X(77) <X(77)>` = X(i)-:term:`cross conjugate <cross-conjugate>` of X(j) for these (i,j): (:ref:`3 <X(3)>`, :ref:`63 <X(63)>`), (:ref:`73 <X(73)>`, 222)
* :ref:`X(77) <X(77)>` = :term:`trilinear pole <trilinear-pole>` of line X(652)X(905)
* :ref:`X(77) <X(77)>` = {X(175),X(176)}-harmonic conjugate of X(962)
* :ref:`X(77) <X(77)>` = :ref:`X(92) <X(92)>`-:term:`isoconjugate <isoconjugate>` of :ref:`X(41) <X(41)>`
* :ref:`X(77) <X(77)>` = perspector of ABC and extraversion triangle of :ref:`X(78) <X(78)>`
* :ref:`X(77) <X(77)>` = X(i)-:term:`beth conjugate <beth-conjugate>` of X(j) for these (i,j): (:ref:`21 <X(21)>`, 990), (:ref:`69 <X(69)>`, :ref:`69 <X(69)>`), (:ref:`86 <X(86)>`, 269), (:ref:`99 <X(99)>`, :ref:`75 <X(75)>`), (332, 326), (336, :ref:`77 <X(77)>`), (662, :ref:`77 <X(77)>`), (664, :ref:`77 <X(77)>`), (811, :ref:`77 <X(77)>`)

Construction
------------

.. literalinclude:: model.py
   :language: python
