:order: 741
:type: center
:canonical_id: X(741)
:dependencies: X(1), X(6), X(21), X(31), X(37), X(42), X(58), X(75), X(81), X(86), X(99), X(101), X(107), X(110), X(190), X(334), X(335), X(512), X(689), X(691), X(740), X(759), X(789), X(798), X(827), X(835), X(839), X(849), X(873), X(876), X(923), X(932), X(934), X(1042), X(1096), X(1326), X(35544), X(38481)

.. _X(741):

X(741) = EVEN (- 1, 1) CIRCUMCIRCLE POINT
=========================================

.. figure:: x-00741.svg
   :alt: X(741) = EVEN (- 1, 1) CIRCUMCIRCLE POINT
   :align: center

   **X(741) = EVEN (- 1, 1) CIRCUMCIRCLE POINT** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`f(a,b,c) : f(b,c,a) : f(c,a,b)`, where f(a,b,c) = 1/[a :sup:`-2`\ (b\ :sup:`1` + c\ :sup:`1`) - a\ :sup:`0`\ (b :sup:`-1` + c :sup:`-1`)]

Barycentrics
~~~~~~~~~~~~

* :math:`g(a,b,c) : g(b,c,a) : g(c,a,b)`, where g(a,b,c) = af(a,b,c)

* **Kimberling (6, 9, 13) Search Value:** :math:`-0.106320646595`

Incidence
---------

:ref:`X(741) <X(741)>` lies on the circumcircle and on these lines:

{:ref:`1 <X(1)>`, :ref:`99 <X(99)>`}, {:ref:`21 <X(21)>`, :ref:`932 <X(932)>`}, {:ref:`31 <X(31)>`, :ref:`110 <X(110)>`}, {:ref:`42 <X(42)>`, :ref:`81 <X(81)>`}, {:ref:`58 <X(58)>`, :ref:`101 <X(101)>`}, {:ref:`86 <X(86)>`, :ref:`789 <X(789)>`}, {:ref:`107 <X(107)>`, 1096}, {:ref:`334 <X(334)>`, :ref:`839 <X(839)>`}, {:ref:`335 <X(335)>`, :ref:`835 <X(835)>`}, {:ref:`689 <X(689)>`, :ref:`873 <X(873)>`}, {:ref:`691 <X(691)>`, :ref:`923 <X(923)>`}, {:ref:`759 <X(759)>`, :ref:`876 <X(876)>`}, {:ref:`827 <X(827)>`, :ref:`849 <X(849)>`}, {:ref:`934 <X(934)>`, 1042}

Relations
---------

* :ref:`X(741) <X(741)>` = :term:`isogonal conjugate <isogonal-conjugate>` of :ref:`X(740) <X(740)>`
* :ref:`X(741) <X(741)>` = :term:`isotomic conjugate <isotomic-conjugate>` of X(35544)
* :ref:`X(741) <X(741)>` = :term:`trilinear pole <trilinear-pole>` of line :ref:`X(6) <X(6)>`\ \ :ref:`X(798) <X(798)>`
* :ref:`X(741) <X(741)>` = Ψ(:ref:`X(6) <X(6)>`, :ref:`X(798) <X(798)>`)
* :ref:`X(741) <X(741)>` = Ψ(:ref:`X(190) <X(190)>`, :ref:`X(37) <X(37)>`)
* :ref:`X(741) <X(741)>` = Ψ(:ref:`X(1) <X(1)>`, :ref:`X(512) <X(512)>`)
* :ref:`X(741) <X(741)>` = Λ(:ref:`X(1) <X(1)>`, :ref:`X(75) <X(75)>`)
* :ref:`X(741) <X(741)>` = :term:`cevapoint <cevapoint>` of :ref:`X(58) <X(58)>` and X(1326)
* :ref:`X(741) <X(741)>` = Conway-circle-inverse of X(38481)
* :ref:`X(741) <X(741)>` = trilinear product of circumcircle intercepts of line :ref:`X(1) <X(1)>`\ \ :ref:`X(512) <X(512)>`

Construction
------------

.. literalinclude:: model.py
   :language: python
