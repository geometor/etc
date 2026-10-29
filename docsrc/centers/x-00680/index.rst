:order: 680
:type: center
:canonical_id: X(680)
:dependencies: X(4), X(6), X(30), X(158), X(511), X(681), X(35970)

.. _X(680):

X(680) = CROSSDIFFERENCE OF X(6) AND X(158)
===========================================

.. figure:: x-00680.svg
   :alt: X(680) = CROSSDIFFERENCE OF X(6) AND X(158)
   :align: center

   **X(680) = CROSSDIFFERENCE OF X(6) AND X(158)** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`f(A,B,C): f(B,C,A) : f(C,A,B)`, where f(A,B,C) = cos\ :sup:`2`\ A (sin B cos\ :sup:`2`\ B - sin C cos\ :sup:`2`\ C)

Barycentrics
~~~~~~~~~~~~

* :math:`g(A,B,C) : g(B,C,A) : g(C,A,B)`, where g(A,B,C) = sin A f(A,B,C)

Notes
-----

.. container:: note-item

   As the :term:`isogonal conjugate <isogonal-conjugate>` of a point on the circumcircle, :ref:`X(680) <X(680)>` lies on the line at infinity.

Incidence
---------

:ref:`X(680) <X(680)>` lies and on these lines:

{:ref:`30 <X(30)>`, :ref:`511 <X(511)>`}

Relations
---------

* :ref:`X(680) <X(680)>` = isogonal conjugate of :ref:`X(681) <X(681)>`
* :ref:`X(680) <X(680)>` = :term:`complementary conjugate <complementary-conjugate>` of X(35970)
* :ref:`X(680) <X(680)>` = :ref:`X(4) <X(4)>`-:term:`Ceva conjugate <ceva-conjugate>` of X(35970)
* :ref:`X(680) <X(680)>` = :term:`crossdifference <crossdifference>` of every pair of points on line :ref:`X(6) <X(6)>`\ \ :ref:`X(158) <X(158)>`

Construction
------------

.. literalinclude:: model.py
   :language: python
