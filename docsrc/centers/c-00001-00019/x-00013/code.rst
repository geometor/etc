:canonical_id: X_13
:subtitle: 1st ISOGONIC CENTER (FERMAT POINT, TORRICELLI POINT)

X_13
====

.. rubric:: 1st ISOGONIC CENTER (FERMAT POINT, TORRICELLI POINT)

.. enunciation::

   Construct the equilateral triangle :g:`BA'C << B C A' >>` having base :g:`BC <[ B C ]>` and vertex :g:`A' <A'>` on the negative side of :g:`BC <[ B C ]>`; similarly construct equilateral triangles :g:`CB'A << C A B' >>` and :g:`AC'B << A B C' >>` based on the other two sides. The lines :g:`AA' <[ A A' ]>`, :g:`BB' <[ B B' ]>`, :g:`CC' <[ C C' ]>` concur in :ref:`X_13 <X_13>`. If each of the angles :g:`A <A>`, :g:`B <B>`, :g:`C <C>` is < 2π/3, then :ref:`X_13 <X_13>` is the only center X for which the angles ``BXC``, ``CXA``, ``AXB`` are equal, and :ref:`X_13 <X_13>` minimizes the sum \|\ ``AX``\ \| + \|\ ``BX``\ \| + \|\ ``CX``\ \|. The :term:`antipedal triangle <antipedal-triangle>` of :ref:`X_13 <X_13>` is equilateral.

.. figure:: x-00013.svg
   :alt: X_13 — 1st ISOGONIC CENTER (FERMAT POINT, TORRICELLI POINT)
   :align: center

   **X_13** (*1st ISOGONIC CENTER (FERMAT POINT, TORRICELLI POINT)*) constructed at :g:`X_13 <X_13>` = :math:`\left(\frac{13727}{2353} - \frac{224 \sqrt{3}}{2353},\; \frac{18816}{2353} - \frac{5523 \sqrt{3}}{2353}\right)` in exact algebraic coordinates on the Heronian reference triangle :math:`(a, b, c) = (15, 13, 14)` over :math:`\mathbb{Q}(\sqrt{3})` with vertices :g:`A <A>` = :math:`(0, 0)`, :g:`B <B>` = :math:`(14, 0)`, :g:`C <C>` = :math:`(5, 12)`.

.. literalinclude:: model.py
   :language: python
