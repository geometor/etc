:order: 913
:type: center
:canonical_id: X(913)
:dependencies: X(4), X(19), X(25), X(27), X(101), X(571), X(608), X(662), X(692), X(914)

.. _X(913):

X(913) = POINT AGENA
====================

.. figure:: x-00913.svg
   :alt: X(913) = POINT AGENA
   :align: center

   **X(913) = POINT AGENA** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`f(a,b,c) : f(b,c,a) : f(c,a,b),`, where f(a,b,c) = a/[(wb + vc)/a - v - w], u : v : w = :ref:`X(4) <X(4)>`

Barycentrics
~~~~~~~~~~~~

* :math:`g(a,b,c) : g(b,c,a) : g(c,a,b)`, where g(a,b,c) = af(a,b,c)

* **Kimberling (6, 9, 13) Search Value:** :math:`-46.970810800139`

Incidence
---------

:ref:`X(913) <X(913)>` lies and on these lines:

{:ref:`19 <X(19)>`, :ref:`101 <X(101)>`}, {:ref:`25 <X(25)>`, :ref:`692 <X(692)>`}, {:ref:`27 <X(27)>`, :ref:`662 <X(662)>`}, {:ref:`571 <X(571)>`, :ref:`608 <X(608)>`}

Relations
---------

* :ref:`X(913) <X(913)>` = :term:`isogonal conjugate <isogonal-conjugate>` of :ref:`X(914) <X(914)>`

Construction
------------

.. literalinclude:: model.py
   :language: python
