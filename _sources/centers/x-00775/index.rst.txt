:order: 775
:type: center
:canonical_id: X(775)
:dependencies: X(1), X(10), X(31), X(158), X(225), X(255), X(412), X(662), X(774), X(801), X(820), X(1097)

.. _X(775):

X(775) = ISOGONAL CONJUGATE OF X(774)
=====================================

.. figure:: x-00775.svg
   :alt: X(775) = ISOGONAL CONJUGATE OF X(774)
   :align: center

   **X(775) = ISOGONAL CONJUGATE OF X(774)** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`f(A,B,C) : f(B,C,A) : f(C,A,B)`, where f(A,B,C) = 1/[cos\ :sup:`2`\ B + cos\ :sup:`2`\ C]

Barycentrics
~~~~~~~~~~~~

* :math:`g(A,B,C) : g(B,C,A) : g(C,A,B)`, where g(A,B,C) = (sin A)f(A,B,C)

* **Kimberling (6, 9, 13) Search Value:** :math:`2.261958826953`

Incidence
---------

:ref:`X(775) <X(775)>` lies and on these lines:

{:ref:`10 <X(10)>`, :ref:`801 <X(801)>`}, {:ref:`31 <X(31)>`, 1097}, {:ref:`158 <X(158)>`, :ref:`255 <X(255)>`}, {:ref:`225 <X(225)>`, :ref:`412 <X(412)>`}, {:ref:`662 <X(662)>`, :ref:`820 <X(820)>`}

Relations
---------

* :ref:`X(775) <X(775)>` = :term:`isogonal conjugate <isogonal-conjugate>` of :ref:`X(774) <X(774)>`
* :ref:`X(775) <X(775)>` = :term:`cevapoint <cevapoint>` of :ref:`X(1) <X(1)>` and :ref:`X(255) <X(255)>`

Construction
------------

.. literalinclude:: model.py
   :language: python
