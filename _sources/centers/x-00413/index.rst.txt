:order: 413
:type: center
:canonical_id: X(413)
:dependencies: X(2), X(3), X(21), X(29), X(409), X(13588), X(13614)

.. _X(413):

X(413) = EULER X(21)-3rd-SUBSTITUTION POINT
===========================================

.. figure:: x-00413.svg
   :alt: X(413) = EULER X(21)-3rd-SUBSTITUTION POINT
   :align: center

   **X(413) = EULER X(21)-3rd-SUBSTITUTION POINT** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`u^{3}(v^{2} + w^{2} - vw) : v^{3}(w^{2} + u^{2} - wu) : w^{3}(u^{2} + v^{2} - uv)`, where, u : v : w = :ref:`X(21) <X(21)>`; e.g., u = u(A,B,C) = 1/(cos B + cos C)

Barycentrics
~~~~~~~~~~~~

* :math:`au^{3}(v^{2} + w^{2} - vw) : bv^{3}(w^{2} + u^{2} - wu) : cw^{3}(u^{2} + v^{2} - uv)`
* :math:`a*(a + b)*(a - b - c)^3*(a + c)*(a^4 + a^3*b + a*b^3 + b^4 + a^3*c + a^2*b*c - a*b^2*c - b^3*c - a*b*c^2 + a*c^3 - b*c^3 + c^4) : :`

* **Kimberling (6, 9, 13) Search Value:** :math:`3.646041986345`

Notes
-----

.. container:: note-item

   As a point on the Euler line, :ref:`X(413) <X(413)>` has Shinagawa coefficients ($aS\ :sub:`A`\ $[($aS\ :sub:`A`\ $)\ :sup:`2` - $bcS\ :sub:`B`\ S\ :sub:`C`\ $] - 2abcFS\ :sup:`2`, -($aS\ :sub:`A`\ $ - abc)[($aS\ :sub:`A`\ $)\ :sup:`2` - $bcS\ :sub:`B`\ S\ :sub:`C`\ $] - 2[$bcS\ :sub:`B`\ S\ :sub:`C`\ $ + $aS\ :sub:`A`\ $F - abcF]S\ :sup:`2`).

Incidence
---------

:ref:`X(413) <X(413)>` lies and on these lines:

{:ref:`2 <X(2)>`, :ref:`3 <X(3)>`}

Relations
---------

* :ref:`X(413) <X(413)>` = {X(i),X(j)}-harmonic conjugate of X(k) for these (i,j,k): {:ref:`21 <X(21)>`, :ref:`29 <X(29)>`, :ref:`409 <X(409)>`}, {:ref:`21 <X(21)>`, 13614, 13588}

Construction
------------

.. literalinclude:: model.py
   :language: python
