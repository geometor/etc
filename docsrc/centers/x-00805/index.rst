:order: 805
:type: center
:canonical_id: X(805)
:dependencies: X(5), X(6), X(39), X(98), X(99), X(110), X(111), X(187), X(249), X(385), X(511), X(512), X(574), X(669), X(691), X(694), X(729), X(804), X(827), X(843), X(882), X(888), X(892), X(9831), X(14295), X(32531)

.. _X(805):

X(805) = o-(- 2, 2) CIRCUMCIRCLE POINT
======================================

.. figure:: x-00805.svg
   :alt: X(805) = o-(- 2, 2) CIRCUMCIRCLE POINT
   :align: center

   **X(805) = o-(- 2, 2) CIRCUMCIRCLE POINT** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`f(a,b,c) : f(b,c,a) : f(c,a,b)`, where f(a,b,c) = 1/[a :sup:`-3`\ (b\ :sup:`2` - c\ :sup:`2`) + a\ :sup:`1`\ (b :sup:`-2` - c :sup:`-2`)]

Barycentrics
~~~~~~~~~~~~

* :math:`g(a,b,c) : g(b,c,a) : g(c,a,b)`, where g(a,b,c) = af(a,b,c)

* **Kimberling (6, 9, 13) Search Value:** :math:`0.223824932622`

Notes
-----

.. container:: note-item

   Let A'B'C' be the vertex-triangle of the 2nd and 3rd Brocard triangles. The lines AA', BB', CC' concur in :ref:`X(805) <X(805)>`. (:person:`Randy Hutson <randy-hutson>`, March 25, 2016)

.. container:: note-item

   Let La, Lb, Lc be the lines through A, B, C, resp. parallel to the Brocard axis. Let Ma, Mb, Mc be the reflections of BC, CA, AB in La, Lb, Lc, resp. Let A' = Mb∩Mc, and define B' and C' cyclically. Triangle A'B'C' is inversely similar to, and 3 times the size of, ABC. The centroid of A'B'C' is :ref:`X(805) <X(805)>`; see :cite:`Hyacinthos #16741 <hyacinthos>`/16782, Sep 2008. (Randy Hutson, March 25, 2016)

.. container:: note-item

   Let La, Lb, Lc be the lines through A, B, C, resp. parallel to the Lemoine axis. Let Ma, Mb, Mc be the reflections of BC, CA, AB in La, Lb, Lc, resp. Let A' = Mb∩Mc, and define B' and C' cyclically. Triangle A'B'C' is inversely similar to, and 3 times the size of, ABC. The centroid of A'B'C' is :ref:`X(805) <X(805)>`; see :cite:`Hyacinthos #16741 <hyacinthos>`/16782, Sep 2008. (Randy Hutson, March 25, 2016)

Incidence
---------

:ref:`X(805) <X(805)>` lies on the circumcircle and on these lines:

{:ref:`98 <X(98)>`, :ref:`385 <X(385)>`}, {:ref:`99 <X(99)>`, :ref:`512 <X(512)>`}, {:ref:`110 <X(110)>`, :ref:`669 <X(669)>`}, {:ref:`111 <X(111)>`, :ref:`694 <X(694)>`}, {:ref:`187 <X(187)>`, :ref:`729 <X(729)>`}, {:ref:`249 <X(249)>`, :ref:`827 <X(827)>`}, {:ref:`574 <X(574)>`, :ref:`843 <X(843)>`}, {:ref:`691 <X(691)>`, :ref:`882 <X(882)>`}, {:ref:`888 <X(888)>`, :ref:`892 <X(892)>`}

Relations
---------

* :ref:`X(805) <X(805)>` = :term:`isogonal conjugate <isogonal-conjugate>` of :ref:`X(804) <X(804)>`
* :ref:`X(805) <X(805)>` = :term:`isotomic conjugate <isotomic-conjugate>` of X(14295)
* :ref:`X(805) <X(805)>` = :term:`trilinear pole <trilinear-pole>` of line :ref:`X(6) <X(6)>`\ \ :ref:`X(694) <X(694)>`
* :ref:`X(805) <X(805)>` = Ψ(:ref:`X(6) <X(6)>`, :ref:`X(694) <X(694)>`)
* :ref:`X(805) <X(805)>` = :term:`cevapoint <cevapoint>` of :ref:`X(511) <X(511)>` and :ref:`X(512) <X(512)>`
* :ref:`X(805) <X(805)>` = reflection of :ref:`X(99) <X(99)>` in the Brocard axis
* :ref:`X(805) <X(805)>` = Brocard-circle-inverse of X(32531)
* :ref:`X(805) <X(805)>` = X(9831)-of-circumsymmedial-triangle
* :ref:`X(805) <X(805)>` = intersection of antipedal lines of :ref:`X(98) <X(98)>` and :ref:`X(99) <X(99)>`
* :ref:`X(805) <X(805)>` = perspector of ABC and the triangle formed by reflecting line :ref:`X(5) <X(5)>`\ \ :ref:`X(39) <X(39)>` in the sides of ABC

Construction
------------

.. literalinclude:: model.py
   :language: python
