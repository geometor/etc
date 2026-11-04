:order: 1314
:canonical_id: X_1314
:subtitle: 3rd MOSES INTERSECTION
:dependencies: X_2, X_3, X_4

.. _X_1314:

X_1314
======

.. rubric:: 3rd MOSES INTERSECTION

.. enunciation::

   :ref:`X_1314 <X_1314>` is a point of intersection of the Euler line and the incircle. For some obtuse triangles, this point is not in the real plane (specifically, for those a,b,c such that Q < 0).

.. figure:: x-01314.svg
   :alt: X_1314 — 3rd MOSES INTERSECTION
   :align: center

   **X_1314** (*3rd MOSES INTERSECTION*) constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :g:`AB <[ A B ]>` = :math:`1`.

.. admonition:: Constructed Elements
   :class: note

   * **Central Lines:** :g:`{2, 3} <{ 2, 3 }>` (:term:`Euler line <euler line>`)
   * **Related Centers:** :g:`X_2 <X_2>` (:ref:`CENTROID <X_2>`), :g:`X_3 <X_3>` (:ref:`CIRCUMCENTER <X_3>`), :g:`X_4 <X_4>` (:ref:`ORTHOCENTER <X_4>`)

.. signature:: center

   | **Trilinears:** :math:`bcf(a,b,c) : caf(b,c,a): abf(c,a,b)`, where f(a,b,c) is the 1st barycentric given below
   | **Barycentrics:** :math:`f(a,b,c) : f(b,c,a) : f(c,a,b)`, where :math:`f(a,b,c) = [d^{2} + (4r - R)R +`\ :math:`\sqrt{Q}`]\ :math:`S_{B}`\ :math:`S_{C}` + (:math:`d^{2}` + :math:`2r^{2}` - :math:`R^{2})`\ :math:`a^{2}`\ :math:`S_{A}`, where :math:`Q = 4d^{2}R(4r - R) + [d^{2} - 3R^{2} + 4r(r + R)]^{2}`, d = distance between :ref:`X_3 <X_3>` and :ref:`X_4 <X_4>`, R = circumradius, r = inradius, :math:`S_{A} = (b^{2} + c^{2} - a^{2})/2`, and :math:`S_{B}` and :math:`S_{C}` are defined cyclically (Peter J. C. Moses, 3/2003)
   | **Search Value (6, 9, 13):** :math:`0.871828089890`

.. container:: note-item

   :ref:`X_1314 <X_1314>` lies on the incircle.

.. collapse:: Incident Central Lines
   :badge: 1 line
   :class: line-catalog

   {:ref:`2 <X_2>`, :ref:`3 <X_3>`}

Notes
-----

.. container:: note-item

   As a point on the Euler line, :ref:`X_1314 <X_1314>` has Shinagawa coefficients :math:`(d^{2} + 2r^{2} - R^{2},4rR - 2r^{2} + Q^{1/2})`.

.. toctree::
   :hidden:

   code
