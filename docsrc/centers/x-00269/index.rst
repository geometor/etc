:order: 269
:type: center
:canonical_id: X(269)
:dependencies: X(1), X(3), X(6), X(7), X(9), X(46), X(56), X(57), X(69), X(86), X(92), X(106), X(142), X(200), X(220), X(241), X(273), X(279), X(292), X(307), X(320), X(326), X(341), X(479), X(480), X(614), X(738), X(934), X(936), X(939), X(948), X(1020), X(1088), X(1103), X(1111), X(1802), X(4328), X(7101), X(11019)

.. _X(269):

X(269) = ISOGONAL CONJUGATE OF X(200)
=====================================

.. figure:: x-00269.svg
   :alt: X(269) = ISOGONAL CONJUGATE OF X(200)
   :align: center

   **X(269) = ISOGONAL CONJUGATE OF X(200)** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`\tan^{2}A/2 : \tan^{2}B/2 : \tan^{2}C/2`
* :math:`[a^{2} - (b - c)^{2}]^{2} : :`
* :math:`1 - \sec^2(A/2) : :`
* :math:`(1 - \cos A)/(1 + \cos A) : :`
* :math:`(1 - \sec A)/(1 + \sec A) : :`

Barycentrics
~~~~~~~~~~~~

* :math:`\sin A \tan^{2}A/2 : :`

* **Kimberling (6, 9, 13) Search Value:** :math:`0.054966828794`

Notes
-----

.. container:: note-item

   :ref:`X(269) <X(269)>` is the :term:`vertex conjugate <vertex-conjugate>` of the foci of the inellipse that is the trilinear square of the Gergonne line. The center of this inellipse is X(11019), and the Brianchon point (perspector) is X(1088). (:person:`Randy Hutson <randy-hutson>`, October 15, 2018)

.. container:: note-item

   Let A\ :sub:`1`\ B\ :sub:`1`\ C\ :sub:`1` be Gemini triangle 1. Let A' be the center of conic {A,B,C,B\ :sub:`1`,C\ :sub:`1`}}, and define B' and C' cyclically. The lines AA', BB', CC' concur in :ref:`X(269) <X(269)>`. (Randy Hutson, January 15, 2019)

Incidence
---------

:ref:`X(269) <X(269)>` lies and on these lines:

{:ref:`1 <X(1)>`, :ref:`7 <X(7)>`}, {:ref:`3 <X(3)>`, :ref:`939 <X(939)>`}, {:ref:`6 <X(6)>`, :ref:`57 <X(57)>`}, {:ref:`9 <X(9)>`, :ref:`241 <X(241)>`}, {:ref:`46 <X(46)>`, 1103}, {:ref:`56 <X(56)>`, :ref:`738 <X(738)>`}, {:ref:`69 <X(69)>`, :ref:`200 <X(200)>`}, {:ref:`86 <X(86)>`, 1088}, {:ref:`106 <X(106)>`, :ref:`934 <X(934)>`}, {:ref:`142 <X(142)>`, :ref:`948 <X(948)>`}, {:ref:`273 <X(273)>`, 1111}, {:ref:`292 <X(292)>`, 1020}, {:ref:`307 <X(307)>`, :ref:`936 <X(936)>`}, {:ref:`320 <X(320)>`, :ref:`326 <X(326)>`}, {:ref:`479 <X(479)>`, :ref:`614 <X(614)>`}

Relations
---------

* :ref:`X(269) <X(269)>` = :term:`isogonal conjugate <isogonal-conjugate>` of :ref:`X(200) <X(200)>`
* :ref:`X(269) <X(269)>` = :term:`isotomic conjugate <isotomic-conjugate>` of :ref:`X(341) <X(341)>`
* :ref:`X(269) <X(269)>` = :ref:`X(279) <X(279)>`-:term:`Ceva conjugate <ceva-conjugate>` of :ref:`X(57) <X(57)>`
* :ref:`X(269) <X(269)>` = :ref:`X(56) <X(56)>`-:term:`cross conjugate <cross-conjugate>` of :ref:`X(57) <X(57)>`
* :ref:`X(269) <X(269)>` = :term:`crosspoint <crosspoint>` of :ref:`X(279) <X(279)>` and :ref:`X(479) <X(479)>`
* :ref:`X(269) <X(269)>` = :term:`crosssum <crosssum>` of :ref:`X(220) <X(220)>` and :ref:`X(480) <X(480)>`
* :ref:`X(269) <X(269)>` = {:ref:`X(1) <X(1)>`,\ :ref:`X(7) <X(7)>`}-harmonic conjugate of X(4328)
* :ref:`X(269) <X(269)>` = polar conjugate of X(7101)
* :ref:`X(269) <X(269)>` = :ref:`X(92) <X(92)>`-:term:`isoconjugate <isoconjugate>` of X(1802)
* :ref:`X(269) <X(269)>` = trilinear square of :ref:`X(57) <X(57)>`

Construction
------------

.. literalinclude:: model.py
   :language: python
