:order: 874
:type: center
:canonical_id: X(874)
:dependencies: X(1), X(75), X(99), X(100), X(190), X(239), X(350), X(646), X(670), X(789), X(798), X(875), X(876), X(1084)

.. _X(874):

X(874) = INTERSECTION OF LINES X(1)X(75) AND X(99)X(670)
========================================================

.. figure:: x-00874.svg
   :alt: X(874) = INTERSECTION OF LINES X(1)X(75) AND X(99)X(670)
   :align: center

   **X(874) = INTERSECTION OF LINES X(1)X(75) AND X(99)X(670)** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`f(a,b,c) : f(b,c,a) : f(c,a,b),`, where f(a,b,c) = (a\ :sup:`2`\ u\ :sup:`2` - bcvw)/[a\ :sup:`2`\ u(bv - cw)], u : v : w = :ref:`X(1) <X(1)>`

Barycentrics
~~~~~~~~~~~~

* :math:`g(a,b,c) : g(b,c,a) : g(c,a,b)`, where g(a,b,c) = af(a,b,c)

* **Kimberling (6, 9, 13) Search Value:** :math:`56.177035853433`

Incidence
---------

:ref:`X(874) <X(874)>` lies and on these lines:

{:ref:`1 <X(1)>`, :ref:`75 <X(75)>`}, {:ref:`99 <X(99)>`, :ref:`670 <X(670)>`}, {:ref:`100 <X(100)>`, :ref:`789 <X(789)>`}, {:ref:`190 <X(190)>`, :ref:`646 <X(646)>`}

Relations
---------

* :ref:`X(874) <X(874)>` = :term:`isogonal conjugate <isogonal-conjugate>` of :ref:`X(875) <X(875)>`
* :ref:`X(874) <X(874)>` = :term:`isotomic conjugate <isotomic-conjugate>` of :ref:`X(876) <X(876)>`
* :ref:`X(874) <X(874)>` = :term:`crossdifference <crossdifference>` of every pair of points on line :ref:`X(798) <X(798)>`\ X(1084)
* :ref:`X(874) <X(874)>` = :term:`trilinear pole <trilinear-pole>` of line :ref:`X(239) <X(239)>`\ \ :ref:`X(350) <X(350)>`

Construction
------------

.. literalinclude:: model.py
   :language: python
