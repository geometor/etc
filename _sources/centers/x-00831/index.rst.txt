:order: 831
:type: center
:canonical_id: X(831)
:dependencies: X(6), X(38), X(662), X(827), X(830)

.. _X(831):

X(831) = o-(1, 3) CIRCUMCIRCLE POINT
====================================

.. figure:: x-00831.svg
   :alt: X(831) = o-(1, 3) CIRCUMCIRCLE POINT
   :align: center

   **X(831) = o-(1, 3) CIRCUMCIRCLE POINT** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`f(a,b,c) : f(b,c,a) : f(c,a,b)`, where f(a,b,c) = 1/[a\ :sup:`0`\ (b\ :sup:`3` - c\ :sup:`3`) + a\ :sup:`2`\ (b\ :sup:`1` - c\ :sup:`1`)]

Barycentrics
~~~~~~~~~~~~

* :math:`g(a,b,c) : g(b,c,a) : g(c,a,b)`, where g(a,b,c) = af(a,b,c)

* **Kimberling (6, 9, 13) Search Value:** :math:`2.269825801880`

Incidence
---------

:ref:`X(831) <X(831)>` lies on the circumcircle.

:ref:`X(831) <X(831)>` lies and on these lines:

{:ref:`662 <X(662)>`, :ref:`827 <X(827)>`}

Relations
---------

* :ref:`X(831) <X(831)>` = :term:`isogonal conjugate <isogonal-conjugate>` of :ref:`X(830) <X(830)>`
* :ref:`X(831) <X(831)>` = :term:`trilinear pole <trilinear-pole>` of line :ref:`X(6) <X(6)>`\ \ :ref:`X(38) <X(38)>`
* :ref:`X(831) <X(831)>` = Ψ(:ref:`X(6) <X(6)>`, :ref:`X(38) <X(38)>`)

Construction
------------

.. literalinclude:: model.py
   :language: python
