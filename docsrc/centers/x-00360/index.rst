:order: 360
:type: center
:canonical_id: X_360
:subtitle: HOFSTADTER ZERO POINT
:dependencies: X_1, X_2, X_3, X_4, X_6, X_8, X_35, X_69, X_75, X_79, X_80, X_186, X_265, X_357, X_358, X_359, X_1028, X_1049, X_1077, X_1085, X_1115, X_1127, X_1129, X_3065, X_5457, X_5458, X_5961, X_5962, X_5963, X_5964, X_7021, X_7041

.. _X_360:
.. _HofstadterZeroPoint:

X_360
=====

.. rubric:: HOFSTADTER ZERO POINT

.. enunciation::

   The limit of this point as r approaches 0 is :ref:`X_360 <X_360>`. The two Hofstadter points, :ref:`X_359 <X_359>` and :ref:`X_360 <X_360>` are examples of transcendental :term:`triangle centers <triangle-center>`, since they have no trilinear or barycentric representation using only algebraic functions of a,b,c (or sin A, sin B, sin C).

.. figure:: x-00360.svg
   :alt: X_360 — HOFSTADTER ZERO POINT
   :align: center

   **X_360** (*HOFSTADTER ZERO POINT*) constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :g:`AB <[ A B ]>` = :math:`1`.

.. signature:: center

   | **Trilinears:** :math:`A/a : B/b : C/c`
   | **Barycentrics:** :math:`A : B : C`
   | **Search Value (6, 9, 13):** :math:`1.045653663244`

.. collapse:: Linear Combinations
   :badge: 1 combination

   * :ref:`X_360 <X_360>` = :math:`A` :g:`A <A>` + :math:`B` :g:`B <B>` + :math:`C` :g:`C <C>`, where :g:`A <A>`, :g:`B <B>`, :g:`C <C>` are the angles and :g:`A <A>`, :g:`B <B>`, :g:`C <C>` are the vertices

.. collapse:: Incident Central Lines
   :badge: 1 line
   :class: line-catalog

   {:ref:`2 <X_2>`, 1115}

.. collapse:: Functional Relations
   :badge: 25 relations

   * :ref:`X_1 <X_1>` = Hofstadter 1/2 point = :term:`antigonal image <antigonal-image>` of :ref:`X_80 <X_80>`
   * :ref:`X_3 <X_3>` = Hofstadter 2 point = antigonal image of :ref:`X_265 <X_265>`
   * :ref:`X_4 <X_4>` = Hofstadter -1 point
   * :ref:`X_35 <X_35>` = Hofstadter 3/2 point
   * :ref:`X_79 <X_79>` = Hofstadter -1/2 point = antigonal image of X_3065
   * :ref:`X_186 <X_186>` = Hofstadter 3 point = antigonal image of X_5962
   * :ref:`X_265 <X_265>` = Hofstadter -2 point = antigonal image of :ref:`X_3 <X_3>`
   * :ref:`X_357 <X_357>` = Hofstadter 1/3 point
   * :ref:`X_358 <X_358>` = Hofstadter 2/3 point
   * :ref:`X_359 <X_359>` = Hofstadter 0 point
   * :ref:`X_360 <X_360>` = Hofstadter 1 point
   * X_1127 = Hofstadter 1/4 point
   * X_1129 = Hofstadter 3/4 point
   * X_5457 = Hofstadter -1/3 point
   * X_5458 = Hofstadter -2/3 point
   * X_5961 = Hofstadter 4 point = antigonal image of X_5964
   * X_5962 = Hofstadter -3 point = antigonal image of :ref:`X_186 <X_186>`
   * X_5963 = Hofstadter 5 point
   * X_5964 = Hofstadter -4 point = antigonal image of X_5961
   * :ref:`X_360 <X_360>` = :term:`isogonal conjugate <isogonal-conjugate>` of :ref:`X_359 <X_359>`
   * :ref:`X_360 <X_360>` = :term:`anticomplement <anticomplement>` of X_1115
   * :ref:`X_360 <X_360>` = X_i-:term:`anticomplementary conjugate <anticomplementary-conjugate>` of X_j for these (i,j): {7021, :ref:`8 <X_8>`}, {7041, :ref:`69 <X_69>`}
   * :ref:`X_360 <X_360>` = X_i-:term:`isoconjugate <isoconjugate>` of X_j for these (i,j): {:ref:`1 <X_1>`, :ref:`359 <X_359>`}, {:ref:`6 <X_6>`, 1077}
   * :ref:`X_360 <X_360>` = barycentric product :ref:`X_75 <X_75>`\ \*X_1049
   * :ref:`X_360 <X_360>` = barycentric quotient X_i/X_j for these {i,j}: {:ref:`1 <X_1>`, 1077}, {:ref:`6 <X_6>`, :ref:`359 <X_359>`}, {1049, :ref:`1 <X_1>`}, {1077, 1028}, {1085, 1049}

Notes
-----

.. container:: note-item

   This point is obtained as a limit of perspectors. Let r denote a real number, but not 0 or 1. Using vertex B as a pivot, swing line :g:`BC <[ B C ]>` toward vertex A through angle rB and swing line :g:`BC <[ B C ]>` about C through angle rC. Let A(r) be the point in which the two swung lines meet. Obtain B(r) and C(r) cyclically. Triangle A(r)B(r)C(r) is the *r-Hofstadter triangle*; its perspector with :g:`ABC << A B C >>`, called the Hofstadter r point, is the point given by trilinears

      (sin rA)/sin(A - rA) : (sin rB)/sin(B - rB) : (sin rC)/sin(C - rC).

.. container:: note-item

   **Clark Kimberling,** "Hofstadter points," *Nieuw Archief voor Wiskunde* 12 (1994) 109-114.

.. container:: note-item

   If r is an integer other than 0, 1, or 2, then the inverse-in-circumcircle of the Hofstadter r point is the Hofstadter (2-r) point;

      * thus, since the isogonal conjugate of the Hofstadter r point is the Hofstadter (1-r) point, if r is not -1, 0 or 1,
      * then the antigonal image of the Hofstadter r point is the Hofstadter -r point.

.. toctree::
   :hidden:

   code
