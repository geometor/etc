:order: 498
:type: center
:canonical_id: X(498)
:dependencies: X(1), X(2), X(3), X(4), X(5), X(9), X(12), X(35), X(36), X(37), X(46), X(47), X(55), X(56), X(91), X(140), X(141), X(171), X(191), X(226), X(255), X(329), X(345), X(388), X(499), X(611), X(750), X(920), X(1089)

.. _X(498):

X(498) = YFF CONCURRENT CONGRUENT CIRCLES POINT
===============================================

.. figure:: x-00498.svg
   :alt: X(498) = YFF CONCURRENT CONGRUENT CIRCLES POINT
   :align: center

   **X(498) = YFF CONCURRENT CONGRUENT CIRCLES POINT** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`1 + 2 \sin B \sin C : 1 + 2 \sin C \sin A : 1 + 2 \sin A \sin B`
* :math:`bc + 2R^2 : :`

Barycentrics
~~~~~~~~~~~~

* :math:`(\sin A)(1 + 2 \sin B \sin C) : (\sin B)(1 + 2 \sin C \sin A) : (\sin C)(1 + 2 \sin A \sin B)`

* **Kimberling (6, 9, 13) Search Value:** :math:`2.071652786830`

Linear Combinations
-------------------

* :ref:`X(498) <X(498)>` = R\*\ :ref:`X(1) <X(1)>` + r\*\ :ref:`X(3) <X(3)>` + 2r\*\ :ref:`X(5) <X(5)>`

Notes
-----

.. container:: note-item

   :ref:`X(498) <X(498)>` and :ref:`X(499) <X(499)>` are harmonic conjugate points with respect to :ref:`X(1) <X(1)>` and :ref:`X(2) <X(2)>`, in analogy with such pairs with respect to :ref:`X(1) <X(1)>`, :ref:`X(4) <X(4)>` and with respect to :ref:`X(1) <X(1)>`, :ref:`X(5) <X(5)>`.

.. container:: note-item

   **Peter Yff,** "Three concurrent congruent circles 'inscribed' in a triangle," manuscript, 1998; :ref:`X(498) <X(498)>` is the point S on page 6.

Incidence
---------

:ref:`X(498) <X(498)>` lies and on these lines:

{:ref:`1 <X(1)>`, :ref:`2 <X(2)>`}, {:ref:`3 <X(3)>`, :ref:`12 <X(12)>`}, {:ref:`4 <X(4)>`, :ref:`35 <X(35)>`}, {:ref:`5 <X(5)>`, :ref:`55 <X(55)>`}, {:ref:`9 <X(9)>`, :ref:`920 <X(920)>`}, {:ref:`36 <X(36)>`, :ref:`388 <X(388)>`}, {:ref:`37 <X(37)>`, :ref:`91 <X(91)>`}, {:ref:`46 <X(46)>`, :ref:`226 <X(226)>`}, {:ref:`47 <X(47)>`, :ref:`171 <X(171)>`}, {:ref:`56 <X(56)>`, :ref:`140 <X(140)>`}, {:ref:`141 <X(141)>`, :ref:`611 <X(611)>`}, {:ref:`191 <X(191)>`, :ref:`329 <X(329)>`}, {:ref:`255 <X(255)>`, :ref:`750 <X(750)>`}, {:ref:`345 <X(345)>`, 1089}

Relations
---------

* :ref:`X(498) <X(498)>` = homothetic center of anti-Euler triangle and (cross-triangle of ABC and 2nd isogonal triangle of :ref:`X(1) <X(1)>`)

Construction
------------

.. literalinclude:: model.py
   :language: python
