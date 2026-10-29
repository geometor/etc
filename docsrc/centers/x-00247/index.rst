:order: 247
:type: center
:canonical_id: X(247)
:dependencies: X(4), X(110), X(115), X(125), X(686)

.. _X(247):

X(247) = X(4)-LINE CONJUGATE OF X(110)
======================================

.. figure:: x-00247.svg
   :alt: X(247) = X(4)-LINE CONJUGATE OF X(110)
   :align: center

   **X(247) = X(4)-LINE CONJUGATE OF X(110)** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`f(A,B,C) : f(B,C,A) : f(C,A,B)`, where, f(A,B,C) = csc(B-A)[sec A csc(B - A) + sec C csc(B - C)] + csc(C - A) u(A,B,C),, u(A,B,C) = [sec A csc(C - A) + sec B csc(C - B)]

* **Kimberling (6, 9, 13) Search Value:** :math:`5.103210291151`

Notes
-----

.. container:: note-item

   Barycentrics (sin A)f(A,B,C) : (sin B)f(B,C,A) : (sin C)f(C,A,B)

Incidence
---------

:ref:`X(247) <X(247)>` lies and on these lines:

{:ref:`4 <X(4)>`, :ref:`110 <X(110)>`}, {:ref:`115 <X(115)>`, :ref:`125 <X(125)>`}

Relations
---------

* :ref:`X(247) <X(247)>` = :term:`crossdifference <crossdifference>` of every pair of points on line :ref:`X(110) <X(110)>`\ \ :ref:`X(686) <X(686)>`
* :ref:`X(247) <X(247)>` = :ref:`X(4) <X(4)>`-:term:`line conjugate <line-conjugate>` of :ref:`X(110) <X(110)>`

Construction
------------

.. literalinclude:: model.py
   :language: python
