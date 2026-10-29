:order: 640
:type: center
:canonical_id: X(640)
:dependencies: X(2), X(3), X(5), X(69), X(141), X(315), X(371), X(372), X(486), X(626), X(638), X(639), X(642)

.. _X(640):

X(640) = COMPLEMENT OF X(372)
=============================

.. figure:: x-00640.svg
   :alt: X(640) = COMPLEMENT OF X(372)
   :align: center

   **X(640) = COMPLEMENT OF X(372)** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`f(a,b,c) : f(b,c,a) : f(c,a,b)`, where f(a,b,c) = [2S\ :sub:`B`\ S\ :sub:`C` + S\ :sub:`A`\ a\ :sup:`2` - 2(b\ :sup:`2` + c\ :sup:`2`) area]/a

Barycentrics
~~~~~~~~~~~~

* :math:`g(a,b,c) : g(b,c,a) : g(c,a,b)`, where g(a,b,c) = af(a,b,c)

* **Kimberling (6, 9, 13) Search Value:** :math:`4.879620959270`

Incidence
---------

:ref:`X(640) <X(640)>` lies and on these lines:

{:ref:`2 <X(2)>`, :ref:`372 <X(372)>`}, {:ref:`3 <X(3)>`, :ref:`642 <X(642)>`}, {:ref:`5 <X(5)>`, :ref:`141 <X(141)>`}, {:ref:`69 <X(69)>`, :ref:`486 <X(486)>`}, {:ref:`315 <X(315)>`, :ref:`371 <X(371)>`}

Relations
---------

* :ref:`X(640) <X(640)>` = midpoint of X(i) and X(j) for these (i,j): (:ref:`315 <X(315)>`, :ref:`371 <X(371)>`), (:ref:`372 <X(372)>`, :ref:`638 <X(638)>`)
* :ref:`X(640) <X(640)>` = reflection of :ref:`X(639) <X(639)>` in :ref:`X(626) <X(626)>`
* :ref:`X(640) <X(640)>` = :term:`complement <complement>` of :ref:`X(372) <X(372)>`
* :ref:`X(640) <X(640)>` = :term:`complementary conjugate <complementary-conjugate>` of :ref:`X(642) <X(642)>`

Construction
------------

.. literalinclude:: model.py
   :language: python
