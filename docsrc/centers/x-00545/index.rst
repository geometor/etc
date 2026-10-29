:order: 545
:type: center
:canonical_id: X(545)
:dependencies: X(2), X(30), X(44), X(45), X(63), X(190), X(321), X(511), X(514), X(519), X(1227), X(1266), X(2161), X(2384), X(35121), X(35168)

.. _X(545):

X(545) = DIRECTION OF VECTOR AX + BX + CX, where X = X(190)
===========================================================

.. figure:: x-00545.svg
   :alt: X(545) = DIRECTION OF VECTOR AX + BX + CX, where X = X(190)
   :align: center

   **X(545) = DIRECTION OF VECTOR AX + BX + CX, where X = X(190)** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`f(a,b,c) : f(b,c,a) : f(c,a,b)`, where, f(a,b,c) = (2ax - by - cz)/a, x = x(a,b,c) = bc/(b - c), y = x(b,c,a), z = x(c,a,b)

Notes
-----

.. container:: note-item

   Barycentrics 2 a^2 - b^2 - c^2 - 2 a b - 2 a c + 4 b c : :

Incidence
---------

:ref:`X(545) <X(545)>` lies on the line at infinity.

:ref:`X(545) <X(545)>` lies and on these lines:

{:ref:`2 <X(2)>`, :ref:`45 <X(45)>`}, {:ref:`30 <X(30)>`, :ref:`511 <X(511)>`}, {:ref:`44 <X(44)>`, 1266}, {:ref:`63 <X(63)>`, 2161}, {:ref:`321 <X(321)>`, 1227}

Relations
---------

* :ref:`X(545) <X(545)>` = :term:`isogonal conjugate <isogonal-conjugate>` of X(2384)
* :ref:`X(545) <X(545)>` = :term:`isotomic conjugate <isotomic-conjugate>` of X(35168)
* :ref:`X(545) <X(545)>` = :ref:`X(2) <X(2)>`-:term:`Ceva conjugate <ceva-conjugate>` of X(35121)
* :ref:`X(545) <X(545)>` = :ref:`X(514) <X(514)>`-:term:`Hirst inverse <hirst-inverse>` of :ref:`X(519) <X(519)>`
* :ref:`X(545) <X(545)>` = perspector of circumconic centered at X(35121)

Construction
------------

.. literalinclude:: model.py
   :language: python
