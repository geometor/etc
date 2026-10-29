:order: 581
:type: center
:canonical_id: X(581)
:dependencies: X(1), X(3), X(4), X(6), X(35), X(40), X(42), X(47), X(81), X(84), X(222), X(284), X(411), X(523), X(579), X(580), X(652), X(936), X(941), X(947), X(966), X(995), X(1035), X(1036), X(1104)

.. _X(581):

X(581) = ORTHOHARMONIC OF X(284)
================================

.. figure:: x-00581.svg
   :alt: X(581) = ORTHOHARMONIC OF X(284)
   :align: center

   **X(581) = ORTHOHARMONIC OF X(284)** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`f(A,B,C) : f(B,C,A) : f(C,A,B)`, where f(A,B,C) = sin A + cot D/2 cos A,, cot D/2 = (2abc - e\ :sub:`1` + e\ :sub:`2`)/[4\*area\*(a + b + c)], where e\ :sub:`1`, e\ :sub:`2` are as for :ref:`X(579) <X(579)>`

* **Kimberling (6, 9, 13) Search Value:** :math:`2.619112999419`

Notes
-----

.. container:: note-item

   Barycentrics (sin A)f(A,B,C): (sin B)f(B,C,A) : (sin C)f(C,A,B)

Incidence
---------

:ref:`X(581) <X(581)>` lies and on these lines:

{:ref:`1 <X(1)>`, :ref:`4 <X(4)>`}, {:ref:`3 <X(3)>`, :ref:`6 <X(6)>`}, {:ref:`35 <X(35)>`, :ref:`47 <X(47)>`}, {:ref:`40 <X(40)>`, :ref:`42 <X(42)>`}, {:ref:`81 <X(81)>`, :ref:`411 <X(411)>`}, {:ref:`84 <X(84)>`, :ref:`941 <X(941)>`}, {:ref:`222 <X(222)>`, 1035}, {:ref:`936 <X(936)>`, :ref:`966 <X(966)>`}, {:ref:`947 <X(947)>`, 1036}, {:ref:`995 <X(995)>`, 1104}

Relations
---------

* :ref:`X(581) <X(581)>` = inverse-in-Brocard-circle of :ref:`X(580) <X(580)>`
* :ref:`X(581) <X(581)>` = :term:`crossdifference <crossdifference>` of every pair of points on line :ref:`X(523) <X(523)>`\ \ :ref:`X(652) <X(652)>`

Construction
------------

.. literalinclude:: model.py
   :language: python
