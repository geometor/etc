:order: 294
:type: center
:canonical_id: X(294)
:dependencies: X(1), X(2), X(4), X(6), X(7), X(8), X(19), X(41), X(55), X(84), X(104), X(105), X(218), X(220), X(239), X(241), X(314), X(580), X(645), X(650), X(666), X(672), X(910), X(919), X(926), X(949), X(1041), X(1279), X(1362), X(1458), X(17060), X(27818)

.. _X(294):

X(294) = ISOGONAL CONJUGATE OF X(241)
=====================================

.. figure:: x-00294.svg
   :alt: X(294) = ISOGONAL CONJUGATE OF X(241)
   :align: center

   **X(294) = ISOGONAL CONJUGATE OF X(241)** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`f(a,b,c) : f(b,c,a) : f(c,a,b)`, where f(a,b,c) = (b + c - a)/(b\ :sup:`2` + c\ :sup:`2` - ab - ac)

* **Kimberling (6, 9, 13) Search Value:** :math:`2.052081234010`

Notes
-----

.. container:: note-item

   :ref:`X(294) <X(294)>` is the perspector of the :term:`anticevian triangle <anticevian-triangle>` of :ref:`X(105) <X(105)>` and the :term:`unary cofactor triangle <unary-cofactor-triangle>` of the intangents triangle. (:person:`Randy Hutson <randy-hutson>`, January 15, 2019)

Incidence
---------

:ref:`X(294) <X(294)>` lies and on these lines:

{:ref:`1 <X(1)>`, :ref:`41 <X(41)>`}, {:ref:`2 <X(2)>`, :ref:`949 <X(949)>`}, {:ref:`4 <X(4)>`, :ref:`218 <X(218)>`}, {:ref:`6 <X(6)>`, :ref:`7 <X(7)>`}, {:ref:`8 <X(8)>`, :ref:`220 <X(220)>`}, {:ref:`19 <X(19)>`, 1041}, {:ref:`84 <X(84)>`, :ref:`580 <X(580)>`}, {:ref:`104 <X(104)>`, :ref:`919 <X(919)>`}, {:ref:`239 <X(239)>`, :ref:`666 <X(666)>`}, {:ref:`241 <X(241)>`, :ref:`910 <X(910)>`}, {:ref:`314 <X(314)>`, :ref:`645 <X(645)>`}

Relations
---------

* :ref:`X(294) <X(294)>` = :term:`isogonal conjugate <isogonal-conjugate>` of :ref:`X(241) <X(241)>`
* :ref:`X(294) <X(294)>` = :term:`isotomic conjugate <isotomic-conjugate>` of X(27818)
* :ref:`X(294) <X(294)>` = :term:`anticomplement <anticomplement>` of X(17060)
* :ref:`X(294) <X(294)>` = :term:`crosssum <crosssum>` of X(i) and X(j) for these (i,j): (:ref:`672 <X(672)>`, 1458), (:ref:`910 <X(910)>`, 1279)
* :ref:`X(294) <X(294)>` = :term:`crossdifference <crossdifference>` of every pair of points on line :ref:`X(926) <X(926)>`\ X(1362)
* :ref:`X(294) <X(294)>` = :ref:`X(1) <X(1)>`-:term:`Hirst inverse <hirst-inverse>` of :ref:`X(105) <X(105)>`
* :ref:`X(294) <X(294)>` = :term:`trilinear pole <trilinear-pole>` of line :ref:`X(55) <X(55)>`\ \ :ref:`X(650) <X(650)>`
* :ref:`X(294) <X(294)>` = perspector of conic {A,B,C,PU(96)}
* :ref:`X(294) <X(294)>` = intersection of :term:`trilinear polars <trilinear-polar>` of P(96) and U(96)

Construction
------------

.. literalinclude:: model.py
   :language: python
