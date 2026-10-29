:order: 586
:type: center
:canonical_id: X(586)
:dependencies: X(8), X(192), X(585)

.. _X(586):

X(586) = 2nd CONGRUENT SHRUNK INSQUARES POINT
=============================================

.. figure:: x-00586.svg
   :alt: X(586) = 2nd CONGRUENT SHRUNK INSQUARES POINT
   :align: center

   **X(586) = 2nd CONGRUENT SHRUNK INSQUARES POINT** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`f(a,b,c) : f(b,c,a) : f(c,a,b)`, where f(a,b,c) = [2\*area\*(1/b + 1/c - 1/a) + a - b - c]/a

Barycentrics
~~~~~~~~~~~~

* :math:`g(a,b,c) : g(b,c,a) : g(c,a,b)`, where g(a,b,c) = 2\*area\*(1/b + 1/c - 1/a) + a - b - c

* **Kimberling (6, 9, 13) Search Value:** :math:`10.544711982653`

Notes
-----

.. container:: note-item

   For a discussion, see `Floor van Lamoen, "Vierkanten in een driehoek: 5. Gekrompen ingeschreven vierkanten" <http://home.wxs.nl/~lamoen/wiskunde/vierkant5.html>`__

Incidence
---------

:ref:`X(586) <X(586)>` lies and on these lines:

{:ref:`8 <X(8)>`, :ref:`192 <X(192)>`}

Relations
---------

* :ref:`X(586) <X(586)>` = {:ref:`X(8) <X(8)>`,\ :ref:`X(192) <X(192)>`}-harmonic conjugate of :ref:`X(585) <X(585)>`

Construction
------------

.. literalinclude:: model.py
   :language: python
