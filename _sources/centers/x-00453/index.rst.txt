:order: 453
:type: center
:canonical_id: X(453)
:dependencies: X(2), X(3), X(46), X(1014), X(1454), X(1800)

.. _X(453):

X(453) = POINT ALSHAIN
======================

.. figure:: x-00453.svg
   :alt: X(453) = POINT ALSHAIN
   :align: center

   **X(453) = POINT ALSHAIN** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`f(A,B,C) : f(B,C,A) : f(C,A,B)`, where f(A,B,C)=(cos B + cos C - cos A)\ :sup:`2`/(cos B + cos C)

Barycentrics
~~~~~~~~~~~~

* :math:`(\sin A)f(A,B,C) : (\sin B)f(B,C,A) : (\sin C)f(C,A,B)`

* **Kimberling (6, 9, 13) Search Value:** :math:`1.182719776028`

Notes
-----

.. container:: note-item

   As a point on the Euler line, :ref:`X(453) <X(453)>` has Shinagawa coefficients (2$aS\ :sub:`B`\ S\ :sub:`C`\ $+$aS\ :sub:`A`\ $(E+2F)-2$a$S\ :sup:`2`-2abcF, -$aS\ :sub:`A`\ $E+2$a$S\ :sup:`2`\ +abcE).

Incidence
---------

:ref:`X(453) <X(453)>` lies and on these lines:

{:ref:`2 <X(2)>`, :ref:`3 <X(3)>`}, {:ref:`46 <X(46)>`, 1800}, {1014, 1454}

Construction
------------

.. literalinclude:: model.py
   :language: python
