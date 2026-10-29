:order: 311
:type: center
:canonical_id: X(311)
:dependencies: X(2), X(4), X(5), X(22), X(53), X(54), X(69), X(76), X(95), X(99), X(141), X(157), X(290), X(300), X(301), X(302), X(303), X(305), X(308), X(324), X(338), X(343), X(512), X(570), X(1007), X(1994), X(2623), X(8882), X(23158)

.. _X(311):

X(311) = ISOTOMIC CONJUGATE OF X(54)
====================================

.. figure:: x-00311.svg
   :alt: X(311) = ISOTOMIC CONJUGATE OF X(54)
   :align: center

   **X(311) = ISOTOMIC CONJUGATE OF X(54)** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`\csc^{2}A \cos(B - C) : :`

Barycentrics
~~~~~~~~~~~~

* :math:`\csc A \cos(B - C) : \csc B \cos(C - A) : \csc C \cos(A - B)`

* **Kimberling (6, 9, 13) Search Value:** :math:`2.175140143881`

Notes
-----

.. container:: note-item

   Let O\ :sub:`A`\ O\ :sub:`B`\ O\ :sub:`C` be the Kosnita triangle. Let A' be the :term:`trilinear pole <trilinear-pole>` of line O\ :sub:`B`\ O\ :sub:`C`, and define B' and C' cyclically. The lines AA', BB', CC' concur in X(1994). Let A″ be the trilinear pole of line B'C', and define B″and C″ cyclically. The lines AA″, BB″, CC″ concur in :ref:`X(311) <X(311)>`. (:person:`Randy Hutson <randy-hutson>`, November 30, 2018)

Incidence
---------

:ref:`X(311) <X(311)>` lies and on these lines:

{:ref:`2 <X(2)>`, :ref:`570 <X(570)>`}, {:ref:`4 <X(4)>`, :ref:`69 <X(69)>`}, {:ref:`22 <X(22)>`, :ref:`157 <X(157)>`}, {:ref:`53 <X(53)>`, :ref:`324 <X(324)>`}, {:ref:`95 <X(95)>`, :ref:`99 <X(99)>`}, {:ref:`141 <X(141)>`, :ref:`338 <X(338)>`}, {:ref:`290 <X(290)>`, :ref:`308 <X(308)>`}, {:ref:`300 <X(300)>`, :ref:`303 <X(303)>`}, {:ref:`301 <X(301)>`, :ref:`302 <X(302)>`}, {:ref:`305 <X(305)>`, 1007}

Relations
---------

* :ref:`X(311) <X(311)>` = :term:`isotomic conjugate <isotomic-conjugate>` of :ref:`X(54) <X(54)>`
* :ref:`X(311) <X(311)>` = :term:`anticomplement <anticomplement>` of :ref:`X(570) <X(570)>`
* :ref:`X(311) <X(311)>` = :term:`complement <complement>` of polar conjugate of :term:`isogonal conjugate <isogonal-conjugate>` of X(23158)
* :ref:`X(311) <X(311)>` = :ref:`X(76) <X(76)>`-:term:`Ceva conjugate <ceva-conjugate>` of :ref:`X(343) <X(343)>`
* :ref:`X(311) <X(311)>` = :term:`cevapoint <cevapoint>` of :ref:`X(5) <X(5)>` and :ref:`X(343) <X(343)>`
* :ref:`X(311) <X(311)>` = :ref:`X(5) <X(5)>`-:term:`cross conjugate <cross-conjugate>` of :ref:`X(324) <X(324)>`
* :ref:`X(311) <X(311)>` = pole wrt polar circle of :term:`trilinear polar <trilinear-polar>` of X(8882) (line :ref:`X(512) <X(512)>`\ X(2623))
* :ref:`X(311) <X(311)>` = polar conjugate of X(8882)
* :ref:`X(311) <X(311)>` = barycentric product :ref:`X(5) <X(5)>`\ \*\ :ref:`X(76) <X(76)>`

Construction
------------

.. literalinclude:: model.py
   :language: python
