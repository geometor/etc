:order: 491
:type: center
:canonical_id: X(491)
:dependencies: X(2), X(3), X(4), X(5), X(6), X(69), X(76), X(264), X(315), X(371), X(372), X(485), X(486), X(487), X(488), X(490), X(492), X(615), X(631), X(637), X(642)

.. _X(491):

X(491) = CEVAPOINT OF X(2) AND X(487)
=====================================

.. figure:: x-00491.svg
   :alt: X(491) = CEVAPOINT OF X(2) AND X(487)
   :align: center

   **X(491) = CEVAPOINT OF X(2) AND X(487)** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`f(A,B,C) : f(B,C,A) : f(C,A,B)`, where f(A,B,C) = (cos A)(1 - csc A sin B sin C) + cos B cos C
* :math:`\sin(A - \pi /4)\csc^{2}A : \sin(B - \pi /4)\csc^{2}B : \sin(C - \pi /4)\csc^{2}C (M. Iliev, 4/12/2007)`
* :math:`(1 - \cot A) \csc A : (1 - \cot B) \csc B : (1 - \cot C) \csc C (M. Iliev, 4/12/2007)`
* :math:`(S - S_{A})/a : (S - S_{B})/b : (S - S_{C})/c (C. Lozada, 8/07/2013)`

* **Kimberling (6, 9, 13) Search Value:** :math:`464.156311966686`

Notes
-----

.. container:: note-item

   Barycentrics (sin A)f(A,B,C) : (sin B)f(B,C,A) : (sin C)f(C,A,B)

   Barycentrics b\ :sup:`2` + c\ :sup:`2` - a\ :sup:`2` - 4σ : c\ :sup:`2` + a\ :sup:`2` - b\ :sup:`2` - 4σ : a\ :sup:`2` + b\ :sup:`2` - c\ :sup:`2` - 4σ (M. Iliev, 5/13/07)

.. container:: note-item

   :ref:`X(491) <X(491)>` is a pole associated with squares that circumscribe ABC. For details and reference, see :ref:`X(488) <X(488)>`. (:person:`Floor van Lamoen <floor-van-lamoen>`, 4/26/98)

Incidence
---------

:ref:`X(491) <X(491)>` lies and on these lines:

{:ref:`2 <X(2)>`, :ref:`6 <X(6)>`}, {:ref:`3 <X(3)>`, :ref:`490 <X(490)>`}, {:ref:`4 <X(4)>`, :ref:`487 <X(487)>`}, {:ref:`5 <X(5)>`, :ref:`637 <X(637)>`}, {:ref:`76 <X(76)>`, :ref:`485 <X(485)>`}, {:ref:`315 <X(315)>`, :ref:`371 <X(371)>`}, {:ref:`372 <X(372)>`, :ref:`642 <X(642)>`}, {:ref:`488 <X(488)>`, :ref:`631 <X(631)>`}

Relations
---------

* :ref:`X(491) <X(491)>` = :term:`isotomic conjugate <isotomic-conjugate>` of :ref:`X(486) <X(486)>`
* :ref:`X(491) <X(491)>` = :term:`anticomplement <anticomplement>` of :ref:`X(615) <X(615)>`
* :ref:`X(491) <X(491)>` = :ref:`X(264) <X(264)>`-:term:`Ceva conjugate <ceva-conjugate>` of :ref:`X(492) <X(492)>`
* :ref:`X(491) <X(491)>` = :term:`cevapoint <cevapoint>` of :ref:`X(2) <X(2)>` and :ref:`X(487) <X(487)>`
* :ref:`X(491) <X(491)>` = :term:`crosspoint <crosspoint>` of :ref:`X(2) <X(2)>` and :ref:`X(487) <X(487)>` wrt both the excentral and :term:`anticomplementary triangles <anticomplementary-triangle>`
* :ref:`X(491) <X(491)>` = {:ref:`X(2) <X(2)>`,\ :ref:`X(69) <X(69)>`}-harmonic conjugate of :ref:`X(492) <X(492)>`
* :ref:`X(491) <X(491)>` = homothetic center of ABC and :term:`unary cofactor triangle <unary-cofactor-triangle>` of 2nd Kenmotu diagonals triangle

Construction
------------

.. literalinclude:: model.py
   :language: python
