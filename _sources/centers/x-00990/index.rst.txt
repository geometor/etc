:order: 990
:type: center
:canonical_id: X(990)
:dependencies: X(1), X(3), X(6), X(7), X(33), X(37), X(57), X(58), X(84), X(165), X(226), X(612), X(971), X(1040), X(12717)

.. _X(990):

X(990) = INTERSECTION OF LINES X(1)X(7) AND X(3)X(37)
=====================================================

.. figure:: x-00990.svg
   :alt: X(990) = INTERSECTION OF LINES X(1)X(7) AND X(3)X(37)
   :align: center

   **X(990) = INTERSECTION OF LINES X(1)X(7) AND X(3)X(37)** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`f(a,b,c) : f(b,c,a) : f(c,a,b),`, where f(a,b,c) = a\ :sup:`5` - a\ :sup:`4`\ (b + c) - 2a\ :sup:`3`\ bc - a(b - c)\ :sup:`2`\ (b\ :sup:`2` + c\ :sup:`2`) + (b - c)\ :sup:`2`\ (b + c)\ :sup:`3`

Barycentrics
~~~~~~~~~~~~

* :math:`g(a,b,c) : g(b,c,a) : g(c,a,b)`, where g(a,b,c) = af(a,b,c)

* **Kimberling (6, 9, 13) Search Value:** :math:`-1.386821299805`

Incidence
---------

:ref:`X(990) <X(990)>` lies and on these lines:

{:ref:`1 <X(1)>`, :ref:`7 <X(7)>`}, {:ref:`3 <X(3)>`, :ref:`37 <X(37)>`}, {:ref:`6 <X(6)>`, :ref:`971 <X(971)>`}, {:ref:`33 <X(33)>`, :ref:`57 <X(57)>`}, {:ref:`58 <X(58)>`, :ref:`84 <X(84)>`}, {:ref:`165 <X(165)>`, :ref:`612 <X(612)>`}, {:ref:`226 <X(226)>`, 1040}

Relations
---------

* :ref:`X(990) <X(990)>` = :term:`complement <complement>`, wrt hexyl triangle, of X(12717)

Construction
------------

.. literalinclude:: model.py
   :language: python
