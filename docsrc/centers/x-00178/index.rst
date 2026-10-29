:order: 178
:type: center
:canonical_id: X(178)
:dependencies: X(2), X(8), X(188), X(236), X(508)

.. _X(178):
.. _SecondMidArcPoint:

X(178) = 2nd MID-ARC POINT
==========================

.. figure:: x-00178.svg
   :alt: X(178) = 2nd MID-ARC POINT
   :align: center

   **X(178) = 2nd MID-ARC POINT** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`(\cos B/2 + \cos C/2) \csc A : (\cos C/2 + \cos A/2) \csc B : (\cos A/2 + \cos B/2) \csc C`

Barycentrics
~~~~~~~~~~~~

* :math:`\cos B/2 + \cos C/2 : \cos C/2 + \cos A/2 : \cos A/2 + \cos B/2`

* **Kimberling (6, 9, 13) Search Value:** :math:`2.359244703059`

Notes
-----

.. container:: note-item

   Let A',B',C' be the first points of intersection of the angle bisectors of ABC with its incircle. Let A″,B″,C″ be the midpoints of segments BC,CA,AB, respectively. The lines A'A″,B'B″,C'C″ concur in :ref:`X(178) <X(178)>`.

.. container:: note-item

   **Clark Kimberling,** Problem 804, *Nieuw Archikef voor Wiskunde* 6 (1988) 170.

Incidence
---------

:ref:`X(178) <X(178)>` lies and on these lines:

{:ref:`2 <X(2)>`, :ref:`188 <X(188)>`}, {:ref:`8 <X(8)>`, :ref:`236 <X(236)>`}

Relations
---------

* :ref:`X(178) <X(178)>` = :term:`complement <complement>` of :ref:`X(188) <X(188)>`
* :ref:`X(178) <X(178)>` = :term:`crosspoint <crosspoint>` of :ref:`X(2) <X(2)>` and :ref:`X(508) <X(508)>`

Construction
------------

.. literalinclude:: model.py
   :language: python
