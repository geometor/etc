:order: 209
:type: center
:canonical_id: X(209)
:dependencies: X(4), X(6), X(10), X(12), X(31), X(37), X(44), X(51), X(272), X(306), X(518)

.. _X(209):

X(209) = X(4)-CEVA CONJUGATE OF X(37)
=====================================

.. figure:: x-00209.svg
   :alt: X(209) = X(4)-CEVA CONJUGATE OF X(37)
   :align: center

   **X(209) = X(4)-CEVA CONJUGATE OF X(37)** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`f(A,B,C) : f(B,C,A) : f(C,A,B)`, where f(A,B,C) = (sin B + sin C)[sin A + sin(A - B) + sin(A - C)]

Barycentrics
~~~~~~~~~~~~

* :math:`(\sin A)f(A,B,C) : (\sin B)f(B,C,A) : (\sin C)f(C,A,B)`

* **Kimberling (6, 9, 13) Search Value:** :math:`-2.027998688698`

Incidence
---------

:ref:`X(209) <X(209)>` lies and on these lines:

{:ref:`6 <X(6)>`, :ref:`31 <X(31)>`}, {:ref:`10 <X(10)>`, :ref:`12 <X(12)>`}, {:ref:`44 <X(44)>`, :ref:`51 <X(51)>`}, {:ref:`306 <X(306)>`, :ref:`518 <X(518)>`}

Relations
---------

* :ref:`X(209) <X(209)>` = :term:`isogonal conjugate <isogonal-conjugate>` of :ref:`X(272) <X(272)>`
* :ref:`X(209) <X(209)>` = :ref:`X(4) <X(4)>`-:term:`Ceva conjugate <ceva-conjugate>` of :ref:`X(37) <X(37)>`

Construction
------------

.. literalinclude:: model.py
   :language: python
