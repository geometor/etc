:order: 388
:type: center
:canonical_id: X(388)
:dependencies: X(1), X(2), X(3), X(4), X(5), X(7), X(8), X(10), X(11), X(12), X(20), X(29), X(35), X(36), X(55), X(57), X(65), X(79), X(108), X(153), X(171), X(201), X(329), X(354), X(355), X(376), X(381), X(406), X(442), X(452), X(495), X(496), X(498), X(603), X(612), X(750), X(938), X(942), X(956), X(958), X(960), X(984), X(999), X(1000), X(1001), X(1036), X(1037), X(1038), X(1059), X(1067), X(1106), X(1181), X(30479)

.. _X(388):

X(388) = X(1)X(4)∩X(7)X(8)
==========================

.. figure:: x-00388.svg
   :alt: X(388) = X(1)X(4)∩X(7)X(8)
   :align: center

   **X(388) = X(1)X(4)∩X(7)X(8)** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`bc[a^{2} + (b + c)^{2}]/(b + c - a)`
* :math:`1 + \cos B \cos C : 1 + \cos C \cos A : 1 + \cos A \cos B`

Barycentrics
~~~~~~~~~~~~

* :math:`[a^{2} + (b + c)^{2}]/(b + c - a)`

* **Kimberling (6, 9, 13) Search Value:** :math:`0.936658594328`

Linear Combinations
-------------------

* :ref:`X(388) <X(388)>` = 2(R/r)\*\ :ref:`X(1) <X(1)>` + 3\ :ref:`X(2) <X(2)>` - 2\ :ref:`X(3) <X(3)>`

Notes
-----

.. container:: note-item

   Let A″B″C″ be the reflection of the Mandart-incircle triangle in :ref:`X(1) <X(1)>`. A″B″C″ is homothetic to the :term:`anticomplementary triangle <anticomplementary-triangle>` at :ref:`X(388) <X(388)>`. (:person:`Randy Hutson <randy-hutson>`, September 14, 2016)

.. container:: note-item

   :ref:`X(388) <X(388)>` is the {:ref:`X(7) <X(7)>`,\ :ref:`X(8) <X(8)>`}-harmonic conjugate of :ref:`X(65) <X(65)>`.

Incidence
---------

:ref:`X(388) <X(388)>` lies and on these lines:

{:ref:`1 <X(1)>`, :ref:`4 <X(4)>`}, {:ref:`2 <X(2)>`, :ref:`12 <X(12)>`}, {:ref:`3 <X(3)>`, :ref:`495 <X(495)>`}, {:ref:`5 <X(5)>`, :ref:`999 <X(999)>`}, {:ref:`7 <X(7)>`, :ref:`8 <X(8)>`}, {:ref:`10 <X(10)>`, :ref:`57 <X(57)>`}, {:ref:`11 <X(11)>`, :ref:`153 <X(153)>`}, {:ref:`20 <X(20)>`, :ref:`55 <X(55)>`}, {:ref:`29 <X(29)>`, 1037}, {:ref:`35 <X(35)>`, :ref:`376 <X(376)>`}, {:ref:`36 <X(36)>`, :ref:`498 <X(498)>`}, {:ref:`79 <X(79)>`, :ref:`1000 <X(1000)>`}, {:ref:`108 <X(108)>`, :ref:`406 <X(406)>`}, {:ref:`171 <X(171)>`, :ref:`603 <X(603)>`}, {:ref:`201 <X(201)>`, :ref:`984 <X(984)>`}, {:ref:`329 <X(329)>`, :ref:`960 <X(960)>`}, {:ref:`354 <X(354)>`, :ref:`938 <X(938)>`}, {:ref:`355 <X(355)>`, :ref:`942 <X(942)>`}, {:ref:`381 <X(381)>`, :ref:`496 <X(496)>`}, {:ref:`442 <X(442)>`, :ref:`956 <X(956)>`}, {:ref:`452 <X(452)>`, 1001}, {:ref:`612 <X(612)>`, 1038}, {:ref:`750 <X(750)>`, 1106}, {1059, 1067}

Relations
---------

* :ref:`X(388) <X(388)>` = :term:`isogonal conjugate <isogonal-conjugate>` of X(1036)
* :ref:`X(388) <X(388)>` = :term:`anticomplement <anticomplement>` of :ref:`X(958) <X(958)>`
* :ref:`X(388) <X(388)>` = X(1181)-of-:term:`intouch triangle <intouch-triangle>`
* :ref:`X(388) <X(388)>` = perspector of ABC and 5th :term:`extouch triangle <extouch-triangle>`
* :ref:`X(388) <X(388)>` = homothetic center of anticomplementary triangle and cross-triangle of ABC and 1st Johnson-Yff triangle
* :ref:`X(388) <X(388)>` = homothetic center of 1st Johnson-Yff triangle and cross-triangle of ABC and 1st Johnson-Yff triangle
* :ref:`X(388) <X(388)>` = :term:`isotomic conjugate <isotomic-conjugate>` of X(30479)
* :ref:`X(388) <X(388)>` = homothetic center of anti-inverse-in-incircle triangle and anti-tangential midarc triangle
* :ref:`X(388) <X(388)>` = centroid of curvatures of anticomplementary circle and excircles

Construction
------------

.. literalinclude:: model.py
   :language: python
