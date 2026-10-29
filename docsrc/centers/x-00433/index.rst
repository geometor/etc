:order: 433
:type: center
:canonical_id: X(433)
:dependencies: X(2), X(3), X(159)

.. _X(433):

X(433) = EULER X(159)-6th-SUBSTITUTION POINT
============================================

.. figure:: x-00433.svg
   :alt: X(433) = EULER X(159)-6th-SUBSTITUTION POINT
   :align: center

   **X(433) = EULER X(159)-6th-SUBSTITUTION POINT** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`(v^{2} + w^{2})\sec A : (w^{2} + u^{2})\sec B : (u^{2} + v^{2})\sec C`, where u : v : w = :ref:`X(159) <X(159)>`

Barycentrics
~~~~~~~~~~~~

* :math:`(v^{2} + w^{2})\tan A : (w^{2} + u^{2})\tan B : (u^{2} + v^{2})\tan C`
* :math:`(a^2 + b^2 - c^2)*(a^2 - b^2 + c^2)*(a^{12}*b^2 + 2*a^{10}*b^4 - a^8*b^6 - 4*a^6*b^8 - a^4*b^{10} + 2*a^2*b^{12} + b^{14} + a^{12}*c^2 - 4*a^{10}*b^2*c^2 + a^8*b^4*c^2 + 8*a^6*b^6*c^2 - 5*a^4*b^8*c^2 - 4*a^2*b^{10}*c^2 + 3*b^{12}*c^2 + 2*a^{10}*c^4 + a^8*b^2*c^4 - 8*a^6*b^4*c^4 + 6*a^4*b^6*c^4 - 2*a^2*b^8*c^4 + b^{10}*c^4 - a^8*c^6 + 8*a^6*b^2*c^6 + 6*a^4*b^4*c^6 + 8*a^2*b^6*c^6 - 5*b^8*c^6 - 4*a^6*c^8 - 5*a^4*b^2*c^8 - 2*a^2*b^4*c^8 - 5*b^6*c^8 - a^4*c^{10} - 4*a^2*b^2*c^{10} + b^4*c^{10} + 2*a^2*c^{12} + 3*b^2*c^{12} + c^{14}) : :`

* **Kimberling (6, 9, 13) Search Value:** :math:`8.967335720280`

Notes
-----

.. container:: note-item

   As a point on the Euler line, :ref:`X(433) <X(433)>` has Shinagawa coefficients (4(E + F)\ :sup:`3`\ F\ :sup:`2` - E\ :sup:`2`\ FS\ :sup:`2`, (E + F)[4(E + F)\ :sup:`3`\ F - (E + 8F)ES\ :sup:`2`]).

Incidence
---------

:ref:`X(433) <X(433)>` lies and on these lines:

{:ref:`2 <X(2)>`, :ref:`3 <X(3)>`}

Construction
------------

.. literalinclude:: model.py
   :language: python
