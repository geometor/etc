:order: 854
:type: center
:canonical_id: X(854)
:dependencies: X(2), X(3), X(8), X(56), X(647)

.. _X(854):

X(854) = INTERCEPT OF EULER LINE AND TRILINEAR POLAR OF X(56)
=============================================================

.. figure:: x-00854.svg
   :alt: X(854) = INTERCEPT OF EULER LINE AND TRILINEAR POLAR OF X(56)
   :align: center

   **X(854) = INTERCEPT OF EULER LINE AND TRILINEAR POLAR OF X(56)** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`f(A,B,C) : f(B,C,A) : f(C,A,B),`, where f(A,B,C) = csc\ :sup:`2`\ (C/2) sin 2B sin(C - A) + csc\ :sup:`2`\ (B/2) sin 2C sin(B - A)

Barycentrics
~~~~~~~~~~~~

* :math:`g(A,B,C) : g(B,C,A) : g(C,A,B)`, where g(A,B,C) = (sin A)f(A,B,C)

* **Kimberling (6, 9, 13) Search Value:** :math:`0.087118721786`

Notes
-----

.. container:: note-item

   As a point on the Euler line, :ref:`X(854) <X(854)>` has Shinagawa coefficients ([(2E-F)F-S\ :sup:`2`]S\ :sup:`2`-$abS\ :sub:`C`\ :sup:`3`\ $ -$abS\ :sub:`A`\ S\ :sub:`B`\ $(E-2F) +$abS\ :sub:`C`\ $[(E+F)\ :sup:`2`-2S\ :sup:`2`], [(E+F)F+S\ :sup:`2`]S\ :sup:`2`-$abS\ :sub:`A`\ S\ :sub:`B`\ $(E+F) +$abS\ :sub:`C`\ $S\ :sup:`2`).

Incidence
---------

:ref:`X(854) <X(854)>` lies and on these lines:

{:ref:`2 <X(2)>`, :ref:`3 <X(3)>`}

Relations
---------

* :ref:`X(854) <X(854)>` = :term:`crossdifference <crossdifference>` of every pair of points on line :ref:`X(8) <X(8)>`\ \ :ref:`X(647) <X(647)>`

Construction
------------

.. literalinclude:: model.py
   :language: python
