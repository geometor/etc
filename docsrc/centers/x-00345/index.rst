:order: 345
:type: center
:canonical_id: X(345)
:dependencies: X(2), X(8), X(21), X(22), X(37), X(57), X(63), X(69), X(78), X(100), X(190), X(219), X(278), X(280), X(304), X(306), X(312), X(329), X(332), X(341), X(348), X(498), X(608), X(728), X(1040), X(1089), X(1118), X(3772), X(30699)

.. _X(345):

X(345) = ISOTOMIC CONJUGATE OF X(278)
=====================================

.. figure:: x-00345.svg
   :alt: X(345) = ISOTOMIC CONJUGATE OF X(278)
   :align: center

   **X(345) = ISOTOMIC CONJUGATE OF X(278)** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`(\csc A)/(1 - \sec A) : (\csc B)/(1 - \sec B) : (\csc C)/(1 - \sec C)`
* :math:`bc(b + c - a)(b^{2} + c^{2} - a^{2}) : :`

Barycentrics
~~~~~~~~~~~~

* :math:`1/(1 - \sec A) : 1/(1 - \sec B) : 1/(1 - \sec C)`

* **Kimberling (6, 9, 13) Search Value:** :math:`5.922999174659`

Notes
-----

.. container:: note-item

   Let A\ :sub:`35`\ B\ :sub:`35`\ C\ :sub:`35` be Gemini triangle 35. Let A' be the perspector of conic {A,B,C,B\ :sub:`35`,C\ :sub:`35`}}, and define B' and C' cyclically. The lines AA', BB', CC' concur in :ref:`X(345) <X(345)>`. (:person:`Randy Hutson <randy-hutson>`, January 15, 2019)

Incidence
---------

:ref:`X(345) <X(345)>` lies and on these lines:

{:ref:`2 <X(2)>`, :ref:`37 <X(37)>`}, {:ref:`8 <X(8)>`, :ref:`21 <X(21)>`}, {:ref:`22 <X(22)>`, :ref:`100 <X(100)>`}, {:ref:`57 <X(57)>`, :ref:`728 <X(728)>`}, {:ref:`63 <X(63)>`, :ref:`69 <X(69)>`}, {:ref:`78 <X(78)>`, 1040}, {:ref:`190 <X(190)>`, :ref:`329 <X(329)>`}, {:ref:`219 <X(219)>`, :ref:`332 <X(332)>`}, {:ref:`280 <X(280)>`, :ref:`341 <X(341)>`}, {:ref:`304 <X(304)>`, :ref:`348 <X(348)>`}, {:ref:`498 <X(498)>`, 1089}

Relations
---------

* :ref:`X(345) <X(345)>` = :term:`isogonal conjugate <isogonal-conjugate>` of :ref:`X(608) <X(608)>`
* :ref:`X(345) <X(345)>` = :term:`isotomic conjugate <isotomic-conjugate>` of :ref:`X(278) <X(278)>`
* :ref:`X(345) <X(345)>` = X(i)-:term:`Ceva conjugate <ceva-conjugate>` of X(j) for these (i,j): (:ref:`304 <X(304)>`, :ref:`69 <X(69)>`), (:ref:`332 <X(332)>`, :ref:`78 <X(78)>`)
* :ref:`X(345) <X(345)>` = X(i)-:term:`cross conjugate <cross-conjugate>` of X(j) for these (i,j): (:ref:`78 <X(78)>`, :ref:`69 <X(69)>`), (:ref:`219 <X(219)>`, :ref:`8 <X(8)>`), (:ref:`306 <X(306)>`, :ref:`312 <X(312)>`)
* :ref:`X(345) <X(345)>` = :term:`complement <complement>` of X(30699)
* :ref:`X(345) <X(345)>` = :term:`anticomplement <anticomplement>` of X(3772)
* :ref:`X(345) <X(345)>` = polar conjugate of X(1118)

Construction
------------

.. literalinclude:: model.py
   :language: python
