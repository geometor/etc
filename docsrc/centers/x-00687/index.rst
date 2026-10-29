:order: 687
:type: center
:canonical_id: X(687)
:dependencies: X(4), X(107), X(110), X(249), X(250), X(648), X(686), X(6334)

.. _X(687):

X(687) = TRILINEAR POLE OF LINE X(4)X(110)
==========================================

.. figure:: x-00687.svg
   :alt: X(687) = TRILINEAR POLE OF LINE X(4)X(110)
   :align: center

   **X(687) = TRILINEAR POLE OF LINE X(4)X(110)** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`f(A,B,C): f(B,C,A) : f(C,A,B)`, where f(A,B,C) = 1/[sec B csc(A - B) + sec C csc(A - C)]

Barycentrics
~~~~~~~~~~~~

* :math:`g(A,B,C) : g(B,C,A) : g(C,A,B)`, where g(A,B,C) = sin A f(A,B,C)

* **Kimberling (6, 9, 13) Search Value:** :math:`-2.864702884868`

Incidence
---------

:ref:`X(687) <X(687)>` lies and on these lines:

{:ref:`107 <X(107)>`, :ref:`250 <X(250)>`}, {:ref:`249 <X(249)>`, :ref:`648 <X(648)>`}

Relations
---------

* :ref:`X(687) <X(687)>` = :term:`isogonal conjugate <isogonal-conjugate>` of :ref:`X(686) <X(686)>`
* :ref:`X(687) <X(687)>` = :term:`isotomic conjugate <isotomic-conjugate>` of X(6334)

Construction
------------

.. literalinclude:: model.py
   :language: python
