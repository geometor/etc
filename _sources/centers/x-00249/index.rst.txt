:order: 249
:type: center
:canonical_id: X(249)
:dependencies: X(2), X(3), X(6), X(24), X(63), X(92), X(99), X(110), X(112), X(115), X(125), X(186), X(187), X(250), X(297), X(316), X(323), X(338), X(351), X(512), X(525), X(620), X(648), X(687), X(805), X(827), X(849), X(1110), X(1379), X(1380), X(1648), X(2970), X(4590), X(8029), X(8754)

.. _X(249):

X(249) = ISOGONAL CONJUGATE OF X(115)
=====================================

.. _preamble-0007:

.. admonition:: Group Preamble — Centers X(249)-X(297)
   :class: note

   Centers :ref:`X(249) <X(249)>`-:ref:`X(297) <X(297)>` are :term:`isogonal conjugates <isogonal-conjugate>` of previously listed centers.

.. figure:: x-00249.svg
   :alt: X(249) = ISOGONAL CONJUGATE OF X(115)
   :align: center

   **X(249) = ISOGONAL CONJUGATE OF X(115)** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`(\csc A)\csc^{2}(B - C) : (\csc B)\csc^{2}(C - A) : (\csc C)\csc^{2}(A - B), = a/(b^{2} - c^{2})^{2} : b/(c^{2} - a^{2})^{2} : c/(a^{2} - b^{2})^{2}`

* **Kimberling (6, 9, 13) Search Value:** :math:`0.395641663632`

Notes
-----

.. container:: note-item

   Barycentrics csc\ :sup:`2`\ (B - C) : csc\ :sup:`2`\ (C - A) : csc\ :sup:`2`\ (A - B)

.. container:: note-item

   :ref:`X(249) <X(249)>` is the :term:`vertex conjugate <vertex-conjugate>` of the foci of the inellipse that is the barycentric square of line :ref:`X(2) <X(2)>`\ \ :ref:`X(6) <X(6)>`. The center of this inellipse is :ref:`X(620) <X(620)>`, and its perspector is X(4590). (:person:`Randy Hutson <randy-hutson>`, October 15, 2018)

.. container:: note-item

   :ref:`X(249) <X(249)>` is the :term:`trilinear pole <trilinear-pole>` of line :ref:`X(110) <X(110)>`\ \ :ref:`X(351) <X(351)>`, which is the tangent to the circumcircle at :ref:`X(110) <X(110)>`, and the locus of trilinear poles of tangents at P to hyperbola {A,B,C,\ :ref:`X(6) <X(6)>`,P}}, as P moves on the Brocard axis. (Randy Hutson, October 15, 2018)

Incidence
---------

:ref:`X(249) <X(249)>` lies and on these lines:

{:ref:`99 <X(99)>`, :ref:`525 <X(525)>`}, {:ref:`110 <X(110)>`, :ref:`512 <X(512)>`}, {:ref:`186 <X(186)>`, :ref:`250 <X(250)>`}, {:ref:`187 <X(187)>`, :ref:`323 <X(323)>`}, {:ref:`297 <X(297)>`, :ref:`316 <X(316)>`}, {:ref:`648 <X(648)>`, :ref:`687 <X(687)>`}, {:ref:`805 <X(805)>`, :ref:`827 <X(827)>`}, {:ref:`849 <X(849)>`, 1110}

Relations
---------

* :ref:`X(249) <X(249)>` = isogonal conjugate of :ref:`X(115) <X(115)>`
* :ref:`X(249) <X(249)>` = :term:`isotomic conjugate <isotomic-conjugate>` of :ref:`X(338) <X(338)>`
* :ref:`X(249) <X(249)>` = :term:`cevapoint <cevapoint>` of X(i) and X(j) for these (i,j): (:ref:`6 <X(6)>`, :ref:`110 <X(110)>`), (:ref:`24 <X(24)>`, :ref:`112 <X(112)>`), (1379, 1380)
* :ref:`X(249) <X(249)>` = X(i)-:term:`cross conjugate <cross-conjugate>` of X(j) for these (i,j): (:ref:`3 <X(3)>`, :ref:`99 <X(99)>`), (:ref:`6 <X(6)>`, :ref:`110 <X(110)>`)
* :ref:`X(249) <X(249)>` = perspector of ABC and reflection of symmedial triangle in the Brocard axis
* :ref:`X(249) <X(249)>` = polar conjugate of X(2970)
* :ref:`X(249) <X(249)>` = :ref:`X(63) <X(63)>`-:term:`isoconjugate <isoconjugate>` of X(8754)
* :ref:`X(249) <X(249)>` = :ref:`X(92) <X(92)>`-isoconjugate of :ref:`X(125) <X(125)>`
* :ref:`X(249) <X(249)>` = :term:`crossdifference <crossdifference>` of every pair of points on line X(1648)X(8029)
* :ref:`X(249) <X(249)>` = Vu circlecevian point of PU(2)

Construction
------------

.. literalinclude:: model.py
   :language: python
