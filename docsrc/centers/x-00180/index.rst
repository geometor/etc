:order: 180
:type: center
:canonical_id: X(180)
:dependencies: X(173), X(179), X(483)

.. _X(180):
.. _SecondAjimaMalfattiPoint:

X(180) = 2nd AJIMA-MALFATTI POINT
=================================

.. figure:: x-00180.svg
   :alt: X(180) = 2nd AJIMA-MALFATTI POINT
   :align: center

   **X(180) = 2nd AJIMA-MALFATTI POINT** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`f(A,B,C) : f(B,C,A) : f(C,A,B)`, where f(A,B,C) = 1/t(B,C,A) + 1/t(C,B,A) - 1/t(A,C,B),, t(A,B,C) = 1 + 2(sec A/4 cos B/4 cos C/4)\ :sup:`2`

* **Kimberling (6, 9, 13) Search Value:** :math:`1.167974364639`

Notes
-----

.. container:: note-item

   Barycentrics g(A,B,C) : g(B,C,A) : g(C,A,B), where g(A,B,C) = (sin A)f(A,B,C)

.. container:: note-item

   Let A″,B″,C″ be the excenters of ABC, and let A',B',C' be as in the construction of :ref:`X(179) <X(179)>`. The lines A'A″,B'B″,B'B″ concur in :ref:`X(180) <X(180)>`. Trilinears are found in Yff's unpublished notes. See :ref:`X(179) <X(179)>`.

Incidence
---------

:ref:`X(180) <X(180)>` lies and on these lines:

{:ref:`173 <X(173)>`, :ref:`483 <X(483)>`}

Construction
------------

.. literalinclude:: model.py
   :language: python
