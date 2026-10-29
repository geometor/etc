:order: 252
:type: center
:canonical_id: X(252)
:dependencies: X(3), X(4), X(5), X(54), X(93), X(140), X(143), X(186), X(930), X(2964), X(31376)

.. _X(252):

X(252) = ISOGONAL CONJUGATE OF X(143)
=====================================

.. figure:: x-00252.svg
   :alt: X(252) = ISOGONAL CONJUGATE OF X(143)
   :align: center

   **X(252) = ISOGONAL CONJUGATE OF X(143)** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`f(A,B,C) : f(B,C,A) : f(C,A,B)`, where, f(A,B,C) = sec(B - C)/[1 - 2 cos(2A)]
* :math:`h(A,B,C) : h(B,C,A) : h(C,A,B)`, where, h(A,B,C) = cos A sec(3A) sec(B - C) (Manol Iliev, 4/01/07)

Barycentrics
~~~~~~~~~~~~

* (sin A)f(A,B,C) : (sin B)f(B,C,A) : (sin C) f(C,A,B) Let A'B'C' be the :term:`orthic triangle <orthic-triangle>`. Let O\ :sub:`A` be the circle with center A passing through A'. Let A″ be the intersection, other than A', of O\ :sub:`A` and the nine-point circle. Define B″ and C″ cyclically. The lines AA″, BB″, CC″ concur in :ref:`X(252) <X(252)>`. (:person:`Randy Hutson <randy-hutson>`, June 7, 2019)

* **Kimberling (6, 9, 13) Search Value:** :math:`2.767922111553`

Notes
-----

.. container:: note-item

   Let H\ :sub:`A` be the reflection of :ref:`X(4) <X(4)>` in the Euler line of BC\ :ref:`X(4) <X(4)>`, and define H\ :sub:`B` and H\ :sub:`C` cyclically. The lines AH\ :sub:`A`, BH\ :sub:`B`, CH\ :sub:`C` concur in :ref:`X(252) <X(252)>`. (Randy Hutson, June 7, 2019)

Incidence
---------

:ref:`X(252) <X(252)>` lies and on these lines:

{:ref:`3 <X(3)>`, :ref:`930 <X(930)>`}, {:ref:`54 <X(54)>`, :ref:`140 <X(140)>`}, {:ref:`93 <X(93)>`, :ref:`186 <X(186)>`}

Relations
---------

* :ref:`X(252) <X(252)>` = :term:`isogonal conjugate <isogonal-conjugate>` of :ref:`X(143) <X(143)>`
* :ref:`X(252) <X(252)>` = :term:`anticomplement <anticomplement>` of X(31376)
* :ref:`X(252) <X(252)>` = :ref:`X(5) <X(5)>`-:term:`isoconjugate <isoconjugate>` of X(2964)

Construction
------------

.. literalinclude:: model.py
   :language: python
