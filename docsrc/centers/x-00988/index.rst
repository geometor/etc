:order: 988
:type: center
:canonical_id: X(988)
:dependencies: X(1), X(3), X(9), X(21), X(38), X(39), X(77), X(78), X(84), X(256), X(404), X(612), X(614), X(936), X(984), X(989), X(1106), X(37552)

.. _X(988):

X(988) = INTERSECTION OF LINES X(1)X(3) AND X(9)X(39)
=====================================================

.. figure:: x-00988.svg
   :alt: X(988) = INTERSECTION OF LINES X(1)X(3) AND X(9)X(39)
   :align: center

   **X(988) = INTERSECTION OF LINES X(1)X(3) AND X(9)X(39)** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`f(a,b,c) : f(b,c,a) : f(c,a,b),`, where f(a,b,c) = a\ :sup:`3` - a\ :sup:`2`\ (b + c) - (3a + b + c)(b\ :sup:`2` + c\ :sup:`2`)

Barycentrics
~~~~~~~~~~~~

* :math:`g(a,b,c) : g(b,c,a) : g(c,a,b)`, where g(a,b,c) = af(a,b,c)

* **Kimberling (6, 9, 13) Search Value:** :math:`2.067148796949`

Incidence
---------

:ref:`X(988) <X(988)>` lies and on these lines:

{:ref:`1 <X(1)>`, :ref:`3 <X(3)>`}, {:ref:`9 <X(9)>`, :ref:`39 <X(39)>`}, {:ref:`21 <X(21)>`, :ref:`614 <X(614)>`}, {:ref:`38 <X(38)>`, :ref:`78 <X(78)>`}, {:ref:`77 <X(77)>`, 1106}, {:ref:`84 <X(84)>`, :ref:`256 <X(256)>`}, {:ref:`404 <X(404)>`, :ref:`612 <X(612)>`}, {:ref:`936 <X(936)>`, :ref:`984 <X(984)>`}

Relations
---------

* :ref:`X(988) <X(988)>` = :term:`isogonal conjugate <isogonal-conjugate>` of :ref:`X(989) <X(989)>`
* :ref:`X(988) <X(988)>` = {:ref:`X(1) <X(1)>`,\ :ref:`X(3) <X(3)>`}-harmonic conjugate of X(37552)

Construction
------------

.. literalinclude:: model.py
   :language: python
