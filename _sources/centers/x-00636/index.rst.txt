:order: 636
:type: center
:canonical_id: X(636)
:dependencies: X(2), X(3), X(5), X(14), X(15), X(17), X(18), X(61), X(62), X(140), X(141), X(298), X(299), X(398), X(533), X(618), X(619), X(628), X(630), X(633), X(634)

.. _X(636):

X(636) = COMPLEMENT OF X(62)
============================

.. figure:: x-00636.svg
   :alt: X(636) = COMPLEMENT OF X(62)
   :align: center

   **X(636) = COMPLEMENT OF X(62)** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`f(a,b,c) : f(b,c,a) : f(c,a,b)`, where f(a,b,c) = [2S\ :sub:`B`\ S\ :sub:`C` + S\ :sub:`A`\ a\ :sup:`2` - 2 sqr(3) (b\ :sup:`2` + c\ :sup:`2`) area]/a

* **Kimberling (6, 9, 13) Search Value:** :math:`4.131403944390`

Notes
-----

.. container:: note-item

   Trilinears F(62)/a + cos(A + π/3) : F(62)/b + cos(B + π/3) : F(62)/c + cos(C + π/3)

.. container:: note-item

   Barycentrics g(a,b,c) : g(b,c,a) : g(c,a,b), where g(a,b,c) = af(a,b,c)

Incidence
---------

:ref:`X(636) <X(636)>` lies and on these lines:

{:ref:`2 <X(2)>`, :ref:`17 <X(17)>`}, {:ref:`3 <X(3)>`, :ref:`619 <X(619)>`}, {:ref:`5 <X(5)>`, :ref:`141 <X(141)>`}, {:ref:`14 <X(14)>`, :ref:`633 <X(633)>`}, {:ref:`15 <X(15)>`, :ref:`628 <X(628)>`}, {:ref:`18 <X(18)>`, :ref:`298 <X(298)>`}, {:ref:`61 <X(61)>`, :ref:`299 <X(299)>`}, {:ref:`140 <X(140)>`, :ref:`618 <X(618)>`}, {:ref:`398 <X(398)>`, :ref:`533 <X(533)>`}

Relations
---------

* :ref:`X(636) <X(636)>` = midpoint of :ref:`X(62) <X(62)>` and :ref:`X(634) <X(634)>`
* :ref:`X(636) <X(636)>` = :term:`complement <complement>` of :ref:`X(62) <X(62)>`
* :ref:`X(636) <X(636)>` = :term:`complementary conjugate <complementary-conjugate>` of :ref:`X(630) <X(630)>`

Construction
------------

.. literalinclude:: model.py
   :language: python
