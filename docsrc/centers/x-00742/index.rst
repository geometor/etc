:order: 742
:type: center
:canonical_id: X(742)
:dependencies: X(6), X(30), X(37), X(69), X(75), X(141), X(192), X(320), X(335), X(511), X(743), X(788)

.. _X(742):

X(742) = EVEN (- 1, 2) INFINITY POINT
=====================================

.. figure:: x-00742.svg
   :alt: X(742) = EVEN (- 1, 2) INFINITY POINT
   :align: center

   **X(742) = EVEN (- 1, 2) INFINITY POINT** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`f(a,b,c) : f(b,c,a) : f(c,a,b)`, where f(a,b,c) = a :sup:`-2`\ (b\ :sup:`2` + c\ :sup:`2`) - a\ :sup:`1`\ (b :sup:`-1` + c :sup:`-1`)

Barycentrics
~~~~~~~~~~~~

* :math:`g(a,b,c) : g(b,c,a) : g(c,a,b)`, where g(a,b,c) = af(a,b,c)

Notes
-----

.. container:: note-item

   As the :term:`isogonal conjugate <isogonal-conjugate>` of a point on the circumcircle, :ref:`X(742) <X(742)>` lies on the line at infinity.

Incidence
---------

:ref:`X(742) <X(742)>` lies and on these lines:

{:ref:`6 <X(6)>`, :ref:`75 <X(75)>`}, {:ref:`30 <X(30)>`, :ref:`511 <X(511)>`}, {:ref:`37 <X(37)>`, :ref:`141 <X(141)>`}, {:ref:`69 <X(69)>`, :ref:`192 <X(192)>`}, {:ref:`320 <X(320)>`, :ref:`335 <X(335)>`}

Relations
---------

* :ref:`X(742) <X(742)>` = isogonal conjugate of :ref:`X(743) <X(743)>`
* :ref:`X(742) <X(742)>` = :term:`crossdifference <crossdifference>` of every pair of points on line :ref:`X(6) <X(6)>`\ \ :ref:`X(788) <X(788)>`

Construction
------------

.. literalinclude:: model.py
   :language: python
