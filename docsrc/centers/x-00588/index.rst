:order: 588
:type: center
:canonical_id: X(588)
:dependencies: X(6), X(39), X(371), X(589), X(590), X(1994)

.. _X(588):

X(588) = 1st KENMOTU-VAN LAMOEN POINT
=====================================

.. figure:: x-00588.svg
   :alt: X(588) = 1st KENMOTU-VAN LAMOEN POINT
   :align: center

   **X(588) = 1st KENMOTU-VAN LAMOEN POINT** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`f(a,b,c) : f(b,c,a) : f(c,a,b)`, where f(a,b,c) = a/(a\ :sup:`2` + 4\*area(ABC))

Barycentrics
~~~~~~~~~~~~

* :math:`g(a,b,c) : g(b,c,a) : g(c,a,b)`, where g(a,b,c) = af(a,b,c)

* **Kimberling (6, 9, 13) Search Value:** :math:`1.800280685203`

Linear Combinations
-------------------

* :person:`Floor van Lamoen <floor-van-lamoen>`, `Some concurrences from Tucker hexagons, <http://forumgeom.fau.edu/FG2002volume2/FG200202index.html>`__ *:cite:`Forum Geometricorum <forum-geometricorum>`* 2 (2002) 5-13.

Notes
-----

.. container:: note-item

   :ref:`X(588) <X(588)>` is the perspector of triangles ABC and A'B'C', where A' is the circumcenter of :ref:`X(371) <X(371)>` and the points where the squares in the Kenmotu configuration with center :ref:`X(371) <X(371)>` meet sideline BC, and B' and C' are defined cyclically. See

.. container:: note-item

   :ref:`X(588) <X(588)>` is the homothetic center of triangle ABC and the Lucas(2:1) homothetic triangle; see :ref:`X(371) <X(371)>` and :ref:`X(589) <X(589)>`. (:person:`Randy Hutson <randy-hutson>`, 9/23/2011)

.. container:: note-item

   Let A'B'C' be the Lucas :term:`central triangle <central-triangle>`. Let A″ be the :term:`trilinear pole <trilinear-pole>` of line B'C'; define B″ and C″ cyclically. Let A\* be the trilinear pole of line B″C″; define B\* and C\* cyclically. The lines AA\*, BB\*, CC\* concur in :ref:`X(588) <X(588)>`. (Randy Hutson, January 29, 2015)

Incidence
---------

:ref:`X(588) <X(588)>` lies and on these lines:

{:ref:`39 <X(39)>`, :ref:`589 <X(589)>`}

Relations
---------

* :ref:`X(588) <X(588)>` = :term:`isogonal conjugate <isogonal-conjugate>` of :ref:`X(590) <X(590)>`
* :ref:`X(588) <X(588)>` = :term:`cevapoint <cevapoint>` of :ref:`X(6) <X(6)>` and :ref:`X(371) <X(371)>`
* :ref:`X(588) <X(588)>` = X(1994)-:term:`cross conjugate <cross-conjugate>` of :ref:`X(589) <X(589)>`

Construction
------------

.. literalinclude:: model.py
   :language: python
