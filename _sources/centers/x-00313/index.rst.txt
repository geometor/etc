:order: 313
:type: center
:canonical_id: X(313)
:dependencies: X(10), X(12), X(32), X(42), X(58), X(71), X(75), X(76), X(80), X(92), X(190), X(264), X(306), X(308), X(314), X(321), X(349), X(560), X(561), X(594), X(696), X(1474), X(2206), X(17148), X(23197)

.. _X(313):

X(313) = ISOTOMIC CONJUGATE OF X(58)
====================================

.. figure:: x-00313.svg
   :alt: X(313) = ISOTOMIC CONJUGATE OF X(58)
   :align: center

   **X(313) = ISOTOMIC CONJUGATE OF X(58)** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`(b + c)b^{3}c^{3} : (c + a)c^{3}a^{3} : (a + b)a^{3}b^{3}, = (b + c)\csc(A - \omega ) : (c + a)\csc(B - \omega ) : (a + b)\csc(C - \omega )`

* **Kimberling (6, 9, 13) Search Value:** :math:`5.158734620701`

Notes
-----

.. container:: note-item

   Barycentrics (b + c)b\ :sup:`2`\ c\ :sup:`2` : (c + a)c\ :sup:`2`\ a\ :sup:`2` : (a + b)a\ :sup:`2`\ b\ :sup:`2`

.. container:: note-item

   Let A\ :sub:`40`\ B\ :sub:`40`\ C\ :sub:`40` be Gemini triangle 40. Let A' be the center of conic {A,B,C,B\ :sub:`40`,C\ :sub:`40`}}, and define B' and C' cyclically. The lines AA', BB', CC' concur in :ref:`X(313) <X(313)>`. (:person:`Randy Hutson <randy-hutson>`, January 15, 2019)

Incidence
---------

:ref:`X(313) <X(313)>` lies and on these lines:

{:ref:`10 <X(10)>`, :ref:`75 <X(75)>`}, {:ref:`12 <X(12)>`, :ref:`349 <X(349)>`}, {:ref:`42 <X(42)>`, :ref:`308 <X(308)>`}, {:ref:`71 <X(71)>`, :ref:`190 <X(190)>`}, {:ref:`80 <X(80)>`, :ref:`314 <X(314)>`}, {:ref:`92 <X(92)>`, :ref:`264 <X(264)>`}, {:ref:`321 <X(321)>`, :ref:`594 <X(594)>`}, {:ref:`561 <X(561)>`, :ref:`696 <X(696)>`}

Relations
---------

* :ref:`X(313) <X(313)>` = :term:`isogonal conjugate <isogonal-conjugate>` of X(2206)
* :ref:`X(313) <X(313)>` = :term:`isotomic conjugate <isotomic-conjugate>` of :ref:`X(58) <X(58)>`
* :ref:`X(313) <X(313)>` = :term:`complement <complement>` of X(17148)
* :ref:`X(313) <X(313)>` = :term:`anticomplement <anticomplement>` of polar conjugate of isogonal conjugate of X(23197)
* :ref:`X(313) <X(313)>` = :ref:`X(76) <X(76)>`-:term:`Ceva conjugate <ceva-conjugate>` of :ref:`X(321) <X(321)>`
* :ref:`X(313) <X(313)>` = :term:`cevapoint <cevapoint>` of :ref:`X(10) <X(10)>` and :ref:`X(306) <X(306)>`
* :ref:`X(313) <X(313)>` = :ref:`X(321) <X(321)>`-:term:`cross conjugate <cross-conjugate>` of :ref:`X(349) <X(349)>`
* :ref:`X(313) <X(313)>` = :term:`crosssum <crosssum>` of :ref:`X(32) <X(32)>` and :ref:`X(560) <X(560)>`
* :ref:`X(313) <X(313)>` = polar conjugate of X(1474)

Construction
------------

.. literalinclude:: model.py
   :language: python
