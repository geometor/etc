:order: 637
:type: center
:canonical_id: X(637)
:dependencies: X(2), X(3), X(4), X(5), X(20), X(30), X(69), X(315), X(371), X(488), X(489), X(490), X(491), X(638), X(639)

.. _X(637):

X(637) = ANTICOMPLEMENT OF X(371)
=================================

.. figure:: x-00637.svg
   :alt: X(637) = ANTICOMPLEMENT OF X(371)
   :align: center

   **X(637) = ANTICOMPLEMENT OF X(371)** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`f(a,b,c) : f(b,c,a) : f(c,a,b)`, where f(a,b,c) = (S\ :sub:`B`\ S\ :sub:`C` + 2S\ :sub:`A` area)/a

Barycentrics
~~~~~~~~~~~~

* :math:`g(a,b,c) : g(b,c,a) : g(c,a,b)`, where g(a,b,c) = af(a,b,c)

* **Kimberling (6, 9, 13) Search Value:** :math:`3.022985510576`

Incidence
---------

:ref:`X(637) <X(637)>` lies and on these lines:

{:ref:`2 <X(2)>`, :ref:`371 <X(371)>`}, {:ref:`3 <X(3)>`, :ref:`489 <X(489)>`}, {:ref:`4 <X(4)>`, :ref:`69 <X(69)>`}, {:ref:`5 <X(5)>`, :ref:`491 <X(491)>`}, {:ref:`20 <X(20)>`, :ref:`488 <X(488)>`}, {:ref:`30 <X(30)>`, :ref:`490 <X(490)>`}

Relations
---------

* :ref:`X(637) <X(637)>` = reflection of X(i) in X(j) for these (i,j): (:ref:`371 <X(371)>`, :ref:`639 <X(639)>`), (:ref:`638 <X(638)>`, :ref:`315 <X(315)>`)
* :ref:`X(637) <X(637)>` = :term:`anticomplement <anticomplement>` of :ref:`X(371) <X(371)>`
* :ref:`X(637) <X(637)>` = :term:`anticomplementary conjugate <anticomplementary-conjugate>` of :ref:`X(488) <X(488)>`

Construction
------------

.. literalinclude:: model.py
   :language: python
