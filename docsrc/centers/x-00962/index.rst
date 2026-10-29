:order: 962
:type: center
:canonical_id: X(962)
:dependencies: X(1), X(2), X(3), X(4), X(7), X(8), X(20), X(30), X(40), X(55), X(65), X(77), X(145), X(149), X(151), X(165), X(175), X(176), X(278), X(309), X(382), X(392), X(411), X(412), X(443), X(484), X(497), X(499), X(515), X(942), X(944), X(946), X(952), X(963), X(1058), X(1125), X(1482), X(20991), X(22124)

.. _X(962):

X(962) = LONGUET-HIGGINS POINT
==============================

.. figure:: x-00962.svg
   :alt: X(962) = LONGUET-HIGGINS POINT
   :align: center

   **X(962) = LONGUET-HIGGINS POINT** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`bc[a^{4} + 2a^{3}(b + c) - 4a^{2}bc - (b + c)(b - c)^{2}(2a + b + c)] : :`
* :math:`\sin B \sin C + \cos B + \cos C - \cos A - 1 : :`
* :math:`\cos B + \cos C + \cos B \cos C - 1 : :`
* :math:`1 - 2 \cos^{2}(B/2) \cos^{2}(C/2) : :`
* :math:`\cos A' : :`, where A' is the angle formed by the tangents from :ref:`X(1) <X(1)>` to the A-excircle

* **Kimberling (6, 9, 13) Search Value:** :math:`-15.860728180405`

Notes
-----

.. container:: note-item

   :ref:`X(962) <X(962)>` is shown in **Michael S. Longuet-Higgins,** "On the principal centers of a triangle," *Elemente der Mathematik* 56 (2001) 122-129, to complete a simple pattern of collinearities.

.. container:: note-item

   Let I = :ref:`X(1) <X(1)>` and H = :ref:`X(4) <X(4)>` in a triangle ABC. Let L\ :sub:`b` be the perpendicular to B at I, and let I\ :sub:`c` be the perpendicular to CI at I. Let A\ :sub:`b` = L\ :sub:`b`\ ∩AH and A\ :sub:`c` = L\ :sub:`c`\ ∩AH. Let U be the circle {I, A\ :sub:`b`, A\ :sub:`c`}}. Let M\ :sub:`b` be the point, other than I, where BI meets U, and let M\ :sub:`c` be the point, other than I, where CI meets U. Let ℓ\ :sub:`a` be the line M\ :sub:`b`\ M\ :sub:`c`, and define ℓ\ :sub:`b` and ℓ\ :sub:`c` cyclically. The lines ℓ\ :sub:`a`, ℓ\ :sub:`b`, ℓ\ :sub:`c` concur in :ref:`X(962) <X(962)>`. (:person:`Angel Montesdeoca <angel-montesdeoca>`, March 12, 2020)

.. container:: note-item

   :ref:`X(962) <X(962)>` is the radical center of the circles centered at A, B, C, with respective

   radii \|CA\| + \|AB\|, \|AB\| + \|BC\|, \|BC\| + \|CA\|. See

.. container:: note-item

   **Floor van Lamoen,** Problem 10734, *American Mathematical Monthly* 107 (2000) 658-659.

Incidence
---------

:ref:`X(962) <X(962)>` lies and on these lines:

{:ref:`1 <X(1)>`, :ref:`7 <X(7)>`}, {:ref:`2 <X(2)>`, :ref:`40 <X(40)>`}, {:ref:`4 <X(4)>`, :ref:`8 <X(8)>`}, {:ref:`30 <X(30)>`, :ref:`944 <X(944)>`}, {:ref:`55 <X(55)>`, :ref:`411 <X(411)>`}, {:ref:`65 <X(65)>`, :ref:`497 <X(497)>`}, {:ref:`145 <X(145)>`, :ref:`515 <X(515)>`}, {:ref:`149 <X(149)>`, :ref:`151 <X(151)>`}, {:ref:`165 <X(165)>`, 1125}, {:ref:`278 <X(278)>`, :ref:`412 <X(412)>`}, {:ref:`382 <X(382)>`, :ref:`952 <X(952)>`}, {:ref:`392 <X(392)>`, :ref:`443 <X(443)>`}, {:ref:`484 <X(484)>`, :ref:`499 <X(499)>`}, {:ref:`942 <X(942)>`, 1058}

Relations
---------

* :ref:`X(962) <X(962)>` = reflection of X(i) in X(j) for these (i,j): (:ref:`8 <X(8)>`, :ref:`4 <X(4)>`), (:ref:`20 <X(20)>`, :ref:`1 <X(1)>`), (:ref:`40 <X(40)>`, :ref:`946 <X(946)>`), (:ref:`944 <X(944)>`, 1482)
* :ref:`X(962) <X(962)>` = :term:`isogonal conjugate <isogonal-conjugate>` of :ref:`X(963) <X(963)>`
* :ref:`X(962) <X(962)>` = :term:`anticomplement <anticomplement>` of :ref:`X(40) <X(40)>`
* :ref:`X(962) <X(962)>` = :term:`isotomic conjugate <isotomic-conjugate>` of isogonal conjugate of X(20991)
* :ref:`X(962) <X(962)>` = polar conjugate of isogonal conjugate of X(22124)
* :ref:`X(962) <X(962)>` = :ref:`X(309) <X(309)>`-:term:`Ceva conjugate <ceva-conjugate>` of :ref:`X(2) <X(2)>`
* :ref:`X(962) <X(962)>` = {:ref:`X(175) <X(175)>`,\ :ref:`X(176) <X(176)>`}-harmonic conjugate of :ref:`X(77) <X(77)>`
* :ref:`X(962) <X(962)>` = :ref:`X(3) <X(3)>`-of-2nd-Conway-triangle
* :ref:`X(962) <X(962)>` = perspector of 2nd Conway triangle and Gemini triangle 29
* :ref:`X(962) <X(962)>` = mixtilinear-incentral-to-mixtilinear-excentral :term:`similarity image <similarity-image>` of :ref:`X(7) <X(7)>`

Construction
------------

.. literalinclude:: model.py
   :language: python
