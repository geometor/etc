:order: 693
:type: center
:canonical_id: X(693)
:dependencies: X(1), X(2), X(6), X(11), X(19), X(25), X(31), X(32), X(42), X(76), X(100), X(101), X(149), X(320), X(321), X(325), X(350), X(514), X(523), X(649), X(650), X(661), X(663), X(667), X(692), X(764), X(812), X(824), X(918), X(927), X(1086), X(1475), X(1783), X(17494), X(22160)

.. _X(693):

X(693) = ISOTOMIC CONJUGATE OF X(100)
=====================================

.. figure:: x-00693.svg
   :alt: X(693) = ISOTOMIC CONJUGATE OF X(100)
   :align: center

   **X(693) = ISOTOMIC CONJUGATE OF X(100)** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`(b - c)/a^{2} : (c - a)/b^{2} : (a - b)/c^{2}`

Barycentrics
~~~~~~~~~~~~

* :math:`(b - c)/a : (c - a)/b : (a - b)/c`
* :math:`|AP(1)| - |AU(1)| : :`
* directed distance from A to line :ref:`X(1) <X(1)>`\ \ :ref:`X(6) <X(6)>` : :

* **Kimberling (6, 9, 13) Search Value:** :math:`43.948021245883`

Notes
-----

.. container:: note-item

   :ref:`X(693) <X(693)>`: Let A\ :sub:`29`\ B\ :sub:`29`\ C\ :sub:`29` and A\ :sub:`30`\ B\ :sub:`30`\ C\ :sub:`30` be Gemini triangles 29 and 30, resp. Let E\ :sub:`29` and E\ :sub:`30` be the {ABC, Gemini 29}-circumconic and {ABC, Gemini 30}-circumconic, resp. Let A' be the intersection of the tangent to E\ :sub:`29` at A\ :sub:`29` and the tangent to E\ :sub:`30` at A\ :sub:`30`. Define B' and C' cyclically. The lines AA', BB', CC″ concur in :ref:`X(693) <X(693)>`. (:person:`Randy Hutson <randy-hutson>`, January 15, 2019)

Incidence
---------

:ref:`X(693) <X(693)>` lies and on these lines:

{:ref:`2 <X(2)>`, :ref:`650 <X(650)>`}, {:ref:`76 <X(76)>`, :ref:`764 <X(764)>`}, {:ref:`100 <X(100)>`, :ref:`927 <X(927)>`}, {:ref:`320 <X(320)>`, :ref:`350 <X(350)>`}, {:ref:`321 <X(321)>`, :ref:`824 <X(824)>`}, {:ref:`325 <X(325)>`, :ref:`523 <X(523)>`}, {:ref:`514 <X(514)>`, :ref:`661 <X(661)>`}, {:ref:`649 <X(649)>`, :ref:`812 <X(812)>`}

Relations
---------

* :ref:`X(693) <X(693)>` = :term:`isogonal conjugate <isogonal-conjugate>` of :ref:`X(692) <X(692)>`
* :ref:`X(693) <X(693)>` = :term:`isotomic conjugate <isotomic-conjugate>` of :ref:`X(100) <X(100)>`
* :ref:`X(693) <X(693)>` = :term:`complement <complement>` of X(17494)
* :ref:`X(693) <X(693)>` = :term:`anticomplement <anticomplement>` of :ref:`X(650) <X(650)>`
* :ref:`X(693) <X(693)>` = :term:`cevapoint <cevapoint>` of :ref:`X(2) <X(2)>` and :ref:`X(149) <X(149)>`
* :ref:`X(693) <X(693)>` = X(i)-:term:`cross conjugate <cross-conjugate>` of X(j) for these (i,j): (:ref:`11 <X(11)>`, :ref:`2 <X(2)>`), (:ref:`523 <X(523)>`, :ref:`514 <X(514)>`)
* :ref:`X(693) <X(693)>` = :term:`crosssum <crosssum>` of X(i) and X(j) for these (i,j): (:ref:`31 <X(31)>`, :ref:`667 <X(667)>`), (:ref:`42 <X(42)>`, :ref:`663 <X(663)>`), (:ref:`649 <X(649)>`, 1475)
* :ref:`X(693) <X(693)>` = :term:`crossdifference <crossdifference>` of every pair of points on line :ref:`X(31) <X(31)>`\ \ :ref:`X(32) <X(32)>`
* :ref:`X(693) <X(693)>` = :term:`trilinear pole <trilinear-pole>` of line :ref:`X(918) <X(918)>`\ X(1086)
* :ref:`X(693) <X(693)>` = pole wrt polar circle of :term:`trilinear polar <trilinear-polar>` of X(1783) (line :ref:`X(19) <X(19)>`\ \ :ref:`X(25) <X(25)>`)
* :ref:`X(693) <X(693)>` = polar conjugate of X(1783)
* :ref:`X(693) <X(693)>` = :ref:`X(6) <X(6)>`-:term:`isoconjugate <isoconjugate>` of :ref:`X(101) <X(101)>`
* :ref:`X(693) <X(693)>` = complement of polar conjugate of isogonal conjugate of X(22160)
* :ref:`X(693) <X(693)>` = perspector of side- and vertex-triangles of Gemini triangles 29 and 30

Construction
------------

.. literalinclude:: model.py
   :language: python
