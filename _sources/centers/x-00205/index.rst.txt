:order: 205
:type: center
:canonical_id: X(205)
:dependencies: X(9), X(25), X(31), X(37), X(41), X(48), X(78), X(101), X(154), X(184), X(213), X(220)

.. _X(205):

X(205) = X(9)-CEVA CONJUGATE OF X(31)
=====================================

.. figure:: x-00205.svg
   :alt: X(205) = X(9)-CEVA CONJUGATE OF X(31)
   :align: center

   **X(205) = X(9)-CEVA CONJUGATE OF X(31)** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`f(a,b,c) : f(b,c,a) : f(c,a,b)`, where f(a,b,c) = a\ :sup:`2`\ [b\ :sup:`2`\ tan B/2 + c\ :sup:`2`\ tan C/2 - a\ :sup:`2`\ tan A/2]

Barycentrics
~~~~~~~~~~~~

* :math:`af(a,b,c) : bf(b,c,a) : cf(c,a,b)`

* **Kimberling (6, 9, 13) Search Value:** :math:`-1.788846215667`

Incidence
---------

:ref:`X(205) <X(205)>` lies and on these lines:

{:ref:`25 <X(25)>`, :ref:`41 <X(41)>`}, {:ref:`37 <X(37)>`, :ref:`48 <X(48)>`}, {:ref:`78 <X(78)>`, :ref:`101 <X(101)>`}, {:ref:`154 <X(154)>`, :ref:`220 <X(220)>`}, {:ref:`184 <X(184)>`, :ref:`213 <X(213)>`}

Relations
---------

* :ref:`X(205) <X(205)>` = :ref:`X(9) <X(9)>`-:term:`Ceva conjugate <ceva-conjugate>` of :ref:`X(31) <X(31)>`

Construction
------------

.. literalinclude:: model.py
   :language: python
