:order: 82
:type: center
:canonical_id: X(82)
:dependencies: X(1), X(10), X(31), X(37), X(38), X(58), X(75), X(83), X(251), X(560), X(596), X(661), X(689), X(715), X(759), X(798), X(812), X(827), X(830), X(1930), X(2084), X(2530), X(3112), X(21249)

.. _X(82):

X(82) = ISOGONAL CONJUGATE OF X(38)
===================================

.. figure:: x-00082.svg
   :alt: X(82) = ISOGONAL CONJUGATE OF X(38)
   :align: center

   **X(82) = ISOGONAL CONJUGATE OF X(38)** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`1/(b^{2} + c^{2}) : 1/(c^{2} + a^{2}) : 1/(a^{2} + b^{2})`
* :math:`\sin A \csc(A + \omega ) : \sin B \csc(B + \omega ) : \sin C \csc(C + \omega )`

* **Kimberling (6, 9, 13) Search Value:** :math:`1.057543146404`

Notes
-----

.. container:: note-item

   Barycentrics a/(b\ :sup:`2` + c\ :sup:`2`) : b/(c\ :sup:`2` + a\ :sup:`2`) : c/(a\ :sup:`2` + b\ :sup:`2`)

.. container:: note-item

   Let A'B'C' be the circummedial triangle. Let A″ be the trilinear product B'\*C', and define B″, C″ cyclically. A″, B″, C″ are collinear on line X(798)X(812) (the :term:`trilinear polar <trilinear-polar>` of X(3112)). The lines AA″, BB″, CC″ concur in :ref:`X(82) <X(82)>`. (:person:`Randy Hutson <randy-hutson>`, October 15, 2018)

Incidence
---------

:ref:`X(82) <X(82)>` lies and on these lines:

{:ref:`1 <X(1)>`, 560}, {:ref:`10 <X(10)>`, :ref:`83 <X(83)>`}, {:ref:`31 <X(31)>`, :ref:`75 <X(75)>`}, {:ref:`37 <X(37)>`, 251}, {:ref:`58 <X(58)>`, 596}, {689, 715}, {759, 827}

Relations
---------

* :ref:`X(82) <X(82)>` = :term:`isogonal conjugate <isogonal-conjugate>` of :ref:`X(38) <X(38)>`
* :ref:`X(82) <X(82)>` = :term:`isotomic conjugate <isotomic-conjugate>` of X(1930)
* :ref:`X(82) <X(82)>` = :term:`anticomplement <anticomplement>` of X(21249)
* :ref:`X(82) <X(82)>` = :term:`cevapoint <cevapoint>` of :ref:`X(1) <X(1)>` and :ref:`X(31) <X(31)>`
* :ref:`X(82) <X(82)>` = :term:`trilinear pole <trilinear-pole>` of line X(661)X(830)
* :ref:`X(82) <X(82)>` = :term:`crossdifference <crossdifference>` of every pair of points on line X(2084)X(2530)
* :ref:`X(82) <X(82)>` = perspector of ABC and extraversion triangle of :ref:`X(82) <X(82)>` (which is also the :term:`anticevian triangle <anticevian-triangle>` of :ref:`X(82) <X(82)>`)
* :ref:`X(82) <X(82)>` = :term:`crosspoint <crosspoint>` of :ref:`X(1) <X(1)>` and :ref:`X(31) <X(31)>` wrt the :term:`excentral triangle <excentral-triangle>`

Construction
------------

.. literalinclude:: model.py
   :language: python
