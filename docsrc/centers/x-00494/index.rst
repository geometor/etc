:order: 494
:type: center
:canonical_id: X(494)
:dependencies: X(25), X(39), X(371), X(372), X(394), X(486), X(493), X(1505), X(3069)

.. _X(494):

X(494) = 2nd VAN LAMOEN HOMOTHETIC CENTER
=========================================

.. figure:: x-00494.svg
   :alt: X(494) = 2nd VAN LAMOEN HOMOTHETIC CENTER
   :align: center

   **X(494) = 2nd VAN LAMOEN HOMOTHETIC CENTER** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`1/(\sin A - \sin B \sin C) : :`

Barycentrics
~~~~~~~~~~~~

* :math:`(\sin A)(\sin A - \sin B \sin C) : :`
* :math:`a^2/(a^2 - S) : :`

* **Kimberling (6, 9, 13) Search Value:** :math:`-0.620505304165`

Notes
-----

.. container:: note-item

   :ref:`X(494) <X(494)>` is a homothetic center of triangles associated with squares that circumscribe ABC. For details and reference, see :ref:`X(493) <X(493)>`. (:person:`Floor van Lamoen <floor-van-lamoen>`, 4/27/98)

.. container:: note-item

   :ref:`X(494) <X(494)>` is the homothetic center of triangle ABC and the Lucas(-1) homothetic triangle; see :ref:`X(371) <X(371)>`.

.. container:: note-item

   Let A″ be the intersection of line BC and the common tangent to the B- and C-Lucas(-1) circles (at their touchpoint). Define B″ and C″ cyclically. Then A″B″C″ is the :term:`cevian triangle <cevian-triangle>` of :ref:`X(494) <X(494)>`. Also, :ref:`X(494) <X(494)>` is the point of intersection of the tangents at :ref:`X(372) <X(372)>` and :ref:`X(486) <X(486)>` to the orthocubic K006. (:person:`Randy Hutson <randy-hutson>`, July 23, 2015)

Incidence
---------

:ref:`X(494) <X(494)>` lies and on these lines:

{:ref:`25 <X(25)>`, :ref:`372 <X(372)>`}, {:ref:`39 <X(39)>`, :ref:`493 <X(493)>`}, {:ref:`394 <X(394)>`, 1505}

Relations
---------

* :ref:`X(494) <X(494)>` = :term:`isogonal conjugate <isogonal-conjugate>` of X(3069)
* :ref:`X(494) <X(494)>` = :ref:`X(394) <X(394)>`-:term:`cross conjugate <cross-conjugate>` of :ref:`X(493) <X(493)>`
* :ref:`X(494) <X(494)>` = perspector of ABC and :term:`unary cofactor triangle <unary-cofactor-triangle>` of inner Vecten triangle
* :ref:`X(494) <X(494)>` = perspector of ABC and unary cofactor triangle of Lucas antipodal triangle

Construction
------------

.. literalinclude:: model.py
   :language: python
