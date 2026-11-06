:order: 359
:canonical_id: X_359
:subtitle: HOFSTADTER ONE POINT
:dependencies: X_1, X_2, X_6, X_31, X_37, X_75, X_360, X_512, X_1028, X_1049, X_1077, X_3067, X_4094, X_4895, X_5945, X_9036, X_42074

.. _X_359:
.. _HofstadterOnePoint:

X_359
=====

.. rubric:: HOFSTADTER ONE POINT

.. enunciation::

   The Hofstadter ellipse E(1/2), given by :math:`x^{2}` + :math:`y^{2}` + :math:`z^{2}` - 2yz - 2xz - 2xy = 0, has center :ref:`X_37 <X_37>` and passes through X_i for these i: 244, 678, 2310, 2632, 2638, 2643, 3248, 4094, 4117, 10501, 23063, 24012.

.. figure:: x-00359.svg
   :alt: X_359 — HOFSTADTER ONE POINT
   :align: center

   **X_359** (*HOFSTADTER ONE POINT*) constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :g:`AB <[ A B ]>` = :math:`1`.

.. admonition:: Constructed Elements
   :class: note

   * **Related Centers:** :g:`X_2 <X_2>` (:ref:`CENTROID <X_2>`)

.. signature:: center

   | **Trilinears:** :math:`a/A : b/B : c/C`
   | **Barycentrics:** :math:`a^{2}/A : b^{2}/B : c^{2}/C`
   | **Search Value (6, 9, 13):** :math:`2.333647742736`

.. collapse:: Incident Central Lines
   :badge: 1 line
   :class: line-catalog

   {:ref:`6 <X_6>`, 9036}

.. collapse:: Functional Relations
   :badge: 6 relations

   * :ref:`X_359 <X_359>` = :term:`isogonal conjugate <isogonal-conjugate>` of :ref:`X_360 <X_360>`
   * :ref:`X_359 <X_359>` = :ref:`X_2 <X_2>`-:term:`Ceva conjugate <ceva-conjugate>` of X_5945
   * :ref:`X_359 <X_359>` = X_i-:term:`isoconjugate <isoconjugate>` of X_j for these (i,j): {:ref:`1 <X_1>`, :ref:`360 <X_360>`}, {:ref:`2 <X_2>`, :ref:`1049 <X_1049>`}
   * :ref:`X_359 <X_359>` = barycentric product X_i\*X_j for these {i,j}: {:ref:`1 <X_1>`, :ref:`1077 <X_1077>`}, {:ref:`1028 <X_1028>`, :ref:`1049 <X_1049>`}
   * :ref:`X_359 <X_359>` = barycentric quotient X_i/X_j for these {i,j}: {:ref:`6 <X_6>`, :ref:`360 <X_360>`}, {:ref:`31 <X_31>`, :ref:`1049 <X_1049>`}, {:ref:`1077 <X_1077>`, :ref:`75 <X_75>`}
   * :ref:`X_359 <X_359>` = perspector of Hofstadter 0-ellipse

Notes
-----

.. container:: note-item

   This point is the limit as r approaches 1 of the Hofstadter r point. See :ref:`X_360 <X_360>` for details.

      :math:`x^{2}` + :math:`y^{2}` + :math:`z^{2}` + yz(D + 1/D) + zx(E + 1/E) + xy(F + 1/F) = 0, where :g:`D <D>` = cos A - sin A cot rA, :g:`E <E>` = cos B - sin B cot rB, :g:`F <F>` = cos C - sin C cot rC.

.. container:: note-item

   Taking the limit of E(r) as r tends to 0 gives information about the circumellipse, E(0) (which is also E(1)):

   Equation: ayz/A + bzx/B + cxy/:g:`C <C>` = 0

   Center: X_5945 = (a/A)(:math:`b^{2}`/B + :math:`c^{2}`/C - :math:`a^{2}`/A) : (b/B)(:math:`c^{2}`/C + :math:`a^{2}`/A - :math:`b^{2}`/B) : (c/C)(:math:`a^{2}`/A + :math:`b^{2}`/B - :math:`c^{2}`/C)

   Intersection with circumcircle (other than :g:`A <A>`, :g:`B <B>`, :g:`C <C>`): :ref:`X_3067 <X_3067>` = a/[A(B - C)] : b/[B(C - A)] : c/[C(A - B)]

.. container:: note-item

   The Hofstadter ellipse E(1/2) is also the incentral inellipse, centered at :ref:`X_37 <X_37>`, and touching :g:`ABC << A B C >>` at the traces of :ref:`X_1 <X_1>`. The ellipse also passes through X_4094, and is the incentral :term:`isotomic conjugate <isotomic-conjugate>` of line :ref:`X_512 <X_512>`\ X_4895. (:person:`Randy Hutson <randy-hutson>`, October 15, 2018)

.. container:: note-item

   See `Hofstadter Ellipse at MathWorld <http://mathworld.wolfram.com/HofstadterEllipse.html>`__.

.. container:: note-item

   See also the preamble just before X_42074.

.. toctree::
   :hidden:

   code
