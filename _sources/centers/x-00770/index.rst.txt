:order: 770
:type: center
:canonical_id: X(770)
:dependencies: X(1), X(44), X(513), X(771), X(1092)

.. _X(770):

X(770) = POINT ACAMAR
=====================

.. figure:: x-00770.svg
   :alt: X(770) = POINT ACAMAR
   :align: center

   **X(770) = POINT ACAMAR** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`f(A,B,C) : f(B,C,A) : f(C,A,B)`, where f(A,B,C) = cos\ :sup:`3`\ B - cos\ :sup:`3`\ C

Barycentrics
~~~~~~~~~~~~

* :math:`g(A,B,C) : g(B,C,A) : g(C,A,B)`, where g(A,B,C) = (sin A)f(A,B,C)

* **Kimberling (6, 9, 13) Search Value:** :math:`-36.735085036081`

Incidence
---------

:ref:`X(770) <X(770)>` lies and on these lines:

{:ref:`44 <X(44)>`, :ref:`513 <X(513)>`}

Relations
---------

* :ref:`X(770) <X(770)>` = :term:`isogonal conjugate <isogonal-conjugate>` of :ref:`X(771) <X(771)>`
* :ref:`X(770) <X(770)>` = :term:`crosssum <crosssum>` of :ref:`X(1) <X(1)>` and :ref:`X(770) <X(770)>`
* :ref:`X(770) <X(770)>` = :term:`crossdifference <crossdifference>` of every pair of points on line :ref:`X(1) <X(1)>`\ X(1092)

Construction
------------

.. literalinclude:: model.py
   :language: python
