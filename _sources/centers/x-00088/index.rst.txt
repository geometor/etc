:order: 88
:type: center
:canonical_id: X(88)
:dependencies: X(1), X(2), X(3), X(6), X(7), X(19), X(28), X(36), X(44), X(45), X(48), X(57), X(63), X(81), X(89), X(92), X(100), X(105), X(111), X(162), X(190), X(274), X(278), X(279), X(291), X(333), X(513), X(517), X(519), X(651), X(653), X(658), X(660), X(662), X(678), X(679), X(799), X(901), X(903), X(1022), X(1052), X(1635), X(4358), X(5440), X(23202), X(30578), X(38462)

.. _X(88):

X(88) = ISOGONAL CONJUGATE OF X(44)
===================================

.. figure:: x-00088.svg
   :alt: X(88) = ISOGONAL CONJUGATE OF X(44)
   :align: center

   **X(88) = ISOGONAL CONJUGATE OF X(44)** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`1/(b + c - 2a) : 1/(c + a - 2b) : 1/(a + b - 2c)`

Barycentrics
~~~~~~~~~~~~

* :math:`a/(b + c - 2a) : b/(c + a - 2b) : c/(a + b - 2c)`

* **Kimberling (6, 9, 13) Search Value:** :math:`0.562219245046`

Linear Combinations
-------------------

* :ref:`X(88) <X(88)>` = (3r\ :sup:`2` + 6rR - s\ :sup:`2`)\*\ :ref:`X(1) <X(1)>` + 9rR\*\ :ref:`X(2) <X(2)>` - 6r\ :sup:`2`\ \*\ :ref:`X(3) <X(3)>` (:person:`Peter Moses <peter-moses>`, April 2, 2013)

Notes
-----

.. container:: note-item

   Let A\ :sub:`9`\ B\ :sub:`9`\ C\ :sub:`9` be Gemini triangle 9. Let A' be the perspector of conic {A,B,C,B\ :sub:`9`,C\ :sub:`9`}}, and define B' and C' cyclically. The lines AA', BB', CC' concur in :ref:`X(88) <X(88)>`. (:person:`Randy Hutson <randy-hutson>`, January 15, 2019)

.. container:: note-item

   See (and hear) :person:`Dan Reznik <dan-reznik>`'s `Dance of the Swans: X(88) and X(162) and their Never-Touching Motion Over the Elliptic Billiard <https://www.youtube.com/watch?v=uv_lZSmX9Pk&feature=youtu.be>`__ (March 4, 2020)

Incidence
---------

:ref:`X(88) <X(88)>` lies and on these lines:

{:ref:`1 <X(1)>`, :ref:`100 <X(100)>`}, {:ref:`2 <X(2)>`, :ref:`45 <X(45)>`}, {:ref:`6 <X(6)>`, :ref:`89 <X(89)>`}, {:ref:`28 <X(28)>`, 162}, {:ref:`44 <X(44)>`, 679}, {:ref:`57 <X(57)>`, 651}, {:ref:`81 <X(81)>`, 662}, {105, 901}, {274, 799}, {278, 653}, {279, 658}, {291, 660}

Relations
---------

* :ref:`X(88) <X(88)>` = :term:`isogonal conjugate <isogonal-conjugate>` of :ref:`X(44) <X(44)>`
* :ref:`X(88) <X(88)>` = :term:`isotomic conjugate <isotomic-conjugate>` of X(4358)
* :ref:`X(88) <X(88)>` = :term:`complement <complement>` of X(30578)
* :ref:`X(88) <X(88)>` = :term:`cevapoint <cevapoint>` of X(i) and X(j) for these (i,j): (:ref:`1 <X(1)>`, :ref:`44 <X(44)>`), (:ref:`6 <X(6)>`, :ref:`36 <X(36)>`)
* :ref:`X(88) <X(88)>` = X(i)-:term:`cross conjugate <cross-conjugate>` of X(j) for these (i,j): (:ref:`44 <X(44)>`, :ref:`1 <X(1)>`), (517, :ref:`7 <X(7)>`)
* :ref:`X(88) <X(88)>` = X(i)-:term:`aleph conjugate <aleph-conjugate>` of X(j) for these (i,j): (:ref:`88 <X(88)>`, :ref:`1 <X(1)>`), (679, :ref:`88 <X(88)>`), (903, :ref:`63 <X(63)>`), (1022, 1052)
* :ref:`X(88) <X(88)>` = X(333)-:term:`beth conjugate <beth-conjugate>` of X(190)
* :ref:`X(88) <X(88)>` = trilinear product of PU(50)
* :ref:`X(88) <X(88)>` = perspector of conic {A,B,C,PU(50)}}
* :ref:`X(88) <X(88)>` = :term:`trilinear pole <trilinear-pole>` of PU(55); the line :ref:`X(1) <X(1)>`\ X(513), the line through :ref:`X(1) <X(1)>` parallel to its :term:`trilinear polar <trilinear-polar>`; also normal to Feuerbach hyperbola at :ref:`X(1) <X(1)>`
* :ref:`X(88) <X(88)>` = :term:`crossdifference <crossdifference>` of every pair of points on line X(678)X(1635)
* :ref:`X(88) <X(88)>` = :ref:`X(6) <X(6)>`-:term:`isoconjugate <isoconjugate>` of X(519)
* :ref:`X(88) <X(88)>` = BSS(a^2→a) of X(111)
* :ref:`X(88) <X(88)>` = polar conjugate of X(38462)
* :ref:`X(88) <X(88)>` = :ref:`X(19) <X(19)>`-isoconjugate of X(5440)
* :ref:`X(88) <X(88)>` = :ref:`X(48) <X(48)>`-isoconjugate of X(38462)
* :ref:`X(88) <X(88)>` = :ref:`X(92) <X(92)>`-isoconjugate of X(23202)

Construction
------------

.. literalinclude:: model.py
   :language: python
