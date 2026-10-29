:order: 866
:type: center
:canonical_id: X(866)
:dependencies: X(2), X(3), X(100), X(244), X(513), X(647), X(665)

.. _X(866):

X(866) = INTERCEPT OF EULER LINE AND TRILINEAR POLAR OF X(513)
==============================================================

.. figure:: x-00866.svg
   :alt: X(866) = INTERCEPT OF EULER LINE AND TRILINEAR POLAR OF X(513)
   :align: center

   **X(866) = INTERCEPT OF EULER LINE AND TRILINEAR POLAR OF X(513)** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`f(A,B,C) : f(B,C,A) : f(C,A,B),`, where f(A,B,C) = sin 2B sin(A - C)/(sin A - sin B) - sin 2C sin(A - B)/(sin A - sin C)

Barycentrics
~~~~~~~~~~~~

* :math:`g(A,B,C) : g(B,C,A) : g(C,A,B)`, where g(A,B,C) = (sin A)f(A,B,C)

* **Kimberling (6, 9, 13) Search Value:** :math:`5.564207379332`

Notes
-----

.. container:: note-item

   As a point on the Euler line, :ref:`X(866) <X(866)>` has Shinagawa coefficients ([(E+F)F+S\ :sup:`2`]S\ :sup:`2`\ +$abS\ :sub:`C`\ :sup:`3`\ $ -$abS\ :sub:`B`\ :sup:`2`\ S\ :sub:`C`\ $+$abS\ :sub:`A`\ S\ :sub:`B`\ $(E+F) -$abS\ :sub:`C`\ $[(E+F)\ :sup:`2`-2S\ :sup:`2`]-3$ab$FS\ :sup:`2`, -[(E+F)\ :sup:`2`\ +S\ :sup:`2`]S\ :sup:`2`-$abS\ :sub:`C`\ $S\ :sup:`2` +$abS\ :sub:`B`\ $S\ :sup:`2`\ +$ab$(E+F)S\ :sup:`2`).

Incidence
---------

:ref:`X(866) <X(866)>` lies and on these lines:

{:ref:`2 <X(2)>`, :ref:`3 <X(3)>`}, {:ref:`244 <X(244)>`, :ref:`665 <X(665)>`}

Relations
---------

* :ref:`X(866) <X(866)>` = :term:`crossdifference <crossdifference>` of every pair of points on line :ref:`X(100) <X(100)>`\ \ :ref:`X(647) <X(647)>`

Construction
------------

.. literalinclude:: model.py
   :language: python
