:order: 732
:type: center
:canonical_id: X(732)
:dependencies: X(6), X(30), X(39), X(69), X(76), X(141), X(194), X(385), X(511), X(688), X(733), X(14970)

.. _X(732):

X(732) = EVEN (- 2, 2) INFINITY POINT
=====================================

.. figure:: x-00732.svg
   :alt: X(732) = EVEN (- 2, 2) INFINITY POINT
   :align: center

   **X(732) = EVEN (- 2, 2) INFINITY POINT** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`f(a,b,c) : f(b,c,a) : f(c,a,b)`, where f(a,b,c) = a :sup:`-3`\ (b\ :sup:`2` + c\ :sup:`2`) - a\ :sup:`1`\ (b :sup:`-2` + c :sup:`-2`)

Barycentrics
~~~~~~~~~~~~

* :math:`(b^2 + c^2) (a^4 - b^2 c^2) : :`

Notes
-----

.. container:: note-item

   As the :term:`isogonal conjugate <isogonal-conjugate>` of a point on the circumcircle, :ref:`X(732) <X(732)>` lies on the line at infinity.

Incidence
---------

:ref:`X(732) <X(732)>` lies and on these lines:

{:ref:`6 <X(6)>`, :ref:`76 <X(76)>`}, {:ref:`30 <X(30)>`, :ref:`511 <X(511)>`}, {:ref:`39 <X(39)>`, :ref:`141 <X(141)>`}, {:ref:`69 <X(69)>`, :ref:`194 <X(194)>`}

Relations
---------

* :ref:`X(732) <X(732)>` = isogonal conjugate of :ref:`X(733) <X(733)>`
* :ref:`X(732) <X(732)>` = :term:`isotomic conjugate <isotomic-conjugate>` of X(14970)
* :ref:`X(732) <X(732)>` = :term:`crossdifference <crossdifference>` of every pair of points on line :ref:`X(6) <X(6)>`\ \ :ref:`X(688) <X(688)>`
* :ref:`X(732) <X(732)>` = :ref:`X(39) <X(39)>`-:term:`Hirst inverse <hirst-inverse>` of :ref:`X(141) <X(141)>`
* :ref:`X(732) <X(732)>` = barycentric product :ref:`X(141) <X(141)>`\ \*\ :ref:`X(385) <X(385)>`

Construction
------------

.. literalinclude:: model.py
   :language: python
