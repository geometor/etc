:order: 713
:type: center
:canonical_id: X(713)
:dependencies: X(32), X(100), X(101), X(560), X(712), X(35531)

.. _X(713):

X(713) = EVEN (- 3, - 2) CIRCUMCIRCLE POINT
===========================================

.. figure:: x-00713.svg
   :alt: X(713) = EVEN (- 3, - 2) CIRCUMCIRCLE POINT
   :align: center

   **X(713) = EVEN (- 3, - 2) CIRCUMCIRCLE POINT** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`f(a,b,c) : f(b,c,a) : f(c,a,b)`, where f(a,b,c) = 1/[a :sup:`-4`\ (b :sup:`-2` + c :sup:`-2`) - a :sup:`-3`\ (b :sup:`-3` + c :sup:`-3`)]

Barycentrics
~~~~~~~~~~~~

* :math:`g(a,b,c) : g(b,c,a) : g(c,a,b)`, where g(a,b,c) = af(a,b,c)

* **Kimberling (6, 9, 13) Search Value:** :math:`-0.616529833082`

Incidence
---------

:ref:`X(713) <X(713)>` lies on the circumcircle.

:ref:`X(713) <X(713)>` lies and on these lines:

{:ref:`32 <X(32)>`, :ref:`100 <X(100)>`}, {:ref:`101 <X(101)>`, :ref:`560 <X(560)>`}

Relations
---------

* :ref:`X(713) <X(713)>` = :term:`isogonal conjugate <isogonal-conjugate>` of :ref:`X(712) <X(712)>`
* :ref:`X(713) <X(713)>` = :term:`isotomic conjugate <isotomic-conjugate>` of X(35531)

Construction
------------

.. literalinclude:: model.py
   :language: python
