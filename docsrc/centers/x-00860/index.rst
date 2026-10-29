:order: 860
:type: center
:canonical_id: X(860)
:dependencies: X(2), X(3), X(8), X(10), X(34), X(48), X(92), X(201), X(240), X(522), X(647), X(997), X(1068), X(3109)

.. _X(860):

X(860) = INTERCEPT OF EULER LINE AND TRILINEAR POLAR OF X(92)
=============================================================

.. figure:: x-00860.svg
   :alt: X(860) = INTERCEPT OF EULER LINE AND TRILINEAR POLAR OF X(92)
   :align: center

   **X(860) = INTERCEPT OF EULER LINE AND TRILINEAR POLAR OF X(92)** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`f(A,B,C) : f(B,C,A) : f(C,A,B),`, where f(A,B,C) = (tan A + tan B) sin 2B sin(C - A) + (tan A + tan C) sin 2C sin(B - A)

Barycentrics
~~~~~~~~~~~~

* :math:`g(A,B,C) : g(B,C,A) : g(C,A,B)`, where g(A,B,C) = (sin A)f(A,B,C)

* **Kimberling (6, 9, 13) Search Value:** :math:`1.652613633134`

Notes
-----

.. container:: note-item

   As a point on the Euler line, :ref:`X(860) <X(860)>` has Shinagawa coefficients ($abS\ :sub:`C`\ $F-$ab$(E+F)F, -$abS\ :sub:`A`\ S\ :sub:`B`\ $+$ab$S\ :sup:`2`).

Incidence
---------

:ref:`X(860) <X(860)>` lies and on these lines:

{:ref:`2 <X(2)>`, :ref:`3 <X(3)>`}, {:ref:`8 <X(8)>`, 1068}, {:ref:`10 <X(10)>`, :ref:`201 <X(201)>`}, {:ref:`34 <X(34)>`, :ref:`997 <X(997)>`}, {:ref:`240 <X(240)>`, :ref:`522 <X(522)>`}

Relations
---------

* :ref:`X(860) <X(860)>` = :term:`crossdifference <crossdifference>` of every pair of points on line :ref:`X(48) <X(48)>`\ \ :ref:`X(647) <X(647)>`
* :ref:`X(860) <X(860)>` = inverse-in-polar-circle of X(3109)

Construction
------------

.. literalinclude:: model.py
   :language: python
