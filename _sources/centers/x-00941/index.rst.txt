:order: 941
:type: center
:canonical_id: X(941)
:dependencies: X(1), X(2), X(6), X(8), X(9), X(21), X(37), X(42), X(63), X(81), X(84), X(111), X(314), X(512), X(573), X(581), X(650), X(931), X(940), X(967), X(4185), X(10472), X(34259), X(34284)

.. _X(941):

X(941) = ISOGONAL CONJUGATE OF X(940)
=====================================

.. figure:: x-00941.svg
   :alt: X(941) = ISOGONAL CONJUGATE OF X(940)
   :align: center

   **X(941) = ISOGONAL CONJUGATE OF X(940)** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`f(a,b,c) : f(b,c,a) : f(c,a,b),`, where f(a,b,c) = 1/[a\ :sup:`2` + a(b + c) + 2bc]

Barycentrics
~~~~~~~~~~~~

* :math:`g(a,b,c) : g(b,c,a) : g(c,a,b)`, where g(a,b,c) = af(a,b,c)

* **Kimberling (6, 9, 13) Search Value:** :math:`1.824565164969`

Incidence
---------

:ref:`X(941) <X(941)>` lies and on these lines:

{:ref:`1 <X(1)>`, :ref:`573 <X(573)>`}, {:ref:`2 <X(2)>`, :ref:`314 <X(314)>`}, {:ref:`6 <X(6)>`, :ref:`21 <X(21)>`}, {:ref:`8 <X(8)>`, :ref:`37 <X(37)>`}, {:ref:`9 <X(9)>`, :ref:`42 <X(42)>`}, {:ref:`81 <X(81)>`, :ref:`967 <X(967)>`}, {:ref:`84 <X(84)>`, :ref:`581 <X(581)>`}, {:ref:`111 <X(111)>`, :ref:`931 <X(931)>`}

Relations
---------

* :ref:`X(941) <X(941)>` = :term:`isogonal conjugate <isogonal-conjugate>` of :ref:`X(940) <X(940)>`
* :ref:`X(941) <X(941)>` = :term:`isotomic conjugate <isotomic-conjugate>` of X(34284)
* :ref:`X(941) <X(941)>` = :term:`anticomplement <anticomplement>` of X(10472)
* :ref:`X(941) <X(941)>` = polar conjugate of isotomic conjugate of X(34259)
* :ref:`X(941) <X(941)>` = :term:`trilinear pole <trilinear-pole>` of line :ref:`X(512) <X(512)>`\ \ :ref:`X(650) <X(650)>`
* :ref:`X(941) <X(941)>` = :ref:`X(63) <X(63)>`-:term:`isoconjugate <isoconjugate>` of X(4185)

Construction
------------

.. literalinclude:: model.py
   :language: python
