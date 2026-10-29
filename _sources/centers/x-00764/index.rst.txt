:order: 764
:type: center
:canonical_id: X(764)
:dependencies: X(1), X(10), X(44), X(56), X(76), X(100), X(244), X(513), X(514), X(667), X(692), X(693), X(765), X(1252), X(8027)

.. _X(764):

X(764) = TRILINEAR CUBE OF X(513)
=================================

.. figure:: x-00764.svg
   :alt: X(764) = TRILINEAR CUBE OF X(513)
   :align: center

   **X(764) = TRILINEAR CUBE OF X(513)** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`(b - c)^{3} : (c - a)^{3} : (a - b)^{3}`

Barycentrics
~~~~~~~~~~~~

* :math:`a(b - c)^{3} : b(c - a)^{3} : c(a - b)^{3}`

* **Kimberling (6, 9, 13) Search Value:** :math:`-1.287854102443`

Incidence
---------

:ref:`X(764) <X(764)>` lies on the cubic K244 and on these lines:

{:ref:`1 <X(1)>`, :ref:`513 <X(513)>`}, {:ref:`10 <X(10)>`, :ref:`514 <X(514)>`}, {:ref:`56 <X(56)>`, :ref:`667 <X(667)>`}, {:ref:`76 <X(76)>`, :ref:`693 <X(693)>`}

Relations
---------

* :ref:`X(764) <X(764)>` = :term:`isotomic conjugate <isotomic-conjugate>` of :term:`isogonal conjugate <isogonal-conjugate>` of X(8027)
* :ref:`X(764) <X(764)>` = :term:`crosspoint <crosspoint>` of :ref:`X(244) <X(244)>` and :ref:`X(513) <X(513)>`
* :ref:`X(764) <X(764)>` = :term:`crosssum <crosssum>` of X(i) and X(j) for these (i,j): (:ref:`100 <X(100)>`, :ref:`765 <X(765)>`), (:ref:`692 <X(692)>`, 1252)
* :ref:`X(764) <X(764)>` = :term:`crossdifference <crossdifference>` of every pair of points on line :ref:`X(44) <X(44)>`\ \ :ref:`X(765) <X(765)>`

Construction
------------

.. literalinclude:: model.py
   :language: python
