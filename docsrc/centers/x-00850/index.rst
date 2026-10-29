:order: 850
:type: center
:canonical_id: X(850)
:dependencies: X(2), X(6), X(25), X(32), X(39), X(51), X(76), X(95), X(98), X(99), X(110), X(112), X(115), X(125), X(127), X(184), X(264), X(297), X(300), X(301), X(311), X(316), X(325), X(338), X(339), X(340), X(476), X(512), X(520), X(523), X(525), X(647), X(669), X(670), X(685), X(804), X(892), X(1502), X(1576), X(31296), X(36901), X(39352)

.. _X(850):

X(850) = BARYCENTRIC MULTIPLIER FOR KIEPERT HYPERBOLA
=====================================================

.. figure:: x-00850.svg
   :alt: X(850) = BARYCENTRIC MULTIPLIER FOR KIEPERT HYPERBOLA
   :align: center

   **X(850) = BARYCENTRIC MULTIPLIER FOR KIEPERT HYPERBOLA** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`(b^{2} - c^{2})/a^{3} : :`

Barycentrics
~~~~~~~~~~~~

* :math:`(b^{2} - c^{2})/a^{2} : :`
* :math:`\csc A \sin(B - C) : :`
* :math:`|AP(1)|^2 - |AU(1)|^2 : :`

* **Kimberling (6, 9, 13) Search Value:** :math:`18.041819248310`

Notes
-----

.. container:: note-item

   The barycentric product of :ref:`X(850) <X(850)>` and the circumcircle is the Kiepert hyperbola.

.. container:: note-item

   Let P1 and P2 be the two points on the de Longchamps line whose :term:`trilinear polars <trilinear-polar>` are parallel to the de Longchamps line. P1 and P2 lie on the Kiepert hyperbola and circle {:ref:`X(2) <X(2)>`, :ref:`X(98) <X(98)>`, :ref:`X(99) <X(99)>`}}. :ref:`X(850) <X(850)>` is the barycentric product P1\*P2. (:person:`Randy Hutson <randy-hutson>`, June 7, 2019)

Incidence
---------

:ref:`X(850) <X(850)>` lies and on these lines:

{:ref:`2 <X(2)>`, :ref:`647 <X(647)>`}, {:ref:`99 <X(99)>`, :ref:`476 <X(476)>`}, {:ref:`110 <X(110)>`, :ref:`685 <X(685)>`}, {:ref:`297 <X(297)>`, :ref:`525 <X(525)>`}, {:ref:`316 <X(316)>`, :ref:`512 <X(512)>`}, {:ref:`325 <X(325)>`, :ref:`523 <X(523)>`}, {:ref:`340 <X(340)>`, :ref:`520 <X(520)>`}, {:ref:`669 <X(669)>`, :ref:`804 <X(804)>`}, {:ref:`670 <X(670)>`, :ref:`892 <X(892)>`}

Relations
---------

* :ref:`X(850) <X(850)>` = :term:`isotomic conjugate <isotomic-conjugate>` of :ref:`X(110) <X(110)>`
* :ref:`X(850) <X(850)>` = :term:`complement <complement>` of X(31296)
* :ref:`X(850) <X(850)>` = :term:`anticomplement <anticomplement>` of :ref:`X(647) <X(647)>`
* :ref:`X(850) <X(850)>` = :term:`anticomplementary conjugate <anticomplementary-conjugate>` of X(39352)
* :ref:`X(850) <X(850)>` = X(i)-:term:`Ceva conjugate <ceva-conjugate>` of X(j) for these (i,j): (:ref:`2 <X(2)>`, 36901), (:ref:`76 <X(76)>`, :ref:`338 <X(338)>`), (:ref:`99 <X(99)>`, :ref:`311 <X(311)>`), (:ref:`264 <X(264)>`, :ref:`339 <X(339)>`)
* :ref:`X(850) <X(850)>` = X(i)-:term:`cross conjugate <cross-conjugate>` of X(j) for these (i,j): (:ref:`115 <X(115)>`, 1502), (:ref:`125 <X(125)>`, :ref:`2 <X(2)>`), (:ref:`338 <X(338)>`, :ref:`76 <X(76)>`), (:ref:`339 <X(339)>`, :ref:`264 <X(264)>`)
* :ref:`X(850) <X(850)>` = :term:`crosspoint <crosspoint>` of :ref:`X(95) <X(95)>` and :ref:`X(99) <X(99)>`
* :ref:`X(850) <X(850)>` = :term:`crosssum <crosssum>` of X(i) and X(j) for these (i,j): (:ref:`32 <X(32)>`, :ref:`669 <X(669)>`), (:ref:`39 <X(39)>`, :ref:`647 <X(647)>`), (:ref:`51 <X(51)>`, :ref:`512 <X(512)>`)
* :ref:`X(850) <X(850)>` = :term:`crossdifference <crossdifference>` of every pair of points on line :ref:`X(32) <X(32)>`\ \ :ref:`X(184) <X(184)>`
* :ref:`X(850) <X(850)>` = :term:`isogonal conjugate <isogonal-conjugate>` of X(1576)
* :ref:`X(850) <X(850)>` = :term:`trilinear pole <trilinear-pole>` of line :ref:`X(115) <X(115)>`\ \ :ref:`X(127) <X(127)>` (polar of :ref:`X(112) <X(112)>` wrt polar circle)
* :ref:`X(850) <X(850)>` = pole wrt polar circle of trilinear polar of :ref:`X(112) <X(112)>` (line :ref:`X(6) <X(6)>`\ \ :ref:`X(25) <X(25)>`)
* :ref:`X(850) <X(850)>` = polar conjugate of :ref:`X(112) <X(112)>`
* :ref:`X(850) <X(850)>` = intersection of trilinear polars of :ref:`X(300) <X(300)>` and :ref:`X(301) <X(301)>`
* :ref:`X(850) <X(850)>` = barycentric product :ref:`X(76) <X(76)>`\ \*\ :ref:`X(523) <X(523)>`

Construction
------------

.. literalinclude:: model.py
   :language: python
