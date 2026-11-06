:order: 3066
:canonical_id: X_3066
:subtitle: 2nd LEMOINE HOMOTHETIC CENTER
:dependencies: X_2, X_3, X_6, X_25, X_51, X_107, X_110, X_125, X_182, X_373, X_381, X_394, X_458, X_1285, X_1350

.. _X_3066:

X_3066
======

.. rubric:: 2nd LEMOINE HOMOTHETIC CENTER

.. enunciation::

   This is a correction for trilinears given in :cite:`TCCT <tcct>`, p. 188.

.. figure:: x-03066.svg
   :alt: X_3066 — 2nd LEMOINE HOMOTHETIC CENTER
   :align: center

   **X_3066** (*2nd LEMOINE HOMOTHETIC CENTER*) constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :g:`AB <[ A B ]>` = :math:`1`.

.. admonition:: Constructed Elements
   :class: note

   * **Central Lines:** :g:`{6, 110} <{ 6, 110 }>`, :g:`{25, 182} <{ 25, 182 }>`
   * **Related Centers:** :g:`X_6 <X_6>` (:ref:`SYMMEDIAN POINT <X_6>`), :g:`X_110 <X_110>` (:ref:`FOCUS OF KIEPERT PARABOLA <X_110>`), :g:`X_25 <X_25>` (:ref:`HOMOTHETIC CENTER OF ORTHIC AND TANGENTIAL TRIANGLES <X_25>`), :g:`X_182 <X_182>` (:ref:`MIDPOINT OF BROCARD DIAMETER <X_182>`)

.. signature:: center

   | **Trilinears:** :math:`f(a,b,c) : f(b,c,a) : f(c,a,b)`, where :math:`f(a,b,c) = a(a^{2} + 3b^{2} - c^{2})(a^{2} - b^{2} + 3c^{2})`
   | **Barycentrics:** :math:`(\sin A)f(A,B,C) : (\sin B)f(B,C,A) : (\sin C)f(C,A,B)`
   | **Search Value (6, 9, 13):** :math:`0.950789516177`

.. collapse:: Incident Central Lines
   :badge: 7 lines
   :class: line-catalog

   {:ref:`2 <X_2>`, :ref:`1350 <X_1350>`}, {:ref:`3 <X_3>`, :ref:`373 <X_373>`}, {:ref:`6 <X_6>`, :ref:`110 <X_110>`}, {:ref:`25 <X_25>`, :ref:`182 <X_182>`}, {:ref:`51 <X_51>`, :ref:`394 <X_394>`}, {:ref:`107 <X_107>`, :ref:`458 <X_458>`}, {:ref:`125 <X_125>`, :ref:`381 <X_381>`}

.. collapse:: Functional Relations
   :badge: 1 relation

   * :ref:`X_3066 <X_3066>` = barycentric product of vertices of submedial triangle

Notes
-----

.. container:: note-item

   Suppose X is a point, with :term:`isogonal conjugate <isogonal-conjugate>` :math:`X^{- 1}`. It is well known that the :term:`pedal triangle <pedal-triangle>` of :g:`X <X>` is homothetic to the :term:`antipedal triangle <antipedal-triangle>` of :math:`X^{- 1}`. The Lemoine homothetic center, :ref:`X_1285 <X_1285>`, is the homothetic center when :g:`X <X>` = :ref:`X_6 <X_6>`, and :ref:`X_3066 <X_3066>` is the homothetic center when :g:`X <X>` = :ref:`X_2 <X_2>`. See also :ref:`X_1285 <X_1285>`. (:person:`Peter Moses <peter-moses>`, Dec. 7, 2005)

.. container:: note-item

   In general if :g:`X <X>` =\ :math:`x : y : z` (trilinears), then the homothetic center is given by

   a(x + y cos C)(x + z cos B) : b(y + z cos A)(y + x cos C): c(z + x cos B)(z + y cos A).

.. toctree::
   :hidden:

   code
