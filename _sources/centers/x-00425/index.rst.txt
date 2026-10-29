:order: 425
:type: center
:canonical_id: X(425)
:dependencies: X(2), X(3), X(4), X(21), X(63), X(73), X(92), X(107), X(112), X(243), X(283), X(525), X(648), X(653), X(656), X(662), X(1098), X(1172), X(1214), X(1940), X(2501), X(2651), X(2707), X(2714), X(2798), X(17923), X(18020), X(23090), X(23695), X(23999), X(25533), X(31623), X(40596), X(41349), X(43746)

.. _X(425):

X(425) = X(4)-HIRST INVERSE OF X(21)
====================================

.. figure:: x-00425.svg
   :alt: X(425) = X(4)-HIRST INVERSE OF X(21)
   :align: center

   **X(425) = X(4)-HIRST INVERSE OF X(21)** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`(u^{2} - vw)\sec A : (v^{2} - wu)\sec B : (v^{2} - uv)\sec C`, where, u : v : w = :ref:`X(283) <X(283)>`; e.g., u = u(A,B,C) = (cos A)/(cos B + cos C)

Barycentrics
~~~~~~~~~~~~

* :math:`(u^{2} - vw)\tan A : (v^{2} - wu)\tan B : (w^{2} - uv)\tan C`
* :math:`(a + b)*(a + c)*(a^2 + b^2 - c^2)*(a^2 - b^2 + c^2)*(a^6 - a^5*b - a^4*b^2 + a^3*b^3 - a^5*c + a^4*b*c + a^3*b^2*c - b^5*c - a^4*c^2 + a^3*b*c^2 + 2*a^2*b^2*c^2 - 2*a*b^3*c^2 + a^3*c^3 - 2*a*b^2*c^3 + 2*b^3*c^3 - b*c^5) : :`

* **Kimberling (6, 9, 13) Search Value:** :math:`1.875882662069`

Notes
-----

.. container:: note-item

   As a point on the Euler line, :ref:`X(425) <X(425)>` has Shinagawa coefficients ((E-2F)\ :sup:`2`\ FS\ :sup:`2`\ +$abS\ :sub:`A`\ S\ :sub:`B`\ $(2E-7F)F +3$ab$F\ :sup:`2`\ S\ :sup:`2`, (E-2F)[(E+F)F- S\ :sup:`2`]S\ :sup:`2` +3$abS\ :sub:`A`\ S\ :sub:`B`\ $[3(E+F)F-2S\ :sup:`2`]-$ab$(E+F)FS\ :sup:`2`).

Incidence
---------

:ref:`X(425) <X(425)>` lies and on these lines:

{:ref:`2 <X(2)>`, :ref:`3 <X(3)>`}, {:ref:`107 <X(107)>`, 2707}, {:ref:`243 <X(243)>`, :ref:`662 <X(662)>`}, {:ref:`653 <X(653)>`, 2651}, {1098, 1940}, {2501, 23090}, {17923, 25533}, {18020, 23999}

Relations
---------

* :ref:`X(425) <X(425)>` = X(41349)-:term:`cross conjugate <cross-conjugate>` of X(23695)
* :ref:`X(425) <X(425)>` = X(i)-:term:`isoconjugate <isoconjugate>` of X(j) for these (i,j): {:ref:`73 <X(73)>`, 43746}, {:ref:`656 <X(656)>`, 2714}
* :ref:`X(425) <X(425)>` = X(2714)-Dao conjugate of X(40596)
* :ref:`X(425) <X(425)>` = barycentric product X(i)\*X(j) for these {i,j}: {:ref:`92 <X(92)>`, 23695}, {:ref:`648 <X(648)>`, 2798}, {31623, 41349}
* :ref:`X(425) <X(425)>` = barycentric quotient X(i)/X(j) for these {i,j}: {:ref:`112 <X(112)>`, 2714}, {1172, 43746}, {2798, :ref:`525 <X(525)>`}, {23695, :ref:`63 <X(63)>`}, {41349, 1214}
* :ref:`X(425) <X(425)>` = {X(i),X(j)}-harmonic conjugate of X(k) for these (i,j,k): {}

Construction
------------

.. literalinclude:: model.py
   :language: python
