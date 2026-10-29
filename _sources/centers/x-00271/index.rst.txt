:order: 271
:type: center
:canonical_id: X(271)
:dependencies: X(2), X(3), X(8), X(9), X(20), X(63), X(78), X(200), X(208), X(255), X(282), X(283), X(342), X(394), X(1034)

.. _X(271):

X(271) = ISOGONAL CONJUGATE OF X(208)
=====================================

.. figure:: x-00271.svg
   :alt: X(271) = ISOGONAL CONJUGATE OF X(208)
   :align: center

   **X(271) = ISOGONAL CONJUGATE OF X(208)** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`f(A,B,C) : f(B,C,A) : f(C,A,B)`, where f(A,B,C) = (cot A cot A/2)/(-1 - cos A + cos B + cos C)

Barycentrics
~~~~~~~~~~~~

* :math:`(\sin A)f(A,B,C) : (\sin B)f(B,C,A) : (\sin C)f(C,A,B)`

* **Kimberling (6, 9, 13) Search Value:** :math:`4.567076249114`

Incidence
---------

:ref:`X(271) <X(271)>` lies and on these lines:

{:ref:`2 <X(2)>`, 1034}, {:ref:`8 <X(8)>`, :ref:`20 <X(20)>`}, {:ref:`78 <X(78)>`, :ref:`394 <X(394)>`}, {:ref:`200 <X(200)>`, :ref:`255 <X(255)>`}, {:ref:`282 <X(282)>`, :ref:`283 <X(283)>`}

Relations
---------

* :ref:`X(271) <X(271)>` = :term:`isogonal conjugate <isogonal-conjugate>` of :ref:`X(208) <X(208)>`
* :ref:`X(271) <X(271)>` = :term:`isotomic conjugate <isotomic-conjugate>` of :ref:`X(342) <X(342)>`
* :ref:`X(271) <X(271)>` = X(i)-:term:`cross conjugate <cross-conjugate>` of X(j) for these (i,j): (:ref:`3 <X(3)>`, :ref:`78 <X(78)>`), (:ref:`9 <X(9)>`, :ref:`63 <X(63)>`)

Construction
------------

.. literalinclude:: model.py
   :language: python
