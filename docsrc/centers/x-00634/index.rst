:order: 634
:type: center
:canonical_id: X(634)
:dependencies: X(2), X(3), X(4), X(5), X(13), X(17), X(18), X(20), X(61), X(62), X(69), X(140), X(141), X(298), X(299), X(303), X(343), X(394), X(397), X(398), X(470), X(471), X(524), X(617), X(624), X(628), X(635), X(636), X(3443)

.. _X(634):

X(634) = ANTICOMPLEMENT OF X(62)
================================

.. figure:: x-00634.svg
   :alt: X(634) = ANTICOMPLEMENT OF X(62)
   :align: center

   **X(634) = ANTICOMPLEMENT OF X(62)** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`f(a,b,c) : f(b,c,a) : f(c,a,b)`, where f(a,b,c) = (S\ :sub:`B`\ S\ :sub:`C` - 2 sqr(3) S\ :sub:`A` area)/a

* **Kimberling (6, 9, 13) Search Value:** :math:`8.637509400092`

Notes
-----

.. container:: note-item

   Trilinears F(62)/a + 2 cos(A + π/3) : F(62)/b + 2 cos(B + π/3) : F(62)/c + 2 cos(C + π/3)

.. container:: note-item

   Barycentrics g(a,b,c) : g(b,c,a) : g(c,a,b), where g(a,b,c) = af(a,b,c)

Incidence
---------

:ref:`X(634) <X(634)>` lies and on these lines:

{:ref:`2 <X(2)>`, :ref:`17 <X(17)>`}, {:ref:`3 <X(3)>`, :ref:`299 <X(299)>`}, {:ref:`4 <X(4)>`, :ref:`69 <X(69)>`}, {:ref:`5 <X(5)>`, :ref:`298 <X(298)>`}, {:ref:`13 <X(13)>`, :ref:`635 <X(635)>`}, {:ref:`18 <X(18)>`, :ref:`624 <X(624)>`}, {:ref:`20 <X(20)>`, :ref:`617 <X(617)>`}, {:ref:`140 <X(140)>`, :ref:`303 <X(303)>`}, {:ref:`141 <X(141)>`, :ref:`397 <X(397)>`}, {:ref:`343 <X(343)>`, :ref:`470 <X(470)>`}, {:ref:`394 <X(394)>`, :ref:`471 <X(471)>`}, {:ref:`398 <X(398)>`, :ref:`524 <X(524)>`}

Relations
---------

* :ref:`X(634) <X(634)>` = reflection of X(i) in X(j) for these (i,j): (:ref:`62 <X(62)>`, :ref:`636 <X(636)>`), (:ref:`61 <X(61)>`, :ref:`635 <X(635)>`)
* :ref:`X(634) <X(634)>` = :term:`isogonal conjugate <isogonal-conjugate>` of X(3443)
* :ref:`X(634) <X(634)>` = :term:`anticomplement <anticomplement>` of :ref:`X(62) <X(62)>`
* :ref:`X(634) <X(634)>` = :term:`anticomplementary conjugate <anticomplementary-conjugate>` of :ref:`X(628) <X(628)>`

Construction
------------

.. literalinclude:: model.py
   :language: python
