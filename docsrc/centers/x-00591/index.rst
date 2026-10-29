:order: 591
:type: center
:canonical_id: X(591)
:dependencies: X(2), X(6), X(372), X(488), X(637), X(754), X(1152), X(1991), X(3071)

.. _X(591):

X(591) = 1st VAN LAMOEN PERPENDICULAR BISECTORS POINT
=====================================================

.. figure:: x-00591.svg
   :alt: X(591) = 1st VAN LAMOEN PERPENDICULAR BISECTORS POINT
   :align: center

   **X(591) = 1st VAN LAMOEN PERPENDICULAR BISECTORS POINT** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`bc[b^{2} + c^{2} - 2a^{2} + 4*area(ABC)]`

* **Kimberling (6, 9, 13) Search Value:** :math:`11.413041315846`

Notes
-----

.. container:: note-item

   Erect squares outwardly on the sides of triangle ABC. Two edges emanate from A; let P and Q be their endpoints. Let a' be the perpendicular bisector of PQ, and define b' and c' cyclically. Then a', b', c' concur in :ref:`X(591) <X(591)>`. See also X(1991). (:person:`Floor van Lamoen <floor-van-lamoen>`, 1/4/2001, :cite:`Hyacinthos #2123 <hyacinthos>`)

Incidence
---------

:ref:`X(591) <X(591)>` lies and on these lines:

{:ref:`2 <X(2)>`, :ref:`6 <X(6)>`}, {:ref:`372 <X(372)>`, :ref:`754 <X(754)>`}, {:ref:`488 <X(488)>`, 3071}, {:ref:`637 <X(637)>`, 1152}

Relations
---------

* :ref:`X(591) <X(591)>` = reflection of X(1991) in :ref:`X(2) <X(2)>`
* :ref:`X(591) <X(591)>` = perspector of inner Vecten triangle and outer Vecten of outer Vecten triangle
* :ref:`X(591) <X(591)>` = centroid of {Ab, Ac, Bc, Ba, Ca, Cb} used in construction of 4th Lozada circle

Construction
------------

.. literalinclude:: model.py
   :language: python
