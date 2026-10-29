:order: 830
:type: center
:canonical_id: X(830)
:dependencies: X(6), X(30), X(38), X(511), X(661), X(831), X(1580)

.. _X(830):

X(830) = ODD (1, 3) INFINITY POINT
==================================

.. figure:: x-00830.svg
   :alt: X(830) = ODD (1, 3) INFINITY POINT
   :align: center

   **X(830) = ODD (1, 3) INFINITY POINT** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`f(a,b,c) : f(b,c,a) : f(c,a,b)`, where f(a,b,c) = a\ :sup:`0`\ (b\ :sup:`3` - c\ :sup:`3`) + a\ :sup:`2`\ (b\ :sup:`1` - c\ :sup:`1`)

Barycentrics
~~~~~~~~~~~~

* :math:`g(a,b,c) : g(b,c,a) : g(c,a,b)`, where g(a,b,c) = af(a,b,c)

Notes
-----

.. container:: note-item

   As the :term:`isogonal conjugate <isogonal-conjugate>` of a point on the circumcircle, :ref:`X(830) <X(830)>` lies on the line at infinity.

Incidence
---------

:ref:`X(830) <X(830)>` lies and on these lines:

{:ref:`30 <X(30)>`, :ref:`511 <X(511)>`}, {:ref:`661 <X(661)>`, 1580}

Relations
---------

* :ref:`X(830) <X(830)>` = isogonal conjugate of :ref:`X(831) <X(831)>`
* :ref:`X(830) <X(830)>` = :term:`crossdifference <crossdifference>` of every pair of points on line :ref:`X(6) <X(6)>`\ \ :ref:`X(38) <X(38)>`

Construction
------------

.. literalinclude:: model.py
   :language: python
