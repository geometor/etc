:order: 13
:type: center
:canonical_id: X(13)
:aliases: FERMAT POINT, TORRICELLI POINT
:dependencies: X(1), X(2), X(3), X(4), X(5), X(6), X(11), X(14), X(15), X(16), X(17), X(18), X(30), X(48), X(61), X(62), X(76), X(80), X(98), X(99), X(115), X(125), X(148), X(202), X(203), X(226), X(262), X(265), X(275), X(298), X(299), X(303), X(381), X(383), X(395), X(396), X(470), X(472), X(484), X(523), X(531), X(532), X(533), X(616), X(617), X(618), X(619), X(621), X(623), X(634), X(635), X(671), X(1080), X(1081), X(1116), X(1251), X(1277), X(1478), X(1637), X(1640), X(1989), X(2394), X(6104), X(8371), X(9200), X(9201), X(9202), X(14446), X(14447), X(30574), X(34317), X(42730), X(42731), X(42732), X(42733), X(42734), X(42735), X(42736), X(42737), X(42738), X(42740)

.. _X(13):
.. _FirstIsogonicCenter:

X(13) = 1st ISOGONIC CENTER (FERMAT POINT, TORRICELLI POINT)
============================================================

.. figure:: x-00013.svg
   :alt: X(13) = 1st ISOGONIC CENTER (FERMAT POINT, TORRICELLI POINT)
   :align: center

   **X(13) = 1st ISOGONIC CENTER (FERMAT POINT, TORRICELLI POINT)** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`\csc(A + \pi /3) : \csc(B + \pi /3) : \csc(C + \pi /3)`
* :math:`\sec(A - \pi /6) : \sec(B - \pi /6) : \sec(C - \pi /6)`

Barycentrics
~~~~~~~~~~~~

* :math:`a^{4} - 2(b^{2} - c^{2})^{2} + a^{2}(b^{2} + c^{2} + 4*\sqrt{3}*Area(ABC)) : :`
* :math:`(SA + \sqrt{3} S) (SB + SC) + 4 SB SC : :`

Tripolars
~~~~~~~~~

* :math:`1/(a^4+a^2 b^2-2 b^4+a^2 c^2+4 b^2 c^2-2 c^4+2 \sqrt{3} a^2 S) : :`

* **Kimberling (6, 9, 13) Search Value:** :math:`0.075945151805`

Linear Combinations
-------------------

* :ref:`X(13) <X(13)>` = 3\ :sup:`1/2`\ (r\ :sup:`2` + 2rR + s\ :sup:`2`)\*\ :ref:`X(1) <X(1)>` - 6r(3\ :sup:`1/2`\ R - 2s)\*\ :ref:`X(2) <X(2)>` - 2r(3\ :sup:`1/2`\ r + 3s)\*\ :ref:`X(3) <X(3)>`
* (:person:`Peter Moses <peter-moses>`, April 2, 2013)

Notes
-----

.. container:: note-item

   Construct the equilateral triangle BA'C having base BC and vertex A' on the negative side of BC; similarly construct equilateral triangles CB'A and AC'B based on the other two sides. The lines AA', BB', CC' concur in :ref:`X(13) <X(13)>`. If each of the angles A, B, C is < 2π/3, then :ref:`X(13) <X(13)>` is the only center X for which the angles BXC, CXA, AXB are equal, and :ref:`X(13) <X(13)>` minimizes the sum \|AX\| + \|BX\| + \|CX\|. The :term:`antipedal triangle <antipedal-triangle>` of :ref:`X(13) <X(13)>` is equilateral.

.. container:: note-item

   If, however, A> 2π/3, then the Fermat point, defined geometrically as the minimizer of \|AX\| + \|BX\| + \|CX\|, is not the 1st isogonic center (which is defined by the above trilinears). Trilinears for the Fermat point when A> 2π/3 are simply 1:0:0. To represent the Fermat point in the form f(a,b,c) : f(b,c,a) : f(c,a,b), one must use Boolean variables, as shown at `Fermat point. <http://en.wikipedia.org/wiki/Fermat_point>`__

