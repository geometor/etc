:order: 370
:type: center
:canonical_id: X_370
:subtitle: EQUILATERAL CEVIAN TRIANGLE POINT

.. _X_370:
.. _EquilateralCevianTrianglePoint:

X_370
=====

.. rubric:: EQUILATERAL CEVIAN TRIANGLE POINT

.. enunciation::

   A point :g:`P <P>` is an equilateral :term:`cevian triangle <cevian-triangle>` point if the cevian triangle of :g:`P <P>` is equilateral. Jiang Huanxin introduced this notion in 1997.

.. figure:: x-00370.svg
   :alt: X_370 — EQUILATERAL CEVIAN TRIANGLE POINT
   :align: center

   **X_370** (*EQUILATERAL CEVIAN TRIANGLE POINT*) constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :g:`AB <[ A B ]>` = :math:`1`.

.. admonition:: Constructed Elements
   :class: note

   * **Derived Triangle:** :term:`Cevian Triangle <cevian triangle>` :g:`△P_aP_bP_c << P_a P_b P_c >>` — vertices :g:`P_a <P_a>`, :g:`P_b <P_b>`, :g:`P_c <P_c>` (Traces of cevians through target center on BC, CA, AB)
   * **Concurrence Lines:** :g:`A–P_a <[ A P_a ]>`, :g:`B–P_b <[ B P_b ]>`, :g:`C–P_c <[ C P_c ]>` concurring at :g:`X_370 <X_370>`

.. signature:: center

   | **Trilinears:** :math:`(see below)`
   | **Barycentrics:** :math:`(see below)`
   | **Search Value (6, 9, 13):** :math:`1.277501263430`

.. container:: note-item

   :ref:`X_370 <X_370>` lies on the Neuberg cubic.

Notes
-----

.. container:: note-item

   Jean-Pierre Ehrmann notes (11/6/02) that the normalized barycentric coordinates (x,y,z) of :ref:`X_370 <X_370>` are the unique solution of this system:

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
