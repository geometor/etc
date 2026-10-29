:order: 17
:type: center
:canonical_id: X(17)
:dependencies: X(2), X(3), X(4), X(5), X(6), X(12), X(13), X(14), X(15), X(16), X(18), X(61), X(62), X(63), X(76), X(83), X(140), X(202), X(203), X(231), X(275), X(299), X(302), X(303), X(397), X(471), X(473), X(499), X(523), X(623), X(624), X(627), X(629), X(633), X(635), X(1209), X(10642), X(14446), X(32627)

.. _X(17):
.. _FirstNapoleonPoint:

X(17) = 1st NAPOLEON POINT
==========================

.. figure:: x-00017.svg
   :alt: X(17) = 1st NAPOLEON POINT
   :align: center

   **X(17) = 1st NAPOLEON POINT** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`\csc(A + \pi /6) : \csc(B + \pi /6) : \csc(C + \pi /6)`
* :math:`\sec(A - \pi /3) : \sec(B - \pi /3) : \sec(C - \pi /3)`

Barycentrics
~~~~~~~~~~~~

* :math:`a \csc(A + \pi /6) : b \csc(B + \pi /6) : c \csc(C + \pi /6)`

Tripolars
~~~~~~~~~

* :math:`(a^2-b^2-c^2-2 \sqrt{3} S) \sqrt{(a^2-3 b^2-3 c^2-2 \sqrt{3} S)} : :`

* **Kimberling (6, 9, 13) Search Value:** :math:`1.386654550070`

Notes
-----

.. container:: note-item

   Let X,Y,Z be the centers of the equilateral triangles in the construction of :ref:`X(13) <X(13)>`. The lines AX, BY, CZ concur in :ref:`X(17) <X(17)>`.

.. container:: note-item

   **John Rigby,** "Napoleon revisited," *Journal of Geometry,*\ 33 (1988) 126-146.

.. container:: note-item

   :ref:`X(17) <X(17)>` is the {X(231),X(1209)}-harmonic conjugate of :ref:`X(18) <X(18)>`.

Incidence
---------

:ref:`X(17) <X(17)>` lies on the Napoleon cubic and on these lines:

{:ref:`2 <X(2)>`, :ref:`62 <X(62)>`}, {:ref:`3 <X(3)>`, :ref:`13 <X(13)>`}, {:ref:`4 <X(4)>`, :ref:`15 <X(15)>`}, {:ref:`5 <X(5)>`, :ref:`14 <X(14)>`}, {:ref:`6 <X(6)>`, :ref:`18 <X(18)>`}, {:ref:`12 <X(12)>`, 203}, {:ref:`16 <X(16)>`, 140}, {:ref:`76 <X(76)>`, 303}, {:ref:`83 <X(83)>`, 624}, {202, 499}, {275, 471}, {299, 635}, {623, 633}

Relations
---------

* :ref:`X(17) <X(17)>` = reflection of X(627) in X(629)
* :ref:`X(17) <X(17)>` = :term:`isogonal conjugate <isogonal-conjugate>` of :ref:`X(61) <X(61)>`
* :ref:`X(17) <X(17)>` = :term:`isotomic conjugate <isotomic-conjugate>` of X(302)
* :ref:`X(17) <X(17)>` = :term:`complement <complement>` of X(627)
* :ref:`X(17) <X(17)>` = :term:`anticomplement <anticomplement>` of X(629)
* :ref:`X(17) <X(17)>` = circumcircle-inverse of X(32627)
* :ref:`X(17) <X(17)>` = X(i)-:term:`cross conjugate <cross-conjugate>` of X(j) for these (i,j): (:ref:`16 <X(16)>`, :ref:`14 <X(14)>`), (140, :ref:`18 <X(18)>`), (397, :ref:`4 <X(4)>`)
* :ref:`X(17) <X(17)>` = polar conjugate of X(473)
* :ref:`X(17) <X(17)>` = trilinear product of vertices of outer Napoleon triangle
* :ref:`X(17) <X(17)>` = Kosnita(:ref:`X(13) <X(13)>`,\ :ref:`X(3) <X(3)>`) point
* :ref:`X(17) <X(17)>` = Kosnita(:ref:`X(17) <X(17)>`,\ :ref:`X(17) <X(17)>`) point
* :ref:`X(17) <X(17)>` = Cundy-Parry Phi transform of :ref:`X(13) <X(13)>`
* :ref:`X(17) <X(17)>` = Cundy-Parry Psi transform of :ref:`X(15) <X(15)>`
* :ref:`X(17) <X(17)>` = :term:`trilinear pole <trilinear-pole>` of line X(523)X(14446)
* :ref:`X(17) <X(17)>` = :ref:`X(63) <X(63)>`-:term:`isoconjugate <isoconjugate>` of X(10642)

Construction
------------

.. literalinclude:: model.py
   :language: python
