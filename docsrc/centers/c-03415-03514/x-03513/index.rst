:order: 3513
:canonical_id: X_3513
:subtitle: 1st DILATION CENTER
:dependencies: X_1, X_3, X_36, X_55, X_56, X_57, X_65, X_165, X_354, X_1420, X_1617, X_2078, X_3514, X_3660

.. _X_3513:

X_3513
======

.. rubric:: 1st DILATION CENTER

.. enunciation::

   For any two points :g:`P <P>`, :g:`Q <Q>` in the set {:g:`A <A>`, :g:`B <B>`, :g:`C <C>`} and arbitrary point :g:`X <X>`, let M(X) = (\|\ :g:`PX <[ P X ]>`\ \| + \|QX\|)/\|\ :g:`PQ <[ P Q ]>`\ \|. The point :g:`X <X>` that minimizes M(X) is :ref:`X_3513 <X_3513>`. See

.. figure:: x-03513.svg
   :alt: X_3513 — 1st DILATION CENTER
   :align: center

   **X_3513** (*1st DILATION CENTER*) constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :g:`AB <[ A B ]>` = :math:`1`.

.. admonition:: Constructed Elements
   :class: note

   * **Central Lines:** :g:`{3514, 3660} <{ 3514, 3660 }>`
   * **Related Centers:** :g:`X_3514 <X_3514>` (:ref:`INVERSE-IN-CIRCUMCIRCLE OF X(3513) <X_3514>`), :g:`X_3660 <X_3660>` (:ref:`MIDPOINT OF {X(3513), X(3514)} <X_3660>`)

.. signature:: center

   | **Trilinears:** :math:`(a - b + c)(a + b - c) + 4r(r^{2} + 4rR)^{1/2} : :` (:person:`Peter Moses <peter-moses>`, 7/22/08)
   | **Tripolars:** :math:`1/r_{a} : :`, where :math:`r_{a}`, :math:`r_{b}`, :math:`r_{c}` are the exradii
   | **Search Value (6, 9, 13):** :math:`0.847390686637`

.. collapse:: Alternate Coordinates
   :badge: 2 forms

   * **Tripolars:** :math:`\tan A' : :`, where :g:`J_aJ_bJ_c << J_a J_b J_c >>` is the :term:`excentral triangle <excentral-triangle>`
   * **Tripolars:** :math:`b + c - a : :`

.. collapse:: Linear Combinations
   :badge: 1 combination

   * :ref:`X_3513 <X_3513>` = :math:`(r + 2R + \sqrt{r^{2} + 4rR})` :ref:`X_1 <X_1>` - :math:`2r` :ref:`X_3 <X_3>`

.. collapse:: Incident Central Lines
   :badge: 1 line
   :class: line-catalog

   {:ref:`1 <X_1>`, :ref:`3 <X_3>`}

.. collapse:: Functional Relations
   :badge: 5 relations

   * :ref:`X_3513 <X_3513>` = reflection of :ref:`X_3514 <X_3514>` in :ref:`X_3660 <X_3660>`
   * :ref:`X_3513 <X_3513>` = circumcircle-inverse of :ref:`X_3514 <X_3514>`
   * :ref:`X_3513 <X_3513>` = incircle-inverse of :ref:`X_3514 <X_3514>`
   * :ref:`X_3513 <X_3513>` = one of two harmonic traces of the Soddy circles; the other is :ref:`X_3514 <X_3514>`
   * :ref:`X_3513 <X_3513>` = {X_i,X_j}-harmonic conjugate of :ref:`X_3514 <X_3514>` for these (i,j): (:ref:`1 <X_1>`, :ref:`57 <X_57>`), (:ref:`3 <X_3>`, :ref:`1617 <X_1617>`), (:ref:`36 <X_36>`, :ref:`2078 <X_2078>`), (:ref:`55 <X_55>`, :ref:`56 <X_56>`), (:ref:`65 <X_65>`, :ref:`354 <X_354>`), (:ref:`165 <X_165>`, :ref:`1420 <X_1420>`)

Notes
-----

.. container:: note-item

   David Eppstein, `The dilation center of a triangle <http://11011110.livejournal.com/144178.html>`__

   for a discussion of :ref:`X_3513 <X_3513>` as a point of intersection of three similar ellipses, each having two of the points :g:`A <A>`, :g:`B <B>`, :g:`C <C>` as foci. (Contributed by David Eppstein, 7/10/08)

.. container:: note-item

   :ref:`X_3513 <X_3513>` is the point P such that the incenter of the circumcevian triangle of :g:`P <P>` is also the incenter of triangle :g:`ABC << A B C >>`. (:person:`Randy Hutson <randy-hutson>`, 9/23/2011)

.. container:: note-item

   :ref:`X_3513 <X_3513>` and :ref:`X_3514 <X_3514>` are the limiting points (point-circles) of the coaxal system that includes the circumcircle and incircle. Their midpoint, :ref:`X_3660 <X_3660>`, is the :term:`radical trace <radical-trace>` of the incircle and circumcircle. (Peter Moses, November 15, 2011)

.. container:: note-item

   In the plane of a triangle :g:`ABC << A B C >>`, let :g:`P <P>` be a point on the line :ref:`X_1 <X_1>`\ \ :ref:`X_3 <X_3>`, and let :g:`DEF << D E F >>` = :term:`intouch triangle <intouch-triangle>`. Let :math:`R_{A}` = reflection of :g:`AP <[ A P ]>` in :g:`EF <[ E F ]>`, and define :math:`R_{B}` and :math:`R_{C}` cyclically. The lines :math:`R_{A}`, :math:`R_{B}`, :math:`R_{C}` concur in a point, :g:`P' <P'>`, that lies on a rectangular hyperbola that circumscribes :g:`DEF << D E F >>`. Let :g:`P″ <P″>` = :g:`DEF << D E F >>`-:term:`isogonal conjugate <isogonal-conjugate>` of :g:`P' <P'>`. The mapping P → :g:`P″ <P″>` is a projective transformation of the line :ref:`X_1 <X_1>`\ \ :ref:`X_3 <X_3>`, and its fixed points are :ref:`X_3513 <X_3513>` and :ref:`X_3514 <X_3514>`. (:person:`Angel Montesdeoca <angel-montesdeoca>`, April 17, 2021)

.. toctree::
   :hidden:

   code
