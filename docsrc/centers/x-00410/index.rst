:order: 410
:type: center
:canonical_id: X(410)
:dependencies: X(1), X(2), X(3), X(21), X(29), X(73), X(414), X(823), X(1214), X(1248), X(2654), X(2656), X(2659), X(2660), X(2662), X(31623)

.. _X(410):

X(410) = EULER X(29)-1st-SUBSTITUTION POINT
===========================================

.. figure:: x-00410.svg
   :alt: X(410) = EULER X(29)-1st-SUBSTITUTION POINT
   :align: center

   **X(410) = EULER X(29)-1st-SUBSTITUTION POINT** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`u^{2} + vw : v^{2} + wu : w^{2} + uv`, where, u : v : w = :ref:`X(29) <X(29)>`; e.g., u = u(A,B,C) = (sec A)/(cos B + cos C)

Barycentrics
~~~~~~~~~~~~

* :math:`a(u^{2} + vw) : b(v^{2} + wu) : c(w^{2} + uv)`
* :math:`(a + b)*(a + c)*(a^2 + b^2 - c^2)*(a^2 - b^2 + c^2)*(a^8*b^2 - 3*a^6*b^4 + 3*a^4*b^6 - a^2*b^8 + 3*a^8*b*c - a^7*b^2*c - 5*a^6*b^3*c + a^5*b^4*c + a^4*b^5*c + a^3*b^6*c + a^2*b^7*c - a*b^8*c + a^8*c^2 - a^7*b*c^2 - 3*a^6*b^2*c^2 + a^5*b^3*c^2 + 2*a^4*b^4*c^2 + a^3*b^5*c^2 + a^2*b^6*c^2 - a*b^7*c^2 - b^8*c^2 - 5*a^6*b*c^3 + a^5*b^2*c^3 + 8*a^4*b^3*c^3 - 2*a^3*b^4*c^3 - a^2*b^5*c^3 + a*b^6*c^3 - 2*b^7*c^3 - 3*a^6*c^4 + a^5*b*c^4 + 2*a^4*b^2*c^4 - 2*a^3*b^3*c^4 + a*b^5*c^4 + b^6*c^4 + a^4*b*c^5 + a^3*b^2*c^5 - a^2*b^3*c^5 + a*b^4*c^5 + 4*b^5*c^5 + 3*a^4*c^6 + a^3*b*c^6 + a^2*b^2*c^6 + a*b^3*c^6 + b^4*c^6 + a^2*b*c^7 - a*b^2*c^7 - 2*b^3*c^7 - a^2*c^8 - a*b*c^8 - b^2*c^8) : :`

* **Kimberling (6, 9, 13) Search Value:** :math:`1.700177224401`

Notes
-----

.. container:: note-item

   As a point on the Euler line, :ref:`X(410) <X(410)>` has Shinagawa coefficients ([S\ :sup:`6` - (2E - F)FS\ :sup:`4` + 3$bc$FS\ :sup:`4` - 3$bcS\ :sub:`B`\ S\ :sub:`C`\ $FS\ :sup:`2`]F, -[S\ :sup:`4` - 4(E - F)FS\ :sup:`2` + 3$bc$FS\ :sup:`2`]FS\ :sup:`2` + $bcS\ :sub:`B`\ S\ :sub:`C`\ $[S\ :sup:`4` - 2(E - 2F)F S\ :sup:`2` + abc$aS\ :sub:`A`\ $F]).

Incidence
---------

:ref:`X(410) <X(410)>` lies and on these lines:

{:ref:`2 <X(2)>`, :ref:`3 <X(3)>`}, {:ref:`73 <X(73)>`, 2659}, {:ref:`823 <X(823)>`, 2660}

:ref:`X(410) <X(410)>` lies and on these lines:

{:ref:`1 <X(1)>`, 1248}, {:ref:`2 <X(2)>`, :ref:`3 <X(3)>`}, {:ref:`73 <X(73)>`, 2659}, {:ref:`823 <X(823)>`, 2654}

Relations
---------

* :ref:`X(410) <X(410)>` = X(2656)-:term:`Ceva conjugate <ceva-conjugate>` of X(2659)
* :ref:`X(410) <X(410)>` = barycentric product X(2662)\*X(31623)
* :ref:`X(410) <X(410)>` = barycentric quotient X(2662)/X(1214)
* :ref:`X(410) <X(410)>` = {X(i),X(j)}-harmonic conjugate of X(k) for these (i,j,k): {:ref:`21 <X(21)>`, :ref:`29 <X(29)>`, :ref:`414 <X(414)>`}
* :ref:`X(410) <X(410)>` = :term:`crosspoint <crosspoint>` of PU(82)

Construction
------------

.. literalinclude:: model.py
   :language: python
