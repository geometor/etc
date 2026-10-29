:order: 266
:type: center
:canonical_id: X(266)
:dependencies: X(1), X(3), X(6), X(40), X(56), X(164), X(174), X(188), X(259), X(260), X(289), X(361), X(505), X(978), X(6729)

.. _X(266):

X(266) = ISOGONAL CONJUGATE OF X(188)
=====================================

.. figure:: x-00266.svg
   :alt: X(266) = ISOGONAL CONJUGATE OF X(188)
   :align: center

   **X(266) = ISOGONAL CONJUGATE OF X(188)** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`\sin A/2 : \sin B/2 : \sin C/2`
* :math:`[a/(b + c - a)]^{1/2} : :`
* :math:`\sin A \sec A/2 : :`
* :math:`\cos A' : :`, where A'B'C' is the :term:`excentral triangle <excentral-triangle>`
* \|\ :ref:`X(1) <X(1)>`\ A'\| : \|\ :ref:`X(1) <X(1)>`\ B'\| : \|\ :ref:`X(1) <X(1)>`\ C'\|, where A'B'C' is the excentral triangle
* cos(angle BIC) : cos(angle CIA) : cos(angle AIB)

Barycentrics
~~~~~~~~~~~~

* :math:`\sin A \sin A/2 : :`

* **Kimberling (6, 9, 13) Search Value:** :math:`0.639005784837`

Notes
-----

.. container:: note-item

   The :term:`trilinear polar <trilinear-polar>` of :ref:`X(266) <X(266)>` passes through X(6729). (:person:`Randy Hutson <randy-hutson>`, October 15, 2018)

Incidence
---------

:ref:`X(266) <X(266)>` lies and on these lines:

{:ref:`1 <X(1)>`, :ref:`164 <X(164)>`}, {:ref:`56 <X(56)>`, :ref:`289 <X(289)>`}, {:ref:`174 <X(174)>`, :ref:`188 <X(188)>`}, {:ref:`259 <X(259)>`, :ref:`260 <X(260)>`}, {:ref:`361 <X(361)>`, :ref:`978 <X(978)>`}

Relations
---------

* :ref:`X(266) <X(266)>` = :term:`isogonal conjugate <isogonal-conjugate>` of :ref:`X(188) <X(188)>`
* :ref:`X(266) <X(266)>` = :term:`eigencenter <eigencenter>` of :term:`cevian triangle <cevian-triangle>` of :ref:`X(174) <X(174)>`
* :ref:`X(266) <X(266)>` = eigencenter of :term:`anticevian triangle <anticevian-triangle>` of :ref:`X(259) <X(259)>`
* :ref:`X(266) <X(266)>` = :ref:`X(174) <X(174)>`-:term:`Ceva conjugate <ceva-conjugate>` of :ref:`X(259) <X(259)>`
* :ref:`X(266) <X(266)>` = :term:`cevapoint <cevapoint>` of :ref:`X(1) <X(1)>` and :ref:`X(361) <X(361)>`
* :ref:`X(266) <X(266)>` = :ref:`X(6) <X(6)>`-:term:`cross conjugate <cross-conjugate>` of :ref:`X(289) <X(289)>`
* :ref:`X(266) <X(266)>` = :term:`crosspoint <crosspoint>` of :ref:`X(1) <X(1)>` and :ref:`X(505) <X(505)>`
* :ref:`X(266) <X(266)>` = :term:`crosssum <crosssum>` of :ref:`X(1) <X(1)>` and :ref:`X(164) <X(164)>`
* :ref:`X(266) <X(266)>` = SS(A→A') of :ref:`X(3) <X(3)>`, where A'B'C' is the excentral triangle
* :ref:`X(266) <X(266)>` = trilinear square root of :ref:`X(56) <X(56)>`
* :ref:`X(266) <X(266)>` = excentral-to-ABC :term:`trilinear image <trilinear-image>` of :ref:`X(40) <X(40)>`
* :ref:`X(266) <X(266)>` = intouch-to-ABC trilinear image of :ref:`X(1) <X(1)>`

Construction
------------

.. literalinclude:: model.py
   :language: python
