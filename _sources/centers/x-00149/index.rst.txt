:order: 149
:type: center
:canonical_id: X(149)
:dependencies: X(2), X(3), X(4), X(7), X(8), X(11), X(20), X(80), X(100), X(104), X(144), X(145), X(151), X(153), X(377), X(404), X(496), X(513), X(962), X(1058), X(1156), X(1320), X(1484), X(3446), X(8047)

.. _X(149):

X(149) = REFLECTION OF X(20) IN X(104)
======================================

.. figure:: x-00149.svg
   :alt: X(149) = REFLECTION OF X(20) IN X(104)
   :align: center

   **X(149) = REFLECTION OF X(20) IN X(104)** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`f(a,b,c) : f(b,c,a) : f(c,a,b)`, where, f(a,b,c) = bc[b\ :sup:`3` + c\ :sup:`3` - a\ :sup:`3` + (a\ :sup:`2` - bc)(b + c) + a(bc - b\ :sup:`2` - c\ :sup:`2`)]

* **Kimberling (6, 9, 13) Search Value:** :math:`2.684434107515`

Notes
-----

.. container:: note-item

   Barycentrics g(a,b,c) : g(b,c,a) : g(c,a,b), where

      * g(a,b,c) = b\ :sup:`3` + c\ :sup:`3` - a\ :sup:`3` + (a\ :sup:`2` - bc)(b + c) + a(bc - b\ :sup:`2` - c\ :sup:`2`)

.. container:: note-item

   Let A' be the reflection of the midpoint of segment BC in :ref:`X(11) <X(11)>`, and define B' and C' cyclically. The lines AA', BB', CC' concur in :ref:`X(149) <X(149)>`. (:person:`Randy Hutson <randy-hutson>`, 9/23/2011)

.. container:: note-item

   :ref:`X(149) <X(149)>` is the {:ref:`X(11) <X(11)>`,\ :ref:`X(100) <X(100)>`}-harmonic conjugate of :ref:`X(2) <X(2)>`. For a list of harmonic conjugates, click **Tables** at the top of this page.

Incidence
---------

:ref:`X(149) <X(149)>` lies on the anticomplementary circle and on these lines:

{:ref:`2 <X(2)>`, :ref:`11 <X(11)>`}, {:ref:`4 <X(4)>`, :ref:`145 <X(145)>`}, {:ref:`8 <X(8)>`, :ref:`80 <X(80)>`}, {:ref:`20 <X(20)>`, :ref:`104 <X(104)>`}, {:ref:`151 <X(151)>`, :ref:`962 <X(962)>`}, {:ref:`377 <X(377)>`, 1058}, {:ref:`404 <X(404)>`, :ref:`496 <X(496)>`}

Relations
---------

* :ref:`X(149) <X(149)>` = reflection of X(i) in X(j) for these (i,j): (:ref:`3 <X(3)>`, 1484), (:ref:`8 <X(8)>`, :ref:`80 <X(80)>`), (:ref:`20 <X(20)>`, :ref:`104 <X(104)>`), (:ref:`100 <X(100)>`, :ref:`11 <X(11)>`), (:ref:`144 <X(144)>`, 1156), (:ref:`145 <X(145)>`, 1320), (:ref:`153 <X(153)>`, :ref:`4 <X(4)>`)
* :ref:`X(149) <X(149)>` = :term:`isogonal conjugate <isogonal-conjugate>` of X(3446)
* :ref:`X(149) <X(149)>` = :term:`isotomic conjugate <isotomic-conjugate>` of X(8047)
* :ref:`X(149) <X(149)>` = :term:`anticomplementary conjugate <anticomplementary-conjugate>` of :ref:`X(513) <X(513)>`
* :ref:`X(149) <X(149)>` = :term:`trilinear pole <trilinear-pole>` wrt :term:`anticomplementary triangle <anticomplementary-triangle>` of line :ref:`X(7) <X(7)>`\ \ :ref:`X(8) <X(8)>`
* :ref:`X(149) <X(149)>` = center of conic through :ref:`X(7) <X(7)>`, :ref:`X(8) <X(8)>`, and the extraversions of :ref:`X(8) <X(8)>`
* :ref:`X(149) <X(149)>` = :ref:`X(100) <X(100)>`-of-anticomplementary-triangle
* :ref:`X(149) <X(149)>` = homothetic center of 2nd Schiffler triangle and polar triangle of AC-incircle

Construction
------------

.. literalinclude:: model.py
   :language: python
