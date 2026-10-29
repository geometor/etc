:order: 833
:type: center
:canonical_id: X(833)
:dependencies: X(6), X(106), X(759), X(832), X(977), X(1010)

.. _X(833):

X(833) = o-(1, 4) CIRCUMCIRCLE POINT
====================================

.. figure:: x-00833.svg
   :alt: X(833) = o-(1, 4) CIRCUMCIRCLE POINT
   :align: center

   **X(833) = o-(1, 4) CIRCUMCIRCLE POINT** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`f(a,b,c) : f(b,c,a) : f(c,a,b)`, where f(a,b,c) = 1/[a\ :sup:`0`\ (b\ :sup:`4` - c\ :sup:`4`) + a\ :sup:`3`\ (b\ :sup:`1` - c\ :sup:`1`)]

Barycentrics
~~~~~~~~~~~~

* :math:`g(a,b,c) : g(b,c,a) : g(c,a,b)`, where g(a,b,c) = af(a,b,c)

* **Kimberling (6, 9, 13) Search Value:** :math:`1.915147865901`

Incidence
---------

:ref:`X(833) <X(833)>` lies on the circumcircle.

:ref:`X(833) <X(833)>` lies and on these lines:

{:ref:`106 <X(106)>`, :ref:`977 <X(977)>`}, {:ref:`759 <X(759)>`, 1010}

Relations
---------

* :ref:`X(833) <X(833)>` = :term:`isogonal conjugate <isogonal-conjugate>` of :ref:`X(832) <X(832)>`
* :ref:`X(833) <X(833)>` = :term:`trilinear pole <trilinear-pole>` of line :ref:`X(6) <X(6)>`\ \ :ref:`X(977) <X(977)>`
* :ref:`X(833) <X(833)>` = Ψ(:ref:`X(6) <X(6)>`, :ref:`X(977) <X(977)>`)

Construction
------------

.. literalinclude:: model.py
   :language: python
