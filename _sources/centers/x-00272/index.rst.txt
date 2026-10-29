:order: 272
:type: center
:canonical_id: X(272)
:dependencies: X(2), X(3), X(7), X(21), X(28), X(58), X(60), X(75), X(81), X(86), X(209), X(261), X(273), X(284), X(310), X(1014), X(1088)

.. _X(272):

X(272) = ISOGONAL CONJUGATE OF X(209)
=====================================

.. figure:: x-00272.svg
   :alt: X(272) = ISOGONAL CONJUGATE OF X(209)
   :align: center

   **X(272) = ISOGONAL CONJUGATE OF X(209)** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`f(A,B,C) : f(B,C,A) : f(C,A,B)`, where, f(A,B,C) = 1/[(sin A + sin(A - B) + sin(A - C))(sin B + sin C)]

* **Kimberling (6, 9, 13) Search Value:** :math:`0.811216421884`

Notes
-----

.. container:: note-item

   Barycentrics (sin A)f(A,B,C) : (sin B)f(B,C,A) : (sin C)f(C,A,B)

Incidence
---------

:ref:`X(272) <X(272)>` lies and on these lines:

{:ref:`2 <X(2)>`, :ref:`284 <X(284)>`}, {:ref:`7 <X(7)>`, :ref:`58 <X(58)>`}, {:ref:`21 <X(21)>`, :ref:`75 <X(75)>`}, {:ref:`28 <X(28)>`, :ref:`273 <X(273)>`}, {:ref:`60 <X(60)>`, :ref:`86 <X(86)>`}, {:ref:`261 <X(261)>`, :ref:`310 <X(310)>`}, {1014, 1088}

Relations
---------

* :ref:`X(272) <X(272)>` = :term:`isogonal conjugate <isogonal-conjugate>` of :ref:`X(209) <X(209)>`
* :ref:`X(272) <X(272)>` = :ref:`X(3) <X(3)>`-:term:`cross conjugate <cross-conjugate>` of :ref:`X(81) <X(81)>`

Construction
------------

.. literalinclude:: model.py
   :language: python
