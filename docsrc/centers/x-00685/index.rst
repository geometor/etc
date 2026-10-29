:order: 685
:type: center
:canonical_id: X(685)
:dependencies: X(4), X(31), X(32), X(92), X(98), X(110), X(250), X(287), X(297), X(468), X(523), X(684), X(850), X(2799), X(6333)

.. _X(685):

X(685) = TRILINEAR POLE OF LINE X(4)X(98)
=========================================

.. figure:: x-00685.svg
   :alt: X(685) = TRILINEAR POLE OF LINE X(4)X(98)
   :align: center

   **X(685) = TRILINEAR POLE OF LINE X(4)X(98)** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`f(A,B,C): f(B,C,A) : f(C,A,B)`, where f(A,B,C) = 1/(sec B sin\ :sup:`3` C - sec C sin\ :sup:`3` B)

Barycentrics
~~~~~~~~~~~~

* :math:`g(A,B,C) : g(B,C,A) : g(C,A,B)`, where g(A,B,C) = sin A f(A,B,C)

* **Kimberling (6, 9, 13) Search Value:** :math:`0.481231651426`

Incidence
---------

:ref:`X(685) <X(685)>` lies and on these lines:

{:ref:`98 <X(98)>`, :ref:`468 <X(468)>`}, {:ref:`110 <X(110)>`, :ref:`850 <X(850)>`}, {:ref:`250 <X(250)>`, :ref:`523 <X(523)>`}, {:ref:`287 <X(287)>`, :ref:`297 <X(297)>`}

Relations
---------

* :ref:`X(685) <X(685)>` = :term:`isogonal conjugate <isogonal-conjugate>` of :ref:`X(684) <X(684)>`
* :ref:`X(685) <X(685)>` = :term:`isotomic conjugate <isotomic-conjugate>` of X(6333)
* :ref:`X(685) <X(685)>` = polar conjugate of X(2799)
* :ref:`X(685) <X(685)>` = :term:`trilinear pole <trilinear-pole>` of line :ref:`X(4) <X(4)>`\ \ :ref:`X(32) <X(32)>`
* :ref:`X(685) <X(685)>` = trilinear product of circumcircle intercepts of line :ref:`X(31) <X(31)>`\ \ :ref:`X(92) <X(92)>`
* :ref:`X(685) <X(685)>` = :term:`vertex conjugate <vertex-conjugate>` of MacBeath circumconic intercepts of Euler line

Construction
------------

.. literalinclude:: model.py
   :language: python