.. container:: note-item

   The Evans conic is introduced in **Evans, Lawrence S.,** "A Conic Through Six :term:`Triangle Centers <triangle-center>`," `Forum Geometricorum <http://forumgeom.fau.edu/FG2002volume2/FG200211index.html>`__ 2 (2002) 89-92.

.. container:: note-item

   Let NaNbNc, Na'Nb'Nc' be the outer and inner Napoleon triangles, respectively. Let A' be the :term:`isogonal conjugate <isogonal-conjugate>` of Na', wrt NaNbNc, and define B' and C' cyclically. The lines NaA', NbB', NcC' concur in :ref:`X(13) <X(13)>`. (:person:`Randy Hutson <randy-hutson>`, January 29, 2015)

.. container:: note-item

   Let P be a point inside triangle ABC such that the line AP bisects angle BPC, and NBP bisets CPA, and CP bisects APB. Then P = :ref:`X(13) <X(13)>`. The locus of P such that AP bisects BPC is the circumcubic given by the barycentric equation c\ :sup:`2`\ xy\ :sup:`2` - b\ :sup:`2`\ xz\ :sup:`2` + (a\ :sup:`2` - b\ :sup:`2` + c\ :sup:`2`)y\ :sup:`2`\ z - (a\ :sup:`2` + b\ :sup:`2` - c\ :sup:`2`)yz\ :sup:`2` = 0, and the other two cubics are given cyclically. :person:`Bernard Gibert <bernard-gibert>` discusses these cubics as K053A, K053B, K053C; see `Apollonian strophoids. <https://bernard-gibert.pagesperso-orange.fr/Exemples/k053.html>`__ (Paul Hanna and Peter Moses, August 6, 2017)

.. container:: note-item

   The line :ref:`X(13) <X(13)>`\ \ :ref:`X(15) <X(15)>` is parallel to the Euler line, and the distance between the two lines is (SB - SC)(SC - SA)(SA - SB)/\|(cot(ω) + 3\ :sup:`1/2`)\|\*((E - 8F)S\ :sup:`2`)\ :sup:`1/2`. (:person:`Kiminari Shinagawa <kiminari-shinagawa>`, February 20, 2018)

.. container:: note-item

   Let A'B'C' be the outer Napoleon triangle and A″B″C″ the inner Napoleon triangle. Let A\* be the isogonal conjugate, wrt A'B'C', of A″, and define B\* and C\* cyclically. The lines A'A\*, B'B\*, C'C\* concur in :ref:`X(13) <X(13)>`. (Randy Hutson, December 2, 2017)

.. container:: note-item

   Let F be :ref:`X(13) <X(13)>` or :ref:`X(14) <X(14)>`. Let L and L' be lines through F such that the angle between them is π/3. Let L\ :sub:`BC` = L∩BC, and define L\ :sub:`CA` and L\ :sub:`AB` cyclically. Let L':sub:`BC` = L'∩BC, and define L':sub:`CA` and L':sub:`AB` cyclically. The lines L\ :sub:`BC`\ L':sub:`CA`, L\ :sub:`CA`\ L':sub:`AB`, L\ :sub:`AB`\ L':sub:`BC` concur. (:person:`Dao Thanh Oai <dao-thanh-oai>`, 2014)

.. container:: note-item

   Let F be :ref:`X(13) <X(13)>` or :ref:`X(14) <X(14)>`. Let A\ :sub:`0`, B\ :sub:`0`, C\ :sub:`0` be points on BC, CA, AB, respectively, such that the directed angles FA\ :sub:`0`-to-FC\ :sub:`0` = π/3 and FC\ :sub:`0`-to-FB\ :sub:`0` = π/3. The points A\ :sub:`0`, B\ :sub:`0`, C\ :sub:`0` are collinear. (Dao Thanh Oai, 2014)

