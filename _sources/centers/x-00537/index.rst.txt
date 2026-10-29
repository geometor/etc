:order: 537
:type: center
:canonical_id: X(537)
:dependencies: X(1), X(2), X(10), X(30), X(37), X(38), X(75), X(190), X(192), X(511), X(513), X(519), X(551), X(668), X(1086), X(2382), X(3241), X(35123)

.. _X(537):

X(537) = DIRECTION OF VECTOR AX + BX + CX, where X = X(38)
==========================================================

.. figure:: x-00537.svg
   :alt: X(537) = DIRECTION OF VECTOR AX + BX + CX, where X = X(38)
   :align: center

   **X(537) = DIRECTION OF VECTOR AX + BX + CX, where X = X(38)** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`f(a,b,c) : f(b,c,a) : f(c,a,b)`, where, f(a,b,c) = (2ax - by - cz)/a, x = x(a,b,c) = b\ :sup:`2` + c\ :sup:`2`, y = x(b,c,a), z = x(c,a,b)

Notes
-----

.. container:: note-item

   Barycentrics af(a,b,c) : bf(b,c,a) : cf(c,a,b)

Incidence
---------

:ref:`X(537) <X(537)>` lies on the line at infinity.

:ref:`X(537) <X(537)>` lies and on these lines:

{:ref:`1 <X(1)>`, :ref:`190 <X(190)>`}, {:ref:`2 <X(2)>`, :ref:`38 <X(38)>`}, {:ref:`10 <X(10)>`, 1086}, {:ref:`30 <X(30)>`, :ref:`511 <X(511)>`}, {:ref:`37 <X(37)>`, :ref:`551 <X(551)>`}, {:ref:`75 <X(75)>`, :ref:`668 <X(668)>`}, {:ref:`192 <X(192)>`, 3241}

Relations
---------

* :ref:`X(537) <X(537)>` = :term:`isogonal conjugate <isogonal-conjugate>` of X(2382)
* :ref:`X(537) <X(537)>` = perspector of circumconic centered at X(35123)
* :ref:`X(537) <X(537)>` = :ref:`X(2) <X(2)>`-:term:`Ceva conjugate <ceva-conjugate>` of X(35123)
* :ref:`X(537) <X(537)>` = :ref:`X(513) <X(513)>`-:term:`Hirst inverse <hirst-inverse>` of :ref:`X(519) <X(519)>`

Construction
------------

.. literalinclude:: model.py
   :language: python
