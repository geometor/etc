:order: 370
:type: center
:canonical_id: X(370)

.. _X(370):
.. _EquilateralCevianTrianglePoint:

X(370) = EQUILATERAL CEVIAN TRIANGLE POINT
==========================================

.. figure:: x-00370.svg
   :alt: X(370) = EQUILATERAL CEVIAN TRIANGLE POINT
   :align: center

   **X(370) = EQUILATERAL CEVIAN TRIANGLE POINT** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`(see below)`

Barycentrics
~~~~~~~~~~~~

* :math:`(see below)`

* **Kimberling (6, 9, 13) Search Value:** :math:`1.277501263430`

Notes
-----

.. container:: note-item

   A point P is an equilateral :term:`cevian triangle <cevian-triangle>` point if the cevian triangle of P is equilateral. Jiang Huanxin introduced this notion in 1997.

      Jean-Pierre Ehrmann notes (11/6/02) that the normalized barycentric coordinates (x,y,z) of :ref:`X(370) <X(370)>` are the unique solution of this system:

   y(1 - y)S\ :sub:`B` + z(1 - z)S\ :sub:`C` = x(1 + x)F

   z(1 - z)S\ :sub:`C` + x(1 - x)S\ :sub:`A` = y(1 + y)F

   x(1 - x)S\ :sub:`A` + y(1 - y)S\ :sub:`B` = z(1 + z)F

   x + y + z = 1,

   where S\ :sub:`A` = (b\ :sup:`2` + c\ :sup:`2` - a\ :sup:`2`)/2; S\ :sub:`B`, S\ :sub:`C` are defined cyclically, F = [2 area(ABC)]/sqrt(3), and x>0, y>0, z>0.

.. container:: note-item

   **Jiang Huanxin and David Goering,** Problem 10358\* and Solution, "Equilateral cevian triangles," *American Mathematical Monthly* 104 (1997) 567-570 [proposed 1994].

Incidence
---------

:ref:`X(370) <X(370)>` lies on the Neuberg cubic.

Construction
------------

.. literalinclude:: model.py
   :language: python
