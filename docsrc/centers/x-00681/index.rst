:order: 681
:type: center
:canonical_id: X(681)
:dependencies: X(6), X(110), X(158), X(680), X(823), X(1612), X(1924), X(35521), X(35970), X(38969)

.. _X(681):

X(681) = TRILINEAR POLE OF LINE X(6)X(158)
==========================================

.. figure:: x-00681.svg
   :alt: X(681) = TRILINEAR POLE OF LINE X(6)X(158)
   :align: center

   **X(681) = TRILINEAR POLE OF LINE X(6)X(158)** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`f(A,B,C): f(B,C,A) : f(C,A,B)`, where f(A,B,C) = (sec\ :sup:`2`\ A)/(sin B cos\ :sup:`2`\ B - sin C cos\ :sup:`2`\ C)

Barycentrics
~~~~~~~~~~~~

* :math:`(\sin A)f(A,B,C): (\sin B)f(B,C,A) : (\sin C)f(C,A,B)`

* **Kimberling (6, 9, 13) Search Value:** :math:`1.927083772921`

Incidence
---------

:ref:`X(681) <X(681)>` lies on the circumcircle.

:ref:`X(681) <X(681)>` lies and on these lines:

{:ref:`110 <X(110)>`, :ref:`823 <X(823)>`}, {1612, 1924}

Relations
---------

* :ref:`X(681) <X(681)>` = :term:`isogonal conjugate <isogonal-conjugate>` of :ref:`X(680) <X(680)>`
* :ref:`X(681) <X(681)>` = :term:`isotomic conjugate <isotomic-conjugate>` of X(35521)
* :ref:`X(681) <X(681)>` = :term:`anticomplement <anticomplement>` of X(35970)
* :ref:`X(681) <X(681)>` = polar-circle-inverse of X(38969)

Construction
------------

.. literalinclude:: model.py
   :language: python
