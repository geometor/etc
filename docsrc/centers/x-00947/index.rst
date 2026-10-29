:order: 947
:type: center
:canonical_id: X(947)
:dependencies: X(29), X(40), X(48), X(55), X(73), X(77), X(92), X(102), X(219), X(282), X(515), X(572), X(581), X(946), X(950), X(951), X(1036), X(1066), X(1067), X(22063)

.. _X(947):

X(947) = ISOGONAL CONJUGATE OF X(946)
=====================================

.. figure:: x-00947.svg
   :alt: X(947) = ISOGONAL CONJUGATE OF X(946)
   :align: center

   **X(947) = ISOGONAL CONJUGATE OF X(946)** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`f(a,b,c) : f(b,c,a) : f(c,a,b),`, where f(a,b,c) = a/[a\ :sup:`3`\ (b + c) + (b - c)\ :sup:`2`\ (a\ :sup:`2` - ab - ac - b\ :sup:`2` - c\ :sup:`2` - 2bc)]

Barycentrics
~~~~~~~~~~~~

* :math:`g(a,b,c) : g(b,c,a) : g(c,a,b)`, where g(a,b,c) = af(a,b,c)

* **Kimberling (6, 9, 13) Search Value:** :math:`5.113096212183`

Incidence
---------

:ref:`X(947) <X(947)>` lies and on these lines:

{:ref:`29 <X(29)>`, :ref:`515 <X(515)>`}, {:ref:`40 <X(40)>`, :ref:`77 <X(77)>`}, {:ref:`48 <X(48)>`, :ref:`282 <X(282)>`}, {:ref:`73 <X(73)>`, :ref:`102 <X(102)>`}, {:ref:`219 <X(219)>`, :ref:`572 <X(572)>`}, {:ref:`581 <X(581)>`, 1036}, {:ref:`950 <X(950)>`, 1067}, {:ref:`951 <X(951)>`, 1066}

Relations
---------

* :ref:`X(947) <X(947)>` = :term:`isogonal conjugate <isogonal-conjugate>` of :ref:`X(946) <X(946)>`
* :ref:`X(947) <X(947)>` = :term:`cevapoint <cevapoint>` of :ref:`X(48) <X(48)>` and :ref:`X(55) <X(55)>`
* :ref:`X(947) <X(947)>` = :ref:`X(92) <X(92)>`-:term:`isoconjugate <isoconjugate>` of X(22063)

Construction
------------

.. literalinclude:: model.py
   :language: python
