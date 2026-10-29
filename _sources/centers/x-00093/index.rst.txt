:order: 93
:type: center
:canonical_id: X(93)
:dependencies: X(3), X(4), X(49), X(50), X(94), X(186), X(252), X(562), X(1994), X(2964), X(34833)

.. _X(93):

X(93) = ISOGONAL CONJUGATE OF X(49)
===================================

.. figure:: x-00093.svg
   :alt: X(93) = ISOGONAL CONJUGATE OF X(49)
   :align: center

   **X(93) = ISOGONAL CONJUGATE OF X(49)** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`\sec 3A : \sec 3B : \sec 3C`

Barycentrics
~~~~~~~~~~~~

* :math:`\sin A \sec 3A : \sin B \sec 3B : \sin C \sec 3C`
* :math:`1/(a^2 (a^2 - b^2 - c^2) (a^4 + b^4 + c^4 - 2 a^2 b^2 - 2 a^2 c^2 - b^2 c^2)) : :`

* **Kimberling (6, 9, 13) Search Value:** :math:`18.573417905067`

Notes
-----

.. container:: note-item

   Let O\ :sub:`A`\ O\ :sub:`B`\ O\ :sub:`C` be the Kosnita triangle. Let A' be the pole wrt polar circle of line O\ :sub:`B`\ O\ :sub:`C`, and define B' and C' cyclically. The lines AA', BB', CC' concur in :ref:`X(93) <X(93)>`. (:person:`Randy Hutson <randy-hutson>`, June 7, 2019)

Incidence
---------

:ref:`X(93) <X(93)>` lies and on these lines:

{:ref:`4 <X(4)>`, :ref:`562 <X(562)>`}, {:ref:`49 <X(49)>`, :ref:`94 <X(94)>`}, {:ref:`186 <X(186)>`, :ref:`252 <X(252)>`}

Relations
---------

* :ref:`X(93) <X(93)>` = :term:`isogonal conjugate <isogonal-conjugate>` of :ref:`X(49) <X(49)>`
* :ref:`X(93) <X(93)>` = :term:`anticomplement <anticomplement>` of X(34833)
* :ref:`X(93) <X(93)>` = :ref:`X(50) <X(50)>`-:term:`cross conjugate <cross-conjugate>` of :ref:`X(94) <X(94)>`
* :ref:`X(93) <X(93)>` = polar conjugate of X(1994)
* :ref:`X(93) <X(93)>` = X(2964)-:term:`isoconjugate <isoconjugate>` of :ref:`X(3) <X(3)>`

Construction
------------

.. literalinclude:: model.py
   :language: python
