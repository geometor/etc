:order: 483
:type: center
:canonical_id: X(483)
:dependencies: X(1), X(8), X(173), X(174), X(175), X(178), X(179), X(180), X(372)

.. _X(483):
.. _RadicalCenterOfAjimaMalfattiCircles:

X(483) = RADICAL CENTER OF AJIMA-MALFATTI CIRCLES
=================================================

.. figure:: x-00483.svg
   :alt: X(483) = RADICAL CENTER OF AJIMA-MALFATTI CIRCLES
   :align: center

   **X(483) = RADICAL CENTER OF AJIMA-MALFATTI CIRCLES** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`\sec^{2}A/4 : \sec^{2}B/4 : \sec^{2}C/4`
* :math:`1/(1 + \cos A/2) : 1/(1 + \cos B/2) : 1/(1 + \cos C/2)`

Barycentrics
~~~~~~~~~~~~

* :math:`\sin A \sec^{2}A/4 : \sin B \sec^{2}B/4 : \sin C \sec^{2}C/4`

* **Kimberling (6, 9, 13) Search Value:** :math:`1.470496841714`

Notes
-----

.. container:: note-item

   The Ajima-Malfatti circles are described at :ref:`X(179) <X(179)>`. (:person:`Peter Yff <peter-yff>`, 6/1/98)

.. container:: note-item

   Let (Ia) be the incircle of BCI, where I=\ :ref:`X(1) <X(1)>`, and define (Ib) and (Ic) cyclically. Let Ea be the touchpoint of (Ia) and BC, and define Eb and Ec cyclically. Let Sa be the insimilicenter of (Ib) and (Ic), and define Sb and Sc cyclically. The lines EaSa, EbSb, EcSc concur in :ref:`X(483) <X(483)>`. Let La be the internal tangent, other than AI, of (Ib) and (Ic). Define Lb and Lc cyclically. Then La, Lb, Lc concur in :ref:`X(483) <X(483)>`. (:person:`Randy Hutson <randy-hutson>`, January 29, 2018)

Incidence
---------

:ref:`X(483) <X(483)>` lies and on these lines:

{:ref:`8 <X(8)>`, :ref:`178 <X(178)>`}, {:ref:`173 <X(173)>`, :ref:`180 <X(180)>`}, {:ref:`174 <X(174)>`, :ref:`175 <X(175)>`}

Relations
---------

* :ref:`X(483) <X(483)>` = :ref:`X(372) <X(372)>`-of-BCI-triangle
* :ref:`X(483) <X(483)>` = BCI-:term:`isogonal conjugate <isogonal-conjugate>` of :ref:`X(1) <X(1)>`

Construction
------------

.. literalinclude:: model.py
   :language: python
