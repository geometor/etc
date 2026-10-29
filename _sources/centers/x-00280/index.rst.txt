:order: 280
:type: center
:canonical_id: X(280)
:dependencies: X(1), X(2), X(7), X(8), X(20), X(21), X(48), X(75), X(78), X(84), X(189), X(196), X(221), X(253), X(268), X(281), X(282), X(285), X(309), X(318), X(341), X(345), X(347), X(521), X(1043), X(3239)

.. _X(280):

X(280) = X(1)-CROSS CONJUGATE OF X(8)
=====================================

.. figure:: x-00280.svg
   :alt: X(280) = X(1)-CROSS CONJUGATE OF X(8)
   :align: center

   **X(280) = X(1)-CROSS CONJUGATE OF X(8)** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`(\csc^{2}A/2)/(-1 - \cos A + \cos B + \cos C)`

* **Kimberling (6, 9, 13) Search Value:** :math:`5.034628048323`

Notes
-----

.. container:: note-item

   Let Ea be the ellipse passing through A, and with foci at B and C (the A-Soddy ellipse). Let La be the polar of :ref:`X(20) <X(20)>` with respect to Ea. Define Lb and Lc cyclically. Let A' = Lb∩Lc, B' = Lc∩La, C' = La∩Lb. The lines AA', BB', CC' concur in :ref:`X(280) <X(280)>`. (:person:`Randy Hutson <randy-hutson>`, September 14, 2016)

Incidence
---------

:ref:`X(280) <X(280)>` lies and on these lines:

{:ref:`2 <X(2)>`, :ref:`318 <X(318)>`}, {:ref:`7 <X(7)>`, :ref:`253 <X(253)>`}, {:ref:`8 <X(8)>`, :ref:`20 <X(20)>`}, {:ref:`21 <X(21)>`, :ref:`268 <X(268)>`}, {:ref:`75 <X(75)>`, :ref:`309 <X(309)>`}, {:ref:`78 <X(78)>`, :ref:`282 <X(282)>`}, {:ref:`285 <X(285)>`, 1043}, {:ref:`341 <X(341)>`, :ref:`345 <X(345)>`}

Relations
---------

* :ref:`X(280) <X(280)>` = :term:`isogonal conjugate <isogonal-conjugate>` of :ref:`X(221) <X(221)>`
* :ref:`X(280) <X(280)>` = :term:`isotomic conjugate <isotomic-conjugate>` of :ref:`X(347) <X(347)>`
* :ref:`X(280) <X(280)>` = :ref:`X(309) <X(309)>`-:term:`Ceva conjugate <ceva-conjugate>` of :ref:`X(189) <X(189)>`
* :ref:`X(280) <X(280)>` = :term:`cevapoint <cevapoint>` of :ref:`X(1) <X(1)>` and :ref:`X(84) <X(84)>`
* :ref:`X(280) <X(280)>` = X(i)-:term:`cross conjugate <cross-conjugate>` of X(j) for these (i,j): (:ref:`1 <X(1)>`, :ref:`8 <X(8)>`), (:ref:`281 <X(281)>`, :ref:`2 <X(2)>`), (:ref:`282 <X(282)>`, :ref:`189 <X(189)>`)
* :ref:`X(280) <X(280)>` = pole wrt polar circle of :term:`trilinear polar <trilinear-polar>` of :ref:`X(196) <X(196)>`
* :ref:`X(280) <X(280)>` = :ref:`X(48) <X(48)>`-:term:`isoconjugate <isoconjugate>` (polar conjugate) of :ref:`X(196) <X(196)>`
* :ref:`X(280) <X(280)>` = :term:`trilinear pole <trilinear-pole>` of line :ref:`X(521) <X(521)>`\ X(3239) (the radical axis of circumcircle and Mandart circle, and the Monge line of the nine-point circles of the A-, B- and C-:term:`extouch triangles <extouch-triangle>`)

Construction
------------

.. literalinclude:: model.py
   :language: python
