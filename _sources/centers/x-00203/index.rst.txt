:order: 203
:type: center
:canonical_id: X(203)
:dependencies: X(1), X(6), X(11), X(12), X(14), X(15), X(16), X(17), X(18), X(36), X(55), X(56), X(61), X(62), X(101), X(396), X(398), X(495), X(496), X(499)

.. _X(203):

X(203) = X(1)-CEVA CONJUGATE OF X(16)
=====================================

.. figure:: x-00203.svg
   :alt: X(203) = X(1)-CEVA CONJUGATE OF X(16)
   :align: center

   **X(203) = X(1)-CEVA CONJUGATE OF X(16)** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`f(A,B,C) : f(B,C,A) : f(C,A,B)`, where f(A,B,C) = u(v + w - u),, u = u(A,B,C) = sin(A - π/3), v = u(B,C,A), w = u(C,A,B)

* **Kimberling (6, 9, 13) Search Value:** :math:`1.122831801616`

Notes
-----

.. container:: note-item

   Trilinears 1 + cos(A + 2π/3) : 1 + cos(B + 2π/3) : 1 + cos(C + 2π/3) (Joe Goggins, Oct. 19, 2005)

.. container:: note-item

   Barycentrics (sin A)f(A,B,C) : (sin B)f(B,C,A) : (sin C)f(C,A,B)

Incidence
---------

:ref:`X(203) <X(203)>` lies and on these lines:

{:ref:`1 <X(1)>`, :ref:`61 <X(61)>`}, {:ref:`6 <X(6)>`, :ref:`101 <X(101)>`}, {:ref:`11 <X(11)>`, :ref:`14 <X(14)>`}, {:ref:`12 <X(12)>`, :ref:`17 <X(17)>`}, {:ref:`15 <X(15)>`, :ref:`55 <X(55)>`}, {:ref:`16 <X(16)>`, :ref:`36 <X(36)>`}, {:ref:`18 <X(18)>`, :ref:`499 <X(499)>`}, {:ref:`56 <X(56)>`, :ref:`62 <X(62)>`}, {:ref:`396 <X(396)>`, :ref:`495 <X(495)>`}, {:ref:`398 <X(398)>`, :ref:`496 <X(496)>`}

Relations
---------

* :ref:`X(203) <X(203)>` = :ref:`X(1) <X(1)>`-:term:`Ceva conjugate <ceva-conjugate>` of :ref:`X(16) <X(16)>`

Construction
------------

.. literalinclude:: model.py
   :language: python
