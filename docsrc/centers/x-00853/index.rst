:order: 853
:type: center
:canonical_id: X(853)
:dependencies: X(2), X(3), X(7), X(55), X(647), X(657), X(663)

.. _X(853):

X(853) = INTERCEPT OF EULER LINE AND TRILINEAR POLAR OF X(55)
=============================================================

.. figure:: x-00853.svg
   :alt: X(853) = INTERCEPT OF EULER LINE AND TRILINEAR POLAR OF X(55)
   :align: center

   **X(853) = INTERCEPT OF EULER LINE AND TRILINEAR POLAR OF X(55)** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`f(A,B,C) : f(B,C,A) : f(C,A,B),`, where f(A,B,C) = sec\ :sup:`2`\ (C/2) sin 2B sin(C - A) + sec\ :sup:`2`\ (B/2) sin 2C sin(B - A)

Barycentrics
~~~~~~~~~~~~

* :math:`g(A,B,C) : g(B,C,A) : g(C,A,B)`, where g(A,B,C) = (sin A)f(A,B,C)

* **Kimberling (6, 9, 13) Search Value:** :math:`6.730258608066`

Notes
-----

.. container:: note-item

   As a point on the Euler line, :ref:`X(853) <X(853)>` has Shinagawa coefficients ([(2E-F)F-S\ :sup:`2`]S\ :sup:`2`-$bcS\ :sub:`A`\ :sup:`2`\ $F +$abS\ :sub:`C`\ $[(E+F)F+S\ :sup:`2`]-$ab$(E+F)S\ :sup:`2`, [(E+F)F+S\ :sup:`2`]S\ :sup:`2`\ +$bcS\ :sub:`A`\ :sup:`2`\ $(E+F) -$abS\ :sub:`C`\ $[(E+F)\ :sup:`2`\ +S\ :sup:`2`]+$ab$(3E+F)S\ :sup:`2`).

Incidence
---------

:ref:`X(853) <X(853)>` lies and on these lines:

{:ref:`2 <X(2)>`, :ref:`3 <X(3)>`}, {:ref:`657 <X(657)>`, :ref:`663 <X(663)>`}

Relations
---------

* :ref:`X(853) <X(853)>` = :term:`crossdifference <crossdifference>` of every pair of points on line :ref:`X(7) <X(7)>`\ \ :ref:`X(647) <X(647)>`

Construction
------------

.. literalinclude:: model.py
   :language: python
