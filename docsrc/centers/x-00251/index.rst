:order: 251
:type: center
:canonical_id: X(251)
:dependencies: X(2), X(6), X(22), X(23), X(32), X(37), X(48), X(82), X(83), X(110), X(111), X(112), X(141), X(184), X(263), X(308), X(385), X(427), X(523), X(609), X(614), X(689), X(694), X(699), X(1235), X(1369), X(8024), X(21248)

.. _X(251):

X(251) = ISOGONAL CONJUGATE OF X(141)
=====================================

.. figure:: x-00251.svg
   :alt: X(251) = ISOGONAL CONJUGATE OF X(141)
   :align: center

   **X(251) = ISOGONAL CONJUGATE OF X(141)** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`a^{2}\csc(A + \omega ) : b^{2}\csc(B + \omega ) : c^{2}\csc(C + \omega ), = a/(b^{2} + c^{2}) : b/(c^{2} + a^{2}) : c/(a^{2} + b^{2})`

* **Kimberling (6, 9, 13) Search Value:** :math:`0.572649002745`

Notes
-----

.. container:: note-item

   Barycentrics a\ :sup:`3`\ csc(A + ω) : b\ :sup:`3`\ csc(B + ω) : c\ :sup:`3`\ csc(C + ω)

.. container:: note-item

   Let K be the symmedian point of ABC and let A' be the symmedian point of the triangle BCK; define B' and C' cyclically. The lines AA', BB', CC' concur in :ref:`X(251) <X(251)>`. (:person:`Randy Hutson <randy-hutson>`, 9/23/2011)

.. container:: note-item

   Let A5'B5'C5' be the 5th anti-Brocard triangle. The radical center of the circumcircles of BCA5', CAB5', ABC5' is :ref:`X(251) <X(251)>`. (Randy Hutson, July 20, 2016)

Incidence
---------

:ref:`X(251) <X(251)>` lies and on these lines:

{:ref:`2 <X(2)>`, :ref:`32 <X(32)>`}, {:ref:`6 <X(6)>`, :ref:`22 <X(22)>`}, {:ref:`37 <X(37)>`, :ref:`82 <X(82)>`}, {:ref:`110 <X(110)>`, :ref:`694 <X(694)>`}, {:ref:`112 <X(112)>`, :ref:`427 <X(427)>`}, {:ref:`184 <X(184)>`, :ref:`263 <X(263)>`}, {:ref:`308 <X(308)>`, :ref:`385 <X(385)>`}, {:ref:`609 <X(609)>`, :ref:`614 <X(614)>`}, {:ref:`689 <X(689)>`, :ref:`699 <X(699)>`}

Relations
---------

* :ref:`X(251) <X(251)>` = :term:`isogonal conjugate <isogonal-conjugate>` of :ref:`X(141) <X(141)>`
* :ref:`X(251) <X(251)>` = :term:`complement <complement>` of X(1369)
* :ref:`X(251) <X(251)>` = :term:`anticomplement <anticomplement>` of X(21248)
* :ref:`X(251) <X(251)>` = :term:`cevapoint <cevapoint>` of :ref:`X(6) <X(6)>` and :ref:`X(32) <X(32)>`
* :ref:`X(251) <X(251)>` = X(i)-:term:`cross conjugate <cross-conjugate>` of X(j) for these (i,j): (:ref:`6 <X(6)>`, :ref:`83 <X(83)>`), (:ref:`23 <X(23)>`, :ref:`111 <X(111)>`), (:ref:`523 <X(523)>`, :ref:`112 <X(112)>`)
* :ref:`X(251) <X(251)>` = :term:`isotomic conjugate <isotomic-conjugate>` of X(8024)
* :ref:`X(251) <X(251)>` = similitude center of ABC and 1st orthosymmedial triangle
* :ref:`X(251) <X(251)>` = pole wrt polar circle of :term:`trilinear polar <trilinear-polar>` of X(1235)
* :ref:`X(251) <X(251)>` = :ref:`X(48) <X(48)>`-:term:`isoconjugate <isoconjugate>` (polar conjugate) of X(1235)
* :ref:`X(251) <X(251)>` = barycentric product of vertices of circummedial triangle
* :ref:`X(251) <X(251)>` = perspector of ABC and cross-triangle of ABC and circummedial triangle
* :ref:`X(251) <X(251)>` = Kosnita(:ref:`X(6) <X(6)>`,\ :ref:`X(6) <X(6)>`) point
* :ref:`X(251) <X(251)>` = homothetic center of 1st orthosymmedial and 1st anti-orthosymmedial triangles

Construction
------------

.. literalinclude:: model.py
   :language: python
