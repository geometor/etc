:order: 931
:type: center
:canonical_id: X(931)
:dependencies: X(6), X(21), X(100), X(101), X(108), X(109), X(111), X(643), X(645), X(648), X(662), X(941), X(8672)

.. _X(931):

X(931) = POINT ALCHIBA
======================

.. figure:: x-00931.svg
   :alt: X(931) = POINT ALCHIBA
   :align: center

   **X(931) = POINT ALCHIBA** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`f(a,b,c) : f(b,c,a) : f(c,a,b),`, where f(a,b,c) = 1/(bw - cv), u : v : w = :ref:`X(21) <X(21)>`

Barycentrics
~~~~~~~~~~~~

* :math:`g(a,b,c) : g(b,c,a) : g(c,a,b)`, where g(a,b,c) = af(a,b,c)

* **Kimberling (6, 9, 13) Search Value:** :math:`2.172567017455`

Incidence
---------

:ref:`X(931) <X(931)>` lies on the circumcircle and on these lines:

{:ref:`100 <X(100)>`, :ref:`645 <X(645)>`}, {:ref:`101 <X(101)>`, :ref:`643 <X(643)>`}, {:ref:`108 <X(108)>`, :ref:`648 <X(648)>`}, {:ref:`109 <X(109)>`, :ref:`662 <X(662)>`}, {:ref:`111 <X(111)>`, :ref:`941 <X(941)>`}

Relations
---------

* :ref:`X(931) <X(931)>` = :term:`isogonal conjugate <isogonal-conjugate>` of X(8672)
* :ref:`X(931) <X(931)>` = :term:`trilinear pole <trilinear-pole>` of line :ref:`X(6) <X(6)>`\ \ :ref:`X(21) <X(21)>`
* :ref:`X(931) <X(931)>` = Ψ(:ref:`X(6) <X(6)>`, :ref:`X(21) <X(21)>`)

Construction
------------

.. literalinclude:: model.py
   :language: python
