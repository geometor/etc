:order: 832
:type: center
:canonical_id: X(832)
:dependencies: X(6), X(30), X(511), X(656), X(667), X(833), X(977)

.. _X(832):

X(832) = ODD (1, 4) INFINITY POINT
==================================

.. figure:: x-00832.svg
   :alt: X(832) = ODD (1, 4) INFINITY POINT
   :align: center

   **X(832) = ODD (1, 4) INFINITY POINT** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`f(a,b,c) : f(b,c,a) : f(c,a,b)`, where f(a,b,c) = a\ :sup:`0`\ (b\ :sup:`4` - c\ :sup:`4`) + a\ :sup:`3`\ (b\ :sup:`1` - c\ :sup:`1`)

Barycentrics
~~~~~~~~~~~~

* :math:`g(a,b,c) : g(b,c,a) : g(c,a,b)`, where g(a,b,c) = af(a,b,c)

Notes
-----

.. container:: note-item

   As the :term:`isogonal conjugate <isogonal-conjugate>` of a point on the circumcircle, :ref:`X(832) <X(832)>` lies on the line at infinity.

Incidence
---------

:ref:`X(832) <X(832)>` lies and on these lines:

{:ref:`30 <X(30)>`, :ref:`511 <X(511)>`}, {:ref:`656 <X(656)>`, :ref:`667 <X(667)>`}

Relations
---------

* :ref:`X(832) <X(832)>` = isogonal conjugate of :ref:`X(833) <X(833)>`
* :ref:`X(832) <X(832)>` = :term:`crossdifference <crossdifference>` of every pair of points on line :ref:`X(6) <X(6)>`\ \ :ref:`X(977) <X(977)>`

Construction
------------

.. literalinclude:: model.py
   :language: python
