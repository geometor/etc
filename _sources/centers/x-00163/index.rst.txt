:order: 163
:type: center
:canonical_id: X(163)
:dependencies: X(1), X(6), X(19), X(21), X(31), X(32), X(48), X(58), X(92), X(99), X(101), X(109), X(110), X(112), X(284), X(293), X(512), X(563), X(610), X(643), X(648), X(656), X(661), X(662), X(667), X(692), X(788), X(798), X(813), X(825), X(827), X(849), X(906), X(909), X(923), X(1018), X(1094), X(1101), X(1109), X(1577), X(2632), X(20948), X(21253), X(21294)

.. _X(163):

X(163) = TRILINEAR PRODUCT X(6)*X(110)
======================================

.. figure:: x-00163.svg
   :alt: X(163) = TRILINEAR PRODUCT X(6)*X(110)
   :align: center

   **X(163) = TRILINEAR PRODUCT X(6)*X(110)** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`(\sin 2A)/(\sin 2B - \sin 2C) : (\sin 2B)/(\sin 2C - \sin 2A) : (\sin 2C)/(\sin 2A - \sin 2B)`
* :math:`a^{2}/(b^{2} - c^{2}) : :`

Barycentrics
~~~~~~~~~~~~

* :math:`a^{3}/(b^{2} - c^{2}) : b^{3}/(c^{2} - a^{2}) : c^{3}/(a^{2} - b^{2})`

* **Kimberling (6, 9, 13) Search Value:** :math:`0.422785826392`

Notes
-----

.. container:: note-item

   Let A'B'C' be the circumcevian triangle of :ref:`X(512) <X(512)>`. Let A″ be the trilinear product B'\*C', and define B″ and C″ cyclically. A″, B″, C″ are collinear on line :ref:`X(667) <X(667)>`\ \ :ref:`X(788) <X(788)>`. The lines AA″, BB″, CC″ concur in :ref:`X(163) <X(163)>`. (:person:`Randy Hutson <randy-hutson>`, August 19, 2019)

Incidence
---------

:ref:`X(163) <X(163)>` lies and on these lines:

{:ref:`1 <X(1)>`, :ref:`293 <X(293)>`}, {:ref:`19 <X(19)>`, :ref:`563 <X(563)>`}, {:ref:`31 <X(31)>`, :ref:`923 <X(923)>`}, {:ref:`32 <X(32)>`, :ref:`849 <X(849)>`}, {:ref:`48 <X(48)>`, 1094}, {:ref:`99 <X(99)>`, :ref:`825 <X(825)>`}, {:ref:`101 <X(101)>`, :ref:`110 <X(110)>`}, {:ref:`109 <X(109)>`, :ref:`112 <X(112)>`}, {:ref:`284 <X(284)>`, :ref:`909 <X(909)>`}, {:ref:`643 <X(643)>`, 1018}, {:ref:`692 <X(692)>`, :ref:`906 <X(906)>`}, {:ref:`798 <X(798)>`, 1101}, {:ref:`813 <X(813)>`, :ref:`827 <X(827)>`}

Relations
---------

* :ref:`X(163) <X(163)>` = :term:`isogonal conjugate <isogonal-conjugate>` of X(1577)
* :ref:`X(163) <X(163)>` = :term:`isotomic conjugate <isotomic-conjugate>` of X(20948)
* :ref:`X(163) <X(163)>` = :term:`complement <complement>` of X(21294)
* :ref:`X(163) <X(163)>` = :term:`anticomplement <anticomplement>` of X(21253)
* :ref:`X(163) <X(163)>` = barycentric product of circumcircle intercepts of line :ref:`X(1) <X(1)>`\ \ :ref:`X(21) <X(21)>`
* :ref:`X(163) <X(163)>` = :term:`crosssum <crosssum>` of :ref:`X(656) <X(656)>` and :ref:`X(661) <X(661)>`
* :ref:`X(163) <X(163)>` = X(i)-:term:`aleph conjugate <aleph-conjugate>` of X(j) for these (i,j): (:ref:`648 <X(648)>`, :ref:`19 <X(19)>`), (:ref:`662 <X(662)>`, :ref:`610 <X(610)>`)
* :ref:`X(163) <X(163)>` = trilinear product of PU(2)
* :ref:`X(163) <X(163)>` = barycentric product of PU(70)
* :ref:`X(163) <X(163)>` = trilinear product of :ref:`X(58) <X(58)>`\ \ :ref:`X(101) <X(101)>`
* :ref:`X(163) <X(163)>` = trilinear product of the 6 vertices of the 1st and 2nd circumperp triangles
* :ref:`X(163) <X(163)>` = :term:`trilinear pole <trilinear-pole>` of line :ref:`X(31) <X(31)>`\ \ :ref:`X(48) <X(48)>`
* :ref:`X(163) <X(163)>` = :ref:`X(92) <X(92)>`-:term:`isoconjugate <isoconjugate>` of :ref:`X(656) <X(656)>`
* :ref:`X(163) <X(163)>` = :term:`crossdifference <crossdifference>` of every pair of points on line X(1109)X(2632)
* :ref:`X(163) <X(163)>` = trilinear product :ref:`X(6) <X(6)>`\ \*\ :ref:`X(110) <X(110)>`

Construction
------------

.. literalinclude:: model.py
   :language: python
