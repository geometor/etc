:order: 18
:type: center
:canonical_id: X(18)
:dependencies: X(2), X(3), X(4), X(5), X(6), X(12), X(13), X(14), X(15), X(16), X(17), X(61), X(62), X(63), X(76), X(83), X(140), X(202), X(203), X(231), X(275), X(298), X(302), X(303), X(398), X(470), X(472), X(499), X(523), X(623), X(624), X(628), X(630), X(634), X(636), X(1209), X(10641), X(14447), X(32628)

.. _X(18):
.. _SecondNapoleonPoint:

X(18) = 2nd NAPOLEON POINT
==========================

.. figure:: x-00018.svg
   :alt: X(18) = 2nd NAPOLEON POINT
   :align: center

   **X(18) = 2nd NAPOLEON POINT** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`\csc(A - \pi /6) : \csc(B - \pi /6) : \csc(C - \pi /6)`
* :math:`\sec(A + \pi /3) : \sec(B + \pi /3) : \sec(C + \pi /3)`

Barycentrics
~~~~~~~~~~~~

* :math:`a \csc(A - \pi /6) : b \csc(B - \pi /6) : c \csc(C - \pi /6)`

Tripolars
~~~~~~~~~

* :math:`(a^2-b^2-c^2+2 \sqrt{3} S) \sqrt{(a^2-3 b^2-3 c^2+2 \sqrt{3} S)} : :`

* **Kimberling (6, 9, 13) Search Value:** :math:`-16.280673997779`

Notes
-----

.. container:: note-item

   Let X,Y,Z be the centers of the equilateral triangles in the construction of :ref:`X(14) <X(14)>`. The lines AX, BY, CZ concur in :ref:`X(18) <X(18)>`.

.. container:: note-item

   :ref:`X(18) <X(18)>` is the {X(231),X(1209)}-harmonic conjugate of :ref:`X(17) <X(17)>`.

Incidence
---------

:ref:`X(18) <X(18)>` lies on the Napoleon cubic and on these lines:

{:ref:`2 <X(2)>`, :ref:`61 <X(61)>`}, {:ref:`3 <X(3)>`, :ref:`14 <X(14)>`}, {:ref:`4 <X(4)>`, :ref:`16 <X(16)>`}, {:ref:`5 <X(5)>`, :ref:`13 <X(13)>`}, {:ref:`6 <X(6)>`, :ref:`17 <X(17)>`}, {:ref:`12 <X(12)>`, 202}, {:ref:`15 <X(15)>`, 140}, {:ref:`76 <X(76)>`, 302}, {:ref:`83 <X(83)>`, 623}, {203, 499}, {275, 470}, {298, 636}, {624, 634}

Relations
---------

* :ref:`X(18) <X(18)>` = reflection of X(628) in X(630)
* :ref:`X(18) <X(18)>` = :term:`isogonal conjugate <isogonal-conjugate>` of :ref:`X(62) <X(62)>`
* :ref:`X(18) <X(18)>` = :term:`isotomic conjugate <isotomic-conjugate>` of X(303)
* :ref:`X(18) <X(18)>` = :term:`complement <complement>` of X(628)
* :ref:`X(18) <X(18)>` = :term:`anticomplement <anticomplement>` of X(630)
* :ref:`X(18) <X(18)>` = circumcircle-inverse of X(32628)
* :ref:`X(18) <X(18)>` = X(i)-:term:`cross conjugate <cross-conjugate>` of X(j) for these (i,j): (:ref:`15 <X(15)>`, :ref:`13 <X(13)>`), (140, :ref:`17 <X(17)>`), (398, :ref:`4 <X(4)>`)
* :ref:`X(18) <X(18)>` = polar conjugate of X(472)
* :ref:`X(18) <X(18)>` = trilinear product of vertices of inner Napoleon triangle
* :ref:`X(18) <X(18)>` = Kosnita(:ref:`X(14) <X(14)>`,\ :ref:`X(3) <X(3)>`) point
* :ref:`X(18) <X(18)>` = Cundy-Parry Phi transform of :ref:`X(14) <X(14)>`
* :ref:`X(18) <X(18)>` = Cundy-Parry Psi transform of :ref:`X(16) <X(16)>`
* :ref:`X(18) <X(18)>` = :term:`trilinear pole <trilinear-pole>` of line X(523)X(14447)
* :ref:`X(18) <X(18)>` = :ref:`X(63) <X(63)>`-:term:`isoconjugate <isoconjugate>` of X(10641)

Construction
------------

.. literalinclude:: model.py
   :language: python
