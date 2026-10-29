:order: 446
:type: center
:canonical_id: X(446)
:dependencies: X(2), X(3), X(98), X(287), X(385), X(511)

.. _X(446):

X(446) = CROSSPOINT OF X(98) AND X(511)
=======================================

.. figure:: x-00446.svg
   :alt: X(446) = CROSSPOINT OF X(98) AND X(511)
   :align: center

   **X(446) = CROSSPOINT OF X(98) AND X(511)** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`u(v^{2} + w^{2}) : v(w^{2} + u^{2}) : w(u^{2} + v^{2})`, where, u : v : w = :ref:`X(98) <X(98)>`; e.g., u(A,B,C) = sec(A + ω)

Barycentrics
~~~~~~~~~~~~

* :math:`au(v^{2} + w^{2}) : bv(w^{2} + u^{2}) : cw(u^{2} + v^{2})`

* **Kimberling (6, 9, 13) Search Value:** :math:`28.482023066739`

Notes
-----

.. container:: note-item

   As a point on the Euler line, :ref:`X(446) <X(446)>` has Shinagawa coefficients ((E + F)\ :sup:`3`\ F - (E + F)(E - 2F)S\ :sup:`2` + S\ :sup:`4`, (E - F)(E + F)\ :sup:`3` - 2(E + F)\ :sup:`2`\ S\ :sup:`2` - S\ :sup:`4`).

Incidence
---------

:ref:`X(446) <X(446)>` lies and on these lines:

{:ref:`2 <X(2)>`, :ref:`3 <X(3)>`}

Relations
---------

* :ref:`X(446) <X(446)>` = :term:`crosspoint <crosspoint>` of :ref:`X(98) <X(98)>` and :ref:`X(511) <X(511)>`
* :ref:`X(446) <X(446)>` = :term:`crosssum <crosssum>` of X(i) and X(j) for these (i,j): (:ref:`98 <X(98)>`, :ref:`511 <X(511)>`), (:ref:`287 <X(287)>`, :ref:`385 <X(385)>`)

Construction
------------

.. literalinclude:: model.py
   :language: python
