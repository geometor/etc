:order: 153
:type: center
:canonical_id: X(153)
:dependencies: X(1), X(2), X(3), X(4), X(7), X(11), X(20), X(80), X(100), X(104), X(119), X(145), X(149), X(388), X(515), X(517), X(908), X(1320), X(1537), X(34182)

.. _X(153):

X(153) = REFLECTION OF X(20) IN X(100)
======================================

.. figure:: x-00153.svg
   :alt: X(153) = REFLECTION OF X(20) IN X(100)
   :align: center

   **X(153) = REFLECTION OF X(20) IN X(100)** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`f(a,b,c) : f(b,c,a) : f(c,a,b)`, where, f(a,b,c) = (by + cz - ax)/a, where x : y : z = :ref:`X(104) <X(104)>`

Barycentrics
~~~~~~~~~~~~

* :math:`a^7 - a^6 (b + c) - a^5 (b^2 - 7 b c + c^2) + a^4 (b + c) (b^2 - 6 b c + c^2) - a^3 (b^4 + 2 b^3 c - 10 b^2 c^2 + 2 b c^3 + c^4) + a^2 (b - c)^2 (b + c) (b^2 + 6 b c + c^2) + a (b^2 - c^2)^2 (b^2 - 5 b c + c^2) - (b - c)^4 (b + c)^3 : :`

* **Kimberling (6, 9, 13) Search Value:** :math:`-14.037672929368`

Notes
-----

.. container:: note-item

   Let T be the P-Brocard triangle for any P on line :ref:`X(1) <X(1)>`\ \ :ref:`X(3) <X(3)>`. Let O\ :sub:`A` be the circle centered at the A-vertex of T and passing through A; define O\ :sub:`B` and O\ :sub:`C` cyclically. :ref:`X(153) <X(153)>` is the radical center of O\ :sub:`A`, O\ :sub:`B`, O\ :sub:`C`. (:person:`Randy Hutson <randy-hutson>`, August 30, 2020)

Incidence
---------

:ref:`X(153) <X(153)>` lies on the anticomplementary circle and on these lines:

{:ref:`2 <X(2)>`, :ref:`104 <X(104)>`}, {:ref:`4 <X(4)>`, :ref:`145 <X(145)>`}, {:ref:`7 <X(7)>`, :ref:`80 <X(80)>`}, {:ref:`11 <X(11)>`, :ref:`388 <X(388)>`}, {:ref:`20 <X(20)>`, :ref:`100 <X(100)>`}, {:ref:`515 <X(515)>`, :ref:`908 <X(908)>`}

Relations
---------

* :ref:`X(153) <X(153)>` = reflection of X(i) in X(j) for these (i,j): (:ref:`20 <X(20)>`, :ref:`100 <X(100)>`), (:ref:`104 <X(104)>`, :ref:`119 <X(119)>`), (:ref:`149 <X(149)>`, :ref:`4 <X(4)>`), (1320, 1537)
* :ref:`X(153) <X(153)>` = :term:`isogonal conjugate <isogonal-conjugate>` of X(34182)
* :ref:`X(153) <X(153)>` = :term:`anticomplementary conjugate <anticomplementary-conjugate>` of :ref:`X(517) <X(517)>`
* :ref:`X(153) <X(153)>` = :ref:`X(104) <X(104)>`-of-:term:`anticomplementary triangle <anticomplementary-triangle>`

Construction
------------

.. literalinclude:: model.py
   :language: python
