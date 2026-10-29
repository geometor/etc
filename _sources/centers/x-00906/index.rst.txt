:order: 906
:type: center
:canonical_id: X(906)
:dependencies: X(3), X(11), X(32), X(41), X(48), X(63), X(72), X(92), X(100), X(101), X(109), X(112), X(163), X(184), X(218), X(219), X(248), X(513), X(577), X(601), X(692), X(1331), X(2969), X(4574), X(17924)

.. _X(906):

X(906) = INTERSECTION OF LINES X(100)X(112) AND X(101)X(109)
============================================================

.. figure:: x-00906.svg
   :alt: X(906) = INTERSECTION OF LINES X(100)X(112) AND X(101)X(109)
   :align: center

   **X(906) = INTERSECTION OF LINES X(100)X(112) AND X(101)X(109)** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* (cos A)/[wb\ :sup:`2` - vc\ :sup:`2` + a(wb - vc)], u : v : w = :ref:`X(3) <X(3)>`
* :math:`(\sin 2A)/(b - c) : :`

Barycentrics
~~~~~~~~~~~~

* :math:`g(a,b,c) : g(b,c,a) : g(c,a,b)`, where g(a,b,c) = a\ :sup:`3`\ (b\ :sup:`2` + c\ :sup:`2` - a\ :sup:`2`)/(b - c)

* **Kimberling (6, 9, 13) Search Value:** :math:`-2.311286980824`

Incidence
---------

:ref:`X(906) <X(906)>` lies and on these lines:

{:ref:`32 <X(32)>`, :ref:`218 <X(218)>`}, {:ref:`41 <X(41)>`, :ref:`601 <X(601)>`}, {:ref:`72 <X(72)>`, :ref:`248 <X(248)>`}, {:ref:`100 <X(100)>`, :ref:`112 <X(112)>`}, {:ref:`101 <X(101)>`, :ref:`109 <X(109)>`}, {:ref:`163 <X(163)>`, :ref:`692 <X(692)>`}, {:ref:`219 <X(219)>`, :ref:`577 <X(577)>`}, {1331, 4574}

Relations
---------

* :ref:`X(906) <X(906)>` = :term:`isogonal conjugate <isogonal-conjugate>` of X(17924)
* :ref:`X(906) <X(906)>` = :ref:`X(92) <X(92)>`-:term:`isoconjugate <isoconjugate>` of :ref:`X(513) <X(513)>`
* :ref:`X(906) <X(906)>` = :term:`trilinear pole <trilinear-pole>` of line :ref:`X(48) <X(48)>`\ \ :ref:`X(184) <X(184)>`
* :ref:`X(906) <X(906)>` = :term:`crossdifference <crossdifference>` of every pair of points on line :ref:`X(11) <X(11)>`\ X(2969)
* :ref:`X(906) <X(906)>` = barycentric product :ref:`X(3) <X(3)>`\ \*\ :ref:`X(100) <X(100)>`
* :ref:`X(906) <X(906)>` = barycentric product of circumcircle intercepts of line :ref:`X(3) <X(3)>`\ \ :ref:`X(63) <X(63)>`

Construction
------------

.. literalinclude:: model.py
   :language: python
