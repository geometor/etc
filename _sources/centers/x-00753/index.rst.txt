:order: 753
:type: center
:canonical_id: X(753)
:dependencies: X(6), X(75), X(100), X(752), X(789), X(825), X(984), X(3250), X(28467), X(35548)

.. _X(753):

X(753) = EVEN (0, 3) CIRCUMCIRCLE POINT
=======================================

.. figure:: x-00753.svg
   :alt: X(753) = EVEN (0, 3) CIRCUMCIRCLE POINT
   :align: center

   **X(753) = EVEN (0, 3) CIRCUMCIRCLE POINT** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`f(a,b,c) : f(b,c,a) : f(c,a,b)`, where f(a,b,c) = 1/[a :sup:`-1`\ (b\ :sup:`3` + c\ :sup:`3`) - a\ :sup:`2`\ (b\ :sup:`0` + c\ :sup:`0`)]

Barycentrics
~~~~~~~~~~~~

* :math:`g(a,b,c) : g(b,c,a) : g(c,a,b)`, where g(a,b,c) = af(a,b,c)

* **Kimberling (6, 9, 13) Search Value:** :math:`2.265834391109`

Incidence
---------

:ref:`X(753) <X(753)>` lies on the circumcircle.

:ref:`X(753) <X(753)>` lies and on these lines:

{:ref:`6 <X(6)>`, :ref:`825 <X(825)>`}, {:ref:`75 <X(75)>`, :ref:`789 <X(789)>`}, {:ref:`100 <X(100)>`, :ref:`984 <X(984)>`}

Relations
---------

* :ref:`X(753) <X(753)>` = :term:`isogonal conjugate <isogonal-conjugate>` of :ref:`X(752) <X(752)>`
* :ref:`X(753) <X(753)>` = :term:`isotomic conjugate <isotomic-conjugate>` of X(35548)
* :ref:`X(753) <X(753)>` = circumcircle-antipode of X(28467)
* :ref:`X(753) <X(753)>` = :term:`trilinear pole <trilinear-pole>` of line :ref:`X(6) <X(6)>`\ X(3250)
* :ref:`X(753) <X(753)>` = Ψ(:ref:`X(6) <X(6)>`, X(3250))

Construction
------------

.. literalinclude:: model.py
   :language: python
