:order: 359
:type: center
:canonical_id: X(359)
:dependencies: X(1), X(2), X(6), X(31), X(37), X(75), X(360), X(512), X(1028), X(1049), X(1077), X(3067), X(4094), X(4895), X(5945), X(9036), X(42074)

.. _X(359):
.. _HofstadterOnePoint:

X(359) = HOFSTADTER ONE POINT
=============================

.. enunciation::

   The Hofstadter ellipse E(1/2), given by :math:`x^{2}` + :math:`y^{2}` + :math:`z^{2}` - 2yz - 2xz - 2xy = 0, has center :ref:`X(37) <X(37)>` and passes through X(i) for these i: 244, 678, 2310, 2632, 2638, 2643, 3248, 4094, 4117, 10501, 23063, 24012.

.. figure:: x-00359.svg
   :alt: X(359) = HOFSTADTER ONE POINT
   :align: center

   **X(359) = HOFSTADTER ONE POINT** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :g:`AB <[ A B ]>` = :math:`1`.

.. signature:: center

   | **Trilinears:** :math:`a/A : b/B : c/C`
   | **Barycentrics:** :math:`a^{2}/A : b^{2}/B : c^{2}/C`
   | **Search Value (6, 9, 13):** :math:`2.333647742736`

.. collapse:: Incident Central Lines
   :badge: 1 line
   :class: line-catalog

   {:ref:`6 <X(6)>`, 9036}

.. collapse:: Functional Relations
   :badge: 6 relations

   * :ref:`X(359) <X(359)>` = :term:`isogonal conjugate <isogonal-conjugate>` of :ref:`X(360) <X(360)>`
   * :ref:`X(359) <X(359)>` = :ref:`X(2) <X(2)>`-:term:`Ceva conjugate <ceva-conjugate>` of X(5945)
   * :ref:`X(359) <X(359)>` = X(i)-:term:`isoconjugate <isoconjugate>` of X(j) for these (i,j): {:ref:`1 <X(1)>`, :ref:`360 <X(360)>`}, {:ref:`2 <X(2)>`, 1049}
   * :ref:`X(359) <X(359)>` = barycentric product X(i)\*X(j) for these {i,j}: {:ref:`1 <X(1)>`, 1077}, {1028, 1049}
   * :ref:`X(359) <X(359)>` = barycentric quotient X(i)/X(j) for these {i,j}: {:ref:`6 <X(6)>`, :ref:`360 <X(360)>`}, {:ref:`31 <X(31)>`, 1049}, {1077, :ref:`75 <X(75)>`}
   * :ref:`X(359) <X(359)>` = perspector of Hofstadter 0-ellipse

Notes
-----

.. container:: note-item

   This point is the limit as r approaches 1 of the Hofstadter r point. See :ref:`X(360) <X(360)>` for details.

      :math:`x^{2}` + :math:`y^{2}` + :math:`z^{2}` + yz(D + 1/D) + zx(E + 1/E) + xy(F + 1/F) = 0, where :g:`D <D>` = cos A - sin A cot rA, :g:`E <E>` = cos B - sin B cot rB, :g:`F <F>` = cos C - sin C cot rC.

.. container:: note-item

   Taking the limit of E(r) as r tends to 0 gives information about the circumellipse, E(0) (which is also E(1)):

   Equation: ayz/A + bzx/B + cxy/:g:`C <C>` = 0

   Center: X(5945) = (a/A)(:math:`b^{2}`/B + :math:`c^{2}`/C - :math:`a^{2}`/A) : (b/B)(:math:`c^{2}`/C + :math:`a^{2}`/A - :math:`b^{2}`/B) : (c/C)(:math:`a^{2}`/A + :math:`b^{2}`/B - :math:`c^{2}`/C)

   Intersection with circumcircle (other than :g:`A <A>`, :g:`B <B>`, :g:`C <C>`): X(3067) = a/[A(B - C)] : b/[B(C - A)] : c/[C(A - B)]

.. container:: note-item

   The Hofstadter ellipse E(1/2) is also the incentral inellipse, centered at :ref:`X(37) <X(37)>`, and touching :g:`ABC << A B C >>` at the traces of :ref:`X(1) <X(1)>`. The ellipse also passes through X(4094), and is the incentral :term:`isotomic conjugate <isotomic-conjugate>` of line :ref:`X(512) <X(512)>`\ X(4895). (:person:`Randy Hutson <randy-hutson>`, October 15, 2018)

.. container:: note-item

   See `Hofstadter Ellipse at MathWorld <http://mathworld.wolfram.com/HofstadterEllipse.html>`__.

.. container:: note-item

   See also the preamble just before X(42074).

.. toctree::
   :hidden:

   code
