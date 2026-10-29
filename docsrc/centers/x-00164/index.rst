:order: 164
:type: center
:canonical_id: X(164)
:dependencies: X(1), X(2), X(3), X(8), X(9), X(40), X(57), X(165), X(167), X(168), X(173), X(177), X(188), X(258), X(361), X(362), X(366), X(503), X(504), X(505), X(844), X(845), X(944), X(3659), X(21633)

.. _X(164):

X(164) = INCENTER OF EXCENTRAL TRIANGLE
=======================================

.. figure:: x-00164.svg
   :alt: X(164) = INCENTER OF EXCENTRAL TRIANGLE
   :align: center

   **X(164) = INCENTER OF EXCENTRAL TRIANGLE** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`\sin B/2 + \sin C/2 - \sin A/2 : \sin C/2 + \sin A/2 - \sin B/2 : \sin A/2 + \sin B/2 - \sin C/2`

Barycentrics
~~~~~~~~~~~~

* :math:`a(\sin B/2 + \sin C/2 - \sin A/2) : b(\sin C/2 + \sin A/2 - \sin B/2) : c(\sin A/2 + \sin B/2 - \sin C/2)`

* **Kimberling (6, 9, 13) Search Value:** :math:`5.601337607767`

Notes
-----

.. container:: note-item

   Let O\ :sub:`A` be the circle centered at the A-vertex of the 1st-circumperp-of-1st-circumperp triangle (which is also the 2nd-circumperp-of-2nd-circumperp triangle) and passing through A; define O\ :sub:`B` and O\ :sub:`C` cyclically. :ref:`X(164) <X(164)>` is the radical center of O\ :sub:`A`, O\ :sub:`B`, O\ :sub:`C`. (:person:`Randy Hutson <randy-hutson>`, August 30, 2020)

.. container:: note-item

   Let O\ :sub:`A` be the circle centered at the A-vertex of the 1st-circumperp-of-2nd-circumperp triangle (which is also the 2nd-circumperp-of-1st-circumperp triangle) and passing through A; define O\ :sub:`B` and O\ :sub:`C` cyclically. :ref:`X(164) <X(164)>` is the radical center of O\ :sub:`A`, O\ :sub:`B`, O\ :sub:`C`. (Randy Hutson, August 30, 2020)

Incidence
---------

:ref:`X(164) <X(164)>` lies and on these lines:

{:ref:`1 <X(1)>`, :ref:`258 <X(258)>`}, {:ref:`3 <X(3)>`, 3659}, {:ref:`9 <X(9)>`, :ref:`168 <X(168)>`}, {:ref:`40 <X(40)>`, :ref:`188 <X(188)>`}, {:ref:`57 <X(57)>`, :ref:`177 <X(177)>`}, {:ref:`165 <X(165)>`, :ref:`167 <X(167)>`}, {:ref:`173 <X(173)>`, :ref:`504 <X(504)>`}, {:ref:`361 <X(361)>`, :ref:`503 <X(503)>`}, {:ref:`362 <X(362)>`, :ref:`845 <X(845)>`}

Relations
---------

* :ref:`X(164) <X(164)>` = :term:`isogonal conjugate <isogonal-conjugate>` of :ref:`X(505) <X(505)>`
* :ref:`X(164) <X(164)>` = :term:`anticomplement <anticomplement>` of X(21633)
* :ref:`X(164) <X(164)>` = :ref:`X(1) <X(1)>`-of-:term:`excentral triangle <excentral-triangle>`
* :ref:`X(164) <X(164)>` = :ref:`X(8) <X(8)>`-of-1st-circumperp-triangle
* :ref:`X(164) <X(164)>` = :ref:`X(944) <X(944)>`-of-2nd-circumperp-triangle
* :ref:`X(164) <X(164)>` = excentral-isogonal conjugate of :ref:`X(164) <X(164)>`
* :ref:`X(164) <X(164)>` = excentral-:term:`isotomic conjugate <isotomic-conjugate>` of :ref:`X(844) <X(844)>`
* :ref:`X(164) <X(164)>` = :ref:`X(188) <X(188)>`-:term:`Ceva conjugate <ceva-conjugate>` of :ref:`X(1) <X(1)>`
* :ref:`X(164) <X(164)>` = X(i)-:term:`aleph conjugate <aleph-conjugate>` of X(j) for these (i,j): (:ref:`1 <X(1)>`, :ref:`361 <X(361)>`), (:ref:`2 <X(2)>`, :ref:`362 <X(362)>`), (:ref:`9 <X(9)>`, :ref:`844 <X(844)>`), (:ref:`188 <X(188)>`, :ref:`164 <X(164)>`), (:ref:`366 <X(366)>`, :ref:`173 <X(173)>`)
* :ref:`X(164) <X(164)>` = centroid of curvatures of extraversions of Conway circle
* :ref:`X(164) <X(164)>` = ABC-to-excentral :term:`trilinear image <trilinear-image>` of :ref:`X(1) <X(1)>`

Construction
------------

.. literalinclude:: model.py
   :language: python
