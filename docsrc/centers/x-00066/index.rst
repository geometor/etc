:order: 66
:type: center
:canonical_id: X(66)
:dependencies: X(2), X(3), X(4), X(6), X(22), X(32), X(63), X(68), X(73), X(125), X(141), X(159), X(193), X(206), X(248), X(290), X(315), X(317), X(427), X(511), X(512), X(571), X(647), X(826), X(879), X(895), X(924), X(976), X(1177), X(2435), X(2892), X(2998), X(3174), X(3448), X(5596), X(8743), X(14376)

.. _X(66):

X(66) = ISOGONAL CONJUGATE OF X(22)
===================================

.. figure:: x-00066.svg
   :alt: X(66) = ISOGONAL CONJUGATE OF X(22)
   :align: center

   **X(66) = ISOGONAL CONJUGATE OF X(22)** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`bc/(b^{4} + c^{4} - a^{4}) : :`

Barycentrics
~~~~~~~~~~~~

* :math:`1/(b^{4} + c^{4} - a^{4}) : :`

* **Kimberling (6, 9, 13) Search Value:** :math:`9.640588374561`

Notes
-----

.. container:: note-item

   Let P be a point on the circumcircle, and let L\ :sub:`P` be its Steiner line. The locus of the orthopole of L\ :sub:`P`, as P varies, is an ellipse with center :ref:`X(4) <X(4)>` and perspector :ref:`X(66) <X(66)>`. (:person:`Randy Hutson <randy-hutson>`, March 29, 2020)

.. container:: note-item

   In the plane of a triangle ABC, let

      * A'B'C' = :term:`anticomplementary triangle <anticomplementary-triangle>`;
      * Oa = circle with diameter BC, and define Ob and Oc cyclically;
      * Ab = A'BC'∩Oa, and define Bc and Ca cyclically;
      * Ac = B'CA'∩Oa, and define Ba and Cb cyclically;
      * A″= BcBa∩CaCb, and define B″ and C″ cyclically.

   The triangle A″B″C″ is perspective to ABC, and the perspector is :ref:`X(66) <X(66)>`. (:person:`Dasari Naga Vijay Krishna <dasari-naga-vijay-krishna>`, April 15, 2021)

Incidence
---------

:ref:`X(66) <X(66)>` lies and on these lines:

{:ref:`2 <X(2)>`, 206}, {:ref:`3 <X(3)>`, 141}, {:ref:`6 <X(6)>`, 427}, {:ref:`68 <X(68)>`, 511}, {:ref:`73 <X(73)>`, 976}, {193, 895}, {248, 571}, {290, 317}, {879, 924}

Relations
---------

* :ref:`X(66) <X(66)>` = midpoint of X(2892) and X(3448)
* :ref:`X(66) <X(66)>` = reflection of X(i) in X(j) for these (i,j): (159, 141), (1177, 125)
* :ref:`X(66) <X(66)>` = :term:`isogonal conjugate <isogonal-conjugate>` of :ref:`X(22) <X(22)>`
* :ref:`X(66) <X(66)>` = :term:`isotomic conjugate <isotomic-conjugate>` of X(315)
* :ref:`X(66) <X(66)>` = :term:`complement <complement>` of X(5596)
* :ref:`X(66) <X(66)>` = :term:`anticomplement <anticomplement>` of X(206)
* :ref:`X(66) <X(66)>` = :term:`cyclocevian conjugate <cyclocevian-conjugate>` of X(2998)
* :ref:`X(66) <X(66)>` = :term:`cevapoint <cevapoint>` of X(125) and X(512)
* :ref:`X(66) <X(66)>` = :ref:`X(32) <X(32)>`-:term:`cross conjugate <cross-conjugate>` of :ref:`X(2) <X(2)>`
* :ref:`X(66) <X(66)>` = :term:`crosssum <crosssum>` of :ref:`X(3) <X(3)>` and X(159)
* :ref:`X(66) <X(66)>` = :term:`trilinear pole <trilinear-pole>` of line X(647)X(826) (radical axis of Brocard and polar circles)
* :ref:`X(66) <X(66)>` = :term:`antigonal image <antigonal-image>` of X(1177)
* :ref:`X(66) <X(66)>` = orthocenter of :ref:`X(3) <X(3)>`\ \ :ref:`X(4) <X(4)>`\ X(2435)
* :ref:`X(66) <X(66)>` = X(3174)-of-orthic-triangle if ABC is acute
* :ref:`X(66) <X(66)>` = polar conjugate of isotomic conjugate of X(14376)
* :ref:`X(66) <X(66)>` = :ref:`X(63) <X(63)>`-:term:`isoconjugate <isoconjugate>` of X(8743)

Construction
------------

.. literalinclude:: model.py
   :language: python
