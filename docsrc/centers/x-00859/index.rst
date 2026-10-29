:order: 859
:type: center
:canonical_id: X(859)
:dependencies: X(2), X(3), X(10), X(36), X(37), X(56), X(58), X(81), X(125), X(198), X(210), X(238), X(250), X(283), X(284), X(333), X(526), X(647), X(758), X(759), X(851), X(855), X(945), X(956), X(957), X(3109), X(3310), X(3738), X(3943), X(6370), X(6741), X(8677), X(34586), X(34589), X(36069), X(38955)

.. _X(859):

X(859) = INTERCEPT OF EULER LINE AND TRILINEAR POLAR OF X(81)
=============================================================

.. figure:: x-00859.svg
   :alt: X(859) = INTERCEPT OF EULER LINE AND TRILINEAR POLAR OF X(81)
   :align: center

   **X(859) = INTERCEPT OF EULER LINE AND TRILINEAR POLAR OF X(81)** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`f(A,B,C) : f(B,C,A) : f(C,A,B),`, where f(A,B,C) = (sin A + sin B) sin 2B sin(C - A) + (sin A + sin C) sin 2C sin(B - A)

Barycentrics
~~~~~~~~~~~~

* :math:`g(A,B,C) : g(B,C,A) : g(C,A,B)`, where g(A,B,C) = (sin A)f(A,B,C)

* **Kimberling (6, 9, 13) Search Value:** :math:`-1.990686716141`

Notes
-----

.. container:: note-item

   As a point on the Euler line, :ref:`X(859) <X(859)>` has Shinagawa coefficients ($aS\ :sub:`A`\ $ + $a$F,- $aS\ :sub:`A`\ $ - $a$(E + F)).

Incidence
---------

:ref:`X(859) <X(859)>` lies and on these lines:

{:ref:`2 <X(2)>`, :ref:`3 <X(3)>`}, {:ref:`36 <X(36)>`, :ref:`238 <X(238)>`}, {:ref:`56 <X(56)>`, :ref:`58 <X(58)>`}, {:ref:`81 <X(81)>`, :ref:`957 <X(957)>`}, {:ref:`198 <X(198)>`, :ref:`284 <X(284)>`}, {:ref:`283 <X(283)>`, :ref:`945 <X(945)>`}, {:ref:`333 <X(333)>`, :ref:`956 <X(956)>`}

Relations
---------

* :ref:`X(859) <X(859)>` = midpoint of :ref:`X(851) <X(851)>` and :ref:`X(855) <X(855)>`
* :ref:`X(859) <X(859)>` = :term:`isogonal conjugate <isogonal-conjugate>` of X(38955)
* :ref:`X(859) <X(859)>` = :term:`trilinear pole <trilinear-pole>` of line X(3310)X(8677)
* :ref:`X(859) <X(859)>` = :term:`crosspoint <crosspoint>` of X(i) and X(j) for these {i,j}: {:ref:`58 <X(58)>`, :ref:`759 <X(759)>`}, {:ref:`250 <X(250)>`, 36069}
* :ref:`X(859) <X(859)>` = isogonal conjugate of :term:`anticomplement <anticomplement>` of X(34586)
* :ref:`X(859) <X(859)>` = :term:`crosssum <crosssum>` of X(i) and X(j) for these {i,j}: {:ref:`10 <X(10)>`, :ref:`758 <X(758)>`}, {:ref:`125 <X(125)>`, 6370}, {:ref:`210 <X(210)>`, 3943}, {:ref:`526 <X(526)>`, 6741}, {3738, 34589}
* :ref:`X(859) <X(859)>` = :term:`crossdifference <crossdifference>` of every pair of points on line :ref:`X(37) <X(37)>`\ \ :ref:`X(647) <X(647)>`
* :ref:`X(859) <X(859)>` = inverse-in-circumcircle of X(3109)

Construction
------------

.. literalinclude:: model.py
   :language: python
