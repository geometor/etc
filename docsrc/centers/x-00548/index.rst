:order: 548
:type: center
:canonical_id: X(548)
:dependencies: X(2), X(3), X(5), X(20), X(140), X(546), X(550), X(3530), X(15712)

.. _X(548):

X(548) = MIDPOINT OF X(5) AND X(20)
===================================

.. figure:: x-00548.svg
   :alt: X(548) = MIDPOINT OF X(5) AND X(20)
   :align: center

   **X(548) = MIDPOINT OF X(5) AND X(20)** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`- \cos(B - C) + 6 \cos A : :`
* :math:`5 \cos A - 2 \cos B \cos C : 5 \cos B - 2 \cos C \cos A : 5 \cos C - 2 \cos A \cos B`
* :math:`2 \sec A - 5 \sec B \sec C : 2 \sec B - 5 \sec C \sec A : 2 \sec C - 5 \sec A \sec B`

* **Kimberling (6, 9, 13) Search Value:** :math:`9.897108470477`

Linear Combinations
-------------------

* :ref:`X(548) <X(548)>` = 3 :ref:`X(2) <X(2)>` - 7 :ref:`X(3) <X(3)>` = 3\ :ref:`X(3) <X(3)>` - :ref:`X(5) <X(5)>`

Notes
-----

.. container:: note-item

   As a point on the Euler line, :ref:`X(548) <X(548)>` has Shinagawa coefficients (5,-7).

Incidence
---------

:ref:`X(548) <X(548)>` lies on the Euler line. (:person:`Antreas Hatzipolakis <antreas-hatzipolakis>`, 1/20/00, :cite:`Hyacinthos #201 <hyacinthos>`)

Relations
---------

* :ref:`X(548) <X(548)>` = midpoint of X(i) and X(j) for these (i,j): (:ref:`3 <X(3)>`, :ref:`550 <X(550)>`), (:ref:`5 <X(5)>`, :ref:`20 <X(20)>`)
* :ref:`X(548) <X(548)>` = reflection of X(i) in X(j) for these (i,j): (:ref:`140 <X(140)>`, :ref:`3 <X(3)>`), (:ref:`546 <X(546)>`, :ref:`140 <X(140)>`)
* :ref:`X(548) <X(548)>` = {:ref:`X(2) <X(2)>`,\ :ref:`X(3) <X(3)>`}-harmonic conjugate of X(15712)
* :ref:`X(548) <X(548)>` = {:ref:`X(3) <X(3)>`,\ :ref:`X(5) <X(5)>`}-harmonic conjugate of X(3530)
* :ref:`X(548) <X(548)>` = radical center of circles centered at vertices of ABC with diameter equal to opposite side

Construction
------------

.. literalinclude:: model.py
   :language: python
