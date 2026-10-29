:order: 834
:type: center
:canonical_id: X(834)
:dependencies: X(2), X(6), X(10), X(30), X(58), X(511), X(522), X(835), X(958), X(39016)

.. _X(834):

X(834) = ODD (2, 3) INFINITY POINT
==================================

.. figure:: x-00834.svg
   :alt: X(834) = ODD (2, 3) INFINITY POINT
   :align: center

   **X(834) = ODD (2, 3) INFINITY POINT** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`f(a,b,c) : f(b,c,a) : f(c,a,b)`, where f(a,b,c) = a\ :sup:`1`\ (b\ :sup:`3` - c\ :sup:`3`) + a\ :sup:`2`\ (b\ :sup:`2` - c\ :sup:`2`)

Barycentrics
~~~~~~~~~~~~

* :math:`g(a,b,c) : g(b,c,a) : g(c,a,b)`, where g(a,b,c) = af(a,b,c)

Notes
-----

.. container:: note-item

   As the :term:`isogonal conjugate <isogonal-conjugate>` of a point on the circumcircle, :ref:`X(834) <X(834)>` lies on the line at infinity.

Incidence
---------

:ref:`X(834) <X(834)>` lies and on these lines:

{:ref:`30 <X(30)>`, :ref:`511 <X(511)>`}

Relations
---------

* :ref:`X(834) <X(834)>` = isogonal conjugate of :ref:`X(835) <X(835)>`
* :ref:`X(834) <X(834)>` = :term:`crosssum <crosssum>` of :ref:`X(522) <X(522)>` and :ref:`X(958) <X(958)>`
* :ref:`X(834) <X(834)>` = :term:`crossdifference <crossdifference>` of every pair of points on line :ref:`X(6) <X(6)>`\ \ :ref:`X(10) <X(10)>`
* :ref:`X(834) <X(834)>` = :ref:`X(2) <X(2)>`-:term:`Ceva conjugate <ceva-conjugate>` of X(39016)
* :ref:`X(834) <X(834)>` = perspector of hyperbola {A,B,C,\ :ref:`X(2) <X(2)>`,\ :ref:`X(58) <X(58)>`}}
* :ref:`X(834) <X(834)>` = barycentric square root of X(39016)

Construction
------------

.. literalinclude:: model.py
   :language: python
