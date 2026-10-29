:order: 964
:type: center
:canonical_id: X(964)
:dependencies: X(1), X(2), X(3), X(6), X(8), X(10), X(31), X(321)

.. _X(964):

X(964) = INTERCEPT OF EULER LINE AND LINE X(6)X(8)
==================================================

.. figure:: x-00964.svg
   :alt: X(964) = INTERCEPT OF EULER LINE AND LINE X(6)X(8)
   :align: center

   **X(964) = INTERCEPT OF EULER LINE AND LINE X(6)X(8)** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`f(a,b,c) : f(b,c,a) : f(c,a,b),`, where f(a,b,c) = bc[a\ :sup:`4` + (b + c)(a\ :sup:`3` + ab\ :sup:`2` + ac\ :sup:`2` + abc + (b + c)(a\ :sup:`2` + bc))]

Barycentrics
~~~~~~~~~~~~

* :math:`g(a,b,c) : g(b,c,a) : g(c,a,b)`, where g(a,b,c) = af(a,b,c)

* **Kimberling (6, 9, 13) Search Value:** :math:`2.536291462852`

Notes
-----

.. container:: note-item

   As a point on the Euler line, :ref:`X(964) <X(964)>` has Shinagawa coefficients (2(E + F)\ :sup:`2` + 2(E + F)\*$bc$ + abc\*$a$, 2S\ :sup:`2`).

Incidence
---------

:ref:`X(964) <X(964)>` lies and on these lines:

{:ref:`1 <X(1)>`, :ref:`321 <X(321)>`}, {:ref:`2 <X(2)>`, :ref:`3 <X(3)>`}, {:ref:`6 <X(6)>`, :ref:`8 <X(8)>`}, {:ref:`10 <X(10)>`, :ref:`31 <X(31)>`}

Construction
------------

.. literalinclude:: model.py
   :language: python
