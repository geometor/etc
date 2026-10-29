:order: 699
:type: center
:canonical_id: X(699)
:dependencies: X(6), X(32), X(99), X(172), X(251), X(385), X(689), X(698), X(932), X(1691), X(3221), X(35524)

.. _X(699):

X(699) = EVEN (- 4, - 2) CIRCUMCIRCLE POINT
===========================================

.. figure:: x-00699.svg
   :alt: X(699) = EVEN (- 4, - 2) CIRCUMCIRCLE POINT
   :align: center

   **X(699) = EVEN (- 4, - 2) CIRCUMCIRCLE POINT** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`f(a,b,c) : f(b,c,a) : f(c,a,b)`, where f(a,b,c) = 1/[a :sup:`-5`\ (b :sup:`-2` + c :sup:`-2`) - a :sup:`-3`\ (b :sup:`-4` + c :sup:`-4`)]

Barycentrics
~~~~~~~~~~~~

* :math:`a^2/(a^2 b^4 + a^2 c^4 - b^4 c^2 - b^2 c^4) : :`

* **Kimberling (6, 9, 13) Search Value:** :math:`-0.588121284539`

Incidence
---------

:ref:`X(699) <X(699)>` lies on the circumcircle and on these lines:

{:ref:`32 <X(32)>`, :ref:`99 <X(99)>`}, {:ref:`172 <X(172)>`, :ref:`932 <X(932)>`}, {:ref:`251 <X(251)>`, :ref:`689 <X(689)>`}

Relations
---------

* :ref:`X(699) <X(699)>` = :term:`isogonal conjugate <isogonal-conjugate>` of :ref:`X(698) <X(698)>`
* :ref:`X(699) <X(699)>` = :term:`isotomic conjugate <isotomic-conjugate>` of X(35524)
* :ref:`X(699) <X(699)>` = :ref:`X(385) <X(385)>`-:term:`cross conjugate <cross-conjugate>` of :ref:`X(251) <X(251)>`
* :ref:`X(699) <X(699)>` = :term:`trilinear pole <trilinear-pole>` of line :ref:`X(6) <X(6)>`\ X(3221)
* :ref:`X(699) <X(699)>` = Ψ(:ref:`X(6) <X(6)>`, X(3221))
* :ref:`X(699) <X(699)>` = :term:`cevapoint <cevapoint>` of :ref:`X(32) <X(32)>` and X(1691)

Construction
------------

.. literalinclude:: model.py
   :language: python
