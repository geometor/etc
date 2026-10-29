:order: 624
:type: center
:canonical_id: X(624)
:dependencies: X(2), X(3), X(5), X(13), X(14), X(15), X(16), X(17), X(30), X(83), X(141), X(299), X(301), X(303), X(316), X(395), X(532), X(619), X(622), X(623), X(625), X(630)

.. _X(624):

X(624) = COMPLEMENT OF X(16)
============================

.. figure:: x-00624.svg
   :alt: X(624) = COMPLEMENT OF X(16)
   :align: center

   **X(624) = COMPLEMENT OF X(16)** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`f(a,b,c) : f(b,c,a) : f(c,a,b)`, where, f(a,b,c) = [2(b\ :sup:`2` + c\ :sup:`2`) area - sqr(3)(a\ :sup:`2`\ S\ :sub:`A` + 2S\ :sub:`B`\ S\ :sub:`C`)]/a

* **Kimberling (6, 9, 13) Search Value:** :math:`7.336158936653`

Notes
-----

.. container:: note-item

   Trilinears F(16)/a - sin(A - π/3) : F(16)/b - sin(B - π/3) : F(16)/c - sin(C - π/3)

.. container:: note-item

   Barycentrics g(a,b,c) : g(b,c,a) : g(c,a,b), where g(a,b,c) = af(a,b,c)

Incidence
---------

:ref:`X(624) <X(624)>` lies and on these lines:

{:ref:`2 <X(2)>`, :ref:`13 <X(13)>`}, {:ref:`3 <X(3)>`, :ref:`630 <X(630)>`}, {:ref:`5 <X(5)>`, :ref:`141 <X(141)>`}, {:ref:`14 <X(14)>`, :ref:`299 <X(299)>`}, {:ref:`15 <X(15)>`, :ref:`303 <X(303)>`}, {:ref:`17 <X(17)>`, :ref:`83 <X(83)>`}, {:ref:`30 <X(30)>`, :ref:`619 <X(619)>`}, {:ref:`395 <X(395)>`, :ref:`532 <X(532)>`}

Relations
---------

* :ref:`X(624) <X(624)>` = midpoint of X(i) and X(j) for these (i,j): (:ref:`14 <X(14)>`, :ref:`299 <X(299)>`), (:ref:`15 <X(15)>`, :ref:`316 <X(316)>`), (:ref:`16 <X(16)>`, :ref:`622 <X(622)>`)
* :ref:`X(624) <X(624)>` = reflection of :ref:`X(623) <X(623)>` in :ref:`X(625) <X(625)>`
* :ref:`X(624) <X(624)>` = inverse-in-nine-point-circle of :ref:`X(623) <X(623)>`
* :ref:`X(624) <X(624)>` = :term:`complement <complement>` of :ref:`X(16) <X(16)>`
* :ref:`X(624) <X(624)>` = :term:`complementary conjugate <complementary-conjugate>` of :ref:`X(619) <X(619)>`
* :ref:`X(624) <X(624)>` = :term:`crosspoint <crosspoint>` of :ref:`X(2) <X(2)>` and :ref:`X(301) <X(301)>`
* :ref:`X(624) <X(624)>` = intersection of extended legs P(5)U(11) and U(5)P(11) of trapezoid PU(5)PU(11)

Construction
------------

.. literalinclude:: model.py
   :language: python
