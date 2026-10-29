:order: 189
:type: center
:canonical_id: X(189)
:dependencies: X(2), X(4), X(7), X(8), X(20), X(29), X(57), X(69), X(77), X(81), X(84), X(92), X(198), X(222), X(223), X(280), X(281), X(282), X(309), X(329), X(522), X(905)

.. _X(189):

X(189) = CYCLOCEVIAN CONJUGATE OF X(8)
======================================

.. figure:: x-00189.svg
   :alt: X(189) = CYCLOCEVIAN CONJUGATE OF X(8)
   :align: center

   **X(189) = CYCLOCEVIAN CONJUGATE OF X(8)** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`bc/(\cos B + \cos C - \cos A - 1) : ca/(\cos C + \cos A - \cos B - 1) : ab/(\cos A + \cos B - \cos C - 1)`

Barycentrics
~~~~~~~~~~~~

* :math:`1/(\cos B + \cos C - \cos A - 1) : 1/(\cos C + \cos A - \cos B - 1) : 1/(\cos A + \cos B - \cos C - 1)`

* **Kimberling (6, 9, 13) Search Value:** :math:`9.489626975767`

Notes
-----

.. container:: note-item

   :ref:`X(189) <X(189)>` is the perspector of triangle ABC and the :term:`pedal triangle <pedal-triangle>` of :ref:`X(84) <X(84)>`.

Incidence
---------

:ref:`X(189) <X(189)>` lies on the Lucas cubic and on these lines:

{:ref:`2 <X(2)>`, :ref:`77 <X(77)>`}, {:ref:`7 <X(7)>`, :ref:`92 <X(92)>`}, {:ref:`8 <X(8)>`, :ref:`20 <X(20)>`}, {:ref:`29 <X(29)>`, :ref:`81 <X(81)>`}, {:ref:`69 <X(69)>`, :ref:`309 <X(309)>`}, {:ref:`222 <X(222)>`, :ref:`281 <X(281)>`}

Relations
---------

* :ref:`X(189) <X(189)>` = :term:`isogonal conjugate <isogonal-conjugate>` of :ref:`X(198) <X(198)>`
* :ref:`X(189) <X(189)>` = :term:`isotomic conjugate <isotomic-conjugate>` of :ref:`X(329) <X(329)>`
* :ref:`X(189) <X(189)>` = :term:`cyclocevian conjugate <cyclocevian-conjugate>` of :ref:`X(8) <X(8)>`
* :ref:`X(189) <X(189)>` = :term:`anticomplement <anticomplement>` of :ref:`X(223) <X(223)>`
* :ref:`X(189) <X(189)>` = :ref:`X(309) <X(309)>`-:term:`Ceva conjugate <ceva-conjugate>` of :ref:`X(280) <X(280)>`
* :ref:`X(189) <X(189)>` = :term:`cevapoint <cevapoint>` of :ref:`X(84) <X(84)>` and :ref:`X(282) <X(282)>`
* :ref:`X(189) <X(189)>` = X(i)-:term:`cross conjugate <cross-conjugate>` of X(j) for these (i,j): (:ref:`4 <X(4)>`, :ref:`7 <X(7)>`), (:ref:`57 <X(57)>`, :ref:`2 <X(2)>`), (:ref:`282 <X(282)>`, :ref:`280 <X(280)>`)
* :ref:`X(189) <X(189)>` = :term:`trilinear pole <trilinear-pole>` of line :ref:`X(522) <X(522)>`\ \ :ref:`X(905) <X(905)>`
* :ref:`X(189) <X(189)>` = perspector of ABC and the reflection in :ref:`X(282) <X(282)>` of the pedal triangle of :ref:`X(282) <X(282)>`

Construction
------------

.. literalinclude:: model.py
   :language: python
