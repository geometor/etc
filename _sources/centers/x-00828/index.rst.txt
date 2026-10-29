:order: 828
:type: center
:canonical_id: X(828)
:dependencies: X(2), X(6), X(158), X(255), X(829)

.. _X(828):

X(828) = CROSSPOINT OF X(2) AND X(255)
======================================

.. figure:: x-00828.svg
   :alt: X(828) = CROSSPOINT OF X(2) AND X(255)
   :align: center

   **X(828) = CROSSPOINT OF X(2) AND X(255)** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`f(A,B,C) : f(B,C,A) : f(C,A,B)`, where f(A,B,C) = sin C sec\ :sup:`2`\ B + sin B sec\ :sup:`2`\ C

Barycentrics
~~~~~~~~~~~~

* :math:`g(A,B,C) : g(B,C,A) : g(C,A,B)`, where g(A,B,C) = sin A f(A,B,C)

* **Kimberling (6, 9, 13) Search Value:** :math:`2.832303021334`

Relations
---------

* :ref:`X(828) <X(828)>` = :term:`isogonal conjugate <isogonal-conjugate>` of :ref:`X(829) <X(829)>`
* :ref:`X(828) <X(828)>` = :term:`crosspoint <crosspoint>` of :ref:`X(2) <X(2)>` and :ref:`X(255) <X(255)>`
* :ref:`X(828) <X(828)>` = :term:`crosssum <crosssum>` of :ref:`X(6) <X(6)>` and :ref:`X(158) <X(158)>`

Construction
------------

.. literalinclude:: model.py
   :language: python
