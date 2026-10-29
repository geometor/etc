:order: 408
:type: center
:canonical_id: X(408)
:dependencies: X(2), X(3), X(29), X(73), X(228), X(412)

.. _X(408):

X(408) = EULER LINE INTERCEPT OF LINE X(73)X(228)
=================================================

.. figure:: x-00408.svg
   :alt: X(408) = EULER LINE INTERCEPT OF LINE X(73)X(228)
   :align: center

   **X(408) = EULER LINE INTERCEPT OF LINE X(73)X(228)** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`(v + w)\cos A : (w + u)\cos B : (u + v)\cos C`, where, u : v : w = :ref:`X(29) <X(29)>`; e.g., u = u(A,B,C) = (sec A)/(cos B + cos C)

* **Kimberling (6, 9, 13) Search Value:** :math:`-5.051954769468`

Notes
-----

.. container:: note-item

   Barycentrics (v + w)sin 2A : (w + u)sin 2B : (u + v)sin2C

.. container:: note-item

   As a point on the Euler line, :ref:`X(408) <X(408)>` has Shinagawa coefficients (($bcS\ :sub:`B`\ S\ :sub:`C`\ $)\ :sup:`2`, -($bcS\ :sub:`B`\ S\ :sub:`C`\ $)\ :sup:`2` + EFS\ :sup:`4`).

Incidence
---------

:ref:`X(408) <X(408)>` lies and on these lines:

{:ref:`2 <X(2)>`, :ref:`3 <X(3)>`}, {:ref:`73 <X(73)>`, :ref:`228 <X(228)>`}

Relations
---------

* :ref:`X(408) <X(408)>` = :term:`crosssum <crosssum>` of :ref:`X(29) <X(29)>` and :ref:`X(412) <X(412)>`

Construction
------------

.. literalinclude:: model.py
   :language: python
