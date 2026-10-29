:order: 259
:type: center
:canonical_id: X(259)
:dependencies: X(1), X(6), X(7), X(9), X(55), X(168), X(173), X(174), X(188), X(258), X(260), X(266), X(289), X(503)

.. _X(259):

X(259) = ISOGONAL CONJUGATE OF X(174)
=====================================

.. figure:: x-00259.svg
   :alt: X(259) = ISOGONAL CONJUGATE OF X(174)
   :align: center

   **X(259) = ISOGONAL CONJUGATE OF X(174)** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`\cos A/2 : :`
* :math:`[a(b + c - a)]^{1/2} : :`
* :math:`\sin A \csc A/2 : :`
* :math:`\sin A' : :`, where A'B'C' is the :term:`excentral triangle <excentral-triangle>`
* :math:`\sin(∠BIC) : :`
* :math:`(b + c - a) \sin A/2 : :`

Barycentrics
~~~~~~~~~~~~

* :math:`\sin A \cos A/2 : :`

* **Kimberling (6, 9, 13) Search Value:** :math:`2.203419929256`

Incidence
---------

:ref:`X(259) <X(259)>` lies and on these lines:

{:ref:`1 <X(1)>`, :ref:`168 <X(168)>`}, {:ref:`258 <X(258)>`, :ref:`289 <X(289)>`}, {:ref:`260 <X(260)>`, :ref:`266 <X(266)>`}

Relations
---------

* :ref:`X(259) <X(259)>` = :term:`isogonal conjugate <isogonal-conjugate>` of :ref:`X(174) <X(174)>`
* :ref:`X(259) <X(259)>` = X(i)-:term:`Ceva conjugate <ceva-conjugate>` of X(j) for these (i,j): (:ref:`174 <X(174)>`, :ref:`266 <X(266)>`), (:ref:`260 <X(260)>`, :ref:`55 <X(55)>`)
* :ref:`X(259) <X(259)>` = :term:`cevapoint <cevapoint>` of :ref:`X(1) <X(1)>` and :ref:`X(503) <X(503)>`
* :ref:`X(259) <X(259)>` = :term:`crosspoint <crosspoint>` of X(i) and X(j) for these (i,j): (:ref:`1 <X(1)>`, :ref:`258 <X(258)>`), (:ref:`174 <X(174)>`, :ref:`188 <X(188)>`)
* :ref:`X(259) <X(259)>` = :term:`crosssum <crosssum>` of X(i) and X(j) for these (i,j): (:ref:`1 <X(1)>`, :ref:`173 <X(173)>`), (:ref:`259 <X(259)>`, :ref:`266 <X(266)>`)
* :ref:`X(259) <X(259)>` = SS(A→A') of :ref:`X(6) <X(6)>`, where A'B'C' is the excentral triangle
* :ref:`X(259) <X(259)>` = trilinear square root of :ref:`X(55) <X(55)>`
* :ref:`X(259) <X(259)>` = perspector of ABC and :term:`unary cofactor triangle <unary-cofactor-triangle>` of tangential mid-arc triangle
* :ref:`X(259) <X(259)>` = excentral-to-ABC :term:`trilinear image <trilinear-image>` of :ref:`X(9) <X(9)>`
* :ref:`X(259) <X(259)>` = intouch-to-ABC trilinear image of :ref:`X(7) <X(7)>`

Construction
------------

.. literalinclude:: model.py
   :language: python
