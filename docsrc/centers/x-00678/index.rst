:order: 678
:type: center
:canonical_id: X(678)
:dependencies: X(1), X(44), X(45), X(55), X(88), X(244), X(679), X(902), X(1022)

.. _X(678):

X(678) = CROSSPOINT OF X(1) AND X(44)
=====================================

.. figure:: x-00678.svg
   :alt: X(678) = CROSSPOINT OF X(1) AND X(44)
   :align: center

   **X(678) = CROSSPOINT OF X(1) AND X(44)** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`f(a,b,c) : f(b,c,a) : f(c,a,b)`, where f(a,b,c) = (b + c - 2a)\ :sup:`2`

Barycentrics
~~~~~~~~~~~~

* :math:`g(a,b,c) : g(b,c,a) : g(c,a,b)`, where g(a,b,c) = af(a,b,c)

* **Kimberling (6, 9, 13) Search Value:** :math:`2.169048499762`

Incidence
---------

:ref:`X(678) <X(678)>` lies on the incentral inellipse (a.k.a. Hofstadter ellipse E(1/2)).

:ref:`X(678) <X(678)>` lies and on these lines:

{:ref:`1 <X(1)>`, :ref:`88 <X(88)>`}, {:ref:`44 <X(44)>`, :ref:`902 <X(902)>`}, {:ref:`45 <X(45)>`, :ref:`55 <X(55)>`}

Relations
---------

* :ref:`X(678) <X(678)>` = :term:`isogonal conjugate <isogonal-conjugate>` of :ref:`X(679) <X(679)>`
* :ref:`X(678) <X(678)>` = :ref:`X(1) <X(1)>`-:term:`Ceva conjugate <ceva-conjugate>` of :ref:`X(44) <X(44)>`
* :ref:`X(678) <X(678)>` = :term:`crosspoint <crosspoint>` of :ref:`X(1) <X(1)>` and :ref:`X(44) <X(44)>`
* :ref:`X(678) <X(678)>` = :term:`crosssum <crosssum>` of X(i) and X(j) for these (i,j): (:ref:`1 <X(1)>`, :ref:`88 <X(88)>`), (:ref:`244 <X(244)>`, 1022)
* :ref:`X(678) <X(678)>` = :term:`crossdifference <crossdifference>` of every pair of points on line :ref:`X(88) <X(88)>`\ X(1022)
* :ref:`X(678) <X(678)>` = trilinear square of :ref:`X(44) <X(44)>`

Construction
------------

.. literalinclude:: model.py
   :language: python
