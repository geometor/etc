:order: 919
:type: center
:canonical_id: X(919)
:dependencies: X(1), X(2), X(6), X(8), X(11), X(41), X(76), X(99), X(100), X(101), X(103), X(104), X(105), X(106), X(109), X(294), X(649), X(650), X(663), X(666), X(672), X(673), X(675), X(692), X(840), X(885), X(910), X(918), X(929), X(1055)

.. _X(919):

X(919) = ISOGONAL CONJUGATE OF X(918)
=====================================

.. figure:: x-00919.svg
   :alt: X(919) = ISOGONAL CONJUGATE OF X(918)
   :align: center

   **X(919) = ISOGONAL CONJUGATE OF X(918)** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`a^{2}/(w/b - v/c) : :`, where u : v : w = :ref:`X(100) <X(100)>`

* **Kimberling (6, 9, 13) Search Value:** :math:`-0.610000059147`

Notes
-----

.. container:: note-item

   Let Q be a point on line :ref:`X(2) <X(2)>`\ \ :ref:`X(11) <X(11)>` other than :ref:`X(2) <X(2)>`. Let A'B'C' be the :term:`cevian triangle <cevian-triangle>` of Q. Let A″ be the {B,C}-harmonic conjugate of A' (or equivalently, A″ = BC∩B'C'), and define B″, C″ cyclically. The circumcircles of AB″C″, BC″A″, CA″B″ concur in :ref:`X(919) <X(919)>`. (:person:`Randy Hutson <randy-hutson>`, February 10, 2016)

.. container:: note-item

   Let A', B', C' be the intersections of line :ref:`X(1) <X(1)>`\ \ :ref:`X(6) <X(6)>` and lines BC, CA, AB, resp. The circumcircles of AB'C', BC'A', CA'B' concur in :ref:`X(919) <X(919)>`. (Randy Hutson, February 10, 2016)

Incidence
---------

:ref:`X(919) <X(919)>` lies on the circumcircle and on these lines:

{:ref:`6 <X(6)>`, :ref:`840 <X(840)>`}, {:ref:`99 <X(99)>`, :ref:`666 <X(666)>`}, {:ref:`100 <X(100)>`, :ref:`650 <X(650)>`}, {:ref:`101 <X(101)>`, :ref:`663 <X(663)>`}, {:ref:`103 <X(103)>`, :ref:`672 <X(672)>`}, {:ref:`104 <X(104)>`, :ref:`294 <X(294)>`}, {:ref:`105 <X(105)>`, :ref:`910 <X(910)>`}, {:ref:`106 <X(106)>`, 1055}, {:ref:`109 <X(109)>`, :ref:`649 <X(649)>`}, {:ref:`673 <X(673)>`, :ref:`675 <X(675)>`}, {:ref:`885 <X(885)>`, :ref:`929 <X(929)>`}

Relations
---------

* :ref:`X(919) <X(919)>` = :term:`isogonal conjugate <isogonal-conjugate>` of :ref:`X(918) <X(918)>`
* :ref:`X(919) <X(919)>` = :term:`trilinear pole <trilinear-pole>` of line :ref:`X(6) <X(6)>`\ \ :ref:`X(692) <X(692)>`
* :ref:`X(919) <X(919)>` = Ψ(X(i), X(j)) for these (i,j): (:ref:`1 <X(1)>`, :ref:`41 <X(41)>`), (:ref:`2 <X(2)>`, :ref:`11 <X(11)>`), (:ref:`6 <X(6)>`, :ref:`692 <X(692)>`), (:ref:`11 <X(11)>`, :ref:`650 <X(650)>`), (:ref:`76 <X(76)>`, :ref:`8 <X(8)>`)
* :ref:`X(919) <X(919)>` = isogonal conjugate of :term:`isotomic conjugate <isotomic-conjugate>` of trilinear pole of line :ref:`X(2) <X(2)>`\ \ :ref:`X(11) <X(11)>`
* :ref:`X(919) <X(919)>` = circumcircle intercept, other than A, B, C, of conic {A,B,C,PU(95)}}
* :ref:`X(919) <X(919)>` = inverse-in-Stevanovic-circle of :ref:`X(100) <X(100)>`
* :ref:`X(919) <X(919)>` = trilinear product :ref:`X(101) <X(101)>`\ \*\ :ref:`X(105) <X(105)>` (circumcircle-:ref:`X(1) <X(1)>` antipodes)
* :ref:`X(919) <X(919)>` = barycentric product :ref:`X(100) <X(100)>`\ \*\ :ref:`X(105) <X(105)>` (circumcircle-:ref:`X(2) <X(2)>` antipodes)

Construction
------------

.. literalinclude:: model.py
   :language: python
