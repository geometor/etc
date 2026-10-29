:order: 820
:type: center
:canonical_id: X(820)
:dependencies: X(1), X(3), X(29), X(158), X(255), X(296), X(662), X(775), X(821), X(836), X(1100)

.. _X(820):

X(820) = CROSSPOINT OF X(1) AND X(255)
======================================

.. figure:: x-00820.svg
   :alt: X(820) = CROSSPOINT OF X(1) AND X(255)
   :align: center

   **X(820) = CROSSPOINT OF X(1) AND X(255)** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`f(A,B,C) : f(B,C,A) : f(C,A,B)`, where f(A,B,C) = cos\ :sup:`2`\ A (cos\ :sup:`2`\ B + cos\ :sup:`2`\ C)

Barycentrics
~~~~~~~~~~~~

* :math:`(\sin A)f(A,B,C) : (\sin B)f(B,C,A) : (\sin C)f(C,A,B)`

* **Kimberling (6, 9, 13) Search Value:** :math:`2.304798246387`

Incidence
---------

:ref:`X(820) <X(820)>` lies and on these lines:

{:ref:`1 <X(1)>`, :ref:`29 <X(29)>`}, {:ref:`3 <X(3)>`, :ref:`296 <X(296)>`}, {:ref:`662 <X(662)>`, :ref:`775 <X(775)>`}, {:ref:`836 <X(836)>`, 1100}

Relations
---------

* :ref:`X(820) <X(820)>` = :term:`isogonal conjugate <isogonal-conjugate>` of :ref:`X(821) <X(821)>`
* :ref:`X(820) <X(820)>` = :term:`crosspoint <crosspoint>` of :ref:`X(1) <X(1)>` and :ref:`X(255) <X(255)>`
* :ref:`X(820) <X(820)>` = :term:`crosssum <crosssum>` of :ref:`X(1) <X(1)>` and :ref:`X(158) <X(158)>`

Construction
------------

.. literalinclude:: model.py
   :language: python
