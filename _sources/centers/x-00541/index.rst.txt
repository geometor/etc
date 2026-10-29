:order: 541
:type: center
:canonical_id: X(541)
:dependencies: X(2), X(30), X(74), X(110), X(125), X(265), X(376), X(381), X(394), X(399), X(511), X(841), X(3028), X(3058), X(3426), X(3448), X(3543)

.. _X(541):

X(541) = DIRECTION OF VECTOR AX + BX + CX, where X = X(74)
==========================================================

.. figure:: x-00541.svg
   :alt: X(541) = DIRECTION OF VECTOR AX + BX + CX, where X = X(74)
   :align: center

   **X(541) = DIRECTION OF VECTOR AX + BX + CX, where X = X(74)** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`f(a,b,c) : f(b,c,a) : f(c,a,b)`, where, f(a,b,c) = (2ax - by - cz)/a, x = x(A,B,C) = 1/(cos A - 2 cos B cos C), y = x(B,C,A), z = x(C,A,B)

Notes
-----

.. container:: note-item

   Barycentrics af(a,b,c) : bf(b,c,a) : cf(c,a,b)

Incidence
---------

:ref:`X(541) <X(541)>` lies on the line at infinity.

:ref:`X(541) <X(541)>` lies and on these lines:

{:ref:`2 <X(2)>`, :ref:`74 <X(74)>`}, {:ref:`30 <X(30)>`, :ref:`511 <X(511)>`}, {:ref:`110 <X(110)>`, :ref:`376 <X(376)>`}, {:ref:`125 <X(125)>`, :ref:`381 <X(381)>`}, {:ref:`265 <X(265)>`, 3426}, {:ref:`394 <X(394)>`, :ref:`399 <X(399)>`}, {3028, 3058}, {3448, 3543}

Relations
---------

* :ref:`X(541) <X(541)>` = :term:`isogonal conjugate <isogonal-conjugate>` of :ref:`X(841) <X(841)>`

Construction
------------

.. literalinclude:: model.py
   :language: python
