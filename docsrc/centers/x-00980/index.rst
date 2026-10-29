:order: 980
:type: center
:canonical_id: X(980)
:dependencies: X(1), X(2), X(3), X(32), X(38), X(39), X(63), X(81), X(213), X(650), X(669), X(869), X(981)

.. _X(980):

X(980) = INTERSECTION OF LINES X(1)X(3) AND X(2)X(39)
=====================================================

.. figure:: x-00980.svg
   :alt: X(980) = INTERSECTION OF LINES X(1)X(3) AND X(2)X(39)
   :align: center

   **X(980) = INTERSECTION OF LINES X(1)X(3) AND X(2)X(39)** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`f(a,b,c) : f(b,c,a) : f(c,a,b),`, where f(a,b,c) = a\ :sup:`2`\ (b\ :sup:`2` + bc + c\ :sup:`2`) + (b\ :sup:`2` + c\ :sup:`2`)(bc + ca + ab)

Barycentrics
~~~~~~~~~~~~

* :math:`g(a,b,c) : g(b,c,a) : g(c,a,b)`, where g(a,b,c) = af(a,b,c)

* **Kimberling (6, 9, 13) Search Value:** :math:`1.906943083314`

Incidence
---------

:ref:`X(980) <X(980)>` lies and on these lines:

{:ref:`1 <X(1)>`, :ref:`3 <X(3)>`}, {:ref:`2 <X(2)>`, :ref:`39 <X(39)>`}, {:ref:`32 <X(32)>`, :ref:`81 <X(81)>`}, {:ref:`38 <X(38)>`, :ref:`869 <X(869)>`}, {:ref:`63 <X(63)>`, :ref:`213 <X(213)>`}

Relations
---------

* :ref:`X(980) <X(980)>` = :term:`isogonal conjugate <isogonal-conjugate>` of :ref:`X(981) <X(981)>`
* :ref:`X(980) <X(980)>` = :term:`crossdifference <crossdifference>` of every pair of points on line :ref:`X(650) <X(650)>`\ \ :ref:`X(669) <X(669)>`

Construction
------------

.. literalinclude:: model.py
   :language: python
