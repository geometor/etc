:order: 903
:type: center
:canonical_id: X(903)
:dependencies: X(1), X(2), X(7), X(19), X(27), X(45), X(48), X(75), X(86), X(99), X(190), X(310), X(320), X(335), X(350), X(514), X(519), X(527), X(528), X(536), X(537), X(648), X(666), X(670), X(675), X(812), X(889), X(901), X(902), X(1017), X(1022), X(1086), X(1960), X(4120), X(4370), X(4895), X(8756), X(17487), X(22356)

.. _X(903):

X(903) = X(1)-BLAIKIE TRANSFORM OF X(2)
=======================================

.. enunciation::

   James Blaikie (1847-1929) proposed the following problem. Let O be any point in the plane of triangle ABC, and let any straight line g through O meet BC in P, CA in Q, AB in R; then, if points P', Q', R' be taken on the line so that PO = OP', QO = OQ', RO = OR'. Prove that AP', BQ', CR' concur.

.. figure:: x-00903.svg
   :alt: X(903) = X(1)-BLAIKIE TRANSFORM OF X(2)
   :align: center

   **X(903) = X(1)-BLAIKIE TRANSFORM OF X(2)** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

.. signature:: center

   | **Trilinears:** :math:`bc/(b + c - 2a) : ca/(c + a - 2b) : ab/(a + b - 2c) : :`
   | **Barycentrics:** 1/(b + c - 2a) : 1/(c + a - 2b) : 1/(a + b - 2c) (:person:`Darij Grinberg <darij-grinberg>`, 12/28/02)
   | **Search Value (6, 9, 13):** :math:`0.781704235605`

.. container:: note-item

   :ref:`X(903) <X(903)>` lies on the Steiner circumellipse.

.. collapse:: Incident Central Lines
   :badge: 12 lines
   :class: line-catalog

   {:ref:`2 <X(2)>`, :ref:`45 <X(45)>`}, {:ref:`7 <X(7)>`, :ref:`528 <X(528)>`}, {:ref:`27 <X(27)>`, :ref:`648 <X(648)>`}, {:ref:`75 <X(75)>`, :ref:`537 <X(537)>`}, {:ref:`86 <X(86)>`, :ref:`99 <X(99)>`}, {:ref:`310 <X(310)>`, :ref:`670 <X(670)>`}, {:ref:`320 <X(320)>`, :ref:`519 <X(519)>`}, {:ref:`335 <X(335)>`, :ref:`536 <X(536)>`}, {:ref:`350 <X(350)>`, :ref:`889 <X(889)>`}, {:ref:`527 <X(527)>`, :ref:`666 <X(666)>`}, {:ref:`675 <X(675)>`, :ref:`901 <X(901)>`}, {:ref:`812 <X(812)>`, 1022}

.. collapse:: Functional Relations
   :badge: 15 relations

   * :ref:`X(903) <X(903)>` = reflection of X(i) in X(j) for these (i,j): (:ref:`2 <X(2)>`, 1086), (:ref:`190 <X(190)>`, :ref:`2 <X(2)>`)
   * :ref:`X(903) <X(903)>` = :term:`isogonal conjugate <isogonal-conjugate>` of :ref:`X(902) <X(902)>`
   * :ref:`X(903) <X(903)>` = :term:`isotomic conjugate <isotomic-conjugate>` of :ref:`X(519) <X(519)>`
   * :ref:`X(903) <X(903)>` = :term:`complement <complement>` of X(17487)
   * :ref:`X(903) <X(903)>` = X(i)-:term:`cross conjugate <cross-conjugate>` of X(j) for these (i,j): (:ref:`320 <X(320)>`, :ref:`86 <X(86)>`), (:ref:`519 <X(519)>`, :ref:`2 <X(2)>`)
   * :ref:`X(903) <X(903)>` = Steiner-circumellipse-antipode of :ref:`X(190) <X(190)>`
   * :ref:`X(903) <X(903)>` = :term:`anticomplement <anticomplement>` of X(4370)
   * :ref:`X(903) <X(903)>` = projection from Steiner inellipse to Steiner circumellipse of X(1086)
   * :ref:`X(903) <X(903)>` = antipode of :ref:`X(2) <X(2)>` in hyperbola {A,B,C,\ :ref:`X(2) <X(2)>`,\ :ref:`X(7) <X(7)>`}
   * :ref:`X(903) <X(903)>` = :term:`trilinear pole <trilinear-pole>` of line :ref:`X(2) <X(2)>`\ \ :ref:`X(514) <X(514)>`
   * :ref:`X(903) <X(903)>` = pole wrt polar circle of :term:`trilinear polar <trilinear-polar>` of X(8756) (line X(4120)X(4895))
   * :ref:`X(903) <X(903)>` = :ref:`X(19) <X(19)>`-:term:`isoconjugate <isoconjugate>` of X(22356)
   * :ref:`X(903) <X(903)>` = :ref:`X(48) <X(48)>`-isoconjugate (polar conjugate) of X(8756)
   * :ref:`X(903) <X(903)>` = :term:`crossdifference <crossdifference>` of PU(99)
   * :ref:`X(903) <X(903)>` = crossdifference of every pair of points on line X(1017)X(1960)

Notes
-----

.. container:: note-item

   Darij Grinberg introduces the term *Blaikie point of O and g* for the point Z of concurrence. If

.. container:: note-item

   O = x : y : z and g = [k : l : m] (barycentric coordinates),

   then Z has first barycentric 1/[k(y-z) - (ly-mz)]. Given a point S = u : v : w, Grinberg then defines the *S-Blaikie transform of O* as the Blaikie point of O and OS. The first barycentric of Z can be written as

      1/[yw(y+x) + zv(z+x) - yz(2u+v+w)].

.. container:: note-item

   Seet `Blaikie theorem in barycentrics. <http://mathforum.org/epigone/geometry-college/glexzhuntwyr>`__ (Darij Grinberg, 12/28/02)

.. toctree::
   :hidden:

   code
