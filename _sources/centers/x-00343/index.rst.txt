:order: 343
:type: center
:canonical_id: X(343)
:dependencies: X(2), X(3), X(5), X(6), X(22), X(25), X(32), X(51), X(53), X(68), X(69), X(76), X(140), X(161), X(216), X(275), X(297), X(311), X(315), X(421), X(427), X(458), X(470), X(471), X(472), X(473), X(511), X(569), X(571), X(621), X(622), X(633), X(634), X(1993), X(2501), X(2917), X(7580), X(8882), X(8884)

.. _X(343):

X(343) = ISOTOMIC CONJUGATE OF X(275)
=====================================

.. figure:: x-00343.svg
   :alt: X(343) = ISOTOMIC CONJUGATE OF X(275)
   :align: center

   **X(343) = ISOTOMIC CONJUGATE OF X(275)** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`\cot A \cos(B - C) : \cot B \cos(C - A) : \cot C \cos(A - B)`

Barycentrics
~~~~~~~~~~~~

* :math:`\cos A \cos(B - C) : \cos B \cos(C - A) : \cos C \cos(A - B)`
* :math:`\tan B \tan C + 1 : :`
* :math:`(b^2 + c^2 - a^2) (a^2 (b^2 + c^2) - (b^2 - c^2)^2) : :`

* **Kimberling (6, 9, 13) Search Value:** :math:`-2.688803421769`

Notes
-----

.. container:: note-item

   :ref:`X(343) <X(343)>` is the barycentric multiplier for the Johnson circumconic. (The barycentric product of :ref:`X(343) <X(343)>` and the circumcircle is the Johnson circumconic.) (:person:`Randy Hutson <randy-hutson>`, August 19, 2019)

Incidence
---------

:ref:`X(343) <X(343)>` lies and on these lines:

{:ref:`2 <X(2)>`, :ref:`6 <X(6)>`}, {:ref:`3 <X(3)>`, :ref:`68 <X(68)>`}, {:ref:`5 <X(5)>`, :ref:`51 <X(51)>`}, {:ref:`22 <X(22)>`, :ref:`161 <X(161)>`}, {:ref:`53 <X(53)>`, :ref:`311 <X(311)>`}, {:ref:`76 <X(76)>`, :ref:`297 <X(297)>`}, {:ref:`140 <X(140)>`, :ref:`569 <X(569)>`}, {:ref:`315 <X(315)>`, :ref:`458 <X(458)>`}, {:ref:`427 <X(427)>`, :ref:`511 <X(511)>`}, {:ref:`470 <X(470)>`, :ref:`634 <X(634)>`}, {:ref:`471 <X(471)>`, :ref:`633 <X(633)>`}, {:ref:`472 <X(472)>`, :ref:`621 <X(621)>`}, {:ref:`473 <X(473)>`, :ref:`622 <X(622)>`}

Relations
---------

* :ref:`X(343) <X(343)>` = :term:`isogonal conjugate <isogonal-conjugate>` of X(8882)
* :ref:`X(343) <X(343)>` = :term:`isotomic conjugate <isotomic-conjugate>` of :ref:`X(275) <X(275)>`
* :ref:`X(343) <X(343)>` = :term:`complement <complement>` of X(1993)
* :ref:`X(343) <X(343)>` = X(i)-:term:`Ceva conjugate <ceva-conjugate>` of X(j) for these (i,j): (:ref:`76 <X(76)>`, :ref:`311 <X(311)>`), (:ref:`311 <X(311)>`, :ref:`5 <X(5)>`)
* :ref:`X(343) <X(343)>` = :ref:`X(216) <X(216)>`-:term:`cross conjugate <cross-conjugate>` of :ref:`X(5) <X(5)>`
* :ref:`X(343) <X(343)>` = :term:`crosspoint <crosspoint>` of :ref:`X(69) <X(69)>` and :ref:`X(76) <X(76)>`
* :ref:`X(343) <X(343)>` = :term:`crosssum <crosssum>` of X(i) and X(j) for these (i,j): (:ref:`6 <X(6)>`, :ref:`571 <X(571)>`), (:ref:`25 <X(25)>`, :ref:`32 <X(32)>`)
* :ref:`X(343) <X(343)>` = pole wrt polar circle of :term:`trilinear polar <trilinear-polar>` of X(8884) (line :ref:`X(421) <X(421)>`\ X(2501))
* :ref:`X(343) <X(343)>` = polar conjugate of X(8884)
* :ref:`X(343) <X(343)>` = crosspoint of :ref:`X(6) <X(6)>` and X(2917) wrt both the excentral and :term:`tangential triangles <tangential-triangle>`
* :ref:`X(343) <X(343)>` = X(7580)-of-orthic-triangle if ABC is acute

Construction
------------

.. literalinclude:: model.py
   :language: python
