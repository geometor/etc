:order: 68
:type: center
:canonical_id: X(68)
:dependencies: X(2), X(3), X(4), X(5), X(6), X(11), X(20), X(24), X(26), X(30), X(52), X(54), X(63), X(64), X(65), X(66), X(73), X(74), X(91), X(96), X(115), X(125), X(136), X(155), X(161), X(186), X(254), X(290), X(315), X(317), X(343), X(511), X(520), X(525), X(568), X(924), X(973), X(1060), X(1069), X(1147), X(6753), X(8745), X(34287)

.. _X(68):

X(68) = PRASOLOV POINT
======================

.. figure:: x-00068.svg
   :alt: X(68) = PRASOLOV POINT
   :align: center

   **X(68) = PRASOLOV POINT** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`\cos A \sec 2A : \cos B \sec 2B : \cos C \sec 2C`

Barycentrics
~~~~~~~~~~~~

* :math:`\tan 2A : \tan 2B : \tan 2C`
* :math:`(b^2 + c^2 - a^2)/(a^4 + b^4 + c^4 - 2a^2b^2 - 2a^2c^2) : :`

* **Kimberling (6, 9, 13) Search Value:** :math:`1.370063903568`

Notes
-----

.. container:: note-item

   Let A'B'C' be the 2nd Euler triangle. The lines AA', BB', CC' concur in :ref:`X(68) <X(68)>`, as proved in **V. V. Prasolov,** *Zadachi po planimetrii,* Moscow, 4th edition, 2001.

.. container:: note-item

   Coordinates for :ref:`X(68) <X(68)>` can be obtained easily from the Ceva ratios given his Prasolov's proof of concurrence.

.. container:: note-item

   Let Oa be the circle centered at the A-vertex of the :term:`orthic triangle <orthic-triangle>` and passing through A; define Ob and Oc cyclically. Then :ref:`X(68) <X(68)>` is the radical center of Oa, Ob, Oc. (:person:`Randy Hutson <randy-hutson>`, November 2, 2017)

.. container:: note-item

   The :ref:`X(3) <X(3)>`-Fuhrmann triangle is inversely similar to ABC, with similitude center :ref:`X(3) <X(3)>`, and perspective to ABC at :ref:`X(68) <X(68)>`. (Randy Hutson, November 3, 2017)

Incidence
---------

:ref:`X(68) <X(68)>` lies and on these lines:

{:ref:`2 <X(2)>`, :ref:`54 <X(54)>`}, {:ref:`3 <X(3)>`, 343}, {:ref:`4 <X(4)>`, :ref:`52 <X(52)>`}, {:ref:`5 <X(5)>`, :ref:`6 <X(6)>`}, {:ref:`11 <X(11)>`, 1069}, {:ref:`20 <X(20)>`, :ref:`74 <X(74)>`}, {:ref:`26 <X(26)>`, 161}, {:ref:`30 <X(30)>`, :ref:`64 <X(64)>`}, {:ref:`65 <X(65)>`, :ref:`91 <X(91)>`}, {:ref:`66 <X(66)>`, 511}, {:ref:`73 <X(73)>`, 1060}, {136, 254}, {290, 315}, {568, 973}

Relations
---------

* :ref:`X(68) <X(68)>` = reflection of X(155) in :ref:`X(5) <X(5)>`
* :ref:`X(68) <X(68)>` = :term:`isogonal conjugate <isogonal-conjugate>` of :ref:`X(24) <X(24)>`
* :ref:`X(68) <X(68)>` = :term:`isotomic conjugate <isotomic-conjugate>` of X(317)
* :ref:`X(68) <X(68)>` = :term:`anticomplement <anticomplement>` of X(1147)
* :ref:`X(68) <X(68)>` = :ref:`X(96) <X(96)>`-:term:`Ceva conjugate <ceva-conjugate>` of :ref:`X(3) <X(3)>`
* :ref:`X(68) <X(68)>` = :term:`cevapoint <cevapoint>` of X(i) and X(j) for these (i,j): (:ref:`6 <X(6)>`, 161), (125, 520)
* :ref:`X(68) <X(68)>` = X(115)-:term:`cross conjugate <cross-conjugate>` of X(525)
* :ref:`X(68) <X(68)>` = pedal antipodal perspector of :ref:`X(4) <X(4)>`
* :ref:`X(68) <X(68)>` = pedal antipodal perspector of X(186)
* :ref:`X(68) <X(68)>` = :ref:`X(63) <X(63)>`-:term:`isoconjugate <isoconjugate>` of X(8745)
* :ref:`X(68) <X(68)>` = :term:`crossdifference <crossdifference>` of every pair of points on line X(924)X(6753)
* :ref:`X(68) <X(68)>` = trilinear product of vertices of :ref:`X(3) <X(3)>`-anti-altimedial triangle
* :ref:`X(68) <X(68)>` = orthic-to-ABC :term:`barycentric image <barycentric-image>` of :ref:`X(52) <X(52)>`
* :ref:`X(68) <X(68)>` = :term:`cyclocevian conjugate <cyclocevian-conjugate>` of X(34287)

Construction
------------

.. literalinclude:: model.py
   :language: python
