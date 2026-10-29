:order: 907
:type: center
:canonical_id: X(907)
:dependencies: X(98), X(111), X(112), X(419), X(620), X(1180), X(1634), X(2501), X(3800)

.. _X(907):

X(907) = POINT ACRUX
====================

.. figure:: x-00907.svg
   :alt: X(907) = POINT ACRUX
   :align: center

   **X(907) = POINT ACRUX** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`f(a,b,c) : f(b,c,a) : f(c,a,b),`, where f(a,b,c) = a/[(b\ :sup:`2` - c\ :sup:`2`)(3a\ :sup:`2` + b\ :sup:`2` + c\ :sup:`2`)]

Barycentrics
~~~~~~~~~~~~

* :math:`g(a,b,c) : g(b,c,a) : g(c,a,b)`, where g(a,b,c) = a\ :sup:`2`/[(b\ :sup:`2` - c\ :sup:`2`)(3a\ :sup:`2` + b\ :sup:`2` + c\ :sup:`2`)]

* **Kimberling (6, 9, 13) Search Value:** :math:`1.553625773911`

Incidence
---------

:ref:`X(907) <X(907)>` lies on the circumcircle and on these lines:

{:ref:`98 <X(98)>`, :ref:`620 <X(620)>`}, {:ref:`111 <X(111)>`, 1180}, {:ref:`112 <X(112)>`, 1634}

Relations
---------

* :ref:`X(907) <X(907)>` = :term:`isogonal conjugate <isogonal-conjugate>` of X(3800)
* :ref:`X(907) <X(907)>` = Λ(:ref:`X(419) <X(419)>`, X(2501)) (line is radical axis of circumcircle and orthosymmedial circle)

Construction
------------

.. literalinclude:: model.py
   :language: python
