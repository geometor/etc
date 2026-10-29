:order: 862
:type: center
:canonical_id: X(862)
:dependencies: X(2), X(3), X(19), X(63), X(647), X(661), X(663)

.. _X(862):

X(862) = INTERCEPT OF EULER LINE AND TRILINEAR POLAR OF X(19)
=============================================================

.. figure:: x-00862.svg
   :alt: X(862) = INTERCEPT OF EULER LINE AND TRILINEAR POLAR OF X(19)
   :align: center

   **X(862) = INTERCEPT OF EULER LINE AND TRILINEAR POLAR OF X(19)** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`f(A,B,C) : f(B,C,A) : f(C,A,B),`, where f(A,B,C) = cot C sin 2B sin(C - A) + cot B sin 2C sin(B - A)
* :math:`g(a,b,c) : g(b,c,a) : g(c,a,b),`, where g(a,b,c) = (a\ :sup:`2` - bc)(b + c)/(b\ :sup:`2` + c\ :sup:`2` - a\ :sup:`2`) (M. Iliev, 5/13/07)

* **Kimberling (6, 9, 13) Search Value:** :math:`0.826096539919`

Notes
-----

.. container:: note-item

   Barycentrics (sin A)f(A,B,C) : (sin B)f(B,C,A) : (sin C)f(C,A,B)

.. container:: note-item

   As a point on the Euler line, :ref:`X(862) <X(862)>` has Shinagawa coefficients ($ab$F, -$abS\ :sub:`C`\ $).

Incidence
---------

:ref:`X(862) <X(862)>` lies and on these lines:

{:ref:`2 <X(2)>`, :ref:`3 <X(3)>`}, {:ref:`661 <X(661)>`, :ref:`663 <X(663)>`}

Relations
---------

* :ref:`X(862) <X(862)>` = :term:`crossdifference <crossdifference>` of every pair of points on line :ref:`X(63) <X(63)>`\ \ :ref:`X(647) <X(647)>`

Construction
------------

.. literalinclude:: model.py
   :language: python
