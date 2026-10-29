:order: 731
:type: center
:canonical_id: X(731)
:dependencies: X(1), X(32), X(100), X(730), X(789), X(825), X(869), X(35539)

.. _X(731):

X(731) = EVEN (- 2, 1) CIRCUMCIRCLE POINT
=========================================

.. figure:: x-00731.svg
   :alt: X(731) = EVEN (- 2, 1) CIRCUMCIRCLE POINT
   :align: center

   **X(731) = EVEN (- 2, 1) CIRCUMCIRCLE POINT** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`f(a,b,c) : f(b,c,a) : f(c,a,b)`, where f(a,b,c) = 1/[a :sup:`-3`\ (b\ :sup:`1` + c\ :sup:`1`) - a\ :sup:`0`\ (b :sup:`-2` + c :sup:`-2`)]

Barycentrics
~~~~~~~~~~~~

* :math:`g(a,b,c) : g(b,c,a) : g(c,a,b)`, where g(a,b,c) = af(a,b,c)

* **Kimberling (6, 9, 13) Search Value:** :math:`-0.377993014271`

Incidence
---------

:ref:`X(731) <X(731)>` lies on the circumcircle.

:ref:`X(731) <X(731)>` lies and on these lines:

{:ref:`1 <X(1)>`, :ref:`789 <X(789)>`}, {:ref:`32 <X(32)>`, :ref:`825 <X(825)>`}, {:ref:`100 <X(100)>`, :ref:`869 <X(869)>`}

Relations
---------

* :ref:`X(731) <X(731)>` = :term:`isogonal conjugate <isogonal-conjugate>` of :ref:`X(730) <X(730)>`
* :ref:`X(731) <X(731)>` = :term:`isotomic conjugate <isotomic-conjugate>` of X(35539)

Construction
------------

.. literalinclude:: model.py
   :language: python
