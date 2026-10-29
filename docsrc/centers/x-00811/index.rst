:order: 811
:type: center
:canonical_id: X(811)
:dependencies: X(1), X(4), X(19), X(27), X(75), X(99), X(108), X(112), X(162), X(336), X(350), X(447), X(645), X(648), X(656), X(661), X(662), X(668), X(789), X(799), X(810), X(823), X(1099), X(2479), X(2480), X(6376), X(16573), X(21300)

.. _X(811):

X(811) = ISOGONAL CONJUGATE OF X(810)
=====================================

.. figure:: x-00811.svg
   :alt: X(811) = ISOGONAL CONJUGATE OF X(810)
   :align: center

   **X(811) = ISOGONAL CONJUGATE OF X(810)** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`(\csc 2A)/(\cos^{2}B - \cos^{2}C) : :`
* :math:`(\csc 2A)/(\sin^2 B - \sin^2 C) : :`

Barycentrics
~~~~~~~~~~~~

* :math:`(\sec A)/(\cos^{2}B - \cos^{2}C) : :`
* :math:`(\sec A)/(\sin^2 B - \sin^2 C) : :`
* :math:`\csc 2A \csc(B - C) : :`
* :math:`bc/[(b^2 - c^2)(b^2 + c^2 - a^2)] : :`

* **Kimberling (6, 9, 13) Search Value:** :math:`-2.269529969762`

Notes
-----

.. container:: note-item

   Let La be the A-extraversion of line :ref:`X(19) <X(19)>`\ \ :ref:`X(27) <X(27)>`, and define Lb, Lc cyclically. Let A' = Lb ∩ Lc, and define B' and C' cyclically. The lines AA', BB', CC' concur in :ref:`X(811) <X(811)>`. (:person:`Randy Hutson <randy-hutson>`, January 29, 2018)

.. container:: note-item

   As the trilinear product of Steiner circumellipse antipodes, :ref:`X(811) <X(811)>` lies on conic {A,B,C,\ :ref:`X(668) <X(668)>`,\ :ref:`X(789) <X(789)>`}} with center X(6376) and perspector :ref:`X(75) <X(75)>`. (Randy Hutson, July 11, 2019)

Incidence
---------

:ref:`X(811) <X(811)>` lies and on these lines:

{:ref:`1 <X(1)>`, :ref:`336 <X(336)>`}, {:ref:`75 <X(75)>`, 1099}, {:ref:`99 <X(99)>`, :ref:`108 <X(108)>`}, {:ref:`112 <X(112)>`, :ref:`789 <X(789)>`}, {:ref:`162 <X(162)>`, :ref:`799 <X(799)>`}, {:ref:`350 <X(350)>`, :ref:`447 <X(447)>`}, {:ref:`645 <X(645)>`, :ref:`648 <X(648)>`}, {:ref:`662 <X(662)>`, :ref:`823 <X(823)>`}

Relations
---------

* :ref:`X(811) <X(811)>` = :term:`isogonal conjugate <isogonal-conjugate>` of :ref:`X(810) <X(810)>`
* :ref:`X(811) <X(811)>` = :term:`isotomic conjugate <isotomic-conjugate>` of :ref:`X(656) <X(656)>`
* :ref:`X(811) <X(811)>` = :term:`complement <complement>` of :term:`anticomplementary conjugate <anticomplementary-conjugate>` of X(21300)
* :ref:`X(811) <X(811)>` = :term:`anticomplement <anticomplement>` of X(16573)
* :ref:`X(811) <X(811)>` = :term:`trilinear pole <trilinear-pole>` of line :ref:`X(19) <X(19)>`\ \ :ref:`X(27) <X(27)>`
* :ref:`X(811) <X(811)>` = polar conjugate of :ref:`X(661) <X(661)>`
* :ref:`X(811) <X(811)>` = perspector of ABC and :term:`tangential triangle <tangential-triangle>`, wrt :term:`anticevian triangle <anticevian-triangle>` of :ref:`X(19) <X(19)>`, of bianticevian conic of :ref:`X(1) <X(1)>` and :ref:`X(4) <X(4)>`
* :ref:`X(811) <X(811)>` = trilinear product :ref:`X(4) <X(4)>`\ \*\ :ref:`X(99) <X(99)>`
* :ref:`X(811) <X(811)>` = trilinear product X(2479)\*X(2480)

Construction
------------

.. literalinclude:: model.py
   :language: python
