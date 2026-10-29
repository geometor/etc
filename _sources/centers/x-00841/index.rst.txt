:order: 841
:type: center
:canonical_id: X(841)
:dependencies: X(6), X(30), X(376), X(476), X(541)

.. _X(841):

X(841) = ISOGONAL CONJUGATE OF X(541)
=====================================

.. figure:: x-00841.svg
   :alt: X(841) = ISOGONAL CONJUGATE OF X(541)
   :align: center

   **X(841) = ISOGONAL CONJUGATE OF X(541)** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`f(a,b,c) : f(b,c,a) : f(c,a,b)`, where f(a,b,c) = a/(2ax - by - cz), x = x(A,B,C) = 1/(cos A - 2 cos B cos C)

Barycentrics
~~~~~~~~~~~~

* :math:`g(a,b,c) : g(b,c,a) : g(c,a,b)`, where g(a,b,c) = af(a,b,c)

* **Kimberling (6, 9, 13) Search Value:** :math:`13.270923068483`

Incidence
---------

:ref:`X(841) <X(841)>` lies on the circumcircle.

:ref:`X(841) <X(841)>` lies and on these lines:

{:ref:`376 <X(376)>`, :ref:`476 <X(476)>`}

Relations
---------

* :ref:`X(841) <X(841)>` = :term:`isogonal conjugate <isogonal-conjugate>` of :ref:`X(541) <X(541)>`
* :ref:`X(841) <X(841)>` = :term:`trilinear pole <trilinear-pole>`, wrt circumcevian triangle of :ref:`X(30) <X(30)>`, of line :ref:`X(6) <X(6)>`\ \ :ref:`X(30) <X(30)>`

Construction
------------

.. literalinclude:: model.py
   :language: python
