:order: 583
:type: center
:canonical_id: X(583)
:dependencies: X(3), X(6), X(37), X(38), X(44), X(71), X(500), X(518), X(584), X(992), X(1009), X(1100)

.. _X(583):

X(583) = ORTHOGONAL OF X(500)
=============================

.. figure:: x-00583.svg
   :alt: X(583) = ORTHOGONAL OF X(500)
   :align: center

   **X(583) = ORTHOGONAL OF X(500)** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`f(a,b,c) : f(b,c,a) : f(c,a,b)`, where f(a,b,c) = a(a\ :sup:`2`\ b + a\ :sup:`2`\ c + 2abc - b\ :sup:`3` - c\ :sup:`3`) (M.Iliev, 5/13/07)

* **Kimberling (6, 9, 13) Search Value:** :math:`-0.396642090479`

Linear Combinations
-------------------

* :ref:`X(583) <X(583)>` = s\*\ :ref:`X(3) <X(3)>` + (r - 3R)\*cot(ω)\*\ :ref:`X(6) <X(6)>`

Notes
-----

.. container:: note-item

   Barycentrics af(a,b,c) : bf(b,c,a) : cf(c,a,b)

Incidence
---------

:ref:`X(583) <X(583)>` lies and on these lines:

{:ref:`3 <X(3)>`, :ref:`6 <X(6)>`}, {:ref:`37 <X(37)>`, :ref:`38 <X(38)>`}, {:ref:`44 <X(44)>`, :ref:`992 <X(992)>`}, {:ref:`71 <X(71)>`, 1100}, {:ref:`518 <X(518)>`, 1009}

Relations
---------

* :ref:`X(583) <X(583)>` = inverse-in-Brocard-circle of :ref:`X(584) <X(584)>`

Construction
------------

.. literalinclude:: model.py
   :language: python
