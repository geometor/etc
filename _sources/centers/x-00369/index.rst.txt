:order: 369
:type: center
:canonical_id: X(369)

.. _X(369):
.. _1st-TrisectedPerimeterPoint:

X(369) = 1st TRISECTED PERIMETER POINT
======================================

.. figure:: x-00369.svg
   :alt: X(369) = 1st TRISECTED PERIMETER POINT
   :align: center

   **X(369) = 1st TRISECTED PERIMETER POINT** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`x : y : z (see below)`

Barycentrics
~~~~~~~~~~~~

* :math:`ax : by : cz`

* **Kimberling (6, 9, 13) Search Value:** :math:`2.053651811125`

Notes
-----

.. container:: note-item

   There exist points A', B', C' on segments BC, CA, AB, respectively, such that AB' + AC' = BC' + BA' = CA' + CB' = (a + b + c)/3, and the lines AA', BB', CC' concur in :ref:`X(369) <X(369)>`. Near the end of the 20th century, Yff found trilinears for :ref:`X(369) <X(369)>` in terms of the unique real root, r, of the cubic polynomial

      2t\ :sup:`3` - 3(a + b + c)t\ :sup:`2` + (a\ :sup:`2` + b\ :sup:`2` + c\ :sup:`2` + 8bc + 8ca + 8ab)t - (cb\ :sup:`2` + ac\ :sup:`2` + ba\ :sup:`2` + 5bc\ :sup:`2` + 5ca\ :sup:`2` + 5ab\ :sup:`2` + 9abc),

   as follows: x = bc(r - c + a)(r - a + b). Here x(a,c,b) ≠ x(a,b,c), so that y and z are not obtained from x by cyclically permutating a,b,c. At the geometry conference held at Miami University of Ohio, October 2, 2004, Yff, proved that :ref:`X(369) <X(369)>` is also given by x\ :sub:`1` : y\ :sub:`1` : z\ :sub:`1` where y\ :sub:`1` : z\ :sub:`1` *are* given by cyclic permutations of a,b,c, in x\ :sub:`1`, where

   x\ :sub:`1` = bc[r\ :sup:`2` - (2c + a)r + (- a\ :sup:`2` + b\ :sup:`2` + 2c\ :sup:`2` + 2bc + 3ca + 2ab].

.. container:: note-item

   His presentation included a proof that there is only one point for which AB' + AC' = BC' + BA' = CA' + CB' .

Construction
------------

.. literalinclude:: model.py
   :language: python
