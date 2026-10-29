:order: 638
:type: center
:canonical_id: X(638)
:dependencies: X(2), X(3), X(4), X(5), X(20), X(30), X(69), X(315), X(372), X(487), X(489), X(490), X(492), X(637), X(640)

.. _X(638):

X(638) = ANTICOMPLEMENT OF X(372)
=================================

.. figure:: x-00638.svg
   :alt: X(638) = ANTICOMPLEMENT OF X(372)
   :align: center

   **X(638) = ANTICOMPLEMENT OF X(372)** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`f(a,b,c) : f(b,c,a) : f(c,a,b)`, where f(a,b,c) = (S\ :sub:`B`\ S\ :sub:`C` - 2S\ :sub:`A` area)/a

Barycentrics
~~~~~~~~~~~~

* :math:`g(a,b,c) : g(b,c,a) : g(c,a,b)`, where g(a,b,c) = af(a,b,c)

* **Kimberling (6, 9, 13) Search Value:** :math:`11.630377459613`

Incidence
---------

:ref:`X(638) <X(638)>` lies and on these lines:

{:ref:`2 <X(2)>`, :ref:`372 <X(372)>`}, {:ref:`3 <X(3)>`, :ref:`490 <X(490)>`}, {:ref:`4 <X(4)>`, :ref:`69 <X(69)>`}, {:ref:`5 <X(5)>`, :ref:`492 <X(492)>`}, {:ref:`20 <X(20)>`, :ref:`487 <X(487)>`}, {:ref:`30 <X(30)>`, :ref:`489 <X(489)>`}

Relations
---------

* :ref:`X(638) <X(638)>` = reflection of X(i) in X(j) for these (i,j): (:ref:`372 <X(372)>`, :ref:`640 <X(640)>`), (:ref:`637 <X(637)>`, :ref:`315 <X(315)>`)
* :ref:`X(638) <X(638)>` = :term:`anticomplement <anticomplement>` of :ref:`X(372) <X(372)>`
* :ref:`X(638) <X(638)>` = :term:`anticomplementary conjugate <anticomplementary-conjugate>` of :ref:`X(487) <X(487)>`

Construction
------------

.. literalinclude:: model.py
   :language: python
