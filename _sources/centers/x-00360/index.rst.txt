:order: 360
:type: center
:canonical_id: X(360)
:dependencies: X(1), X(2), X(3), X(4), X(6), X(8), X(35), X(69), X(75), X(79), X(80), X(186), X(265), X(357), X(358), X(359), X(1028), X(1049), X(1077), X(1085), X(1115), X(1127), X(1129), X(3065), X(5457), X(5458), X(5961), X(5962), X(5963), X(5964), X(7021), X(7041)

.. _X(360):
.. _HofstadterZeroPoint:

X(360) = HOFSTADTER ZERO POINT
==============================

.. enunciation::

   The limit of this point as r approaches 0 is :ref:`X(360) <X(360)>`. The two Hofstadter points, :ref:`X(359) <X(359)>` and :ref:`X(360) <X(360)>` are examples of transcendental :term:`triangle centers <triangle-center>`, since they have no trilinear or barycentric representation using only algebraic functions of a,b,c (or sin A, sin B, sin C).

.. figure:: x-00360.svg
   :alt: X(360) = HOFSTADTER ZERO POINT
   :align: center

   **X(360) = HOFSTADTER ZERO POINT** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :g:`AB <[ A B ]>` = :math:`1`.

.. signature:: center

   | **Trilinears:** :math:`A/a : B/b : C/c`
   | **Barycentrics:** :math:`A : B : C`
   | **Search Value (6, 9, 13):** :math:`1.045653663244`

.. collapse:: Linear Combinations
   :badge: 1 combination

   * :ref:`X(360) <X(360)>` = :math:`A` :g:`A <A>` + :math:`B` :g:`B <B>` + :math:`C` :g:`C <C>`, where :g:`A <A>`, :g:`B <B>`, :g:`C <C>` are the angles and :g:`A <A>`, :g:`B <B>`, :g:`C <C>` are the vertices

.. collapse:: Incident Central Lines
   :badge: 1 line
   :class: line-catalog

   {:ref:`2 <X(2)>`, 1115}

.. collapse:: Functional Relations
   :badge: 25 relations

   * :ref:`X(1) <X(1)>` = Hofstadter 1/2 point = :term:`antigonal image <antigonal-image>` of :ref:`X(80) <X(80)>`
   * :ref:`X(3) <X(3)>` = Hofstadter 2 point = antigonal image of :ref:`X(265) <X(265)>`
   * :ref:`X(4) <X(4)>` = Hofstadter -1 point
   * :ref:`X(35) <X(35)>` = Hofstadter 3/2 point
   * :ref:`X(79) <X(79)>` = Hofstadter -1/2 point = antigonal image of X(3065)
   * :ref:`X(186) <X(186)>` = Hofstadter 3 point = antigonal image of X(5962)
   * :ref:`X(265) <X(265)>` = Hofstadter -2 point = antigonal image of :ref:`X(3) <X(3)>`
   * :ref:`X(357) <X(357)>` = Hofstadter 1/3 point
   * :ref:`X(358) <X(358)>` = Hofstadter 2/3 point
   * :ref:`X(359) <X(359)>` = Hofstadter 0 point
   * :ref:`X(360) <X(360)>` = Hofstadter 1 point
   * X(1127) = Hofstadter 1/4 point
   * X(1129) = Hofstadter 3/4 point
   * X(5457) = Hofstadter -1/3 point
   * X(5458) = Hofstadter -2/3 point
   * X(5961) = Hofstadter 4 point = antigonal image of X(5964)
   * X(5962) = Hofstadter -3 point = antigonal image of :ref:`X(186) <X(186)>`
   * X(5963) = Hofstadter 5 point
   * X(5964) = Hofstadter -4 point = antigonal image of X(5961)
   * :ref:`X(360) <X(360)>` = :term:`isogonal conjugate <isogonal-conjugate>` of :ref:`X(359) <X(359)>`
   * :ref:`X(360) <X(360)>` = :term:`anticomplement <anticomplement>` of X(1115)
   * :ref:`X(360) <X(360)>` = X(i)-:term:`anticomplementary conjugate <anticomplementary-conjugate>` of X(j) for these (i,j): {7021, :ref:`8 <X(8)>`}, {7041, :ref:`69 <X(69)>`}
   * :ref:`X(360) <X(360)>` = X(i)-:term:`isoconjugate <isoconjugate>` of X(j) for these (i,j): {:ref:`1 <X(1)>`, :ref:`359 <X(359)>`}, {:ref:`6 <X(6)>`, 1077}
   * :ref:`X(360) <X(360)>` = barycentric product :ref:`X(75) <X(75)>`\ \*X(1049)
   * :ref:`X(360) <X(360)>` = barycentric quotient X(i)/X(j) for these {i,j}: {:ref:`1 <X(1)>`, 1077}, {:ref:`6 <X(6)>`, :ref:`359 <X(359)>`}, {1049, :ref:`1 <X(1)>`}, {1077, 1028}, {1085, 1049}

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
