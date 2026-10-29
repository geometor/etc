:order: 848
:type: center
:canonical_id: X(848)

.. _X(848):

X(848) = YIU ANGLE POINT
========================

.. figure:: x-00848.svg
   :alt: X(848) = YIU ANGLE POINT
   :align: center

   **X(848) = YIU ANGLE POINT** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`(\csc A)/(\cot A - \cot A') : :`, where A' = 2πa/(a + b + c)

Barycentrics
~~~~~~~~~~~~

* :math:`g(A,B,C) : g(B,C,A) : g(C,A,B)`, where g(A,B,C) = 1/(cot A - cot A'), A' = 2πa/(a + b + c)

* **Kimberling (6, 9, 13) Search Value:** :math:`2.959966790242`

Notes
-----

.. container:: note-item

   :ref:`X(848) <X(848)>` point is introduced by :person:`Paul Yiu <paul-yiu>` in :cite:`Hyacinthos #2704 <hyacinthos>`, April 7, 2001 (see also #2708, April 10, 2001) as the solution X of the equation

.. container:: note-item

   angle BXC : angle CXA : angle AXB = a : b : c.

Construction
------------

.. literalinclude:: model.py
   :language: python