.. container:: note-item

   Video showing circular porisim-orbits of :ref:`X(13) <X(13)>`, :ref:`X(14) <X(14)>`, :ref:`X(15) <X(15)>`, and :ref:`X(16) <X(16)>`: `3-Periodics in a Concentric Homothetic Poncelet Pair: Circular Loci of Four Triangle Centers <https://youtu.be/ZwTfwaJJitE>`__. (:person:`Dan Reznik <dan-reznik>`, August 9, 2020) See also `Loci of Centers of Ellipse-Mounted Triangles <https://dan-reznik.github.io/ellipse-mounted-loci-p5js/?sc=16.495&a=3.000&asp=anim&amn=1.01&amx=4&lc1=trilins&Xn1=13&mt1=homothetic&dr1=true&lc2=trilins&Xn2=14&mt2=homothetic&lc3=trilins&Xn3=15&mt3=homothetic&lc4=trilins&Xn4=16&mt4=homothetic>`__. (Dan Reznik, August 26, 2020)

.. container:: note-item

   If P is a point not on the line :ref:`X(13) <X(13)>`\ \ :ref:`X(14) <X(14)>`, then the circle {P, :ref:`X(13) <X(13)>`, :ref:`X(14) <X(14)>`}} is orthogonal to the orthocentroidal circle. (Peter Moses, April 22, 2021)

.. container:: note-item

   Several notable circles pass through :ref:`X(13) <X(13)>` and :ref:`X(14) <X(14)>`. For each circle listed here, the appearance of (i; [name], [list]) means that the center is X(i), and the points with listed indices lie on the circle:

      * (X(1116); Lester circle, :ref:`3 <X(3)>`, :ref:`5 <X(5)>`, :ref:`13 <X(13)>`, :ref:`14 <X(14)>`, 1117, 5671, 14854, 15475, 15535, 15536, 15537, 15538, 15539, 15540, 15541, 15542, 15543, 15544, 15545, 15546, 15547, 15548, 15549, 15550, 15551, 15552, 15553, 15554, 15555, 34365)
      * (X(1637); Dao-Moses-Telv circle; :ref:`13 <X(13)>`, :ref:`14 <X(14)>`, 5000, 5001, 6104, 6105, 6106, 6107, 6108, 6109, 6110, 6111, 24007, 24008)
      * (X(1640); :ref:`13 <X(13)>`, :ref:`14 <X(14)>`, 10653, 10654, 32618, 32619)
      * (X(8371); Hutson-Parry circle, :ref:`2 <X(2)>`, :ref:`13 <X(13)>`, :ref:`14 <X(14)>`, 111, 476, 5466, 5640, 6032, 6792, 7698, 9140, 9159, 11628, 11639, 11640, 13636, 13722, 14846, 14932, 34320)
      * (X(9200); :ref:`13 <X(13)>`, :ref:`14 <X(14)>`, :ref:`16 <X(16)>`, 5623, 11586, 30439)
      * (X(9201); :ref:`13 <X(13)>`, :ref:`14 <X(14)>`, :ref:`15 <X(15)>`, 5624, 15743, 30440)
      * (X(9202); :ref:`13 <X(13)>`, :ref:`14 <X(14)>`, :ref:`16 <X(16)>`, 5623, 11586, 30439)
      * (X(14446); :ref:`13 <X(13)>`, :ref:`14 <X(14)>`, 5616, 5668, 6779, 8172, 11600, 38943)
      * (X(14447); :ref:`13 <X(13)>`, :ref:`14 <X(14)>`, 5612, 5669, 6780, 8173, 11601, 38944)
      * (X(30574); :ref:`13 <X(13)>`, :ref:`14 <X(14)>`, :ref:`80 <X(80)>`,484, 3464, 5540, 5902, 34301, 37718)
      * (X(42731); :ref:`13 <X(13)>`, :ref:`14 <X(14)>`, 112, 1141, 1157, 5667, 5890, 6761, 14644, 14651)
      * (X(42732); :ref:`13 <X(13)>`, :ref:`14 <X(14)>`, 112, 1141, 1157, 5667, 5890, 6761, 14644, 14651)
      * (X(42733); :ref:`4 <X(4)>`, :ref:`13 <X(13)>`, :ref:`14 <X(14)>`, 2132, 2394, 6794, 22265, 34298)
      * (X(42734); :ref:`13 <X(13)>`, :ref:`14 <X(14)>`, 616, 621, 5675, 16260, 39133)
      * (X(42735); :ref:`13 <X(13)>`, :ref:`14 <X(14)>`, 617, 621, 5674, 16259, 39132)
      * (X(42736); :ref:`13 <X(13)>`, :ref:`14 <X(14)>`, 125, 1637, 11657, 14847, 34310)
      * (X(42737); :ref:`13 <X(13)>`, :ref:`14 <X(14)>`, 110, 3448, 34306, 34308)
      * (X(42738); :ref:`13 <X(13)>`, :ref:`14 <X(14)>`, :ref:`98 <X(98)>`, 11005, 14223, 23969)
      * (X(42730); :ref:`13 <X(13)>`, :ref:`14 <X(14)>`, :ref:`74 <X(74)>`, 5627, 5670, 18331)
      * (X(42740); Dao-Parry circle of :ref:`X(1) <X(1)>`, :ref:`1 <X(1)>`, :ref:`13 <X(13)>`, :ref:`14 <X(14)>`, :ref:`79 <X(79)>`, 5677, 42748, 42749)

   Related circles are discussed in trhe preamble just before X(42740).

