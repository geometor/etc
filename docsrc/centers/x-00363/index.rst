:order: 363
:type: center
:canonical_id: X(363)
:dependencies: X(1), X(40), X(57), X(164), X(165), X(166), X(168), X(289), X(8075)

.. _X(363):
.. _EqualPerimetersIsoscelizerPoint:

X(363) = EQUAL PERIMETERS ISOSCELIZER POINT
===========================================

.. enunciation::

   If :g:`X <X>` = :ref:`X(363) <X(363)>`, the :term:`isoscelizer <isoscelizer>` triangles of X have equal perimeters.

.. figure:: x-00363.svg
   :alt: X(363) = EQUAL PERIMETERS ISOSCELIZER POINT
   :align: center

   **X(363) = EQUAL PERIMETERS ISOSCELIZER POINT** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :g:`AB <[ A B ]>` = :math:`1`.

.. signature:: center

   | **Trilinears:** :math:`b/(1 + \sin B/2) + c/(1 + \sin C/2) - a/(1 + \sin A/2) : :`
   | **Search Value (6, 9, 13):** :math:`2.584980945018`

.. collapse:: Incident Central Lines
   :badge: 3 lines
   :class: line-catalog

   {:ref:`1 <X(1)>`, :ref:`289 <X(289)>`}, {:ref:`40 <X(40)>`, :ref:`164 <X(164)>`}, {:ref:`165 <X(165)>`, :ref:`166 <X(166)>`}

.. collapse:: Functional Relations
   :badge: 2 relations

   * :ref:`X(363) <X(363)>` = :ref:`X(57) <X(57)>` of :term:`excentral triangle <excentral-triangle>`
   * :ref:`X(363) <X(363)>` = homothetic center of :g:`ABC << A B C >>` and :term:`orthic triangle <orthic-triangle>` of inner Hutson triangle

Notes
-----

.. container:: note-item

   :ref:`X(363) <X(363)>` is the homothetic center of the excentral triangle and the inner Hutson triangle. A construction of the latter follows. The internal bisector of angle A meets the :g:`A <A>`-excircle in two points. Let :g:`P_{A} <P_A>` be the point closer to line :g:`BC <[ B C ]>` and let :g:`Q_{A} <Q_A>` be the other point. Define :g:`P_{B} <P_B>` and :g:`P_{C} <P_C>` cyclically, and define :g:`Q_{B} <Q_B>` and :g:`Q_{C} <Q_C>` cyclically. Let :g:`L_{A} <L_A>` be the line tangent to the :g:`A <A>`-excircle at :g:`P_{A} <P_A>`, and define :g:`L_{B} <L_B>` and :g:`L_{C} <L_C>` cyclically. Let :g:`M_{A} <M_A>` be the line tangent to the :g:`A <A>`-excircle at :g:`Q_{A} <Q_A>`, and define :g:`M_{B} <M_B>` and :g:`M_{C} <M_C>` cyclically. The inner Hutson triangle is the triangle :g:`A'B'C' << A' B' C' >>` given by :g:`A' <A'>` = :g:`L_{B} <L_B>`\ ∩\ :g:`L_{C} <L_C>`, :g:`B' <B'>` = :g:`L_{C} <L_C>`\ ∩\ :g:`L_{A} <L_A>`, :g:`C' <C'>` = :g:`L_{A} <L_A>`\ ∩\ :g:`L_{B} <L_B>`; the outer Hutson triangle is given by :g:`A″ <A″>` = :g:`M_{B} <M_B>`\ ∩\ :g:`M_{C} <M_C>`, :g:`B″ <B″>` = :g:`M_{C} <M_C>`\ ∩\ :g:`M_{A} <M_A>`, :g:`C' <C'>` = :g:`M_{A} <M_A>`\ ∩\ :g:`M_{B} <M_B>`. (Based on a description of :g:`A'B'C' << A' B' C' >>` by :person:`Randy Hutson <randy-hutson>`, September 23, 2011)

.. container:: note-item

   :person:`Peter Moses <peter-moses>` (November 10, 2011) found trilinears for :g:`A'B'C' << A' B' C' >>` and :g:`A″B″C″ << A″ B″ C″ >>`. As these are :term:`central triangles <central-triangle>`, trilinears for :g:`A' <A'>` and :g:`A″ <A″>` suffice:

   :g:`A' <A'>` = :math:`aU_{A}(a^{2} + b^{2} + c^{2} - 2bc - 2ca - 2ab)` + :math:`bU_{B}(b + c - a)`\ (c + a - b) + :math:`cU_{C}(b + c - a)`\ (a + b - c)

   : :math:`aU_{A}(a^{2} + b^{2} - 3c^{2} + 2bc + 2ca - 2ab)` + :g:`U_{B} <U_B>`\ (c - a)(-a + b + c)(a - b + c) - :math:`cU_{C}(-a + b + c)`\ (a + b - c)

   : :math:`aU_{A}(a^{2} - 3b^{2} + c^{2} + 2bc - 2ca + 2ab)` - :math:`bU_{B}(-a + b + c)`\ (a - b + c) + :g:`U_{C} <U_C>`\ (b - a)(-a + b + c)(a + b - c)

   :g:`A″ <A″>` = :math:`aU_{A}(a^{2} + b^{2} + c^{2} - 2bc - 2ca - 2ab)` - :math:`bU_{B}(b + c - a)`\ (c + a - b) - :math:`cU_{C}(b + c - a)`\ (a + b - c)

   : :math:`aU_{A}(a^{2} + b^{2} - 3c^{2} + 2bc + 2ca - 2ab)` - :g:`U_{B} <U_B>`\ (c - a)(-a + b + c)(a - b + c) + :math:`cU_{C}(-a + b + c)`\ (a + b - c)

   : :math:`aU_{A}(a^{2} - 3b^{2} + c^{2} + 2bc - 2ca + 2ab)` + :math:`bU_{B}(-a + b + c)`\ (a - b + c) - :g:`U_{C} <U_C>`\ (b - a)(-a + b + c)(a + b - c),

   where :g:`U_{A} <U_A>` = sqrt[bc/((a - b + c)(a + b - c)] = (1/2)csc(A/2), and :g:`U_{B} <U_B>` and :g:`U_{C} <U_C>` are defined cyclically.

.. container:: note-item

   :g:`A'B'C' << A' B' C' >>` is perspective to the following triangles: intouch, hexyl,Yff, and the 1st and 2nd circumperp triangles. :g:`A″B″C″ << A″ B″ C″ >>` is perspective to these: :g:`ABC << A B C >>`, intouch, hexyl, Yff, and the 1st and 2nd circumperp triangles. :g:`A'B'C' << A' B' C' >>` is homothetic to :g:`A″B″C″ << A″ B″ C″ >>`, which is perspective to the excentral triangle at :ref:`X(168) <X(168)>`. (Peter Moses, 11/10/11)

.. container:: note-item

   Let :g:`UVW << U V W >>` and :g:`U'V'W' << U' V' W' >>` be the tangential-midarc triangles introduced in the preamble to X(8075). The inner and outer Hutson triangles introduced at :ref:`X(363) <X(363)>` are the excircles-version of :g:`UVW << U V W >>` and :g:`U'V'W' << U' V' W' >>`. (Randy Hutson and :person:`César Lozada <cesar-lozada>`, August 29, 2015)

.. toctree::
   :hidden:

   code
