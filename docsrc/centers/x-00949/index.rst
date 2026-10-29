:order: 949
:type: center
:canonical_id: X(949)
:dependencies: X(1), X(2), X(3), X(6), X(9), X(41), X(48), X(77), X(78), X(220), X(294), X(607), X(652), X(926), X(948), X(1037)

.. _X(949):

X(949) = ISOGONAL CONJUGATE OF X(948)
=====================================

.. figure:: x-00949.svg
   :alt: X(949) = ISOGONAL CONJUGATE OF X(948)
   :align: center

   **X(949) = ISOGONAL CONJUGATE OF X(948)** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`f(a,b,c) : f(b,c,a) : f(c,a,b),`, where f(a,b,c) = au/[a\ :sup:`3` - a\ :sup:`2`\ (b + c) + a(b + c)\ :sup:`2` - (b - c)(b\ :sup:`2` - c\ :sup:`2`)],, where u : v : w = :ref:`X(9) <X(9)>`

Barycentrics
~~~~~~~~~~~~

* :math:`g(a,b,c) : g(b,c,a) : g(c,a,b)`, where g(a,b,c) = af(a,b,c)

* **Kimberling (6, 9, 13) Search Value:** :math:`2.379115196684`

Incidence
---------

:ref:`X(949) <X(949)>` lies and on these lines:

{:ref:`1 <X(1)>`, :ref:`607 <X(607)>`}, {:ref:`2 <X(2)>`, :ref:`294 <X(294)>`}, {:ref:`3 <X(3)>`, :ref:`41 <X(41)>`}, {:ref:`6 <X(6)>`, :ref:`77 <X(77)>`}, {:ref:`48 <X(48)>`, 1037}, {:ref:`78 <X(78)>`, :ref:`220 <X(220)>`}

Relations
---------

* :ref:`X(949) <X(949)>` = :term:`isogonal conjugate <isogonal-conjugate>` of :ref:`X(948) <X(948)>`
* :ref:`X(949) <X(949)>` = :term:`trilinear pole <trilinear-pole>` of line :ref:`X(652) <X(652)>`\ \ :ref:`X(926) <X(926)>`

Construction
------------

.. literalinclude:: model.py
   :language: python
