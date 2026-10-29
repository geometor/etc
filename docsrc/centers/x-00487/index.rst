:order: 487
:type: center
:canonical_id: X(487)
:dependencies: X(2), X(3), X(4), X(20), X(69), X(193), X(371), X(372), X(376), X(486), X(488), X(489), X(490), X(491), X(492), X(631), X(638), X(642), X(8946)

.. _X(487):

X(487) = ANTICOMPLEMENT OF X(486)
=================================

.. figure:: x-00487.svg
   :alt: X(487) = ANTICOMPLEMENT OF X(486)
   :align: center

   **X(487) = ANTICOMPLEMENT OF X(486)** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`f(A,B,C) : f(B,C,A) : f(C,A,B)`, where f(A,B,C) = (cos A)(1 - csc A sin B sin C)

Barycentrics
~~~~~~~~~~~~

* :math:`(\sin A)f(A,B,C) : (\sin B)f(B,C,A) : (\sin C)f(C,A,B)`
* :math:`(b^{2} + c^{2} - a^{2})(a^{2} - 2σ) : (c^{2} + a^{2} - b^{2})(b^{2} - 2σ) : (a^{2} + b^{2} - c^{2})(c^{2} - 2σ) (M. Iliev, 5/13/07)`

* **Kimberling (6, 9, 13) Search Value:** :math:`4.179064973709`

Notes
-----

.. container:: note-item

   :ref:`X(487) <X(487)>` is a perspector of triangles associated with squares that circumscribe ABC. (:person:`Floor van Lamoen <floor-van-lamoen>`, 4/29/98)

.. container:: note-item

   Let O\ :sub:`A` be the circle centered at the A-vertex of the inner Vecten triangle and passing through A; define O\ :sub:`B` and O\ :sub:`C` cyclically. :ref:`X(487) <X(487)>` is the radical center of O\ :sub:`A`, O\ :sub:`B`, O\ :sub:`C`. (:person:`Randy Hutson <randy-hutson>`, August 30, 2020)

Incidence
---------

:ref:`X(487) <X(487)>` lies and on these lines:

{:ref:`2 <X(2)>`, :ref:`371 <X(371)>`}, {:ref:`3 <X(3)>`, :ref:`69 <X(69)>`}, {:ref:`4 <X(4)>`, :ref:`489 <X(489)>`}, {:ref:`20 <X(20)>`, :ref:`638 <X(638)>`}, {:ref:`193 <X(193)>`, :ref:`372 <X(372)>`}, {:ref:`376 <X(376)>`, :ref:`490 <X(490)>`}, {:ref:`492 <X(492)>`, :ref:`631 <X(631)>`}

Relations
---------

* :ref:`X(487) <X(487)>` = reflection of :ref:`X(486) <X(486)>` in :ref:`X(642) <X(642)>`
* :ref:`X(487) <X(487)>` = :term:`anticomplement <anticomplement>` of :ref:`X(486) <X(486)>`
* :ref:`X(487) <X(487)>` = :term:`anticomplementary conjugate <anticomplementary-conjugate>` of :ref:`X(638) <X(638)>`
* :ref:`X(487) <X(487)>` = X(i)-:term:`Ceva conjugate <ceva-conjugate>` of X(j) for these (i,j): (:ref:`4 <X(4)>`, :ref:`488 <X(488)>`), (:ref:`489 <X(489)>`, :ref:`20 <X(20)>`), (:ref:`491 <X(491)>`, :ref:`2 <X(2)>`)
* :ref:`X(487) <X(487)>` = :term:`isogonal conjugate <isogonal-conjugate>` of X(8946)
* :ref:`X(487) <X(487)>` = :ref:`X(20) <X(20)>`-of-inner-Vecten-triangle
* :ref:`X(487) <X(487)>` = orthologic center of outer Vecten to inner Vecten triangles

Construction
------------

.. literalinclude:: model.py
   :language: python
