:order: 869
:type: center
:canonical_id: X(869)
:dependencies: X(1), X(2), X(6), X(31), X(32), X(38), X(55), X(100), X(101), X(192), X(210), X(292), X(649), X(693), X(731), X(743), X(870), X(871), X(893), X(980), X(1045), X(1107)

.. _X(869):

X(869) = INTERSECTION OF LINES X(1)X(2) AND X(31)X(32)
======================================================

.. figure:: x-00869.svg
   :alt: X(869) = INTERSECTION OF LINES X(1)X(2) AND X(31)X(32)
   :align: center

   **X(869) = INTERSECTION OF LINES X(1)X(2) AND X(31)X(32)** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`f(a,b,c) : f(b,c,a) : f(c,a,b),`, where f(a,b,c) = a\ :sup:`2`\ (b\ :sup:`2` + c\ :sup:`2` + bc)

Barycentrics
~~~~~~~~~~~~

* :math:`g(a,b,c) : g(b,c,a) : g(c,a,b)`, where g(a,b,c) = af(a,b,c)

* **Kimberling (6, 9, 13) Search Value:** :math:`0.945619416021`

Incidence
---------

:ref:`X(869) <X(869)>` lies and on these lines:

{:ref:`1 <X(1)>`, :ref:`2 <X(2)>`}, {:ref:`6 <X(6)>`, :ref:`292 <X(292)>`}, {:ref:`31 <X(31)>`, :ref:`32 <X(32)>`}, {:ref:`38 <X(38)>`, :ref:`980 <X(980)>`}, {:ref:`55 <X(55)>`, :ref:`893 <X(893)>`}, {:ref:`100 <X(100)>`, :ref:`731 <X(731)>`}, {:ref:`101 <X(101)>`, :ref:`743 <X(743)>`}, {:ref:`192 <X(192)>`, 1045}, {:ref:`210 <X(210)>`, 1107}

Relations
---------

* :ref:`X(869) <X(869)>` = :term:`isogonal conjugate <isogonal-conjugate>` of :ref:`X(870) <X(870)>`
* :ref:`X(869) <X(869)>` = :term:`isotomic conjugate <isotomic-conjugate>` of :ref:`X(871) <X(871)>`
* :ref:`X(869) <X(869)>` = :term:`crossdifference <crossdifference>` of every pair of points on line :ref:`X(649) <X(649)>`\ \ :ref:`X(693) <X(693)>`

Construction
------------

.. literalinclude:: model.py
   :language: python
