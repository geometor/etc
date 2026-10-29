:order: 352
:type: center
:canonical_id: X(352)
:dependencies: X(2), X(3), X(6), X(23), X(110), X(111), X(187), X(353), X(373), X(511), X(512), X(843), X(2502), X(2709), X(3815), X(6094)

.. _X(352):

X(352) = INVERSE-IN-CIRCUMCIRCLE OF X(353)
==========================================

.. figure:: x-00352.svg
   :alt: X(352) = INVERSE-IN-CIRCUMCIRCLE OF X(353)
   :align: center

   **X(352) = INVERSE-IN-CIRCUMCIRCLE OF X(353)** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`f(a,b,c) : f(b,c,a) : f(c,a,b)`, where f(a,b,c) = a(-a\ :sup:`4` - b\ :sup:`4` - c\ :sup:`4` - 5b\ :sup:`2`\ c\ :sup:`2` + 4a\ :sup:`2`\ b\ :sup:`2` + 4a\ :sup:`2`\ c\ :sup:`2`)

Barycentrics
~~~~~~~~~~~~

* :math:`af(a,b,c) : bf(b,c,a) : cf(c,a,b)`

* **Kimberling (6, 9, 13) Search Value:** :math:`-8.749665363574`

Incidence
---------

:ref:`X(352) <X(352)>` lies on the Parry circle and on these lines:

{:ref:`2 <X(2)>`, :ref:`6 <X(6)>`}, {:ref:`3 <X(3)>`, :ref:`353 <X(353)>`}, {:ref:`23 <X(23)>`, 2502}, {:ref:`110 <X(110)>`, :ref:`187 <X(187)>`}, {:ref:`111 <X(111)>`, :ref:`511 <X(511)>`}

Relations
---------

* :ref:`X(352) <X(352)>` = reflection of :ref:`X(843) <X(843)>` in :ref:`X(187) <X(187)>`
* :ref:`X(352) <X(352)>` = :term:`isogonal conjugate <isogonal-conjugate>` of X(6094)
* :ref:`X(352) <X(352)>` = inverse-in-circumcircle of :ref:`X(353) <X(353)>`
* :ref:`X(352) <X(352)>` = :term:`crossdifference <crossdifference>` of every pair of points on line :ref:`X(373) <X(373)>`\ \ :ref:`X(512) <X(512)>`
* :ref:`X(352) <X(352)>` = :ref:`X(23) <X(23)>`-of-circumsymmedial-triangle
* :ref:`X(352) <X(352)>` = inverse-in-{circumcircle, nine-point circle}-inverter of X(3815)
* :ref:`X(352) <X(352)>` = orthocentroidal-to-ABC :term:`similarity image <similarity-image>` of :ref:`X(111) <X(111)>`
* :ref:`X(352) <X(352)>` = 4th-Brocard-to-circumsymmedial similarity image of :ref:`X(111) <X(111)>`
* :ref:`X(352) <X(352)>` = X(2709)-of-1st-Parry-triangle
* :ref:`X(352) <X(352)>` = :ref:`X(843) <X(843)>`-of-2nd-Parry-triangle
* :ref:`X(352) <X(352)>` = :ref:`X(110) <X(110)>`-of-3rd-Parry-triangle
* :ref:`X(352) <X(352)>` = inverse-in-Parry-isodynamic-circle of :ref:`X(23) <X(23)>`; see :ref:`X(2) <X(2)>`
* :ref:`X(352) <X(352)>` = :term:`radical trace <radical-trace>` of circumcircles of Artzt and anti-Artzt triangles
* :ref:`X(352) <X(352)>` = :term:`trilinear pole <trilinear-pole>`, wrt 3rd Parry triangle, of Lemoine axis

Construction
------------

.. literalinclude:: model.py
   :language: python
