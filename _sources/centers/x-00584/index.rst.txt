:order: 584
:type: center
:canonical_id: X(584)
:dependencies: X(3), X(6), X(37), X(41), X(42), X(48), X(354), X(500), X(560), X(583)

.. _X(584):

X(584) = ORTHOHARMONIC OF X(500)
================================

.. figure:: x-00584.svg
   :alt: X(584) = ORTHOHARMONIC OF X(500)
   :align: center

   **X(584) = ORTHOHARMONIC OF X(500)** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`f(a,b,c) : f(b,c,a) : f(c,a,b)`, where f(a,b,c) = a(ab\ :sup:`2` + ac\ :sup:`2` + bc\ :sup:`2` + b\ :sup:`2`\ c + 2abc - a\ :sup:`3`) (M.Iliev, 5/13/07)

* **Kimberling (6, 9, 13) Search Value:** :math:`1.931776158859`

Linear Combinations
-------------------

* :ref:`X(584) <X(584)>` = s\*\ :ref:`X(3) <X(3)>` + (r + 3R)\*cot(ω)\*\ :ref:`X(6) <X(6)>`

Notes
-----

.. container:: note-item

   Barycentrics af(a,b,c) : bf(b,c,a) : cf(c,a,b)

Incidence
---------

:ref:`X(584) <X(584)>` lies and on these lines:

{:ref:`3 <X(3)>`, :ref:`6 <X(6)>`}, {:ref:`37 <X(37)>`, :ref:`41 <X(41)>`}, {:ref:`42 <X(42)>`, :ref:`560 <X(560)>`}, {:ref:`48 <X(48)>`, :ref:`354 <X(354)>`}

Relations
---------

* :ref:`X(584) <X(584)>` = inverse-in-Brocard-circle of :ref:`X(583) <X(583)>`

Construction
------------

.. literalinclude:: model.py
   :language: python
