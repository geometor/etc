:order: 196
:type: center
:canonical_id: X(196)
:dependencies: X(1), X(2), X(4), X(7), X(19), X(34), X(40), X(55), X(57), X(65), X(92), X(108), X(207), X(208), X(221), X(226), X(268), X(278), X(280), X(281), X(329), X(342), X(347), X(521), X(648), X(653), X(937), X(3239)

.. _X(196):

X(196) = X(7)-CEVA CONJUGATE OF X(4)
====================================

.. figure:: x-00196.svg
   :alt: X(196) = X(7)-CEVA CONJUGATE OF X(4)
   :align: center

   **X(196) = X(7)-CEVA CONJUGATE OF X(4)** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`f(A,B,C) : f(B,C,A) : f(C,A,B)`, where f(A,B,C) = (cos B + cos C - cos A - 1) sec A tan A/2

Barycentrics
~~~~~~~~~~~~

* :math:`g(A,B,C) : g(B,C,A) : g(C,A,B)`, where g(A,B,C) = (cos B + cos C - cos A - 1) tan A tan A/2

* **Kimberling (6, 9, 13) Search Value:** :math:`0.283379483064`

Incidence
---------

:ref:`X(196) <X(196)>` lies and on these lines:

{:ref:`1 <X(1)>`, :ref:`207 <X(207)>`}, {:ref:`2 <X(2)>`, :ref:`653 <X(653)>`}, {:ref:`4 <X(4)>`, :ref:`65 <X(65)>`}, {:ref:`7 <X(7)>`, :ref:`92 <X(92)>`}, {:ref:`19 <X(19)>`, :ref:`57 <X(57)>`}, {:ref:`34 <X(34)>`, :ref:`937 <X(937)>`}, {:ref:`40 <X(40)>`, :ref:`208 <X(208)>`}, {:ref:`55 <X(55)>`, :ref:`108 <X(108)>`}, {:ref:`226 <X(226)>`, :ref:`281 <X(281)>`}, {:ref:`329 <X(329)>`, :ref:`342 <X(342)>`}

Relations
---------

* :ref:`X(196) <X(196)>` = :term:`isogonal conjugate <isogonal-conjugate>` of :ref:`X(268) <X(268)>`
* :ref:`X(196) <X(196)>` = X(i)-:term:`Ceva conjugate <ceva-conjugate>` of X(j) for these (i,j): (:ref:`7 <X(7)>`, :ref:`4 <X(4)>`), (:ref:`92 <X(92)>`, :ref:`278 <X(278)>`)
* :ref:`X(196) <X(196)>` = :term:`cevapoint <cevapoint>` of :ref:`X(19) <X(19)>` and :ref:`X(207) <X(207)>`
* :ref:`X(196) <X(196)>` = :ref:`X(221) <X(221)>`-:term:`cross conjugate <cross-conjugate>` of :ref:`X(347) <X(347)>`
* :ref:`X(196) <X(196)>` = X(i)-:term:`beth conjugate <beth-conjugate>` of X(j) for these (i,j): (:ref:`648 <X(648)>`, :ref:`2 <X(2)>`), (:ref:`653 <X(653)>`, :ref:`196 <X(196)>`)
* :ref:`X(196) <X(196)>` = Danneels point of :ref:`X(653) <X(653)>`
* :ref:`X(196) <X(196)>` = pole wrt polar circle of :term:`trilinear polar <trilinear-polar>` of :ref:`X(280) <X(280)>` (line :ref:`X(521) <X(521)>`\ X(3239))
* :ref:`X(196) <X(196)>` = polar conjugate of :ref:`X(280) <X(280)>`

Construction
------------

.. literalinclude:: model.py
   :language: python
