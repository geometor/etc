:order: 438
:type: center
:canonical_id: X(438)
:dependencies: X(2), X(3), X(204), X(5895), X(6330), X(35711), X(42287)

.. _X(438):

X(438) = EULER X(204)-8th-SUBSTITUTION POINT
============================================

.. figure:: x-00438.svg
   :alt: X(438) = EULER X(204)-8th-SUBSTITUTION POINT
   :align: center

   **X(438) = EULER X(204)-8th-SUBSTITUTION POINT** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`(u^{2} + vw)\csc A : (v^{2} + wu)\csc B : (w^{2} + uv)\csc C`, where, u : v : w = :ref:`X(204) <X(204)>`; e.g., u(A,B,C) = (tan A)(tan B + tan C - tan A)

Barycentrics
~~~~~~~~~~~~

* :math:`u^{2} + vw : v^{2} + wu : w^{2} + uv`
* :math:`(a^2 + b^2 - c^2)*(a^2 - b^2 + c^2)*(5*a^{12} - 7*a^{10}*b^2 - 8*a^8*b^4 + 18*a^6*b^6 - 11*a^4*b^8 + 5*a^2*b^{10} - 2*b^{12} - 7*a^{10}*c^2 + 26*a^8*b^2*c^2 - 18*a^6*b^4*c^2 - 16*a^4*b^6*c^2 + 17*a^2*b^8*c^2 - 2*b^{10}*c^2 - 8*a^8*c^4 - 18*a^6*b^2*c^4 + 54*a^4*b^4*c^4 - 22*a^2*b^6*c^4 - 6*b^8*c^4 + 18*a^6*c^6 - 16*a^4*b^2*c^6 - 22*a^2*b^4*c^6 + 20*b^6*c^6 - 11*a^4*c^8 + 17*a^2*b^2*c^8 - 6*b^4*c^8 + 5*a^2*c^{10} - 2*b^2*c^{10} - 2*c^{12}) : :`

* **Kimberling (6, 9, 13) Search Value:** :math:`1.578456191935`

Notes
-----

.. container:: note-item

   As a point on the Euler line, :ref:`X(438) <X(438)>` has Shinagawa coefficients (4(E + F)\ :sup:`2`\ F\ :sup:`2` - (E + 3F)FS\ :sup:`2`, -[4(E - F)F - S\ :sup:`2`]S\ :sup:`2`)

Incidence
---------

:ref:`X(438) <X(438)>` lies and on these lines:

{:ref:`2 <X(2)>`, :ref:`3 <X(3)>`}, {5895, 6330}, {35711, 42287}

Construction
------------

.. literalinclude:: model.py
   :language: python
