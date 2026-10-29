:order: 646
:type: center
:canonical_id: X(646)
:dependencies: X(2), X(8), X(190), X(210), X(314), X(522), X(644), X(645), X(650), X(668), X(3669), X(35158)

.. _X(646):

X(646) = BARYCENTRIC MULTIPLIER FOR YFF PARABOLA
================================================

.. figure:: x-00646.svg
   :alt: X(646) = BARYCENTRIC MULTIPLIER FOR YFF PARABOLA
   :align: center

   **X(646) = BARYCENTRIC MULTIPLIER FOR YFF PARABOLA** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`f(a,b,c) : f(b,c,a) : f(c,a,b)`, where f(a,b,c) = (b + c - a)/[a\ :sup:`2`\ (b - c)]

Barycentrics
~~~~~~~~~~~~

* :math:`g(a,b,c) : g(b,c,a) : g(c,a,b)`, where g(a,b,c) = (b + c - a)/[a(b - c)]

* **Kimberling (6, 9, 13) Search Value:** :math:`9.403725070080`

Notes
-----

.. container:: note-item

   :ref:`X(646) <X(646)>` satisfies the equation X\*(incircle) = Yff parabola, where \* denotes barycentric multiplication, defined by

   (u : v : w) \* (x : y : z) = ux : vy : wz (barycentric coordinates, see note at :ref:`X(2) <X(2)>`).

Incidence
---------

:ref:`X(646) <X(646)>` lies and on these lines:

{:ref:`190 <X(190)>`, :ref:`668 <X(668)>`}, {:ref:`644 <X(644)>`, :ref:`645 <X(645)>`}

Relations
---------

* :ref:`X(646) <X(646)>` = :term:`isotomic conjugate <isotomic-conjugate>` of X(3669)
* :ref:`X(646) <X(646)>` = :term:`trilinear pole <trilinear-pole>` of line :ref:`X(8) <X(8)>`\ \ :ref:`X(210) <X(210)>` (the tangent to Feuerbach hyperbola at :ref:`X(8) <X(8)>`)
* :ref:`X(646) <X(646)>` = :ref:`X(650) <X(650)>`-:term:`cross conjugate <cross-conjugate>` of :ref:`X(8) <X(8)>`
* :ref:`X(646) <X(646)>` = :ref:`X(522) <X(522)>`-cross conjugate of :ref:`X(314) <X(314)>`
* :ref:`X(646) <X(646)>` = PU(4)-harmonic conjugate of polar conjugate of X(35158)

Construction
------------

.. literalinclude:: model.py
   :language: python
