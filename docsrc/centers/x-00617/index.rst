:order: 617
:type: center
:canonical_id: X(617)
:dependencies: X(2), X(3), X(4), X(13), X(14), X(16), X(20), X(30), X(69), X(74), X(99), X(148), X(298), X(299), X(302), X(303), X(381), X(533), X(549), X(616), X(619), X(622), X(628), X(634), X(3441), X(39133)

.. _X(617):

X(617) = ANTICOMPLEMENT OF X(14)
================================

.. figure:: x-00617.svg
   :alt: X(617) = ANTICOMPLEMENT OF X(14)
   :align: center

   **X(617) = ANTICOMPLEMENT OF X(14)** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`f(a,b,c) : f(b,c,a) : f(c,a,b)`, where f(a,b,c) = [S\ :sub:`B`\ S\ :sub:`C` - 2S\ :sub:`A`\ (a\ :sup:`2` - sqr(3) area)]/a
* :math:`F(14)/a - 2 \csc(A - \pi /3) : F(14)/b - 2 \csc(B - \pi /3) : F(14)/c - 2 \csc(C - \pi /3)`

* **Kimberling (6, 9, 13) Search Value:** :math:`-0.858757166561`

Notes
-----

.. container:: note-item

   Let O\ :sub:`A` be the circle centered at the A-vertex of the inner Napoleon triangle and passing through A; define O\ :sub:`B` and O\ :sub:`C` cyclically. :ref:`X(617) <X(617)>` is the radical center of O\ :sub:`A`, O\ :sub:`B`, O\ :sub:`C`. (:person:`Randy Hutson <randy-hutson>`, August 30, 2020)

Incidence
---------

:ref:`X(617) <X(617)>` lies on the Neuberg cubic and on these lines:

{:ref:`2 <X(2)>`, :ref:`14 <X(14)>`}, {:ref:`3 <X(3)>`, :ref:`298 <X(298)>`}, {:ref:`4 <X(4)>`, :ref:`628 <X(628)>`}, {:ref:`13 <X(13)>`, :ref:`148 <X(148)>`}, {:ref:`16 <X(16)>`, :ref:`533 <X(533)>`}, {:ref:`20 <X(20)>`, :ref:`634 <X(634)>`}, {:ref:`30 <X(30)>`, :ref:`299 <X(299)>`}, {:ref:`69 <X(69)>`, :ref:`74 <X(74)>`}, {:ref:`302 <X(302)>`, :ref:`549 <X(549)>`}, {:ref:`303 <X(303)>`, :ref:`381 <X(381)>`}

Relations
---------

* :ref:`X(617) <X(617)>` = reflection of X(i) in X(j) for these (i,j): (:ref:`14 <X(14)>`, :ref:`619 <X(619)>`), (:ref:`148 <X(148)>`, :ref:`13 <X(13)>`), (:ref:`616 <X(616)>`, :ref:`99 <X(99)>`), (:ref:`622 <X(622)>`, :ref:`299 <X(299)>`)
* :ref:`X(617) <X(617)>` = :term:`isogonal conjugate <isogonal-conjugate>` of X(3441)
* :ref:`X(617) <X(617)>` = :term:`anticomplement <anticomplement>` of :ref:`X(14) <X(14)>`
* :ref:`X(617) <X(617)>` = :term:`anticomplementary conjugate <anticomplementary-conjugate>` of :ref:`X(622) <X(622)>`
* :ref:`X(617) <X(617)>` = antigonal conjugate of X(39133)
* :ref:`X(617) <X(617)>` = :ref:`X(30) <X(30)>`-:term:`Ceva conjugate <ceva-conjugate>` of :ref:`X(616) <X(616)>`
* :ref:`X(617) <X(617)>` = :ref:`X(299) <X(299)>`-Ceva conjugate of :ref:`X(2) <X(2)>`

Construction
------------

.. literalinclude:: model.py
   :language: python
