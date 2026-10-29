:order: 644
:type: center
:canonical_id: X(644)
:dependencies: X(1), X(8), X(9), X(55), X(78), X(100), X(101), X(105), X(145), X(190), X(218), X(219), X(220), X(244), X(346), X(645), X(646), X(650), X(651), X(666), X(668), X(728), X(764), X(813), X(932), X(934), X(1015), X(1025), X(1083), X(1280), X(1357), X(3669), X(4904), X(24002)

.. _X(644):

X(644) = TRILINEAR MULTIPLIER FOR YFF PARABOLA
==============================================

.. figure:: x-00644.svg
   :alt: X(644) = TRILINEAR MULTIPLIER FOR YFF PARABOLA
   :align: center

   **X(644) = TRILINEAR MULTIPLIER FOR YFF PARABOLA** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`f(a,b,c) : f(b,c,a) : f(c,a,b)`, where f(a,b,c) = (b + c - a)/(b - c)

Barycentrics
~~~~~~~~~~~~

* :math:`g(a,b,c) : g(b,c,a) : g(c,a,b)`, where g(a,b,c) = af(a,b,c)

* **Kimberling (6, 9, 13) Search Value:** :math:`9.556744265007`

Notes
-----

.. container:: note-item

   :ref:`X(644) <X(644)>` satisfies the equation X\*(incircle) = Yff parabola, where \* denotes trilinear multiplication, defined by

   (u : v : w) \* (x : y : z) = ux : vy : wz.

.. container:: note-item

   :ref:`X(644) <X(644)>` is the perspector of the :term:`anticevian triangle <anticevian-triangle>` of :ref:`X(100) <X(100)>` and the :term:`unary cofactor triangle <unary-cofactor-triangle>` of the intangents triangle. (:person:`Randy Hutson <randy-hutson>`, January 15, 2019)

Incidence
---------

:ref:`X(644) <X(644)>` lies and on these lines:

{:ref:`8 <X(8)>`, :ref:`220 <X(220)>`}, {:ref:`78 <X(78)>`, :ref:`728 <X(728)>`}, {:ref:`100 <X(100)>`, :ref:`101 <X(101)>`}, {:ref:`105 <X(105)>`, 1083}, {:ref:`145 <X(145)>`, :ref:`218 <X(218)>`}, {:ref:`190 <X(190)>`, :ref:`651 <X(651)>`}, {:ref:`219 <X(219)>`, :ref:`346 <X(346)>`}, {:ref:`645 <X(645)>`, :ref:`646 <X(646)>`}, {:ref:`666 <X(666)>`, :ref:`668 <X(668)>`}, {:ref:`813 <X(813)>`, :ref:`932 <X(932)>`}, {:ref:`934 <X(934)>`, 1025}

Relations
---------

* :ref:`X(644) <X(644)>` = reflection of X(i) in X(j) for these (i,j): (:ref:`105 <X(105)>`, 1083), (1280, :ref:`1 <X(1)>`)
* :ref:`X(644) <X(644)>` = :term:`isogonal conjugate <isogonal-conjugate>` of X(3669)
* :ref:`X(644) <X(644)>` = :term:`isotomic conjugate <isotomic-conjugate>` of X(24002)
* :ref:`X(644) <X(644)>` = :term:`anticomplement <anticomplement>` of X(4904)
* :ref:`X(644) <X(644)>` = :ref:`X(190) <X(190)>`-:term:`Ceva conjugate <ceva-conjugate>` of :ref:`X(100) <X(100)>`
* :ref:`X(644) <X(644)>` = :term:`crosssum <crosssum>` of :ref:`X(764) <X(764)>` and X(1015)
* :ref:`X(644) <X(644)>` = :term:`crossdifference <crossdifference>` of every pair of points on line :ref:`X(244) <X(244)>`\ X(1357)
* :ref:`X(644) <X(644)>` = :term:`trilinear pole <trilinear-pole>` of line :ref:`X(9) <X(9)>`\ \ :ref:`X(55) <X(55)>` (tangent to Feuerbach hyperbola at :ref:`X(9) <X(9)>`)
* :ref:`X(644) <X(644)>` = :ref:`X(650) <X(650)>`-:term:`cross conjugate <cross-conjugate>` of :ref:`X(9) <X(9)>`
* :ref:`X(644) <X(644)>` = :term:`eigencenter <eigencenter>` of Caelum triangle
* :ref:`X(644) <X(644)>` = eigencenter of 5th mixtilinear triangle
* :ref:`X(644) <X(644)>` = perspector of unary cofactor triangles of 3rd and 5th mixtilinear triangles
* :ref:`X(644) <X(644)>` = perspector of 5th mixtilinear triangle and unary cofactor triangle of 3rd mixtilinear triangle
* :ref:`X(644) <X(644)>` = intersection, other than vertices of Gemini triangle 29, of {ABC, Gemini 29}-circumconic and {Gemini 29, Gemini 30}-circumconic

Construction
------------

.. literalinclude:: model.py
   :language: python
