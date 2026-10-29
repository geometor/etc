:order: 288
:type: center
:canonical_id: X(288)
:dependencies: X(6), X(51), X(53), X(54), X(97), X(216), X(233), X(275), X(1157), X(1510)

.. _X(288):

X(288) = CEVAPOINT OF X(6) AND X(54)
====================================

.. figure:: x-00288.svg
   :alt: X(288) = CEVAPOINT OF X(6) AND X(54)
   :align: center

   **X(288) = CEVAPOINT OF X(6) AND X(54)** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`f(A,B,C) : f(B,C,A) : f(C,A,B)`, where f(A,B,C) = [sec(B - C)]/[b cos(C - A) + c cos(B - A)]

Barycentrics
~~~~~~~~~~~~

* :math:`a/(b \sec(A - B) + c \sec(A - C)) : :`

* **Kimberling (6, 9, 13) Search Value:** :math:`0.255273525396`

Incidence
---------

:ref:`X(288) <X(288)>` lies and on these lines:

{:ref:`51 <X(51)>`, :ref:`54 <X(54)>`}, {:ref:`53 <X(53)>`, :ref:`275 <X(275)>`}, {:ref:`97 <X(97)>`, :ref:`216 <X(216)>`}

Relations
---------

* :ref:`X(288) <X(288)>` = :term:`isogonal conjugate <isogonal-conjugate>` of :ref:`X(233) <X(233)>`
* :ref:`X(288) <X(288)>` = :term:`cevapoint <cevapoint>` of :ref:`X(6) <X(6)>` and :ref:`X(54) <X(54)>`
* :ref:`X(288) <X(288)>` = :term:`trilinear pole <trilinear-pole>` of line X(1157)X(1510)

Construction
------------

.. literalinclude:: model.py
   :language: python
