:order: 245
:type: center
:canonical_id: X(245)
:dependencies: X(1), X(60), X(110), X(115), X(125)

.. _X(245):

X(245) = X(1)-LINE CONJUGATE OF X(110)
======================================

.. figure:: x-00245.svg
   :alt: X(245) = X(1)-LINE CONJUGATE OF X(110)
   :align: center

   **X(245) = X(1)-LINE CONJUGATE OF X(110)** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`f(A,B,C) : f(B,C,A) : f(C,A,B)`, where, f(A,B,C) = csc\ :sup:`2`\ (C - A) + csc(C - B) [csc(C - A) -csc(B - A)] + csc\ :sup:`2`\ (A - B)

* **Kimberling (6, 9, 13) Search Value:** :math:`2.204587745588`

Notes
-----

.. container:: note-item

   Barycentrics (sin A)f(A,B,C) : (sin B)f(B,C,A) : (sin C)f(C,A,B)

Incidence
---------

:ref:`X(245) <X(245)>` lies and on these lines:

{:ref:`1 <X(1)>`, :ref:`60 <X(60)>`}, {:ref:`115 <X(115)>`, :ref:`125 <X(125)>`}

Relations
---------

* :ref:`X(245) <X(245)>` = :ref:`X(1) <X(1)>`-:term:`line conjugate <line-conjugate>` of :ref:`X(110) <X(110)>`

Construction
------------

.. literalinclude:: model.py
   :language: python
