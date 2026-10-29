:order: 221
:type: center
:canonical_id: X(221)
:dependencies: X(1), X(3), X(6), X(8), X(19), X(31), X(34), X(40), X(55), X(56), X(64), X(84), X(92), X(101), X(102), X(109), X(110), X(196), X(198), X(201), X(204), X(207), X(220), X(222), X(223), X(280), X(347), X(651), X(960), X(1038), X(20306)

.. _X(221):

X(221) = X(1)-CEVA CONJUGATE OF X(56)
=====================================

.. figure:: x-00221.svg
   :alt: X(221) = X(1)-CEVA CONJUGATE OF X(56)
   :align: center

   **X(221) = X(1)-CEVA CONJUGATE OF X(56)** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`(\sin^{2}A/2)(\cos B + \cos C - \cos A - 1) : :`
* :math:`(1 - \cos A)(1 + \cos A - \cos B - \cos C) : :`

* **Kimberling (6, 9, 13) Search Value:** :math:`-0.330449218124`

Notes
-----

.. container:: note-item

   Let I = :ref:`X(1) <X(1)>` = incenter, and A'B'C' = :term:`medial triangle <medial-triangle>`. Let A\ :sub:`B` = AC∩IA', and define B\ :sub:`C` and C\ :sub:`A` cyclically. Let A\ :sub:`C` = AB∩IA', and define B\ :sub:`A` and C\ :sub:`B` cyclically. Let O\ :sub:`A` be the circumcircle of AA\ :sub:`B`\ A\ :sub:`C`, and define O\ :sub:`B` and O\ :sub:`C` cyclically. Then :ref:`X(221) <X(221)>` is the radical center of O\ :sub:`A`, O\ :sub:`B`, O\ :sub:`C`. (:person:`Angel Montesdeoca <angel-montesdeoca>`, April 27, 2021)

Incidence
---------

:ref:`X(221) <X(221)>` lies and on these lines:

{:ref:`1 <X(1)>`, :ref:`84 <X(84)>`}, {:ref:`3 <X(3)>`, :ref:`102 <X(102)>`}, {:ref:`6 <X(6)>`, :ref:`19 <X(19)>`}, {:ref:`8 <X(8)>`, :ref:`651 <X(651)>`}, {:ref:`31 <X(31)>`, :ref:`56 <X(56)>`}, {:ref:`40 <X(40)>`, :ref:`223 <X(223)>`}, {:ref:`55 <X(55)>`, :ref:`64 <X(64)>`}, {:ref:`201 <X(201)>`, :ref:`220 <X(220)>`}, {:ref:`204 <X(204)>`, :ref:`207 <X(207)>`}, {:ref:`960 <X(960)>`, 1038}

Relations
---------

* :ref:`X(221) <X(221)>` = :term:`isogonal conjugate <isogonal-conjugate>` of :ref:`X(280) <X(280)>`
* :ref:`X(221) <X(221)>` = :term:`anticomplement <anticomplement>` of X(20306)
* :ref:`X(221) <X(221)>` = X(i)-:term:`Ceva conjugate <ceva-conjugate>` of X(j) for these (i,j): (:ref:`1 <X(1)>`, :ref:`56 <X(56)>`), (:ref:`222 <X(222)>`, :ref:`6 <X(6)>`), (:ref:`223 <X(223)>`, :ref:`198 <X(198)>`)
* :ref:`X(221) <X(221)>` = :term:`crosspoint <crosspoint>` of X(i) and X(j) for these (i,j): (:ref:`1 <X(1)>`, :ref:`40 <X(40)>`), (:ref:`196 <X(196)>`, :ref:`347 <X(347)>`)
* :ref:`X(221) <X(221)>` = :term:`crosssum <crosssum>` of :ref:`X(1) <X(1)>` and :ref:`X(84) <X(84)>`
* :ref:`X(221) <X(221)>` = X(i)-:term:`beth conjugate <beth-conjugate>` of X(j) for these (i,j): (:ref:`1 <X(1)>`, :ref:`34 <X(34)>`), (:ref:`40 <X(40)>`, :ref:`40 <X(40)>`), (:ref:`101 <X(101)>`, :ref:`220 <X(220)>`), (:ref:`109 <X(109)>`, :ref:`221 <X(221)>`), (:ref:`110 <X(110)>`, :ref:`3 <X(3)>`)
* :ref:`X(221) <X(221)>` = trilinear product :ref:`X(40) <X(40)>`\ \*\ :ref:`X(56) <X(56)>`
* :ref:`X(221) <X(221)>` = :ref:`X(92) <X(92)>`-:term:`isoconjugate <isoconjugate>` of X(268
* :ref:`X(221) <X(221)>` = perspector of :term:`unary cofactor triangles <unary-cofactor-triangle>` of 1st and 3rd :term:`extouch triangles <extouch-triangle>`

Construction
------------

.. literalinclude:: model.py
   :language: python
