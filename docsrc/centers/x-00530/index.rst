:order: 530
:type: center
:canonical_id: X(530)
:dependencies: X(2), X(13), X(14), X(30), X(99), X(115), X(148), X(187), X(298), X(299), X(316), X(395), X(396), X(511), X(619), X(671), X(2378), X(2482), X(3181)

.. _X(530):

X(530) = DIRECTION OF VECTOR AX + BX + CX, where X = X(13)
==========================================================

.. figure:: x-00530.svg
   :alt: X(530) = DIRECTION OF VECTOR AX + BX + CX, where X = X(13)
   :align: center

   **X(530) = DIRECTION OF VECTOR AX + BX + CX, where X = X(13)** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`(2ax - by - cz)/a : :`, where x = x(A,B,C) = csc(A + π/3), y = x(B,C,A), z = x(C,A,B)

Notes
-----

.. container:: note-item

   Let A' be the nine-point center of BC\ :ref:`X(14) <X(14)>`, and define B' and C' cyclically. A'B'C' is an equilateral triangle concyclic with :ref:`X(2) <X(2)>` and :ref:`X(14) <X(14)>` (inscribed in the 2nd Hutson circle). The isogonal (and isotomic) conjugate of :ref:`X(2) <X(2)>` wrt A'B'C' is :ref:`X(530) <X(530)>`. (:person:`Randy Hutson <randy-hutson>`, February 10, 2016)

Incidence
---------

:ref:`X(530) <X(530)>` lies on the line at infinity.

:ref:`X(530) <X(530)>` lies and on these lines:

{:ref:`2 <X(2)>`, :ref:`13 <X(13)>`}, {:ref:`14 <X(14)>`, :ref:`671 <X(671)>`}, {:ref:`30 <X(30)>`, :ref:`511 <X(511)>`}, {:ref:`99 <X(99)>`, :ref:`299 <X(299)>`}, {:ref:`115 <X(115)>`, :ref:`395 <X(395)>`}, {:ref:`148 <X(148)>`, 3181}, {:ref:`187 <X(187)>`, :ref:`396 <X(396)>`}, {:ref:`298 <X(298)>`, :ref:`316 <X(316)>`}, {:ref:`619 <X(619)>`, 2482}

Relations
---------

* :ref:`X(530) <X(530)>` = :term:`isogonal conjugate <isogonal-conjugate>` of X(2378)

Construction
------------

.. literalinclude:: model.py
   :language: python
