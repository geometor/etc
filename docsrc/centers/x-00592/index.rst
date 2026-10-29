:order: 592
:type: center
:canonical_id: X(592)
:dependencies: X(6), X(182)

.. _X(592):

X(592) = VAN LAMOEN CIRCUMCENTERS POINT
=======================================

.. figure:: x-00592.svg
   :alt: X(592) = VAN LAMOEN CIRCUMCENTERS POINT
   :align: center

   **X(592) = VAN LAMOEN CIRCUMCENTERS POINT** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`f(A,B,C) : f(B,C,A) : f(C,A,B)`, where f(A,B,C) = 1/[cos A + 2 cos(B - ω) cos(C - ω)]

Barycentrics
~~~~~~~~~~~~

* :math:`g(A,B,C) : g(B,C,A) : g(C,A,B)`, where g(A,B,C) = (sin A)f(A,B,C)

* **Kimberling (6, 9, 13) Search Value:** :math:`2.043062756727`

Notes
-----

.. container:: note-item

   Let P be the point where the line through :ref:`X(6) <X(6)>` parallel to line CA meets line BC, and let Q be the point where the line through :ref:`X(6) <X(6)>` parallel to line AB meets line BC. Let X = :ref:`X(182) <X(182)>`, and let A' be the circumcenter of the triangle PQX. Define B' and C' cyclically. The lines AA', BB', CC' concur in :ref:`X(592) <X(592)>`. (:person:`Floor van Lamoen <floor-van-lamoen>`, 1/4/01)

Construction
------------

.. literalinclude:: model.py
   :language: python
