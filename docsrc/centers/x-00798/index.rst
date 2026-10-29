:order: 798
:type: center
:canonical_id: X(798)
:dependencies: X(1), X(2), X(6), X(31), X(38), X(44), X(75), X(86), X(99), X(163), X(190), X(512), X(513), X(645), X(661), X(667), X(668), X(670), X(688), X(765), X(788), X(799), X(813), X(872), X(1019), X(1101), X(1107), X(1964), X(2667), X(3121), X(4117), X(4602), X(17217), X(38986)

.. _X(798):

X(798) = CROSSDIFFERENCE OF X(1) AND X(75)
==========================================

.. figure:: x-00798.svg
   :alt: X(798) = CROSSDIFFERENCE OF X(1) AND X(75)
   :align: center

   **X(798) = CROSSDIFFERENCE OF X(1) AND X(75)** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`a^{2}(b^{2} - c^{2}) : :`
* S\ :sub:`B`\ S\ :sub:`B` - S\ :sub:`C`\ S\ :sub:`C` : :
* :math:`Area(BCP(1)) - Area(BCU(1)) : :`

Barycentrics
~~~~~~~~~~~~

* :math:`a^{3}(b^{2} - c^{2}) : :`

* **Kimberling (6, 9, 13) Search Value:** :math:`7.168537293119`

Incidence
---------

:ref:`X(798) <X(798)>` lies and on these lines:

{:ref:`44 <X(44)>`, :ref:`513 <X(513)>`}, {:ref:`163 <X(163)>`, 1101}, {:ref:`667 <X(667)>`, :ref:`788 <X(788)>`}, {:ref:`688 <X(688)>`, :ref:`872 <X(872)>`}, {:ref:`765 <X(765)>`, :ref:`813 <X(813)>`}

Relations
---------

* :ref:`X(798) <X(798)>` = :term:`isogonal conjugate <isogonal-conjugate>` of :ref:`X(799) <X(799)>`
* :ref:`X(798) <X(798)>` = :term:`isotomic conjugate <isotomic-conjugate>` of X(4602)
* :ref:`X(798) <X(798)>` = :term:`complement <complement>` of X(17217)
* :ref:`X(798) <X(798)>` = :ref:`X(163) <X(163)>`-:term:`Ceva conjugate <ceva-conjugate>` of :ref:`X(31) <X(31)>`
* :ref:`X(798) <X(798)>` = :term:`crosspoint <crosspoint>` of :ref:`X(31) <X(31)>` and :ref:`X(163) <X(163)>`
* :ref:`X(798) <X(798)>` = :term:`crosssum <crosssum>` of X(i) and X(j) for these (i,j): (:ref:`1 <X(1)>`, :ref:`798 <X(798)>`), (:ref:`38 <X(38)>`, :ref:`661 <X(661)>`), (:ref:`86 <X(86)>`, 1019), (:ref:`99 <X(99)>`, :ref:`645 <X(645)>`), (:ref:`190 <X(190)>`, :ref:`668 <X(668)>`), (:ref:`513 <X(513)>`, 1107)
* :ref:`X(798) <X(798)>` = :term:`crossdifference <crossdifference>` of every pair of points on line :ref:`X(1) <X(1)>`\ \ :ref:`X(75) <X(75)>`
* :ref:`X(798) <X(798)>` = bicentric difference of PU(i) for i in (36, 85)
* :ref:`X(798) <X(798)>` = PU(36)-harmonic conjugate of X(1964)
* :ref:`X(798) <X(798)>` = PU(85)-harmonic conjugate of X(2667)
* :ref:`X(798) <X(798)>` = perspector wrt :term:`excentral triangle <excentral-triangle>` of the bianticevian conic of :ref:`X(1) <X(1)>` and :ref:`X(2) <X(2)>`
* :ref:`X(798) <X(798)>` = :ref:`X(6) <X(6)>`-:term:`isoconjugate <isoconjugate>` of :ref:`X(670) <X(670)>`
* :ref:`X(798) <X(798)>` = trilinear product of PU(105)
* :ref:`X(798) <X(798)>` = :ref:`X(2) <X(2)>`-Ceva conjugate of X(38986)
* :ref:`X(798) <X(798)>` = perspector of hyperbola {A,B,C,\ :ref:`X(1) <X(1)>`,\ :ref:`X(31) <X(31)>`}}
* :ref:`X(798) <X(798)>` = :term:`trilinear pole <trilinear-pole>` of line X(3121)X(4117) (the tangent to the inellipse that is the trilinear square of the Lemoine axis, at the trilinear square of :ref:`X(512) <X(512)>`)

Construction
------------

.. literalinclude:: model.py
   :language: python
