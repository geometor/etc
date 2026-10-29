:order: 363
:type: center
:canonical_id: X(363)
:dependencies: X(1), X(40), X(57), X(164), X(165), X(166), X(168), X(289), X(8075)

.. _X(363):
.. _EqualPerimetersIsoscelizerPoint:

X(363) = EQUAL PERIMETERS ISOSCELIZER POINT
===========================================

.. figure:: x-00363.svg
   :alt: X(363) = EQUAL PERIMETERS ISOSCELIZER POINT
   :align: center

   **X(363) = EQUAL PERIMETERS ISOSCELIZER POINT** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`b/(1 + \sin B/2) + c/(1 + \sin C/2) - a/(1 + \sin A/2) : :`

* **Kimberling (6, 9, 13) Search Value:** :math:`2.584980945018`

Notes
-----

.. container:: note-item

   If X = :ref:`X(363) <X(363)>`, the :term:`isoscelizer <isoscelizer>` triangles of X have equal perimeters.

.. container:: note-item

   :ref:`X(363) <X(363)>` is the homothetic center of the :term:`excentral triangle <excentral-triangle>` and the inner Hutson triangle. A construction of the latter follows. The internal bisector of angle A meets the A-excircle in two points. Let P\ :sub:`A` be the point closer to line BC and let Q\ :sub:`A` be the other point. Define P\ :sub:`B` and P\ :sub:`C` cyclically, and define Q\ :sub:`B` and Q\ :sub:`C` cyclically. Let L\ :sub:`A` be the line tangent to the A-excircle at P\ :sub:`A`, and define L\ :sub:`B` and L\ :sub:`C` cyclically. Let M\ :sub:`A` be the line tangent to the A-excircle at Q\ :sub:`A`, and define M\ :sub:`B` and M\ :sub:`C` cyclically. The inner Hutson triangle is the triangle A'B'C' given by A' = L\ :sub:`B`\ ∩L\ :sub:`C`, B' = L\ :sub:`C`\ ∩L\ :sub:`A`, C' = L\ :sub:`A`\ ∩L\ :sub:`B`; the outer Hutson triangle is given by A'' = M\ :sub:`B`\ ∩M\ :sub:`C`, B'' = M\ :sub:`C`\ ∩M\ :sub:`A`, C' = M\ :sub:`A`\ ∩M\ :sub:`B`. (Based on a description of A'B'C' by :person:`Randy Hutson <randy-hutson>`, September 23, 2011)

.. container:: note-item

   :person:`Peter Moses <peter-moses>` (November 10, 2011) found trilinears for A'B'C' and A''B''C''. As these are :term:`central triangles <central-triangle>`, trilinears for A' and A'' suffice:

   A' = aU\ :sub:`A`\ (a\ :sup:`2` + b\ :sup:`2` + c\ :sup:`2` - 2bc - 2ca - 2ab) + bU\ :sub:`B`\ (b + c - a)(c + a - b) + cU\ :sub:`C`\ (b + c - a)(a + b - c)

   : aU\ :sub:`A`\ (a\ :sup:`2` + b\ :sup:`2` - 3c\ :sup:`2` + 2bc + 2ca - 2ab) + U\ :sub:`B`\ (c - a)(-a + b + c)(a - b + c) - cU\ :sub:`C`\ (-a + b + c)(a + b - c)

   : aU\ :sub:`A`\ (a\ :sup:`2` - 3b\ :sup:`2` + c\ :sup:`2` + 2bc - 2ca + 2ab) - bU\ :sub:`B`\ (-a + b + c)(a - b + c) + U\ :sub:`C`\ (b - a)(-a + b + c)(a + b - c)

.. container:: note-item

   A'' = aU\ :sub:`A`\ (a\ :sup:`2` + b\ :sup:`2` + c\ :sup:`2` - 2bc - 2ca - 2ab) - bU\ :sub:`B`\ (b + c - a)(c + a - b) - cU\ :sub:`C`\ (b + c - a)(a + b - c)

   : aU\ :sub:`A`\ (a\ :sup:`2` + b\ :sup:`2` - 3c\ :sup:`2` + 2bc + 2ca - 2ab) - U\ :sub:`B`\ (c - a)(-a + b + c)(a - b + c) + cU\ :sub:`C`\ (-a + b + c)(a + b - c)

   : aU\ :sub:`A`\ (a\ :sup:`2` - 3b\ :sup:`2` + c\ :sup:`2` + 2bc - 2ca + 2ab) + bU\ :sub:`B`\ (-a + b + c)(a - b + c) - U\ :sub:`C`\ (b - a)(-a + b + c)(a + b - c),

   where U\ :sub:`A` = sqrt[bc/((a - b + c)(a + b - c)] = (1/2)csc(A/2), and U\ :sub:`B` and U\ :sub:`C` are defined cyclically.

.. container:: note-item

   A'B'C' is perspective to the following triangles: intouch, hexyl,Yff, and the 1st and 2nd circumperp triangles. A''B''C'' is perspective to these: ABC, intouch, hexyl, Yff, and the 1st and 2nd circumperp triangles. A'B'C' is homothetic to A''B''C'', which is perspective to the excentral triangle at :ref:`X(168) <X(168)>`. (Peter Moses, 11/10/11)

.. container:: note-item

   Let UVW and U'V'W' be the tangential-midarc triangles introduced in the preamble to X(8075). The inner and outer Hutson triangles introduced at :ref:`X(363) <X(363)>` are the excircles-version of UVW and U'V'W'. (Randy Hutson and :person:`César Lozada <cesar-lozada>`, August 29, 2015)

Incidence
---------

:ref:`X(363) <X(363)>` lies and on these lines:

{:ref:`1 <X(1)>`, :ref:`289 <X(289)>`}, {:ref:`40 <X(40)>`, :ref:`164 <X(164)>`}, {:ref:`165 <X(165)>`, :ref:`166 <X(166)>`}

Relations
---------

* :ref:`X(363) <X(363)>` = :ref:`X(57) <X(57)>` of excentral triangle
* :ref:`X(363) <X(363)>` = homothetic center of ABC and :term:`orthic triangle <orthic-triangle>` of inner Hutson triangle

Construction
------------

.. literalinclude:: model.py
   :language: python
