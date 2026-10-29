:order: 836
:type: center
:canonical_id: X(836)
:dependencies: X(1), X(37), X(73), X(393), X(394), X(820), X(837), X(1100)

.. _X(836):

X(836) = CROSSPOINT OF X(1) AND X(394)
======================================

.. figure:: x-00836.svg
   :alt: X(836) = CROSSPOINT OF X(1) AND X(394)
   :align: center

   **X(836) = CROSSPOINT OF X(1) AND X(394)** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`f(A,B,C) : f(B,C,A) : f(C,A,B)`, where f(A,B,C) = sin B sec\ :sup:`2`\ B + sin C sec\ :sup:`2`\ C

Barycentrics
~~~~~~~~~~~~

* :math:`g(A,B,C) : g(B,C,A) : g(C,A,B)`, where g(A,B,C) = sin A f(A,B,C)

* **Kimberling (6, 9, 13) Search Value:** :math:`2.621417052429`

Incidence
---------

:ref:`X(836) <X(836)>` lies and on these lines:

{:ref:`1 <X(1)>`, :ref:`393 <X(393)>`}, {:ref:`37 <X(37)>`, :ref:`73 <X(73)>`}, {:ref:`820 <X(820)>`, 1100}

Relations
---------

* :ref:`X(836) <X(836)>` = :term:`isogonal conjugate <isogonal-conjugate>` of :ref:`X(837) <X(837)>`
* :ref:`X(836) <X(836)>` = :term:`crosspoint <crosspoint>` of :ref:`X(1) <X(1)>` and :ref:`X(394) <X(394)>`
* :ref:`X(836) <X(836)>` = :term:`crosssum <crosssum>` of :ref:`X(1) <X(1)>` and :ref:`X(393) <X(393)>`

Construction
------------

.. literalinclude:: model.py
   :language: python
