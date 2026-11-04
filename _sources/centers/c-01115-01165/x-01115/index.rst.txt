:order: 1115
:canonical_id: X_1115
:subtitle: EXTERIOR-ANGLE CURVATURE CENTROID
:dependencies: X_1, X_2, X_3, X_6, X_10, X_75, X_99, X_141, X_359, X_360, X_1077, X_7021, X_7036, X_7039, X_7041, X_7044, X_18294, X_18295

.. _X_1115:
.. _Exterior-AngleCurvatureCentroid:

X_1115
======

.. rubric:: EXTERIOR-ANGLE CURVATURE CENTROID

.. enunciation::

   :ref:`X_1115 <X_1115>` is the center of mass of a point-mass system obtained by placing at vertex *\ :g:`A* <A*>` a mass equal to the magnitude of the exterior angle (that's π - *\ :g:`A* <A*>`) at *\ :g:`A* <A*>`, and cyclically for *\ :g:`B* <B*>` and *\ :g:`C* <C*>`. ( Peter Scales , :cite:`Hyacinthos #5528 <hyacinthos>`, 5/22/02) This description is also found in Honsberger , Episodes in Nineteenth and Twentieth Century Eulidean Geometry , p. 120, where it is mistakenly attributed to the Steiner point, :ref:`X_99 <X_99>`.

.. figure:: x-01115.svg
   :alt: X_1115 — EXTERIOR-ANGLE CURVATURE CENTROID
   :align: center

   **X_1115** (*EXTERIOR-ANGLE CURVATURE CENTROID*) constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :g:`AB <[ A B ]>` = :math:`1`.

.. admonition:: Constructed Elements
   :class: note

   * **Central Lines:** :g:`{2, 360} <{ 2, 360 }>`
   * **Related Centers:** :g:`X_2 <X_2>` (:ref:`CENTROID <X_2>`), :g:`X_360 <X_360>` (:ref:`HOFSTADTER ZERO POINT <X_360>`)

.. signature:: center

   | **Trilinears:** :math:`(\pi - A)/a : (\pi - B)/b : (\pi - C)/c`
   | **Barycentrics:** :math:`\pi - A : \pi - B : \pi - C`
   | **Search Value (6, 9, 13):** :math:`3.421226357111`

.. collapse:: Linear Combinations
   :badge: 1 combination

   * :ref:`X_1115 <X_1115>` = :math:`9` :ref:`X_2 <X_2>` - :math:`5` X_18295, :math:`3` :ref:`X_360 <X_360>` - :math:`5` X_18295, :math:`6` X_18294 - :math:`5` X_18295

.. collapse:: Incident Central Lines
   :badge: 1 line
   :class: line-catalog

   {:ref:`2 <X_2>`, :ref:`360 <X_360>`}

.. collapse:: Functional Relations
   :badge: 10 relations

   * :ref:`X_1115 <X_1115>` = reflection of :ref:`X_360 <X_360>` in X_18294
   * :ref:`X_1115 <X_1115>` = :term:`isogonal conjugate <isogonal-conjugate>` of X_7021
   * :ref:`X_1115 <X_1115>` = :term:`complement <complement>` of :ref:`X_360 <X_360>`
   * :ref:`X_1115 <X_1115>` = :term:`anticomplement <anticomplement>` of X_18294
   * :ref:`X_1115 <X_1115>` = complement of the isogonal conjugate of :ref:`X_359 <X_359>`
   * :ref:`X_1115 <X_1115>` = X_i-:term:`complementary conjugate <complementary-conjugate>` of X_j for these (i,j): {:ref:`359 <X_359>`, :ref:`10 <X_10>`}, {:ref:`1077 <X_1077>`, :ref:`141 <X_141>`}
   * :ref:`X_1115 <X_1115>` = X_i-:term:`isoconjugate <isoconjugate>` of X_j for these (i,j): {:ref:`1 <X_1>`, 7021}, {:ref:`6 <X_6>`, 7041}
   * :ref:`X_1115 <X_1115>` = barycentric product :ref:`X_75 <X_75>`\ \*X_7039
   * :ref:`X_1115 <X_1115>` = barycentric quotient X_i/X_j for these {i,j}: {:ref:`1 <X_1>`, 7041}, {:ref:`6 <X_6>`, 7021}, {7039, :ref:`1 <X_1>`}, {7041, 7036}, {7044, 7039}
   * :ref:`X_1115 <X_1115>` = {:ref:`X_2 <X_2>`,\ :ref:`X_360 <X_360>`}-harmonic conjugate of X_18294

Notes
-----

.. container:: note-item

   :ref:`X_1115 <X_1115>` should not be confused with Jakob Steiner's actual "Curvature Centroid" (discovered in 1825), applicable to all polygons, obtained as the weighted sum of vertices with weights determined by sines of doubled vertex angles [1]. Remarkably, the pedal polygon of a polygon with respect to this point has extremal area: it is minimal (resp. maximal) if the sign of the sum of sines of double angles is negative (resp. positive) [1] . For a triangle, this point is the circumcenter :ref:`X_3 <X_3>` and the extremal :term:`pedal triangle <pedal-triangle>` is the :term:`medial triangle <medial-triangle>`. (:person:`Dan Reznik <dan-reznik>`, July 7, 2020).

      [1] Jakob Steiner , "Krümmungs Schwerpunkt ebener Curven" , Abhandlungen der Königlich Preussischen Akademie der Wissenschaften , 1838. (Dan Reznick, July 7, 2020)

.. toctree::
   :hidden:

   code
