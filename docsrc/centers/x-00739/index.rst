:order: 739
:type: center
:canonical_id: X(739)
:dependencies: X(1), X(2), X(6), X(8), X(31), X(81), X(99), X(100), X(101), X(108), X(109), X(190), X(513), X(536), X(604), X(608), X(650), X(667), X(813), X(902), X(35543)

.. _X(739):

X(739) = EVEN (- 1, 0) CIRCUMCIRCLE POINT
=========================================

.. figure:: x-00739.svg
   :alt: X(739) = EVEN (- 1, 0) CIRCUMCIRCLE POINT
   :align: center

   **X(739) = EVEN (- 1, 0) CIRCUMCIRCLE POINT** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`1/[a^{-2}(b^{0} + c^{0}) - a ^{-1}(b ^{-1} + c ^{-1})] : :`
* :math:`a/(2 b c - c a - a b) : :`

* **Kimberling (6, 9, 13) Search Value:** :math:`-0.398312135219`

Incidence
---------

:ref:`X(739) <X(739)>` lies on the circumcircle and on these lines:

{:ref:`6 <X(6)>`, :ref:`100 <X(100)>`}, {:ref:`31 <X(31)>`, :ref:`101 <X(101)>`}, {:ref:`81 <X(81)>`, :ref:`99 <X(99)>`}, {:ref:`108 <X(108)>`, :ref:`608 <X(608)>`}, {:ref:`109 <X(109)>`, :ref:`604 <X(604)>`}, {:ref:`813 <X(813)>`, :ref:`902 <X(902)>`}

Relations
---------

* :ref:`X(739) <X(739)>` = :term:`isogonal conjugate <isogonal-conjugate>` of :ref:`X(536) <X(536)>`
* :ref:`X(739) <X(739)>` = :term:`isotomic conjugate <isotomic-conjugate>` of X(35543)
* :ref:`X(739) <X(739)>` = :term:`trilinear pole <trilinear-pole>` of line :ref:`X(6) <X(6)>`\ \ :ref:`X(667) <X(667)>`
* :ref:`X(739) <X(739)>` = Ψ(:ref:`X(6) <X(6)>`, :ref:`X(667) <X(667)>`)
* :ref:`X(739) <X(739)>` = Ψ(:ref:`X(190) <X(190)>`, :ref:`X(1) <X(1)>`)
* :ref:`X(739) <X(739)>` = Ψ(:ref:`X(8) <X(8)>`, :ref:`X(650) <X(650)>`)
* :ref:`X(739) <X(739)>` = barycentric product of circumcircle intercepts of line :ref:`X(2) <X(2)>`\ \ :ref:`X(513) <X(513)>`
* :ref:`X(739) <X(739)>` = trilinear pole wrt circumsymmedial triangle of line :ref:`X(1) <X(1)>`\ \ :ref:`X(6) <X(6)>`

Construction
------------

.. literalinclude:: model.py
   :language: python
