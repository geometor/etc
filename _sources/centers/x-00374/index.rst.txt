:order: 374
:type: center
:canonical_id: X(374)
:dependencies: X(6), X(9), X(44), X(51), X(65), X(210), X(354), X(517), X(966), X(3740)

.. _X(374):

X(374) = CENTROID OF THE PEDAL TRIANGLE OF X(9)
===============================================

.. figure:: x-00374.svg
   :alt: X(374) = CENTROID OF THE PEDAL TRIANGLE OF X(9)
   :align: center

   **X(374) = CENTROID OF THE PEDAL TRIANGLE OF X(9)** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`f(a,b,c) : f(b,c,a) : f(c,a,b)`, where f(a,b,c) = 2b + 2c - 3a + (c + a)cos C + (b + a)cos B

Barycentrics
~~~~~~~~~~~~

* :math:`af(a,b,c) : bf(b,c,a) : cf(c,a,b)`

* **Kimberling (6, 9, 13) Search Value:** :math:`2.141317916799`

Incidence
---------

:ref:`X(374) <X(374)>` lies and on these lines:

{:ref:`6 <X(6)>`, :ref:`354 <X(354)>`}, {:ref:`9 <X(9)>`, :ref:`517 <X(517)>`}, {:ref:`44 <X(44)>`, :ref:`65 <X(65)>`}, {:ref:`51 <X(51)>`, :ref:`210 <X(210)>`}, {:ref:`966 <X(966)>`, 3740}

Construction
------------

.. literalinclude:: model.py
   :language: python
