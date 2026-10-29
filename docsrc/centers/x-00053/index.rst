:order: 53
:type: center
:canonical_id: X(53)
:dependencies: X(3), X(4), X(5), X(6), X(25), X(30), X(45), X(51), X(95), X(97), X(115), X(128), X(133), X(137), X(138), X(139), X(141), X(157), X(216), X(232), X(264), X(273), X(275), X(281), X(288), X(311), X(317), X(318), X(323), X(324), X(393), X(395), X(396), X(401), X(427), X(472), X(473), X(524), X(577), X(594), X(1086), X(12077), X(15451), X(34386), X(34828)

.. _X(53):

X(53) = SYMMEDIAN POINT OF ORTHIC TRIANGLE
==========================================

.. figure:: x-00053.svg
   :alt: X(53) = SYMMEDIAN POINT OF ORTHIC TRIANGLE
   :align: center

   **X(53) = SYMMEDIAN POINT OF ORTHIC TRIANGLE** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`\tan A \cos(B - C) : \tan B \cos(C - A) : \tan C \cos(A - B)`

Barycentrics
~~~~~~~~~~~~

* :math:`a \tan A \cos(B - C) : b \tan B \cos(C - A) : c \tan C \cos(A - B)`
* :math:`(a^2 (b^2 + c^2) - (b^2 - c^2)^2)/(a^2 - b^2 - c^2) : :`

* **Kimberling (6, 9, 13) Search Value:** :math:`-0.134512425200`

Notes
-----

.. container:: note-item

   Let A'B'C' be the Euler triangle. Let L\ :sub:`A` be the :term:`trilinear polar <trilinear-polar>` of A', and define L\ :sub:`B` and L\ :sub:`C` cyclically. Let A″ = L\ :sub:`B`\ ∩L\ :sub:`C`, and define B″ and C″ cyclically. The lines AA″, BB″, CC″ concur in :ref:`X(53) <X(53)>`. (:person:`Randy Hutson <randy-hutson>`, June 7, 2019)

.. container:: note-item

   :ref:`X(53) <X(53)>` is the {:ref:`X(4) <X(4)>`,X(393)}-harmonic conjugate of :ref:`X(6) <X(6)>`.

Incidence
---------

:ref:`X(53) <X(53)>` lies and on these lines:

{:ref:`4 <X(4)>`, :ref:`6 <X(6)>`}, {:ref:`5 <X(5)>`, 216}, {:ref:`25 <X(25)>`, 157}, {:ref:`30 <X(30)>`, 577}, {:ref:`45 <X(45)>`, 281}, {115, 133}, {128, 139}, {137, 138}, {141, 264}, {232, 427}, {273, 1086}, {275, 288}, {311, 324}, {317, 524}, {318, 594}, {395, 472}, {396, 473}

Relations
---------

* :ref:`X(53) <X(53)>` = :term:`isogonal conjugate <isogonal-conjugate>` of :ref:`X(97) <X(97)>`
* :ref:`X(53) <X(53)>` = :term:`isotomic conjugate <isotomic-conjugate>` of X(34386)
* :ref:`X(53) <X(53)>` = :term:`anticomplement <anticomplement>` of X(34828)
* :ref:`X(53) <X(53)>` = X(i)-:term:`Ceva conjugate <ceva-conjugate>` of X(j) for these (i,j): (:ref:`4 <X(4)>`, :ref:`51 <X(51)>`), (324, :ref:`5 <X(5)>`)
* :ref:`X(53) <X(53)>` = :ref:`X(51) <X(51)>`-:term:`cross conjugate <cross-conjugate>` of :ref:`X(5) <X(5)>`
* :ref:`X(53) <X(53)>` = :term:`crosssum <crosssum>` of :ref:`X(3) <X(3)>` and X(577)
* :ref:`X(53) <X(53)>` = Kosnita(:ref:`X(4) <X(4)>`,\ :ref:`X(6) <X(6)>`) point
* :ref:`X(53) <X(53)>` = :term:`trilinear pole <trilinear-pole>` of line X(12077)X(15451) (the polar of :ref:`X(95) <X(95)>` wrt polar circle)
* :ref:`X(53) <X(53)>` = pole wrt polar circle of trilinear polar of :ref:`X(95) <X(95)>` (line X(323)X(401))
* :ref:`X(53) <X(53)>` = polar conjugate of :ref:`X(95) <X(95)>`
* :ref:`X(53) <X(53)>` = excentral-to-ABC :term:`functional image <functional-image>` of :ref:`X(6) <X(6)>`

Construction
------------

.. literalinclude:: model.py
   :language: python
