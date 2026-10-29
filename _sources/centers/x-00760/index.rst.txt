:order: 760
:type: center
:canonical_id: X(760)
:dependencies: X(1), X(6), X(8), X(10), X(30), X(32), X(315), X(511), X(626), X(761), X(1491)

.. _X(760):

X(760) = EVEN (1, 4) INFINITY POINT
===================================

.. figure:: x-00760.svg
   :alt: X(760) = EVEN (1, 4) INFINITY POINT
   :align: center

   **X(760) = EVEN (1, 4) INFINITY POINT** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`f(a,b,c) : f(b,c,a) : f(c,a,b)`, where f(a,b,c) = a\ :sup:`0`\ (b\ :sup:`4` + c\ :sup:`4`) - a\ :sup:`3`\ (b\ :sup:`1` + c\ :sup:`1`)

Barycentrics
~~~~~~~~~~~~

* :math:`g(a,b,c) : g(b,c,a) : g(c,a,b)`, where g(a,b,c) = af(a,b,c)

Notes
-----

.. container:: note-item

   As the :term:`isogonal conjugate <isogonal-conjugate>` of a point on the circumcircle, :ref:`X(760) <X(760)>` lies on the line at infinity.

Incidence
---------

:ref:`X(760) <X(760)>` lies and on these lines:

{:ref:`1 <X(1)>`, :ref:`32 <X(32)>`}, {:ref:`8 <X(8)>`, :ref:`315 <X(315)>`}, {:ref:`10 <X(10)>`, :ref:`626 <X(626)>`}, {:ref:`30 <X(30)>`, :ref:`511 <X(511)>`}

Relations
---------

* :ref:`X(760) <X(760)>` = isogonal conjugate of :ref:`X(761) <X(761)>`
* :ref:`X(760) <X(760)>` = :term:`crossdifference <crossdifference>` of every pair of points on line :ref:`X(6) <X(6)>`\ X(1491)

Construction
------------

.. literalinclude:: model.py
   :language: python
