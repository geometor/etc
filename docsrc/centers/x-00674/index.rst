:order: 674
:type: center
:canonical_id: X(674)
:dependencies: X(6), X(30), X(31), X(51), X(210), X(511), X(514), X(675)

.. _X(674):

X(674) = CROSSDIFFERENCE OF X(6) AND X(514)
===========================================

.. figure:: x-00674.svg
   :alt: X(674) = CROSSDIFFERENCE OF X(6) AND X(514)
   :align: center

   **X(674) = CROSSDIFFERENCE OF X(6) AND X(514)** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`f(a,b,c) : f(b,c,a) : f(c,a,b)`, where f(a,b,c) = a[b\ :sup:`3` + c\ :sup:`3` - a(b\ :sup:`2` + c\ :sup:`2`)]

Barycentrics
~~~~~~~~~~~~

* :math:`g(a,b,c) : g(b,c,a) : g(c,a,b)`, where g(a,b,c) = af(a,b,c)

Notes
-----

.. container:: note-item

   As the :term:`isogonal conjugate <isogonal-conjugate>` of a point on the circumcircle, :ref:`X(674) <X(674)>` lies on the line at infinity.

Incidence
---------

:ref:`X(674) <X(674)>` lies and on these lines:

{:ref:`6 <X(6)>`, :ref:`31 <X(31)>`}, {:ref:`30 <X(30)>`, :ref:`511 <X(511)>`}, {:ref:`51 <X(51)>`, :ref:`210 <X(210)>`}

Relations
---------

* :ref:`X(674) <X(674)>` = isogonal conjugate of :ref:`X(675) <X(675)>`
* :ref:`X(674) <X(674)>` = :term:`crossdifference <crossdifference>` of every pair of points on line :ref:`X(6) <X(6)>`\ \ :ref:`X(514) <X(514)>`

Construction
------------

.. literalinclude:: model.py
   :language: python
