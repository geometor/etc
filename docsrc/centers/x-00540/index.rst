:order: 540
:type: center
:canonical_id: X(540)
:dependencies: X(2), X(30), X(58), X(340), X(376), X(447), X(511), X(3430)

.. _X(540):

X(540) = DIRECTION OF VECTOR AX + BX + CX, where X = X(58)
==========================================================

.. figure:: x-00540.svg
   :alt: X(540) = DIRECTION OF VECTOR AX + BX + CX, where X = X(58)
   :align: center

   **X(540) = DIRECTION OF VECTOR AX + BX + CX, where X = X(58)** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`f(a,b,c) : f(b,c,a) : f(c,a,b)`, where, f(a,b,c) = (2ax - by - cz)/a, x = x(a,b,c) = a/(b + c), y = x(b,c,a), z = x(c,a,b)

Notes
-----

.. container:: note-item

   Barycentrics af(a,b,c) : bf(b,c,a) : cf(c,a,b)

Incidence
---------

:ref:`X(540) <X(540)>` lies on the line at infinity.

:ref:`X(540) <X(540)>` lies and on these lines:

{:ref:`2 <X(2)>`, :ref:`58 <X(58)>`}, {:ref:`30 <X(30)>`, :ref:`511 <X(511)>`}, {:ref:`340 <X(340)>`, :ref:`447 <X(447)>`}, {:ref:`376 <X(376)>`, 3430}

Construction
------------

.. literalinclude:: model.py
   :language: python
