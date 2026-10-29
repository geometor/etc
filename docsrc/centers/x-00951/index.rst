:order: 951
:type: center
:canonical_id: X(951)
:dependencies: X(29), X(56), X(57), X(73), X(77), X(78), X(219), X(226), X(284), X(738), X(946), X(947), X(950), X(1066), X(1067)

.. _X(951):

X(951) = ISOGONAL CONJUGATE OF X(950)
=====================================

.. figure:: x-00951.svg
   :alt: X(951) = ISOGONAL CONJUGATE OF X(950)
   :align: center

   **X(951) = ISOGONAL CONJUGATE OF X(950)** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`f(a,b,c) : f(b,c,a) : f(c,a,b),`, where f(a,b,c) = a/[(b + c - a)[2a\ :sup:`3` + (b + c)(a\ :sup:`2` + (b - c)\ :sup:`2`)]]

Barycentrics
~~~~~~~~~~~~

* :math:`g(a,b,c) : g(b,c,a) : g(c,a,b)`, where g(a,b,c) = af(a,b,c)

* **Kimberling (6, 9, 13) Search Value:** :math:`0.728817415227`

Incidence
---------

:ref:`X(951) <X(951)>` lies and on these lines:

{:ref:`29 <X(29)>`, :ref:`226 <X(226)>`}, {:ref:`56 <X(56)>`, :ref:`219 <X(219)>`}, {:ref:`57 <X(57)>`, :ref:`78 <X(78)>`}, {:ref:`73 <X(73)>`, :ref:`284 <X(284)>`}, {:ref:`77 <X(77)>`, :ref:`738 <X(738)>`}, {:ref:`946 <X(946)>`, 1067}, {:ref:`947 <X(947)>`, 1066}

Relations
---------

* :ref:`X(951) <X(951)>` = :term:`isogonal conjugate <isogonal-conjugate>` of :ref:`X(950) <X(950)>`
* :ref:`X(951) <X(951)>` = :term:`cevapoint <cevapoint>` of :ref:`X(56) <X(56)>` and :ref:`X(73) <X(73)>`

Construction
------------

.. literalinclude:: model.py
   :language: python
