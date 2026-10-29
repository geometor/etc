:order: 414
:type: center
:canonical_id: X(414)
:dependencies: X(21), X(29), X(410)

.. _X(414):

X(414) = EULER X(29)-3rd-SUBSTITUTION POINT
===========================================

.. figure:: x-00414.svg
   :alt: X(414) = EULER X(29)-3rd-SUBSTITUTION POINT
   :align: center

   **X(414) = EULER X(29)-3rd-SUBSTITUTION POINT** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`u^{3}(v^{2} + w^{2} - vw) : v^{3}(w^{2} + u^{2} - wu) : w^{3}(u^{2} + v^{2} - uv)`, where, u : v : w = :ref:`X(29) <X(29)>`; e.g., u = u(A,B,C) = (sec A)1/(cos B + cos C)

Barycentrics
~~~~~~~~~~~~

* :math:`au^{3}(v^{2} + w^{2} - vw) : bv^{3}(w^{2} + u^{2} - wu) : cw^{3}(u^{2} + v^{2} - uv)`
* :math:`(a + b)*(a - b - c)^3*(a + c)*(a^2 + b^2 - c^2)*(a^2 - b^2 + c^2)*(a^8*b^2 + 2*a^7*b^3 - a^6*b^4 - 4*a^5*b^5 - a^4*b^6 + 2*a^3*b^7 + a^2*b^8 - a^8*b*c - a^7*b^2*c + 3*a^6*b^3*c + 3*a^5*b^4*c - 3*a^4*b^5*c - 3*a^3*b^6*c + a^2*b^7*c + a*b^8*c + a^8*c^2 - a^7*b*c^2 - 3*a^6*b^2*c^2 + a^5*b^3*c^2 + 4*a^4*b^4*c^2 + a^3*b^5*c^2 - 3*a^2*b^6*c^2 - a*b^7*c^2 + b^8*c^2 + 2*a^7*c^3 + 3*a^6*b*c^3 + a^5*b^2*c^3 - a^2*b^5*c^3 - 3*a*b^6*c^3 - 2*b^7*c^3 - a^6*c^4 + 3*a^5*b*c^4 + 4*a^4*b^2*c^4 + 4*a^2*b^4*c^4 + 3*a*b^5*c^4 - b^6*c^4 - 4*a^5*c^5 - 3*a^4*b*c^5 + a^3*b^2*c^5 - a^2*b^3*c^5 + 3*a*b^4*c^5 + 4*b^5*c^5 - a^4*c^6 - 3*a^3*b*c^6 - 3*a^2*b^2*c^6 - 3*a*b^3*c^6 - b^4*c^6 + 2*a^3*c^7 + a^2*b*c^7 - a*b^2*c^7 - 2*b^3*c^7 + a^2*c^8 + a*b*c^8 + b^2*c^8) : :`

* **Kimberling (6, 9, 13) Search Value:** :math:`3.791063862784`

Notes
-----

.. container:: note-item

   As a point on the Euler line, :ref:`X(414) <X(414)>` has Shinagawa coefficients ([(2E-F)F-S\ :sup:`2`]FS\ :sup:`4` -$abS\ :sub:`A`\ S\ :sub:`B`\ $F\ :sup:`2`\ S\ :sup:`2` +$ab$F\ :sup:`2`\ S\ :sup:`4`, -[(3E-F)F-S\ :sup:`2`]FS\ :sup:`4` -$ab(S\ :sub:`A`\ S\ :sub:`B`)\ :sup:`3`\ $ +2$abS\ :sub:`C`\ :sup:`3`\ $FS\ :sup:`2` -4$abS\ :sub:`A`\ S\ :sub:`B`\ $F\ :sup:`2`\ S\ :sup:`2` -2$abS\ :sub:`C`\ $[(E+F)\ :sup:`2`-2S\ :sup:`2`]FS\ :sup:`2` -$ab$F\ :sup:`2`\ S\ :sup:`4`).

Relations
---------

* :ref:`X(414) <X(414)>` = {X(i),X(j)}-harmonic conjugate of X(k) for these (i,j,k): {:ref:`21 <X(21)>`, :ref:`29 <X(29)>`, :ref:`410 <X(410)>`}

Construction
------------

.. literalinclude:: model.py
   :language: python
