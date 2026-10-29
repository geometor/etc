:order: 493
:type: center
:canonical_id: X(493)
:dependencies: X(25), X(39), X(371), X(394), X(485), X(494), X(588), X(589), X(1504), X(3068)

.. _X(493):

X(493) = 1st VAN LAMOEN HOMOTHETIC CENTER
=========================================

.. figure:: x-00493.svg
   :alt: X(493) = 1st VAN LAMOEN HOMOTHETIC CENTER
   :align: center

   **X(493) = 1st VAN LAMOEN HOMOTHETIC CENTER** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`1/(\sin A + \sin B \sin C) : :`

Barycentrics
~~~~~~~~~~~~

* :math:`(\sin A)/(\sin A + \sin B \sin C) : :`
* :math:`a^2/(a^2 + S) : :`

* **Kimberling (6, 9, 13) Search Value:** :math:`1.847641056142`

Notes
-----

.. container:: note-item

   :ref:`X(493) <X(493)>` is a homothetic center of triangles associated with squares that circumscribe ABC. For details, see `Vierkanten in een driehoek: 4. Ingeschreven vierkanten <http://home.wxs.nl/~lamoen/wiskunde/vierkant4.html>`__ (:person:`Floor van Lamoen <floor-van-lamoen>`, 4/27/98)

.. container:: note-item

   :ref:`X(493) <X(493)>` is the homothetic center of triangle ABC and the Lucas homothetic triangle; see :ref:`X(371) <X(371)>`. Writing t for the ratio L:W at :ref:`X(371) <X(371)>`, let L\ :sub:`A` be the line through the intersections, other than A, of the A-Lucas(t) circle and sides CA and AB. Define L\ :sub:`B` and L\ :sub:`C` cyclically. Let A' = L\ :sub:`B`\ ∩L\ :sub:`C`, and define B' and C' cyclically. Then the triangle A'B'C', here introduced as the Lucas(t) homothetic triangle, is homothetic to triangle ABC. If t = 1, the center of homothety is :ref:`X(493) <X(493)>`; for t = -1, it is :ref:`X(494) <X(494)>`; for t = 2, it is :ref:`X(588) <X(588)>`; and for t = -2, it is :ref:`X(589) <X(589)>`. (:person:`Randy Hutson <randy-hutson>`, February 9, 2013)

.. container:: note-item

   Let A″ be the intersection of line BC and the common tangent to the B- and C-Lucas circles (at their touchpoint). Define B″ and C″ cyclically. Then A″B″C″ is the :term:`cevian triangle <cevian-triangle>` of :ref:`X(493) <X(493)>`. Also, :ref:`X(493) <X(493)>` is the point of intersection of the tangents at :ref:`X(371) <X(371)>` and :ref:`X(485) <X(485)>` to the orthocubic K006. (Randy Hutson, July 23, 2015)

Incidence
---------

:ref:`X(493) <X(493)>` lies and on these lines:

{:ref:`25 <X(25)>`, :ref:`371 <X(371)>`}, {:ref:`39 <X(39)>`, :ref:`494 <X(494)>`}, {:ref:`394 <X(394)>`, 1504}

Relations
---------

* :ref:`X(493) <X(493)>` = :term:`isogonal conjugate <isogonal-conjugate>` of X(3068)
* :ref:`X(493) <X(493)>` = :ref:`X(394) <X(394)>`-:term:`cross conjugate <cross-conjugate>` of :ref:`X(494) <X(494)>`
* :ref:`X(493) <X(493)>` = perspector of ABC and :term:`unary cofactor triangle <unary-cofactor-triangle>` of outer Vecten triangle
* :ref:`X(493) <X(493)>` = perspector of ABC and unary cofactor triangle of Lucas(-1) antipodal triangle

Construction
------------

.. literalinclude:: model.py
   :language: python
