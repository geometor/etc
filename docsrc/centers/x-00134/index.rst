:order: 134
:type: center
:canonical_id: X(134)
:dependencies: X(3), X(52), X(53), X(96), X(107), X(128)

.. _X(134):

X(134) = X(107)-OF-ORTHIC-TRIANGLE
==================================

.. figure:: x-00134.svg
   :alt: X(134) = X(107)-OF-ORTHIC-TRIANGLE
   :align: center

   **X(134) = X(107)-OF-ORTHIC-TRIANGLE** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`f(A,B,C) : f(B,C,A) : f(C,A,B)`, where, f(A,B,C) = (sec A) u(A,B,C) [v(B,C,A) - v(C,B,A)],, u(A,B,C) = (sin 2A)[sin\ :sup:`2`\ (2B) - sin\ :sup:`2`\ (2C)][sin\ :sup:`2`\ (2B) + sin\ :sup:`2`\ (2C) - sin\ :sup:`2`\ (2A)]\ :sup:`2`,, v(B,C,A) = sin 2C [sin\ :sup:`2`\ (2A) - sin\ :sup:`2`\ (2B)][sin\ :sup:`2`\ (2A) + sin\ :sup:`2`\ (2B) - sin\ :sup:`2`\ (2C)]\ :sup:`2`

* **Kimberling (6, 9, 13) Search Value:** :math:`1.743812662514`

Notes
-----

.. container:: note-item

   Barycentrics g(A,B,C) : g(B,C,A) : g(C,A,B), where g(A,B,C) = (sin A) f(A,B,C)

Incidence
---------

:ref:`X(134) <X(134)>` lies on the nine-point circle

:ref:`X(134) <X(134)>` lies and on these lines:

{:ref:`52 <X(52)>`, :ref:`128 <X(128)>`}

Relations
---------

* :ref:`X(134) <X(134)>` = :ref:`X(107) <X(107)>`-of-:term:`orthic triangle <orthic-triangle>`
* :ref:`X(134) <X(134)>` = center of the rectangular hyperbola that passes through A, B, C, and :ref:`X(52) <X(52)>`
* :ref:`X(134) <X(134)>` = :term:`trilinear pole <trilinear-pole>` wrt orthic triangle of line :ref:`X(52) <X(52)>`\ \ :ref:`X(53) <X(53)>`
* :ref:`X(134) <X(134)>` = :term:`crosssum <crosssum>` of circumcircle intercepts of line :ref:`X(3) <X(3)>`\ \ :ref:`X(96) <X(96)>`
* :ref:`X(134) <X(134)>` = orthopole of line :ref:`X(3) <X(3)>`\ \ :ref:`X(96) <X(96)>`
* :ref:`X(134) <X(134)>` = Kirikami-six-circles-image of :ref:`X(52) <X(52)>`

Construction
------------

.. literalinclude:: model.py
   :language: python
