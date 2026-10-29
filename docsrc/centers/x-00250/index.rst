:order: 250
:type: center
:canonical_id: X(250)
:dependencies: X(3), X(22), X(23), X(24), X(25), X(99), X(101), X(107), X(110), X(112), X(125), X(162), X(186), X(199), X(232), X(249), X(270), X(325), X(338), X(339), X(340), X(476), X(520), X(523), X(648), X(687), X(691), X(827), X(933), X(935), X(1113), X(1114)

.. _X(250):

X(250) = ISOGONAL CONJUGATE OF X(125)
=====================================

.. figure:: x-00250.svg
   :alt: X(250) = ISOGONAL CONJUGATE OF X(125)
   :align: center

   **X(250) = ISOGONAL CONJUGATE OF X(125)** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`(\sec A)\csc^{2}(B - C) : (\sec B)\csc^{2}(C - A) : (\sec C)\csc^{2}(A - B), = (a^{2}\sec A)/(b^{2} - c^{2})^{2} : (b^{2}\sec B)/(c^{2} - a^{2})^{2} : (c^{2}\sec C)/(a^{2} - b^{2})^{2}`

* **Kimberling (6, 9, 13) Search Value:** :math:`-0.110816929619`

Notes
-----

.. container:: note-item

   Barycentrics (tan A)csc\ :sup:`2`\ (B - C) : (tan B)csc\ :sup:`2`\ (C - A) : (tan C)csc\ :sup:`2`\ (A - B)

.. container:: note-item

   :ref:`X(250) <X(250)>` is the :term:`trilinear pole <trilinear-pole>` of line :ref:`X(110) <X(110)>`\ \ :ref:`X(112) <X(112)>`, which is the tangent to the MacBeath circumconic at :ref:`X(110) <X(110)>`, and the locus of trilinear poles of tangents at P to conic {A,B,C,\ :ref:`X(3) <X(3)>`,P}}, as P moves on the Brocard axis. (:person:`Randy Hutson <randy-hutson>`, March 21, 2019)

Incidence
---------

:ref:`X(250) <X(250)>` lies and on these lines:

{:ref:`23 <X(23)>`, :ref:`232 <X(232)>`}, {:ref:`107 <X(107)>`, :ref:`687 <X(687)>`}, {:ref:`110 <X(110)>`, :ref:`520 <X(520)>`}, {:ref:`112 <X(112)>`, :ref:`691 <X(691)>`}, {:ref:`186 <X(186)>`, :ref:`249 <X(249)>`}, {:ref:`325 <X(325)>`, :ref:`340 <X(340)>`}, {:ref:`476 <X(476)>`, :ref:`933 <X(933)>`}, {:ref:`523 <X(523)>`, :ref:`648 <X(648)>`}, {:ref:`827 <X(827)>`, :ref:`935 <X(935)>`}

Relations
---------

* :ref:`X(250) <X(250)>` = :term:`isogonal conjugate <isogonal-conjugate>` of :ref:`X(125) <X(125)>`
* :ref:`X(250) <X(250)>` = :term:`isotomic conjugate <isotomic-conjugate>` of :ref:`X(339) <X(339)>`
* :ref:`X(250) <X(250)>` = :term:`cevapoint <cevapoint>` of X(i) and X(j) for these (i,j): (:ref:`3 <X(3)>`, :ref:`110 <X(110)>`), (:ref:`25 <X(25)>`, :ref:`112 <X(112)>`), (:ref:`162 <X(162)>`, :ref:`270 <X(270)>`), (1113, 1114)
* :ref:`X(250) <X(250)>` = X(i)-:term:`cross conjugate <cross-conjugate>` of X(j) for these (i,j): (:ref:`3 <X(3)>`, :ref:`110 <X(110)>`), (:ref:`22 <X(22)>`, :ref:`99 <X(99)>`), (:ref:`24 <X(24)>`, :ref:`107 <X(107)>`), (:ref:`25 <X(25)>`, :ref:`112 <X(112)>`), (:ref:`199 <X(199)>`, :ref:`101 <X(101)>`)
* :ref:`X(250) <X(250)>` = polar conjugate of :ref:`X(338) <X(338)>`
* :ref:`X(250) <X(250)>` = circumcenter of reflection triangle of :ref:`X(125) <X(125)>`
* :ref:`X(250) <X(250)>` = barycentric product :ref:`X(99) <X(99)>`\ \*\ :ref:`X(112) <X(112)>`
* :ref:`X(250) <X(250)>` = cevapoint of MacBeath circumconic intercepts of Brocard axis

Construction
------------

.. literalinclude:: model.py
   :language: python
