:order: 38
:type: center
:canonical_id: X(38)
:dependencies: X(1), X(2), X(3), X(8), X(9), X(10), X(21), X(31), X(37), X(42), X(56), X(57), X(63), X(75), X(78), X(82), X(92), X(99), X(201), X(210), X(240), X(244), X(310), X(321), X(354), X(518), X(596), X(612), X(614), X(643), X(661), X(726), X(745), X(830), X(869), X(899), X(912), X(976), X(980), X(986), X(988), X(1038), X(1064), X(1106), X(1215), X(2084), X(2530), X(3112), X(8041)

.. _X(38):

X(38) = CROSSPOINT OF X(1) AND X(75)
====================================

.. figure:: x-00038.svg
   :alt: X(38) = CROSSPOINT OF X(1) AND X(75)
   :align: center

   **X(38) = CROSSPOINT OF X(1) AND X(75)** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`b^{2} + c^{2} : :`
* :math:`\csc A \sin(A + \omega ) : \csc B \sin(B + \omega ) : \csc C \sin(C + \omega )`
* :math:`S_{A} + S_{\omega } : :`

Barycentrics
~~~~~~~~~~~~

* :math:`a(b^{2} + c^{2}) : :`
* :math:`\sin(A + \omega ) : \sin(B + \omega ) : \sin(C + \omega )`

* **Kimberling (6, 9, 13) Search Value:** :math:`2.431598760008`

Linear Combinations
-------------------

* :ref:`X(38) <X(38)>` = (3r\ :sup:`2` + 8rR - s\ :sup:`2`)\*\ :ref:`X(1) <X(1)>` - 6rR\*\ :ref:`X(2) <X(2)>` - 4r\ :sup:`2`\ \*\ :ref:`X(3) <X(3)>` (:person:`Peter Moses <peter-moses>`, April 2, 2013)

Notes
-----

.. container:: note-item

   :ref:`X(38) <X(38)>` is the {:ref:`X(1) <X(1)>`,\ :ref:`X(63) <X(63)>`}-harmonic conjugate of :ref:`X(31) <X(31)>`.

Incidence
---------

:ref:`X(38) <X(38)>` lies and on these lines:

{:ref:`1 <X(1)>`, :ref:`21 <X(21)>`}, {:ref:`2 <X(2)>`, 244}, {:ref:`3 <X(3)>`, 976}, {:ref:`8 <X(8)>`, 986}, {:ref:`9 <X(9)>`, 614}, {:ref:`10 <X(10)>`, 596}, {:ref:`37 <X(37)>`, 354}, {:ref:`42 <X(42)>`, 518}, {:ref:`56 <X(56)>`, 201}, {:ref:`57 <X(57)>`, 612}, {:ref:`75 <X(75)>`, 310}, {:ref:`78 <X(78)>`, 988}, {:ref:`92 <X(92)>`, 240}, {:ref:`99 <X(99)>`, 745}, {210, 899}, {321, 726}, {869, 980}, {912, 1064}, {1038, 1106}

Relations
---------

* :ref:`X(38) <X(38)>` = :term:`isogonal conjugate <isogonal-conjugate>` of :ref:`X(82) <X(82)>`
* :ref:`X(38) <X(38)>` = :term:`isotomic conjugate <isotomic-conjugate>` of X(3112)
* :ref:`X(38) <X(38)>` = :term:`anticomplement <anticomplement>` of X(1215)
* :ref:`X(38) <X(38)>` = :term:`crosspoint <crosspoint>` of :ref:`X(1) <X(1)>` and :ref:`X(75) <X(75)>`
* :ref:`X(38) <X(38)>` = :term:`crosssum <crosssum>` of :ref:`X(1) <X(1)>` and :ref:`X(31) <X(31)>`
* :ref:`X(38) <X(38)>` = :term:`crossdifference <crossdifference>` of every pair of points on line X(661)X(830)
* :ref:`X(38) <X(38)>` = X(643)-:term:`beth conjugate <beth-conjugate>` of :ref:`X(38) <X(38)>`
* :ref:`X(38) <X(38)>` = bicentric sum of PU(35)
* :ref:`X(38) <X(38)>` = PU(35)-harmonic conjugate of X(661)
* :ref:`X(38) <X(38)>` = :term:`trilinear pole <trilinear-pole>` of line X(2084)X(2530)
* :ref:`X(38) <X(38)>` = perspector of ABC and extraversion triangle of :ref:`X(38) <X(38)>` (which is also the :term:`anticevian triangle <anticevian-triangle>` of :ref:`X(38) <X(38)>`)
* :ref:`X(38) <X(38)>` = barycentric square root of X(8041)

Construction
------------

.. literalinclude:: model.py
   :language: python
