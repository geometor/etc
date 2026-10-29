:order: 643
:type: center
:canonical_id: X(643)
:dependencies: X(8), X(9), X(21), X(99), X(100), X(101), X(109), X(110), X(162), X(163), X(190), X(212), X(283), X(312), X(931), X(1018), X(1043), X(1098), X(4017), X(4077)

.. _X(643):

X(643) = TRILINEAR MULTIPLIER FOR KIEPERT PARABOLA
==================================================

.. figure:: x-00643.svg
   :alt: X(643) = TRILINEAR MULTIPLIER FOR KIEPERT PARABOLA
   :align: center

   **X(643) = TRILINEAR MULTIPLIER FOR KIEPERT PARABOLA** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`f(a,b,c) : f(b,c,a) : f(c,a,b)`, where f(a,b,c) = (b + c - a)/(b\ :sup:`2` - c\ :sup:`2`)

Barycentrics
~~~~~~~~~~~~

* :math:`g(a,b,c) : g(b,c,a) : g(c,a,b)`, where g(a,b,c) = af(a,b,c)

* **Kimberling (6, 9, 13) Search Value:** :math:`8.674646291873`

Notes
-----

.. container:: note-item

   :ref:`X(643) <X(643)>` satisfies the equation X\*(incircle) = Kiepert parabola, where \* denotes trilinear multiplication, defined by

   (u : v : w) \* (x : y : z) = ux : vy : wz.

Incidence
---------

:ref:`X(643) <X(643)>` lies and on these lines:

{:ref:`8 <X(8)>`, 1098}, {:ref:`99 <X(99)>`, :ref:`109 <X(109)>`}, {:ref:`100 <X(100)>`, :ref:`110 <X(110)>`}, {:ref:`101 <X(101)>`, :ref:`931 <X(931)>`}, {:ref:`162 <X(162)>`, :ref:`190 <X(190)>`}, {:ref:`163 <X(163)>`, 1018}, {:ref:`212 <X(212)>`, :ref:`312 <X(312)>`}, {:ref:`283 <X(283)>`, 1043}

Relations
---------

* :ref:`X(643) <X(643)>` = :term:`isogonal conjugate <isogonal-conjugate>` of X(4017)
* :ref:`X(643) <X(643)>` = :term:`isotomic conjugate <isotomic-conjugate>` of X(4077)
* :ref:`X(643) <X(643)>` = :term:`trilinear pole <trilinear-pole>` of line :ref:`X(9) <X(9)>`\ \ :ref:`X(21) <X(21)>`

Construction
------------

.. literalinclude:: model.py
   :language: python
