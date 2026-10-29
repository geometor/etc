:order: 704
:type: center
:canonical_id: X(704)
:dependencies: X(30), X(511), X(705)

.. _X(704):

X(704) = EVEN (- 4, 1) INFINITY POINT
=====================================

.. figure:: x-00704.svg
   :alt: X(704) = EVEN (- 4, 1) INFINITY POINT
   :align: center

   **X(704) = EVEN (- 4, 1) INFINITY POINT** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`f(a,b,c) : f(b,c,a) : f(c,a,b)`, where f(a,b,c) = a :sup:`-5`\ (b\ :sup:`1` + c\ :sup:`1`) - a\ :sup:`0`\ (b :sup:`-4` + c :sup:`-4`)

Barycentrics
~~~~~~~~~~~~

* :math:`g(a,b,c) : g(b,c,a) : g(c,a,b)`, where g(a,b,c) = af(a,b,c)

Notes
-----

.. container:: note-item

   As the :term:`isogonal conjugate <isogonal-conjugate>` of a point on the circumcircle, :ref:`X(704) <X(704)>` lies on the line at infinity.

Incidence
---------

:ref:`X(704) <X(704)>` lies and on these lines:

{:ref:`30 <X(30)>`, :ref:`511 <X(511)>`}

Relations
---------

* :ref:`X(704) <X(704)>` = isogonal conjugate of :ref:`X(705) <X(705)>`

Construction
------------

.. literalinclude:: model.py
   :language: python