.. container:: note-item

   :ref:`X(13) <X(13)>` is the {:ref:`X(6) <X(6)>`,X(381)}-harmonic conjugate of :ref:`X(14) <X(14)>`.

Incidence
---------

:ref:`X(13) <X(13)>` lies on the Neuberg cubic and on these lines:

{:ref:`2 <X(2)>`, :ref:`16 <X(16)>`}, {:ref:`3 <X(3)>`, :ref:`17 <X(17)>`}, {:ref:`4 <X(4)>`, :ref:`61 <X(61)>`}, {:ref:`5 <X(5)>`, :ref:`18 <X(18)>`}, {:ref:`6 <X(6)>`, :ref:`14 <X(14)>`}, {:ref:`11 <X(11)>`, 202}, {:ref:`15 <X(15)>`, :ref:`30 <X(30)>`}, {:ref:`76 <X(76)>`, 299}, {:ref:`80 <X(80)>`, 1251}, {:ref:`98 <X(98)>`, 1080}, {:ref:`99 <X(99)>`, 303}, {148, 617}, {203, 1478}, {226, 1081}, {262, 383}, {275, 472}, {298, 532}, {484, 1277}, {531, 671}, {533, 621}, {634, 635}

Relations
---------

* :ref:`X(13) <X(13)>` = reflection of X(i) in X(j) for these (i,j): (:ref:`14 <X(14)>`, 115), (:ref:`15 <X(15)>`, 396), (:ref:`99 <X(99)>`, 619), (298, 623), (616, 618)
* :ref:`X(13) <X(13)>` = isogonal conjugate of :ref:`X(15) <X(15)>`
* :ref:`X(13) <X(13)>` = :term:`isotomic conjugate <isotomic-conjugate>` of X(298)
* :ref:`X(13) <X(13)>` = circumcircle-inverse of X(6104)
* :ref:`X(13) <X(13)>` = orthocentroidal-circle inverse of :ref:`X(14) <X(14)>`
* :ref:`X(13) <X(13)>` = :term:`complement <complement>` of X(616)
* :ref:`X(13) <X(13)>` = :term:`anticomplement <anticomplement>` of X(618)
* :ref:`X(13) <X(13)>` = :term:`cevapoint <cevapoint>` of :ref:`X(15) <X(15)>` and :ref:`X(62) <X(62)>`
* :ref:`X(13) <X(13)>` = X(i)-:term:`cross conjugate <cross-conjugate>` of X(j) for these (i,j): (:ref:`15 <X(15)>`, :ref:`18 <X(18)>`), (:ref:`30 <X(30)>`, :ref:`14 <X(14)>`), (396, :ref:`2 <X(2)>`)
* :ref:`X(13) <X(13)>` = :term:`trilinear pole <trilinear-pole>` of line X(395)X(523) (polar of X(470) wrt polar circle)
* :ref:`X(13) <X(13)>` = pole wrt polar circle of :term:`trilinear polar <trilinear-polar>` of X(470)
* :ref:`X(13) <X(13)>` = :ref:`X(48) <X(48)>`-:term:`isoconjugate <isoconjugate>` (polar conjugate) of X(470)
* :ref:`X(13) <X(13)>` = :term:`antigonal image <antigonal-image>` of :ref:`X(14) <X(14)>`
* :ref:`X(13) <X(13)>` = reflection of :ref:`X(14) <X(14)>` in line X(115)X(125)
* :ref:`X(13) <X(13)>` = :ref:`X(15) <X(15)>`-of-4th-Brocard-triangle
* :ref:`X(13) <X(13)>` = :ref:`X(15) <X(15)>`-of-orthocentroidal-triangle
* :ref:`X(13) <X(13)>` = orthocorrespondent of :ref:`X(13) <X(13)>`
* :ref:`X(13) <X(13)>` = homothetic center of outer Napoleon triangle and antipedal triangle of :ref:`X(13) <X(13)>`
* :ref:`X(13) <X(13)>` = inner-Napoleon-to-outer-Napoleon :term:`similarity image <similarity-image>` of :ref:`X(15) <X(15)>`
* :ref:`X(13) <X(13)>` = outer-Napoleon-isogonal conjugate of :ref:`X(3) <X(3)>`
* :ref:`X(13) <X(13)>` = outer-Napoleon-to-inner-Napoleon similarity image of :ref:`X(14) <X(14)>`
* :ref:`X(13) <X(13)>` = orthocenter of :ref:`X(14) <X(14)>`\ \ :ref:`X(98) <X(98)>`\ X(2394)
* :ref:`X(13) <X(13)>` = :ref:`X(15) <X(15)>`-of-pedal-triangle of :ref:`X(13) <X(13)>`
* :ref:`X(13) <X(13)>` = {X(265),X(1989)}-harmonic Conjugate of :ref:`X(14) <X(14)>`
* :ref:`X(13) <X(13)>` = homothetic center of (equilateral) antipedal triangle of :ref:`X(13) <X(13)>` and triangle formed by circumcenters of BC\ :ref:`X(13) <X(13)>`, CA\ :ref:`X(13) <X(13)>`, AB\ :ref:`X(13) <X(13)>`
* :ref:`X(13) <X(13)>` = homothetic center of triangle formed by circumcenters of BC\ :ref:`X(14) <X(14)>`, CA\ :ref:`X(14) <X(14)>`, AB\ :ref:`X(14) <X(14)>` and triangle formed by nine-point centers of BC\ :ref:`X(13) <X(13)>`, CA\ :ref:`X(13) <X(13)>`, AB\ :ref:`X(13) <X(13)>`
* :ref:`X(13) <X(13)>` = Cundy-Parry Phi transform of :ref:`X(17) <X(17)>`
* :ref:`X(13) <X(13)>` = Cundy-Parry Psi transform of :ref:`X(61) <X(61)>`
* :ref:`X(13) <X(13)>` = Kosnita(:ref:`X(13) <X(13)>`,\ :ref:`X(1) <X(1)>`) point
* :ref:`X(13) <X(13)>` = Kosnita(:ref:`X(13) <X(13)>`,\ :ref:`X(13) <X(13)>`) point
* :ref:`X(13) <X(13)>` = Thomson-isogonal conjugate of X(34317)

Construction
------------

.. literalinclude:: model.py
   :language: python
