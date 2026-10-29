:order: 755
:type: center
:canonical_id: X(755)
:dependencies: X(6), X(39), X(76), X(99), X(110), X(141), X(689), X(733), X(754), X(827), X(882), X(32473), X(35549)

.. _X(755):

X(755) = EVEN (0, 4) CIRCUMCIRCLE POINT
=======================================

.. figure:: x-00755.svg
   :alt: X(755) = EVEN (0, 4) CIRCUMCIRCLE POINT
   :align: center

   **X(755) = EVEN (0, 4) CIRCUMCIRCLE POINT** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`f(a,b,c) : f(b,c,a) : f(c,a,b)`, where f(a,b,c) = 1/[a :sup:`-1`\ (b\ :sup:`4` + c\ :sup:`4`) - a\ :sup:`3`\ (b\ :sup:`0` + c\ :sup:`0`)]

Barycentrics
~~~~~~~~~~~~

* :math:`g(a,b,c) : g(b,c,a) : g(c,a,b)`, where g(a,b,c) = af(a,b,c)

* **Kimberling (6, 9, 13) Search Value:** :math:`3.469059259665`

Incidence
---------

:ref:`X(755) <X(755)>` lies on the circumcircle.

:ref:`X(755) <X(755)>` lies and on these lines:

{:ref:`6 <X(6)>`, :ref:`827 <X(827)>`}, {:ref:`39 <X(39)>`, :ref:`110 <X(110)>`}, {:ref:`76 <X(76)>`, :ref:`689 <X(689)>`}, {:ref:`99 <X(99)>`, :ref:`141 <X(141)>`}, {:ref:`733 <X(733)>`, :ref:`882 <X(882)>`}

Relations
---------

* :ref:`X(755) <X(755)>` = :term:`isogonal conjugate <isogonal-conjugate>` of :ref:`X(754) <X(754)>`
* :ref:`X(755) <X(755)>` = :term:`isotomic conjugate <isotomic-conjugate>` of X(35549)
* :ref:`X(755) <X(755)>` = Thomson-isogonal conjugate of X(32473)
* :ref:`X(755) <X(755)>` = Lucas-isogonal conjugate of X(32473)

Construction
------------

.. literalinclude:: model.py
   :language: python
