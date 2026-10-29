:order: 801
:type: center
:canonical_id: X(801)
:dependencies: X(2), X(4), X(6), X(10), X(20), X(99), X(235), X(394), X(520), X(523), X(775), X(800), X(1092), X(2071), X(13567)

.. _X(801):

X(801) = ISOGONAL CONJUGATE OF X(800)
=====================================

.. figure:: x-00801.svg
   :alt: X(801) = ISOGONAL CONJUGATE OF X(800)
   :align: center

   **X(801) = ISOGONAL CONJUGATE OF X(800)** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`f(A,B,C) : f(B,C,A) : f(C,A,B)`, where f(A,B,C) = (csc A)/(cos\ :sup:`2`\ B + cos\ :sup:`2`\ C)

Barycentrics
~~~~~~~~~~~~

* :math:`1/(a^4 (b^2 + c^2) - 2 a^2 (b^2 - c^2)^2 + (b^2 - c^2)^2 (b^2 + c^2)) : :`

* **Kimberling (6, 9, 13) Search Value:** :math:`3.291163117829`

Incidence
---------

:ref:`X(801) <X(801)>` lies and on these lines:

{:ref:`4 <X(4)>`, 1092}, {:ref:`10 <X(10)>`, :ref:`775 <X(775)>`}

Relations
---------

* :ref:`X(801) <X(801)>` = :term:`isogonal conjugate <isogonal-conjugate>` of :ref:`X(800) <X(800)>`
* :ref:`X(801) <X(801)>` = :term:`isotomic conjugate <isotomic-conjugate>` of X(13567)
* :ref:`X(801) <X(801)>` = polar conjugate of :ref:`X(235) <X(235)>`
* :ref:`X(801) <X(801)>` = :term:`trilinear pole <trilinear-pole>` of line :ref:`X(523) <X(523)>`\ X(2071) (the polar of :ref:`X(20) <X(20)>` wrt circumcircle)
* :ref:`X(801) <X(801)>` = :term:`cevapoint <cevapoint>` of X(i) and X(j) for these (i,j): (:ref:`2 <X(2)>`, :ref:`394 <X(394)>`), (:ref:`6 <X(6)>`, :ref:`20 <X(20)>`)
* :ref:`X(801) <X(801)>` = :ref:`X(520) <X(520)>`-:term:`cross conjugate <cross-conjugate>` of :ref:`X(99) <X(99)>`

Construction
------------

.. literalinclude:: model.py
   :language: python
