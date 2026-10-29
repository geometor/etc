:order: 945
:type: center
:canonical_id: X(945)
:dependencies: X(3), X(56), X(78), X(283), X(517), X(859), X(944)

.. _X(945):

X(945) = ISOGONAL CONJUGATE OF X(944)
=====================================

.. figure:: x-00945.svg
   :alt: X(945) = ISOGONAL CONJUGATE OF X(944)
   :align: center

   **X(945) = ISOGONAL CONJUGATE OF X(944)** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`f(a,b,c) : f(b,c,a) : f(c,a,b),`, where f(a,b,c) = a/[3a\ :sup:`4` - 2a\ :sup:`3`\ (b + c) + (b - c)\ :sup:`2`\ (2ab + 2ac - 2bc - b\ :sup:`2` - c\ :sup:`2` - 2a\ :sup:`2`)]

Barycentrics
~~~~~~~~~~~~

* :math:`g(a,b,c) : g(b,c,a) : g(c,a,b)`, where g(a,b,c) = af(a,b,c)

* **Kimberling (6, 9, 13) Search Value:** :math:`-28.107306354614`

Incidence
---------

:ref:`X(945) <X(945)>` lies and on these lines:

{:ref:`78 <X(78)>`, :ref:`517 <X(517)>`}, {:ref:`283 <X(283)>`, :ref:`859 <X(859)>`}

Relations
---------

* :ref:`X(945) <X(945)>` = :term:`isogonal conjugate <isogonal-conjugate>` of :ref:`X(944) <X(944)>`
* :ref:`X(945) <X(945)>` = :ref:`X(3) <X(3)>`-:term:`vertex conjugate <vertex-conjugate>` of :ref:`X(56) <X(56)>`

Construction
------------

.. literalinclude:: model.py
   :language: python
