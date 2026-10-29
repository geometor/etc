:order: 618
:type: center
:canonical_id: X(618)
:dependencies: X(2), X(3), X(5), X(13), X(14), X(15), X(17), X(30), X(39), X(61), X(99), X(140), X(141), X(298), X(395), X(396), X(532), X(542), X(616), X(619), X(620), X(623), X(627), X(629), X(630), X(635)

.. _X(618):

X(618) = COMPLEMENT OF X(13)
============================

.. figure:: x-00618.svg
   :alt: X(618) = COMPLEMENT OF X(13)
   :align: center

   **X(618) = COMPLEMENT OF X(13)** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`f(a,b,c) : f(b,c,a) : f(c,a,b)`, where, f(a,b,c) = [2S\ :sub:`B`\ S\ :sub:`C` + 5S\ :sub:`A`\ a\ :sup:`2` + 2 sqr(3)(b\ :sup:`2` + c\ :sup:`2`) area]/a

* **Kimberling (6, 9, 13) Search Value:** :math:`3.906080612831`

Notes
-----

.. container:: note-item

   Trilinears F(13)/a - csc(A + π/3) : F(13)/b - csc(B + π/3) : F(13)/c - csc(C + π/3)

.. container:: note-item

   Barycentrics g(a,b,c) : g(b,c,a) : g(c,a,b), where g(a,b,c) = af(a,b,c)

Incidence
---------

:ref:`X(618) <X(618)>` lies and on these lines:

{:ref:`2 <X(2)>`, :ref:`13 <X(13)>`}, {:ref:`3 <X(3)>`, :ref:`635 <X(635)>`}, {:ref:`5 <X(5)>`, :ref:`629 <X(629)>`}, {:ref:`14 <X(14)>`, :ref:`99 <X(99)>`}, {:ref:`15 <X(15)>`, :ref:`298 <X(298)>`}, {:ref:`30 <X(30)>`, :ref:`623 <X(623)>`}, {:ref:`39 <X(39)>`, :ref:`395 <X(395)>`}, {:ref:`61 <X(61)>`, :ref:`627 <X(627)>`}, {:ref:`140 <X(140)>`, :ref:`630 <X(630)>`}, {:ref:`141 <X(141)>`, :ref:`542 <X(542)>`}, {:ref:`396 <X(396)>`, :ref:`532 <X(532)>`}

Relations
---------

* :ref:`X(618) <X(618)>` = midpoint of X(i) and X(j) for these (i,j): (:ref:`13 <X(13)>`, :ref:`616 <X(616)>`), (:ref:`14 <X(14)>`, :ref:`99 <X(99)>`), (:ref:`15 <X(15)>`, :ref:`298 <X(298)>`)
* :ref:`X(618) <X(618)>` = reflection of :ref:`X(619) <X(619)>` in :ref:`X(620) <X(620)>`
* :ref:`X(618) <X(618)>` = :term:`complementary conjugate <complementary-conjugate>` of :ref:`X(623) <X(623)>`
* :ref:`X(618) <X(618)>` = :ref:`X(2) <X(2)>`-:term:`Ceva conjugate <ceva-conjugate>` of :ref:`X(396) <X(396)>`
* :ref:`X(618) <X(618)>` = :term:`crosspoint <crosspoint>` of :ref:`X(2) <X(2)>` and :ref:`X(298) <X(298)>`
* :ref:`X(618) <X(618)>` = :ref:`X(13) <X(13)>`-of-medial-triangle
* :ref:`X(618) <X(618)>` = perspector of circumconic centered at :ref:`X(396) <X(396)>`
* :ref:`X(618) <X(618)>` = center of circumconic that is locus of :term:`trilinear poles <trilinear-pole>` of lines passing through :ref:`X(396) <X(396)>`
* :ref:`X(618) <X(618)>` = :ref:`X(2) <X(2)>`-Ceva conjugate of :ref:`X(396) <X(396)>`
* :ref:`X(618) <X(618)>` = :ref:`X(15) <X(15)>`-of-:ref:`X(2) <X(2)>`-Brocard-triangle
* :ref:`X(618) <X(618)>` = outer Napoleon :term:`isogonal conjugate <isogonal-conjugate>` of :ref:`X(17) <X(17)>`

Construction
------------

.. literalinclude:: model.py
   :language: python
