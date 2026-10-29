:order: 89
:type: center
:canonical_id: X(89)
:dependencies: X(1), X(2), X(6), X(44), X(45), X(88), X(649), X(902), X(1022), X(4671), X(20973), X(22083), X(34824)

.. _X(89):

X(89) = ISOGONAL CONJUGATE OF X(45)
===================================

.. figure:: x-00089.svg
   :alt: X(89) = ISOGONAL CONJUGATE OF X(45)
   :align: center

   **X(89) = ISOGONAL CONJUGATE OF X(45)** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`1/(2b + 2c - a) : 1/(2c + 2a - b) : 1/(2a + 2b - c)`

Barycentrics
~~~~~~~~~~~~

* :math:`a/(2b + 2c - a) : b/(2c + 2a - b) : c/(2a + 2b - c)`

* **Kimberling (6, 9, 13) Search Value:** :math:`1.010174849101`

Notes
-----

.. container:: note-item

   Let A\ :sub:`9`\ B\ :sub:`9`\ C\ :sub:`9` be the Gemini triangle 9. Let L\ :sub:`A` be the line through A\ :sub:`9` parallel to BC, and define L\ :sub:`B` and L\ :sub:`C` cyclically. Let A':sub:`9` = L\ :sub:`B`\ ∩L\ :sub:`C`, and define B':sub:`9`, C':sub:`9` cyclically. Triangle A':sub:`9`\ B':sub:`9`\ C':sub:`9` is homothetic to ABC at :ref:`X(89) <X(89)>`. (:person:`Randy Hutson <randy-hutson>`, November 30, 2018)

Incidence
---------

:ref:`X(89) <X(89)>` lies and on these lines:

{:ref:`1 <X(1)>`, 902}, {:ref:`2 <X(2)>`, :ref:`44 <X(44)>`}, {:ref:`6 <X(6)>`, :ref:`88 <X(88)>`}, {649, 1022}

Relations
---------

* :ref:`X(89) <X(89)>` = :term:`isogonal conjugate <isogonal-conjugate>` of :ref:`X(45) <X(45)>`
* :ref:`X(89) <X(89)>` = :term:`isotomic conjugate <isotomic-conjugate>` of X(4671)
* :ref:`X(89) <X(89)>` = :term:`anticomplement <anticomplement>` of isotomic conjugate of isogonal conjugate of X(20973)
* :ref:`X(89) <X(89)>` = anticomplement of polar conjugate of isogonal conjugate of X(22083)
* :ref:`X(89) <X(89)>` = anticomplement of :term:`complementary conjugate <complementary-conjugate>` of X(34824)

Construction
------------

.. literalinclude:: model.py
   :language: python
