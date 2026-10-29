:order: 735
:type: center
:canonical_id: X(735)
:dependencies: X(734), X(35541)

.. _X(735):

X(735) = EVEN (- 2, 3) CIRCUMCIRCLE POINT
=========================================

.. figure:: x-00735.svg
   :alt: X(735) = EVEN (- 2, 3) CIRCUMCIRCLE POINT
   :align: center

   **X(735) = EVEN (- 2, 3) CIRCUMCIRCLE POINT** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`f(a,b,c) : f(b,c,a) : f(c,a,b)`, where f(a,b,c) = 1/[a :sup:`-3`\ (b\ :sup:`3` + c\ :sup:`3`) - a\ :sup:`2`\ (b :sup:`-2` + c :sup:`-2`)]

Barycentrics
~~~~~~~~~~~~

* :math:`g(a,b,c) : g(b,c,a) : g(c,a,b)`, where g(a,b,c) = af(a,b,c)

* **Kimberling (6, 9, 13) Search Value:** :math:`0.263865779842`

Incidence
---------

:ref:`X(735) <X(735)>` lies on the circumcircle.

Relations
---------

* :ref:`X(735) <X(735)>` = :term:`isogonal conjugate <isogonal-conjugate>` of :ref:`X(734) <X(734)>`
* :ref:`X(735) <X(735)>` = :term:`isotomic conjugate <isotomic-conjugate>` of X(35541)

Construction
------------

.. literalinclude:: model.py
   :language: python
