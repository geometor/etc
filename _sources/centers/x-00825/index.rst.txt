:order: 825
:type: center
:canonical_id: X(825)
:dependencies: X(1), X(2), X(6), X(31), X(32), X(76), X(99), X(103), X(105), X(163), X(560), X(572), X(692), X(717), X(731), X(743), X(753), X(761), X(767), X(813), X(824), X(870), X(985)

.. _X(825):

X(825) = o-(0, 3) CIRCUMCIRCLE POINT
====================================

.. figure:: x-00825.svg
   :alt: X(825) = o-(0, 3) CIRCUMCIRCLE POINT
   :align: center

   **X(825) = o-(0, 3) CIRCUMCIRCLE POINT** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`1/[a^{-1}(b^{3} - c^{3}) + a^{2}(b^{0} - c^{0})] : :`

* **Kimberling (6, 9, 13) Search Value:** :math:`0.617886287890`

Notes
-----

.. container:: note-item

   Let Q be a point on line :ref:`X(2) <X(2)>`\ \ :ref:`X(31) <X(31)>` other than :ref:`X(2) <X(2)>`. Let A'B'C' be the :term:`cevian triangle <cevian-triangle>` of Q. Let A″ be the {B,C}-harmonic conjugate of A'; equivalently, A″ = BC∩B'C'/ Define B″ and C″ cyclically. The circumcircles of AB″C″, BC″A″, CA″B″ concur in :ref:`X(825) <X(825)>`. (:person:`Randy Hutson <randy-hutson>`, December 29, 2015)

Incidence
---------

:ref:`X(825) <X(825)>` lies on the circumcircle and on these lines:

{:ref:`1 <X(1)>`, :ref:`761 <X(761)>`}, {:ref:`6 <X(6)>`, :ref:`753 <X(753)>`}, {:ref:`31 <X(31)>`, :ref:`743 <X(743)>`}, {:ref:`32 <X(32)>`, :ref:`731 <X(731)>`}, {:ref:`99 <X(99)>`, :ref:`163 <X(163)>`}, {:ref:`103 <X(103)>`, :ref:`572 <X(572)>`}, {:ref:`105 <X(105)>`, :ref:`985 <X(985)>`}, {:ref:`560 <X(560)>`, :ref:`717 <X(717)>`}, {:ref:`692 <X(692)>`, :ref:`813 <X(813)>`}, {:ref:`767 <X(767)>`, :ref:`870 <X(870)>`}

Relations
---------

* :ref:`X(825) <X(825)>` = :term:`isogonal conjugate <isogonal-conjugate>` of :ref:`X(824) <X(824)>`
* :ref:`X(825) <X(825)>` = intersection, other than A, B, C, of circumcircle and hyperbola {A,B,C,PU(12)}}
* :ref:`X(825) <X(825)>` = :term:`trilinear pole <trilinear-pole>` of line :ref:`X(6) <X(6)>`\ \ :ref:`X(560) <X(560)>`
* :ref:`X(825) <X(825)>` = Ψ(:ref:`X(1) <X(1)>`, :ref:`X(32) <X(32)>`)
* :ref:`X(825) <X(825)>` = Ψ(:ref:`X(2) <X(2)>`, :ref:`X(31) <X(31)>`)
* :ref:`X(825) <X(825)>` = Ψ(:ref:`X(6) <X(6)>`, :ref:`X(560) <X(560)>`)
* :ref:`X(825) <X(825)>` = Ψ(:ref:`X(76) <X(76)>`, :ref:`X(1) <X(1)>`)
* :ref:`X(825) <X(825)>` = barycentric product of circumcircle intercepts of line :ref:`X(2) <X(2)>`\ \ :ref:`X(31) <X(31)>`

Construction
------------

.. literalinclude:: model.py
   :language: python
