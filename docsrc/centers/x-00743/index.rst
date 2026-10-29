:order: 743
:type: center
:canonical_id: X(743)
:dependencies: X(2), X(6), X(31), X(101), X(665), X(742), X(761), X(788), X(789), X(825), X(869), X(35545)

.. _X(743):

X(743) = EVEN (- 1, 2) CIRCUMCIRCLE POINT
=========================================

.. figure:: x-00743.svg
   :alt: X(743) = EVEN (- 1, 2) CIRCUMCIRCLE POINT
   :align: center

   **X(743) = EVEN (- 1, 2) CIRCUMCIRCLE POINT** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`f(a,b,c) : f(b,c,a) : f(c,a,b)`, where f(a,b,c) = 1/[a :sup:`-2`\ (b\ :sup:`2` + c\ :sup:`2`) - a\ :sup:`1`\ (b :sup:`-1` + c :sup:`-1`)]

Barycentrics
~~~~~~~~~~~~

* :math:`g(a,b,c) : g(b,c,a) : g(c,a,b)`, where g(a,b,c) = af(a,b,c)

* **Kimberling (6, 9, 13) Search Value:** :math:`0.351334943710`

Incidence
---------

:ref:`X(743) <X(743)>` lies on the circumcircle and on these lines:

{:ref:`2 <X(2)>`, :ref:`789 <X(789)>`}, {:ref:`31 <X(31)>`, :ref:`825 <X(825)>`}, {:ref:`101 <X(101)>`, :ref:`869 <X(869)>`}, {:ref:`665 <X(665)>`, :ref:`761 <X(761)>`}

Relations
---------

* :ref:`X(743) <X(743)>` = :term:`isogonal conjugate <isogonal-conjugate>` of :ref:`X(742) <X(742)>`
* :ref:`X(743) <X(743)>` = :term:`isotomic conjugate <isotomic-conjugate>` of X(35545)
* :ref:`X(743) <X(743)>` = :term:`trilinear pole <trilinear-pole>` of line :ref:`X(6) <X(6)>`\ \ :ref:`X(788) <X(788)>`
* :ref:`X(743) <X(743)>` = Ψ(:ref:`X(6) <X(6)>`, :ref:`X(788) <X(788)>`)

Construction
------------

.. literalinclude:: model.py
   :language: python
