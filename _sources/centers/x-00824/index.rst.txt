:order: 824
:type: center
:canonical_id: X(824)
:dependencies: X(6), X(30), X(321), X(511), X(560), X(693), X(825), X(4586)

.. _X(824):

X(824) = ODD (0, 3) INFINITY POINT
==================================

.. figure:: x-00824.svg
   :alt: X(824) = ODD (0, 3) INFINITY POINT
   :align: center

   **X(824) = ODD (0, 3) INFINITY POINT** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`f(a,b,c) : f(b,c,a) : f(c,a,b)`, where f(a,b,c) = a :sup:`-1`\ (b\ :sup:`3` - c\ :sup:`3`) + a\ :sup:`2`\ (b\ :sup:`0` - c\ :sup:`0`)

Barycentrics
~~~~~~~~~~~~

* :math:`g(a,b,c) : g(b,c,a) : g(c,a,b)`, where g(a,b,c) = af(a,b,c)

Notes
-----

.. container:: note-item

   As the :term:`isogonal conjugate <isogonal-conjugate>` of a point on the circumcircle, :ref:`X(824) <X(824)>` lies on the line at infinity.

Incidence
---------

:ref:`X(824) <X(824)>` lies and on these lines:

{:ref:`30 <X(30)>`, :ref:`511 <X(511)>`}, {:ref:`321 <X(321)>`, :ref:`693 <X(693)>`}

Relations
---------

* :ref:`X(824) <X(824)>` = isogonal conjugate of :ref:`X(825) <X(825)>`
* :ref:`X(824) <X(824)>` = :term:`isotomic conjugate <isotomic-conjugate>` of X(4586)
* :ref:`X(824) <X(824)>` = :term:`crossdifference <crossdifference>` of every pair of points on line :ref:`X(6) <X(6)>`\ \ :ref:`X(560) <X(560)>`

Construction
------------

.. literalinclude:: model.py
   :language: python
