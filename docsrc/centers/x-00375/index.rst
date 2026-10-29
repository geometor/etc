:order: 375
:type: center
:canonical_id: X(375)
:dependencies: X(10), X(44), X(51), X(181), X(210), X(354), X(373)

.. _X(375):

X(375) = CENTROID OF THE PEDAL TRIANGLE OF X(10)
================================================

.. figure:: x-00375.svg
   :alt: X(375) = CENTROID OF THE PEDAL TRIANGLE OF X(10)
   :align: center

   **X(375) = CENTROID OF THE PEDAL TRIANGLE OF X(10)** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`f(a,b,c) : f(b,c,a) : f(c,a,b)`, where f(a,b,c) = 2bc(b + c) + ca(c + a)cos C + ab(a + b)cos B

Barycentrics
~~~~~~~~~~~~

* :math:`af(a,b,c) : bf(b,c,a) : cf(c,a,b)`

* **Kimberling (6, 9, 13) Search Value:** :math:`2.037957695106`

Incidence
---------

:ref:`X(375) <X(375)>` lies and on these lines:

{:ref:`44 <X(44)>`, :ref:`181 <X(181)>`}, {:ref:`51 <X(51)>`, :ref:`210 <X(210)>`}, {:ref:`354 <X(354)>`, :ref:`373 <X(373)>`}

Relations
---------

* :ref:`X(375) <X(375)>` = midpoint of :ref:`X(51) <X(51)>` and :ref:`X(210) <X(210)>`

Construction
------------

.. literalinclude:: model.py
   :language: python
