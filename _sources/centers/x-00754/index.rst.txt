:order: 754
:type: center
:canonical_id: X(754)
:dependencies: X(2), X(30), X(32), X(115), X(187), X(230), X(316), X(325), X(511), X(625), X(755)

.. _X(754):

X(754) = EVEN (0, 4) INFINITY POINT
===================================

.. figure:: x-00754.svg
   :alt: X(754) = EVEN (0, 4) INFINITY POINT
   :align: center

   **X(754) = EVEN (0, 4) INFINITY POINT** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`f(a,b,c) : f(b,c,a) : f(c,a,b)`, where f(a,b,c) = a :sup:`-1`\ (b\ :sup:`4` + c\ :sup:`4`) - a\ :sup:`3`\ (b\ :sup:`0` + c\ :sup:`0`)

Barycentrics
~~~~~~~~~~~~

* :math:`g(a,b,c) : g(b,c,a) : g(c,a,b)`, where g(a,b,c) = af(a,b,c)

Notes
-----

.. container:: note-item

   As the :term:`isogonal conjugate <isogonal-conjugate>` of a point on the circumcircle, :ref:`X(754) <X(754)>` lies on the line at infinity.

Incidence
---------

:ref:`X(754) <X(754)>` lies and on these lines:

{:ref:`2 <X(2)>`, :ref:`32 <X(32)>`}, {:ref:`30 <X(30)>`, :ref:`511 <X(511)>`}, {:ref:`115 <X(115)>`, :ref:`316 <X(316)>`}, {:ref:`187 <X(187)>`, :ref:`325 <X(325)>`}, {:ref:`230 <X(230)>`, :ref:`625 <X(625)>`}

Relations
---------

* :ref:`X(754) <X(754)>` = isogonal conjugate of :ref:`X(755) <X(755)>`

Construction
------------

.. literalinclude:: model.py
   :language: python
