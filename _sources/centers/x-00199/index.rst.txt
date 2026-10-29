:order: 199
:type: center
:canonical_id: X(199)
:dependencies: X(2), X(3), X(6), X(10), X(42), X(51), X(55), X(101), X(125), X(172), X(184), X(250), X(430), X(514), X(572), X(573), X(1030), X(8044), X(8053), X(34119)

.. _X(199):

X(199) = X(10)-CEVA CONJUGATE OF X(6)
=====================================

.. figure:: x-00199.svg
   :alt: X(199) = X(10)-CEVA CONJUGATE OF X(6)
   :align: center

   **X(199) = X(10)-CEVA CONJUGATE OF X(6)** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`f(a,b,c) : f(b,c,a) : f(c,a,b)`, where f(a,b,c) = a[b\ :sup:`4` + c\ :sup:`4` - a\ :sup:`4` + (b\ :sup:`2` + c\ :sup:`2` - a\ :sup:`2`)(bc + ca + ab)]

Barycentrics
~~~~~~~~~~~~

* :math:`af(A,B,C) : bf(B,C,A) : cf(C,A,B)`

* **Kimberling (6, 9, 13) Search Value:** :math:`13.467812089845`

Notes
-----

.. container:: note-item

   As a point on the Euler line, :ref:`X(199) <X(199)>` has Shinagawa coefficients (E + 2F + $bc$, -2E - 2F + $bc$).

.. container:: note-item

   Let I\ :sub:`A`, I\ :sub:`B`, I\ :sub:`C` be the excenters. Let (O\ :sub:`A`) be the circle tangent to the circumcircle at A and passing through I\ :sub:`A`. Let A' be the antipode of A in (O\ :sub:`A`). Let L\ :sub:`A` be the tangent to (O\ :sub:`A`) at A'. Define L\ :sub:`B` and L\ :sub:`C` cyclically. Let T\ :sub:`A` = L\ :sub:`B`\ ∩L\ :sub:`C`, and define T\ :sub:`B` and T\ :sub:`C` cyclically. Triangle T\ :sub:`A`\ T\ :sub:`B`\ T\ :sub:`C` is homothetic to the :term:`tangential triangle <tangential-triangle>` at :ref:`X(199) <X(199)>`. (:person:`Randy Hutson <randy-hutson>`, June 7, 2019)

Incidence
---------

:ref:`X(199) <X(199)>` lies and on these lines:

{:ref:`2 <X(2)>`, :ref:`3 <X(3)>`}, {:ref:`42 <X(42)>`, :ref:`172 <X(172)>`}, {:ref:`51 <X(51)>`, :ref:`572 <X(572)>`}, {:ref:`55 <X(55)>`, 1030}, {:ref:`184 <X(184)>`, :ref:`573 <X(573)>`}

Relations
---------

* :ref:`X(199) <X(199)>` = :term:`isogonal conjugate <isogonal-conjugate>` of X(8044)
* :ref:`X(199) <X(199)>` = :term:`anticomplement <anticomplement>` of X(34119)
* :ref:`X(199) <X(199)>` = :ref:`X(10) <X(10)>`-:term:`Ceva conjugate <ceva-conjugate>` of :ref:`X(6) <X(6)>`
* :ref:`X(199) <X(199)>` = :term:`crosspoint <crosspoint>` of :ref:`X(101) <X(101)>` and :ref:`X(250) <X(250)>`
* :ref:`X(199) <X(199)>` = :term:`crosssum <crosssum>` of :ref:`X(125) <X(125)>` and :ref:`X(514) <X(514)>`
* :ref:`X(199) <X(199)>` = tangential isogonal conjugate of X(8053)
* :ref:`X(199) <X(199)>` = orthic-to-tangential :term:`similarity image <similarity-image>` of :ref:`X(430) <X(430)>`

Construction
------------

.. literalinclude:: model.py
   :language: python
