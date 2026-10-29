:order: 610
:type: center
:canonical_id: X(610)
:dependencies: X(1), X(3), X(6), X(9), X(19), X(40), X(57), X(63), X(71), X(159), X(165), X(169), X(197), X(204), X(219), X(281), X(326), X(515), X(572), X(662), X(2165), X(2184)

.. _X(610):

X(610) = X(63)-CEVA CONJUGATE OF X(1)
=====================================

.. figure:: x-00610.svg
   :alt: X(610) = X(63)-CEVA CONJUGATE OF X(1)
   :align: center

   **X(610) = X(63)-CEVA CONJUGATE OF X(1)** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`area - a^{2} \cot A : area - b^{2} \cot B : area - c^{2}\cot C`
* tan B + tan C - tan A : tan C + tan A - tan B : tan A + tan B - tan C (:person:`Randy Hutson <randy-hutson>`, 9/23/2011)
* S\ :sub:`B`\ S\ :sub:`C` - a\ :sup:`2`\ S\ :sub:`A` : : (C. Lozada, 9/07/2013)
* :math:`3a^4 - 2a^2(b^2 + c^2) - (b^2 - c^2)^2 : :`

* **Kimberling (6, 9, 13) Search Value:** :math:`-6.409966276989`

Notes
-----

.. container:: note-item

   Barycentrics a(area - a\ :sup:`2` cot A) : b(area - b\ :sup:`2` cot B) : c(area - c\ :sup:`2` cot C)

Incidence
---------

:ref:`X(610) <X(610)>` lies and on these lines:

{:ref:`1 <X(1)>`, :ref:`19 <X(19)>`}, {:ref:`3 <X(3)>`, :ref:`9 <X(9)>`}, {:ref:`6 <X(6)>`, :ref:`57 <X(57)>`}, {:ref:`40 <X(40)>`, :ref:`219 <X(219)>`}, {:ref:`71 <X(71)>`, :ref:`165 <X(165)>`}, {:ref:`159 <X(159)>`, :ref:`197 <X(197)>`}, {:ref:`169 <X(169)>`, :ref:`572 <X(572)>`}, {:ref:`281 <X(281)>`, :ref:`515 <X(515)>`}, {:ref:`326 <X(326)>`, :ref:`662 <X(662)>`}

Relations
---------

* :ref:`X(610) <X(610)>` = :term:`isogonal conjugate <isogonal-conjugate>` of X(2184)
* :ref:`X(610) <X(610)>` = :ref:`X(63) <X(63)>`-:term:`Ceva conjugate <ceva-conjugate>` of :ref:`X(1) <X(1)>`
* :ref:`X(610) <X(610)>` = :ref:`X(204) <X(204)>`-:term:`cross conjugate <cross-conjugate>` of :ref:`X(1) <X(1)>`
* :ref:`X(610) <X(610)>` = X(2165)-of-excentral-triangle

Construction
------------

.. literalinclude:: model.py
   :language: python
