:order: 863
:type: center
:canonical_id: X(863)
:dependencies: X(2), X(3), X(31), X(75), X(647), X(667), X(788)

.. _X(863):

X(863) = INTERCEPT OF EULER LINE AND TRILINEAR POLAR OF X(31)
=============================================================

.. figure:: x-00863.svg
   :alt: X(863) = INTERCEPT OF EULER LINE AND TRILINEAR POLAR OF X(31)
   :align: center

   **X(863) = INTERCEPT OF EULER LINE AND TRILINEAR POLAR OF X(31)** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`f(A,B,C) : f(B,C,A) : f(C,A,B),`, where f(A,B,C) = csc\ :sup:`2`\ C sin 2B sin(C - A) + csc\ :sup:`2`\ B sin 2C sin(B - A)

Barycentrics
~~~~~~~~~~~~

* :math:`g(A,B,C) : g(B,C,A) : g(C,A,B)`, where g(A,B,C) = (sin A)f(A,B,C)

* **Kimberling (6, 9, 13) Search Value:** :math:`-0.431852977608`

Notes
-----

.. container:: note-item

   As a point on the Euler line, :ref:`X(863) <X(863)>` has Shinagawa coefficients ($abS\ :sub:`A`\ S\ :sub:`B`\ $+$abS\ :sub:`C`\ $F, -$abS\ :sub:`C`\ :sup:`2`\ $ -$ab$S\ :sup:`2`).

Incidence
---------

:ref:`X(863) <X(863)>` lies and on these lines:

{:ref:`2 <X(2)>`, :ref:`3 <X(3)>`}, {:ref:`667 <X(667)>`, :ref:`788 <X(788)>`}

Relations
---------

* :ref:`X(863) <X(863)>` = :term:`crossdifference <crossdifference>` of every pair of points on line :ref:`X(75) <X(75)>`\ \ :ref:`X(647) <X(647)>`

Construction
------------

.. literalinclude:: model.py
   :language: python
