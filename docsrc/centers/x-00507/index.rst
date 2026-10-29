:order: 507
:type: center
:canonical_id: X(507)
:dependencies: X(174)

.. _X(507):

X(507) = 5th ISOSCELIZER POINT
==============================

.. figure:: x-00507.svg
   :alt: X(507) = 5th ISOSCELIZER POINT
   :align: center

   **X(507) = 5th ISOSCELIZER POINT** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`f(A,B,C) : f(B,C,A) : f(C,A,B)`, where f(A,B,C) = (cos A/2)\ :sup:`-1/2`

Barycentrics
~~~~~~~~~~~~

* :math:`af(A,B,C) : bf(B,C,A) : cf(C,A,B)`

* **Kimberling (6, 9, 13) Search Value:** :math:`1.426982771047`

Notes
-----

.. container:: note-item

   The :term:`isoscelizer <isoscelizer>` equations

      [area of T(A,X)][X(A)]\ :sup:`2` = [area of T(B,X)][X(B)]\ :sup:`2` = [area of T(C,X)][X(C)]\ :sup:`2`

.. container:: note-item

   have solution X = :ref:`X(507) <X(507)>`. (:person:`Peter Yff <peter-yff>`, 4/9/99)

Relations
---------

* :ref:`X(507) <X(507)>` = trilinear square root of :ref:`X(174) <X(174)>`

Construction
------------

.. literalinclude:: model.py
   :language: python
