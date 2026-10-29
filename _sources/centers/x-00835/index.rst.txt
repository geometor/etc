:order: 835
:type: center
:canonical_id: X(835)
:dependencies: X(6), X(10), X(110), X(190), X(335), X(522), X(741), X(834), X(958)

.. _X(835):

X(835) = o-(2, 3) CIRCUMCIRCLE POINT
====================================

.. figure:: x-00835.svg
   :alt: X(835) = o-(2, 3) CIRCUMCIRCLE POINT
   :align: center

   **X(835) = o-(2, 3) CIRCUMCIRCLE POINT** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`f(a,b,c) : f(b,c,a) : f(c,a,b)`, where f(a,b,c) = 1/[a\ :sup:`1`\ (b\ :sup:`3` - c\ :sup:`3`) + a\ :sup:`2`\ (b\ :sup:`2` - c\ :sup:`2`)]

Barycentrics
~~~~~~~~~~~~

* :math:`g(a,b,c) : g(b,c,a) : g(c,a,b)`, where g(a,b,c) = af(a,b,c)

* **Kimberling (6, 9, 13) Search Value:** :math:`3.602232534142`

Incidence
---------

:ref:`X(835) <X(835)>` lies on the circumcircle and on these lines:

{:ref:`110 <X(110)>`, :ref:`190 <X(190)>`}, {:ref:`335 <X(335)>`, :ref:`741 <X(741)>`}

Relations
---------

* :ref:`X(835) <X(835)>` = :term:`isogonal conjugate <isogonal-conjugate>` of :ref:`X(834) <X(834)>`
* :ref:`X(835) <X(835)>` = :term:`trilinear pole <trilinear-pole>` of line :ref:`X(6) <X(6)>`\ \ :ref:`X(10) <X(10)>`
* :ref:`X(835) <X(835)>` = Ψ(:ref:`X(6) <X(6)>`, :ref:`X(10) <X(10)>`)
* :ref:`X(835) <X(835)>` = :term:`cevapoint <cevapoint>` of :ref:`X(522) <X(522)>` and :ref:`X(958) <X(958)>`

Construction
------------

.. literalinclude:: model.py
   :language: python
