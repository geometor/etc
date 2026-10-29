:order: 435
:type: center
:canonical_id: X(435)
:dependencies: X(2), X(3), X(399)

.. _X(435):

X(435) = EULER X(399)-6th-SUBSTITUTION POINT
============================================

.. figure:: x-00435.svg
   :alt: X(435) = EULER X(399)-6th-SUBSTITUTION POINT
   :align: center

   **X(435) = EULER X(399)-6th-SUBSTITUTION POINT** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`(v^{2} + w^{2})\sec A : (w^{2} + u^{2})\sec B : (u^{2} + v^{2})\sec C`, where u : v : w = :ref:`X(399) <X(399)>`

Barycentrics
~~~~~~~~~~~~

* :math:`(v^{2} + w^{2})\tan A : (w^{2} + u^{2})\tan B : (u^{2} + v^{2})\tan C`
* :math:`(a^2 + b^2 - c^2)*(a^2 - b^2 + c^2)*(a^{16}*b^2 - 8*a^{14}*b^4 + 28*a^{12}*b^6 - 56*a^{10}*b^8 + 70*a^8*b^{10} - 56*a^6*b^{12} + 28*a^4*b^{14} - 8*a^2*b^{16} + b^{18} + a^{16}*c^2 + 8*a^{14}*b^2*c^2 - 22*a^{12}*b^4*c^2 - 2*a^{10}*b^6*c^2 + 26*a^8*b^8*c^2 + 20*a^6*b^{10}*c^2 - 62*a^4*b^{12}*c^2 + 38*a^2*b^{14}*c^2 - 7*b^{16}*c^2 - 8*a^{14}*c^4 - 22*a^{12}*b^2*c^4 + 108*a^{10}*b^4*c^4 - 95*a^8*b^6*c^4 - 34*a^6*b^8*c^4 + 99*a^4*b^{10}*c^4 - 68*a^2*b^{12}*c^4 + 20*b^{14}*c^4 + 28*a^{12}*c^6 - 2*a^{10}*b^2*c^6 - 95*a^8*b^4*c^6 + 140*a^6*b^6*c^6 - 65*a^4*b^8*c^6 + 58*a^2*b^{10}*c^6 - 28*b^{12}*c^6 - 56*a^{10}*c^8 + 26*a^8*b^2*c^8 - 34*a^6*b^4*c^8 - 65*a^4*b^6*c^8 - 40*a^2*b^8*c^8 + 14*b^{10}*c^8 + 70*a^8*c^{10} + 20*a^6*b^2*c^{10} + 99*a^4*b^4*c^{10} + 58*a^2*b^6*c^{10} + 14*b^8*c^{10} - 56*a^6*c^{12} - 62*a^4*b^2*c^{12} - 68*a^2*b^4*c^{12} - 28*b^6*c^{12} + 28*a^4*c^{14} + 38*a^2*b^2*c^{14} + 20*b^4*c^{14} - 8*a^2*c^{16} - 7*b^2*c^{16} + c^{18}) : :`

* **Kimberling (6, 9, 13) Search Value:** :math:`14.361362948940`

Notes
-----

.. container:: note-item

   As a point on the Euler line, :ref:`X(435) <X(435)>` has Shinagawa coefficients (9E\ :sup:`2`\ F + 144EF\ :sup:`2` - 64FS\ :sup:`2`, -9E\ :sup:`3` + 89E\ :sup:`2`\ F - 128EF\ :sup:`2` - 64F\ :sup:`3` + 32(E - 2F)S\ :sup:`2`)

Incidence
---------

:ref:`X(435) <X(435)>` lies and on these lines:

{:ref:`2 <X(2)>`, :ref:`3 <X(3)>`}

Construction
------------

.. literalinclude:: model.py
   :language: python
