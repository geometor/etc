:order: 855
:type: center
:canonical_id: X(855)
:dependencies: X(2), X(3), X(9), X(57), X(513), X(647), X(663), X(851), X(859)

.. _X(855):

X(855) = INTERCEPT OF EULER LINE AND TRILINEAR POLAR OF X(57)
=============================================================

.. figure:: x-00855.svg
   :alt: X(855) = INTERCEPT OF EULER LINE AND TRILINEAR POLAR OF X(57)
   :align: center

   **X(855) = INTERCEPT OF EULER LINE AND TRILINEAR POLAR OF X(57)** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`f(A,B,C) : f(B,C,A) : f(C,A,B),`, where f(A,B,C) = cot(C/2) sin 2B sin(C - A) + cot(B/2) sin 2C sin(B - A)

Barycentrics
~~~~~~~~~~~~

* :math:`g(A,B,C) : g(B,C,A) : g(C,A,B)`, where g(A,B,C) = (sin A)f(A,B,C)

* **Kimberling (6, 9, 13) Search Value:** :math:`0.008868750603`

Notes
-----

.. container:: note-item

   As a point on the Euler line, :ref:`X(855) <X(855)>` has Shinagawa coefficients (ES\ :sup:`2`\ +$abS\ :sub:`C`\ :sup:`2`\ $+$abS\ :sub:`A`\ S\ :sub:`B`\ $ -$abS\ :sub:`C`\ $(E+F), -3ES\ :sup:`2`-3$abS\ :sub:`A`\ S\ :sub:`B`\ $ +2$ab$S\ :sup:`2`).

Incidence
---------

:ref:`X(855) <X(855)>` lies and on these lines:

{:ref:`2 <X(2)>`, :ref:`3 <X(3)>`}, {:ref:`513 <X(513)>`, :ref:`663 <X(663)>`}

Relations
---------

* :ref:`X(855) <X(855)>` = reflection of :ref:`X(851) <X(851)>` in :ref:`X(859) <X(859)>`
* :ref:`X(855) <X(855)>` = :term:`crossdifference <crossdifference>` of every pair of points on line :ref:`X(9) <X(9)>`\ \ :ref:`X(647) <X(647)>`

Construction
------------

.. literalinclude:: model.py
   :language: python
