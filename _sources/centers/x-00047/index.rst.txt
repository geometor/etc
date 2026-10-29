:order: 47
:type: center
:canonical_id: X(47)
:dependencies: X(1), X(2), X(3), X(19), X(21), X(33), X(34), X(35), X(36), X(46), X(48), X(90), X(91), X(92), X(110), X(158), X(162), X(171), X(212), X(238), X(275), X(371), X(372), X(498), X(499), X(564), X(602), X(643), X(656), X(921), X(1109), X(1820), X(20571), X(34825)

.. _X(47):

X(47) = -BETH CONJUGATE OF X(34)
================================

.. figure:: x-00047.svg
   :alt: X(47) = -BETH CONJUGATE OF X(34)
   :align: center

   **X(47) = -BETH CONJUGATE OF X(34)** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`\cos 2A : \cos 2B : \cos 2C = f(a,b,c) : f(b,c,a) : f(c,a,b)`, where, f(a,b,c) = a\ :sup:`2`\ (a\ :sup:`4` + b\ :sup:`4` + c\ :sup:`4` - 2a\ :sup:`2`\ b\ :sup:`2` - 2a\ :sup:`2`\ c\ :sup:`2`)
* :math:`a^{2} - 2R^{2} : b^{2} - 2R^{2} : c^{2} - 2R^{2}`
* :math:`\tan A \cot 2A : :`
* :math:`\cos^2 A - \sin^2 A : :`
* :math:`1 - 2 \sin^2 A : :`
* :math:`1 - 2 \cos^2 A : :`

Barycentrics
~~~~~~~~~~~~

* :math:`a \cos 2A : b \cos 2B : c \cos 2C`

* **Kimberling (6, 9, 13) Search Value:** :math:`-56.512488734291`

Linear Combinations
-------------------

* :ref:`X(47) <X(47)>` = (r\ :sup:`2` - R\ :sup:`2` + s\ :sup:`2`)\*\ :ref:`X(1) <X(1)>` - 6rR\*\ :ref:`X(2) <X(2)>` - 4r\ :sup:`2`\ \*\ :ref:`X(3) <X(3)>` (:person:`Peter Moses <peter-moses>`, April 2, 2013)

Notes
-----

.. container:: note-item

   Let A'B'C' be the Kosnita triangle. Let A″ be the trilinear product B'\*C', and define B″, C″ cyclically. The lines AA″, BB″, CC″ concur in :ref:`X(47) <X(47)>`. (:person:`Randy Hutson <randy-hutson>`, March 21, 2019)

.. container:: note-item

   Let A'B'C' and A″B″C″ be the Lucas and Lucas(-1) tangents triangles. Let A\* be the trilinear product A'\*A″, and define B\*, C\* cyclically. The lines AA\*, BB\*, CC\* concur in :ref:`X(47) <X(47)>`. (Randy Hutson, March 21, 2019)

.. container:: note-item

   :ref:`X(47) <X(47)>` is the {:ref:`X(91) <X(91)>`,\ :ref:`X(92) <X(92)>`}-harmonic conjugate of X(564).

Incidence
---------

:ref:`X(47) <X(47)>` lies and on these lines:

{:ref:`1 <X(1)>`, :ref:`21 <X(21)>`}, {:ref:`19 <X(19)>`, 921}, {:ref:`33 <X(33)>`, :ref:`90 <X(90)>`}, {:ref:`34 <X(34)>`, :ref:`46 <X(46)>`}, {:ref:`35 <X(35)>`, 212}, {:ref:`36 <X(36)>`, 602}, {:ref:`91 <X(91)>`, :ref:`92 <X(92)>`}, {158, 162}, {171, 498}, {238, 499}

Relations
---------

* :ref:`X(47) <X(47)>` = :term:`isogonal conjugate <isogonal-conjugate>` of :ref:`X(91) <X(91)>`
* :ref:`X(47) <X(47)>` = :term:`isotomic conjugate <isotomic-conjugate>` of X(20571)
* :ref:`X(47) <X(47)>` = :term:`anticomplement <anticomplement>` of X(34825)
* :ref:`X(47) <X(47)>` = trilinear product X(371)\*X(372)
* :ref:`X(47) <X(47)>` = :ref:`X(92) <X(92)>`-:term:`isoconjugate <isoconjugate>` of X(1820)
* :ref:`X(47) <X(47)>` = perspector of ABC and extraversion triangle of :ref:`X(47) <X(47)>` (which is also the :term:`anticevian triangle <anticevian-triangle>` of :ref:`X(47) <X(47)>`)
* :ref:`X(47) <X(47)>` = :term:`eigencenter <eigencenter>` of :term:`cevian triangle <cevian-triangle>` of :ref:`X(92) <X(92)>`
* :ref:`X(47) <X(47)>` = eigencenter of anticevian triangle of :ref:`X(48) <X(48)>`
* :ref:`X(47) <X(47)>` = :ref:`X(92) <X(92)>`-:term:`Ceva conjugate <ceva-conjugate>` of :ref:`X(48) <X(48)>`
* :ref:`X(47) <X(47)>` = :term:`crosssum <crosssum>` of X(i) and X(j) for these (i,j): (656, 1109)
* :ref:`X(47) <X(47)>` = X(275)-:term:`aleph conjugate <aleph-conjugate>` of :ref:`X(92) <X(92)>`
* :ref:`X(47) <X(47)>` = X(i)-:term:`beth conjugate <beth-conjugate>` of X(j) for these (i,j): (110, :ref:`34 <X(34)>`), (643, :ref:`47 <X(47)>`)
* :ref:`X(47) <X(47)>` = trilinear product of X(371) and X(372)

Construction
------------

.. literalinclude:: model.py
   :language: python
