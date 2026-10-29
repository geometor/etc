:order: 961
:type: center
:canonical_id: X(961)
:dependencies: X(1), X(2), X(6), X(12), X(56), X(57), X(65), X(81), X(92), X(105), X(108), X(274), X(429), X(523), X(572), X(959), X(960), X(1014), X(1104), X(1106), X(22074)

.. _X(961):

X(961) = ISOGONAL CONJUGATE OF X(960)
=====================================

.. figure:: x-00961.svg
   :alt: X(961) = ISOGONAL CONJUGATE OF X(960)
   :align: center

   **X(961) = ISOGONAL CONJUGATE OF X(960)** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`f(a,b,c) : f(b,c,a) : f(c,a,b),`, where f(a,b,c) = 1/[(b + c - a)(b\ :sup:`2` + c\ :sup:`2` + ab + ac)]

Barycentrics
~~~~~~~~~~~~

* :math:`g(a,b,c) : g(b,c,a) : g(c,a,b)`, where g(a,b,c) = af(a,b,c)

* **Kimberling (6, 9, 13) Search Value:** :math:`0.319867802756`

Incidence
---------

:ref:`X(961) <X(961)>` lies and on these lines:

{:ref:`1 <X(1)>`, :ref:`572 <X(572)>`}, {:ref:`2 <X(2)>`, :ref:`12 <X(12)>`}, {:ref:`6 <X(6)>`, :ref:`959 <X(959)>`}, {:ref:`57 <X(57)>`, 1106}, {:ref:`65 <X(65)>`, :ref:`81 <X(81)>`}, {:ref:`105 <X(105)>`, 1104}, {:ref:`108 <X(108)>`, :ref:`429 <X(429)>`}, {:ref:`274 <X(274)>`, 1014}

Relations
---------

* :ref:`X(961) <X(961)>` = :term:`isogonal conjugate <isogonal-conjugate>` of :ref:`X(960) <X(960)>`
* :ref:`X(961) <X(961)>` = :term:`cevapoint <cevapoint>` of :ref:`X(56) <X(56)>` and :ref:`X(65) <X(65)>`
* :ref:`X(961) <X(961)>` = :ref:`X(523) <X(523)>`-:term:`cross conjugate <cross-conjugate>` of :ref:`X(108) <X(108)>`
* :ref:`X(961) <X(961)>` = :ref:`X(92) <X(92)>`-:term:`isoconjugate <isoconjugate>` of X(22074)

Construction
------------

.. literalinclude:: model.py
   :language: python
