:order: 85
:type: center
:canonical_id: X(85)
:dependencies: X(1), X(2), X(7), X(8), X(9), X(12), X(29), X(33), X(34), X(41), X(56), X(57), X(75), X(76), X(77), X(92), X(99), X(100), X(109), X(120), X(142), X(150), X(169), X(226), X(241), X(264), X(273), X(274), X(279), X(309), X(331), X(342), X(348), X(355), X(508), X(522), X(657), X(664), X(668), X(693), X(767), X(789), X(799), X(811), X(870), X(1120), X(1212), X(1320), X(3177), X(4041), X(6604)

.. _X(85):

X(85) = ISOTOMIC CONJUGATE OF X(9)
==================================

.. figure:: x-00085.svg
   :alt: X(85) = ISOTOMIC CONJUGATE OF X(9)
   :align: center

   **X(85) = ISOTOMIC CONJUGATE OF X(9)** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`b^{2}c^{2}/(b + c - a) : c^{2}a^{2}/(c + a - b) : a^{2}b^{2}/(a + b - c), = \tan(A/2) \csc^{2}A : \tan(B/2) \csc^{2}B : \tan(C/2) \csc^{2}C`

Barycentrics
~~~~~~~~~~~~

* :math:`bc/(b + c - a) : ca/(c + a - b) : ab/(a + b - c)`
* :math:`\cot A' : :`, where A'B'C' is the :term:`excentral triangle <excentral-triangle>`

* **Kimberling (6, 9, 13) Search Value:** :math:`1.369706806417`

Notes
-----

.. container:: note-item

   Let A\ :sub:`38`\ B\ :sub:`38`\ C\ :sub:`38` be Gemini triangle 38. Let A' be the perspector of conic {A,B,C,B\ :sub:`38`,C\ :sub:`38`}}, and define B' and C' cyclically. The lines AA', BB', CC' concur in :ref:`X(85) <X(85)>`. (:person:`Randy Hutson <randy-hutson>`, January 15, 2019)

Incidence
---------

:ref:`X(85) <X(85)>` lies and on these lines:

{:ref:`1 <X(1)>`, 664}, {:ref:`2 <X(2)>`, 241}, {:ref:`7 <X(7)>`, :ref:`8 <X(8)>`}, {:ref:`12 <X(12)>`, 120}, {:ref:`29 <X(29)>`, :ref:`34 <X(34)>`}, {:ref:`56 <X(56)>`, 870}, {:ref:`57 <X(57)>`, 274}, {:ref:`76 <X(76)>`, 226}, {:ref:`92 <X(92)>`, 331}, {109, 767}, {150, 355}, {264, 309}

Relations
---------

* :ref:`X(85) <X(85)>` = :term:`isogonal conjugate <isogonal-conjugate>` of :ref:`X(41) <X(41)>`
* :ref:`X(85) <X(85)>` = :term:`isotomic conjugate <isotomic-conjugate>` of :ref:`X(9) <X(9)>`
* :ref:`X(85) <X(85)>` = :term:`complement <complement>` of X(3177)
* :ref:`X(85) <X(85)>` = :term:`anticomplement <anticomplement>` of X(1212)
* :ref:`X(85) <X(85)>` = X(274)-:term:`Ceva conjugate <ceva-conjugate>` of X(348)
* :ref:`X(85) <X(85)>` = :term:`cevapoint <cevapoint>` of X(i) and X(j) for these (i,j): (:ref:`1 <X(1)>`, 169), (:ref:`2 <X(2)>`, :ref:`7 <X(7)>`), (:ref:`57 <X(57)>`, :ref:`77 <X(77)>`), (:ref:`92 <X(92)>`, 342)
* :ref:`X(85) <X(85)>` = X(i)-:term:`cross conjugate <cross-conjugate>` of X(j) for these (i,j): (:ref:`2 <X(2)>`, :ref:`75 <X(75)>`), (:ref:`57 <X(57)>`, 273), (:ref:`92 <X(92)>`, 309), (142, :ref:`2 <X(2)>`), (226, :ref:`7 <X(7)>`)
* :ref:`X(85) <X(85)>` = X(i)-:term:`beth conjugate <beth-conjugate>` of X(j) for these (i,j): (:ref:`76 <X(76)>`, :ref:`76 <X(76)>`), (:ref:`85 <X(85)>`, 279), (:ref:`99 <X(99)>`, :ref:`1 <X(1)>`), (274, :ref:`85 <X(85)>`), (668, :ref:`85 <X(85)>`), (789, :ref:`85 <X(85)>`), (799, :ref:`85 <X(85)>`), (811, :ref:`85 <X(85)>`)
* :ref:`X(85) <X(85)>` = :term:`trilinear pole <trilinear-pole>` of line X(522)X(693) (the isotomic conjugate of the circumconic centered at :ref:`X(1) <X(1)>`, conic {A,B,C,\ :ref:`X(100) <X(100)>`,X(664),X(1120),X(1320)}; also the polar of :ref:`X(33) <X(33)>` wrt polar circle)
* :ref:`X(85) <X(85)>` = pole wrt polar circle of :term:`trilinear polar <trilinear-polar>` of :ref:`X(33) <X(33)>` (line X(657)X(4041))
* :ref:`X(85) <X(85)>` = polar conjugate of :ref:`X(33) <X(33)>`
* :ref:`X(85) <X(85)>` = {:ref:`X(7) <X(7)>`,\ :ref:`X(8) <X(8)>`}-harmonic conjugate of X(6604)
* :ref:`X(85) <X(85)>` = trilinear square of X(508)
* :ref:`X(85) <X(85)>` = trilinear product of vertices of Gemini triangle 9
* :ref:`X(85) <X(85)>` = trilinear product of vertices of Gemini triangle 10

Construction
------------

.. literalinclude:: model.py
   :language: python
