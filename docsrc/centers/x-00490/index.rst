:order: 490
:type: center
:canonical_id: X(490)
:dependencies: X(3), X(4), X(20), X(30), X(64), X(175), X(376), X(486), X(487), X(488), X(491), X(637), X(664), X(671), X(3070)

.. _X(490):

X(490) = CEVAPOINT OF X(20) AND X(488)
======================================

.. figure:: x-00490.svg
   :alt: X(490) = CEVAPOINT OF X(20) AND X(488)
   :align: center

   **X(490) = CEVAPOINT OF X(20) AND X(488)** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`f(A,B,C) : f(B,C,A) : f(C,A,B)`, where f(A,B,C) = (cos A)(1 + csc A sin B sin C) - cos B cos C

Barycentrics
~~~~~~~~~~~~

* :math:`(\sin A)f(A,B,C) : (\sin B)f(B,C,A) : (\sin C)f(C,A,B)`

* **Kimberling (6, 9, 13) Search Value:** :math:`9.219285468823`

Notes
-----

.. container:: note-item

   :ref:`X(490) <X(490)>` is a perspector of triangles associated with squares that circumscribe ABC. For details and reference, see :ref:`X(488) <X(488)>`. (:person:`Floor van Lamoen <floor-van-lamoen>`, 4/29/98)

Incidence
---------

:ref:`X(490) <X(490)>` lies and on these lines:

{:ref:`3 <X(3)>`, :ref:`491 <X(491)>`}, {:ref:`4 <X(4)>`, :ref:`488 <X(488)>`}, {:ref:`20 <X(20)>`, :ref:`64 <X(64)>`}, {:ref:`30 <X(30)>`, :ref:`637 <X(637)>`}, {:ref:`175 <X(175)>`, :ref:`664 <X(664)>`}, {:ref:`376 <X(376)>`, :ref:`487 <X(487)>`}, {:ref:`486 <X(486)>`, :ref:`671 <X(671)>`}

Relations
---------

* :ref:`X(490) <X(490)>` = :term:`anticomplement <anticomplement>` of X(3070)
* :ref:`X(490) <X(490)>` = :term:`cevapoint <cevapoint>` of :ref:`X(20) <X(20)>` and :ref:`X(488) <X(488)>`
* :ref:`X(490) <X(490)>` = :term:`crosspoint <crosspoint>` of :ref:`X(20) <X(20)>` and :ref:`X(488) <X(488)>` wrt both the excentral and :term:`anticomplementary triangles <anticomplementary-triangle>`

Construction
------------

.. literalinclude:: model.py
   :language: python
