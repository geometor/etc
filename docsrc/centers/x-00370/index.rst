:order: 370
:type: center
:canonical_id: X(370)

.. _X(370):
.. _EquilateralCevianTrianglePoint:

X(370) = EQUILATERAL CEVIAN TRIANGLE POINT
==========================================

.. enunciation::

   A point :g:`P <P>` is an equilateral :term:`cevian triangle <cevian-triangle>` point if the cevian triangle of :g:`P <P>` is equilateral. Jiang Huanxin introduced this notion in 1997.

.. figure:: x-00370.svg
   :alt: X(370) = EQUILATERAL CEVIAN TRIANGLE POINT
   :align: center

   **X(370) = EQUILATERAL CEVIAN TRIANGLE POINT** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :g:`AB <[ A B ]>` = :math:`1`.

.. signature:: center

   | **Trilinears:** :math:`(see below)`
   | **Barycentrics:** :math:`(see below)`
   | **Search Value (6, 9, 13):** :math:`1.277501263430`

.. container:: note-item

   :ref:`X(370) <X(370)>` lies on the Neuberg cubic.

Notes
-----

.. container:: note-item

   Jean-Pierre Ehrmann notes (11/6/02) that the normalized barycentric coordinates (x,y,z) of :ref:`X(370) <X(370)>` are the unique solution of this system:

   y(1 - y)\ :math:`S_{B}` + z(1 - z)\ :math:`S_{C}` = x(1 + x)F

   z(1 - z)\ :math:`S_{C}` + x(1 - x)\ :math:`S_{A}` = y(1 + y)F

   x(1 - x)\ :math:`S_{A}` + y(1 - y)\ :math:`S_{B}` = z(1 + z)F

   x + y + z = 1,

   where :math:`S_{A}` = (:math:`b^{2}` + :math:`c^{2}` - :math:`a^{2})`/2; :math:`S_{B}`, :math:`S_{C}` are defined cyclically, :g:`F <F>` = [2 area(:g:`ABC << A B C >>`)]/:math:`\sqrt{3}`, and x>0, y>0, z>0.

.. container:: note-item

   **Jiang Huanxin and David Goering,** Problem 10358\* and Solution, "Equilateral cevian triangles," *American Mathematical Monthly* 104 (1997) 567-570 [proposed 1994].

.. toctree::
   :hidden:

   code
