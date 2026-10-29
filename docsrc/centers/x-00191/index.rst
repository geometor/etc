:order: 191
:type: center
:canonical_id: X(191)
:dependencies: X(1), X(2), X(3), X(6), X(8), X(9), X(10), X(20), X(21), X(30), X(35), X(36), X(37), X(40), X(46), X(54), X(58), X(72), X(79), X(109), X(165), X(188), X(190), X(201), X(267), X(329), X(366), X(442), X(498), X(501), X(502), X(643), X(661), X(960), X(1045), X(1079), X(1089), X(2605), X(5426), X(5506), X(11263), X(14450)

.. _X(191):

X(191) = X(10)-CEVA CONJUGATE OF X(1)
=====================================

.. _preamble-0005:

.. admonition:: Group Preamble — Centers X(191)-X(236)
   :class: note

   Centers :ref:`X(191) <X(191)>`-:ref:`X(236) <X(236)>` are :term:`Ceva conjugates <ceva-conjugate>`. (The P-Ceva conjugate of Q is the perspector of the :term:`cevian triangle <cevian-triangle>` of P and the :term:`anticevian triangle <anticevian-triangle>` of Q.)

.. figure:: x-00191.svg
   :alt: X(191) = X(10)-CEVA CONJUGATE OF X(1)
   :align: center

   **X(191) = X(10)-CEVA CONJUGATE OF X(1)** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`(b + c - a)(bc + ca + ab) + b^{3} + c^{3} - a^{3} : :`
* :math:`S_{A} + rR : S_{B} + rR : S_{C} + rR`

* **Kimberling (6, 9, 13) Search Value:** :math:`4.664025211173`

Linear Combinations
-------------------

* :ref:`X(191) <X(191)>` = :ref:`X(1) <X(1)>` - 2 :ref:`X(21) <X(21)>`

Notes
-----

.. container:: note-item

   Let Ia be the reflection of :ref:`X(1) <X(1)>` in the perpendicular bisector of BC, and define Ib and Ic cyclically. :ref:`X(191) <X(191)>` = :ref:`X(21) <X(21)>` of IaIbIc. (:person:`Randy Hutson <randy-hutson>`, December 2, 2017)

.. container:: note-item

   Let IaIbIc be the :term:`excentral triangle <excentral-triangle>`. Let Na be the nine-point center of BCIa, and define Nb and Nc cyclically. The lines IaNa, IbNb, IcNc concur in :ref:`X(191) <X(191)>`; c.f. X(5506). (Randy Hutson, December 2, 2017)

Incidence
---------

:ref:`X(191) <X(191)>` lies and on these lines:

{:ref:`1 <X(1)>`, :ref:`21 <X(21)>`}, {:ref:`9 <X(9)>`, :ref:`46 <X(46)>`}, {:ref:`10 <X(10)>`, :ref:`267 <X(267)>`}, {:ref:`30 <X(30)>`, :ref:`40 <X(40)>`}, {:ref:`35 <X(35)>`, :ref:`72 <X(72)>`}, {:ref:`36 <X(36)>`, :ref:`960 <X(960)>`}, {:ref:`109 <X(109)>`, :ref:`201 <X(201)>`}, {:ref:`165 <X(165)>`, 1079}, {:ref:`190 <X(190)>`, 1089}, {:ref:`329 <X(329)>`, :ref:`498 <X(498)>`}

Relations
---------

* :ref:`X(191) <X(191)>` = reflection of X(i) in X(j) for these (i,j): (:ref:`1 <X(1)>`, :ref:`21 <X(21)>`), (:ref:`79 <X(79)>`, :ref:`442 <X(442)>`)
* :ref:`X(191) <X(191)>` = :term:`isogonal conjugate <isogonal-conjugate>` of :ref:`X(267) <X(267)>`
* :ref:`X(191) <X(191)>` = :ref:`X(10) <X(10)>`-Ceva conjugate of :ref:`X(1) <X(1)>`
* :ref:`X(191) <X(191)>` = :term:`crosspoint <crosspoint>` of X(i) and X(j) for these (i,j): (:ref:`10 <X(10)>`, :ref:`502 <X(502)>`)
* :ref:`X(191) <X(191)>` = :term:`crosssum <crosssum>` of :ref:`X(58) <X(58)>` and :ref:`X(501) <X(501)>`
* :ref:`X(191) <X(191)>` = excentral-isogonal conjugate of :ref:`X(3) <X(3)>`
* :ref:`X(191) <X(191)>` = X(i)-:term:`aleph conjugate <aleph-conjugate>` of X(j) for these (i,j): (:ref:`2 <X(2)>`, :ref:`2 <X(2)>`), (:ref:`8 <X(8)>`, :ref:`20 <X(20)>`), (:ref:`10 <X(10)>`, :ref:`191 <X(191)>`), (:ref:`37 <X(37)>`, 1045), (:ref:`188 <X(188)>`, :ref:`3 <X(3)>`), (:ref:`366 <X(366)>`, :ref:`6 <X(6)>`)
* :ref:`X(191) <X(191)>` = :ref:`X(643) <X(643)>`-:term:`beth conjugate <beth-conjugate>` of :ref:`X(191) <X(191)>`
* :ref:`X(191) <X(191)>` = :term:`crossdifference <crossdifference>` of every pair of points on line :ref:`X(661) <X(661)>`\ X(2605)
* :ref:`X(191) <X(191)>` = :ref:`X(54) <X(54)>`-of-excentral-triangle
* :ref:`X(191) <X(191)>` = perspector of excentral triangle and Fuhrmann triangle
* :ref:`X(191) <X(191)>` = intersection of Euler lines of outer and inner Garcia triangles
* :ref:`X(191) <X(191)>` = {:ref:`X(1) <X(1)>`,\ :ref:`X(21) <X(21)>`}-harmonic conjugate of X(5426)
* :ref:`X(191) <X(191)>` = :term:`complement <complement>` of X(14450)
* :ref:`X(191) <X(191)>` = :term:`anticomplement <anticomplement>` of X(11263)

Construction
------------

.. literalinclude:: model.py
   :language: python
