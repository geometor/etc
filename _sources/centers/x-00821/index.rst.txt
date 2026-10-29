:order: 821
:type: center
:canonical_id: X(821)
:dependencies: X(1), X(158), X(243), X(255), X(411), X(774), X(820), X(823), X(6508)

.. _X(821):

X(821) = ISOGONAL CONJUGATE OF X(820)
=====================================

.. figure:: x-00821.svg
   :alt: X(821) = ISOGONAL CONJUGATE OF X(820)
   :align: center

   **X(821) = ISOGONAL CONJUGATE OF X(820)** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`f(A,B,C) : f(B,C,A) : f(C,A,B)`, where f(A,B,C) = sec\ :sup:`2`\ A /(cos\ :sup:`2`\ B + cos\ :sup:`2`\ C)

Barycentrics
~~~~~~~~~~~~

* :math:`g(A,B,C) : g(B,C,A) : g(C,A,B)`, where g(A,B,C) = (sin A)f(A,B,C)

* **Kimberling (6, 9, 13) Search Value:** :math:`1.095032026161`

Incidence
---------

:ref:`X(821) <X(821)>` lies and on these lines:

{:ref:`158 <X(158)>`, :ref:`255 <X(255)>`}, {:ref:`243 <X(243)>`, :ref:`411 <X(411)>`}, {:ref:`774 <X(774)>`, :ref:`823 <X(823)>`}

Relations
---------

* :ref:`X(821) <X(821)>` = :term:`isogonal conjugate <isogonal-conjugate>` of :ref:`X(820) <X(820)>`
* :ref:`X(821) <X(821)>` = :term:`cevapoint <cevapoint>` of :ref:`X(1) <X(1)>` and :ref:`X(158) <X(158)>`
* :ref:`X(821) <X(821)>` = polar conjugate of X(6508)

Construction
------------

.. literalinclude:: model.py
   :language: python
