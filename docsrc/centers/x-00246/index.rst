:order: 246
:type: center
:canonical_id: X(246)
:dependencies: X(3), X(74), X(110), X(115), X(125)

.. _X(246):

X(246) = X(3)-LINE CONJUGATE OF X(110)
======================================

.. figure:: x-00246.svg
   :alt: X(246) = X(3)-LINE CONJUGATE OF X(110)
   :align: center

   **X(246) = X(3)-LINE CONJUGATE OF X(110)** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`f(A,B,C) : f(B,C,A) : f(C,A,B)`, where, f(A,B,C) = csc(B-A)[cos A csc(B - A) + cos C csc(B - C)] + csc(C - A) u(A,B,C),, u(A,B,C) = [cos A csc(C - A) + cos B csc(C - B)]

* **Kimberling (6, 9, 13) Search Value:** :math:`4.199423192172`

Notes
-----

.. container:: note-item

   Barycentrics (sin A)f(A,B,C) : (sin B)f(B,C,A) : (sin C)f(C,A,B)

Incidence
---------

:ref:`X(246) <X(246)>` lies and on these lines:

{:ref:`3 <X(3)>`, :ref:`74 <X(74)>`}, {:ref:`115 <X(115)>`, :ref:`125 <X(125)>`}

Relations
---------

* :ref:`X(246) <X(246)>` = :ref:`X(3) <X(3)>`-:term:`line conjugate <line-conjugate>` of :ref:`X(110) <X(110)>`

Construction
------------

.. literalinclude:: model.py
   :language: python
