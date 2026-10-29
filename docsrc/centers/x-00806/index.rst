:order: 806
:type: center
:canonical_id: X(806)
:dependencies: X(30), X(511), X(807)

.. _X(806):

X(806) = ODD (- 2, 3) INFINITY POINT
====================================

.. figure:: x-00806.svg
   :alt: X(806) = ODD (- 2, 3) INFINITY POINT
   :align: center

   **X(806) = ODD (- 2, 3) INFINITY POINT** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`f(a,b,c) : f(b,c,a) : f(c,a,b)`, where f(a,b,c) = a :sup:`-3`\ (b\ :sup:`3` - c\ :sup:`3`) + a\ :sup:`2`\ (b :sup:`-2` - c :sup:`-2`)

Barycentrics
~~~~~~~~~~~~

* :math:`g(a,b,c) : g(b,c,a) : g(c,a,b)`, where g(a,b,c) = af(a,b,c)

Notes
-----

.. container:: note-item

   As the :term:`isogonal conjugate <isogonal-conjugate>` of a point on the circumcircle, :ref:`X(806) <X(806)>` lies on the line at infinity.

Incidence
---------

:ref:`X(806) <X(806)>` lies and on these lines:

{:ref:`30 <X(30)>`, :ref:`511 <X(511)>`}

Relations
---------

* :ref:`X(806) <X(806)>` = isogonal conjugate of :ref:`X(807) <X(807)>`

Construction
------------

.. literalinclude:: model.py
   :language: python
