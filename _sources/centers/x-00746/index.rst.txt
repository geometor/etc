:order: 746
:type: center
:canonical_id: X(746)
:dependencies: X(30), X(32), X(37), X(75), X(192), X(315), X(511), X(626), X(747)

.. _X(746):

X(746) = EVEN (- 1, 4) INFINITY POINT
=====================================

.. figure:: x-00746.svg
   :alt: X(746) = EVEN (- 1, 4) INFINITY POINT
   :align: center

   **X(746) = EVEN (- 1, 4) INFINITY POINT** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`f(a,b,c) : f(b,c,a) : f(c,a,b)`, where f(a,b,c) = a :sup:`-2`\ (b\ :sup:`4` + c\ :sup:`4`) - a\ :sup:`3`\ (b :sup:`-1` + c :sup:`-1`)

Barycentrics
~~~~~~~~~~~~

* :math:`g(a,b,c) : g(b,c,a) : g(c,a,b)`, where g(a,b,c) = af(a,b,c)

Notes
-----

.. container:: note-item

   As the :term:`isogonal conjugate <isogonal-conjugate>` of a point on the circumcircle, :ref:`X(746) <X(746)>` lies on the line at infinity.

Incidence
---------

:ref:`X(746) <X(746)>` lies and on these lines:

{:ref:`30 <X(30)>`, :ref:`511 <X(511)>`}, {:ref:`32 <X(32)>`, :ref:`75 <X(75)>`}, {:ref:`37 <X(37)>`, :ref:`626 <X(626)>`}, {:ref:`192 <X(192)>`, :ref:`315 <X(315)>`}

Relations
---------

* :ref:`X(746) <X(746)>` = isogonal conjugate of :ref:`X(747) <X(747)>`

Construction
------------

.. literalinclude:: model.py
   :language: python
