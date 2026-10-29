:order: 697
:type: center
:canonical_id: X(697)
:dependencies: X(100), X(560), X(696), X(35523)

.. _X(697):

X(697) = EVEN (- 4, - 3) CIRCUMCIRCLE POINT
===========================================

.. figure:: x-00697.svg
   :alt: X(697) = EVEN (- 4, - 3) CIRCUMCIRCLE POINT
   :align: center

   **X(697) = EVEN (- 4, - 3) CIRCUMCIRCLE POINT** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`f(a,b,c) : f(b,c,a) : f(c,a,b)`, where f(a,b,c) = 1/[a :sup:`-5`\ (b :sup:`-3` + c :sup:`-3`) - a :sup:`-4`\ (b :sup:`-4` + c :sup:`-4`)]

Barycentrics
~~~~~~~~~~~~

* :math:`g(a,b,c) : g(b,c,a) : g(c,a,b)`, where g(a,b,c) = af(a,b,c)

* **Kimberling (6, 9, 13) Search Value:** :math:`-0.534181898858`

Notes
-----

.. container:: note-item

   1/[a\ :sup:`m-1`\ (b\ :sup:`n` + c\ :sup:`n`) - a\ :sup:`n-1`\ (b\ :sup:`m` + c\ :sup:`m`)],

   hence the name "(m, n)-circumcircle point".

Incidence
---------

:ref:`X(697) <X(697)>` lies on the circumcircle. This is one of several points of the form given by first trilinear

:ref:`X(697) <X(697)>` lies and on these lines:

{:ref:`100 <X(100)>`, :ref:`560 <X(560)>`}

Relations
---------

* :ref:`X(697) <X(697)>` = :term:`isogonal conjugate <isogonal-conjugate>` of :ref:`X(696) <X(696)>`
* :ref:`X(697) <X(697)>` = :term:`isotomic conjugate <isotomic-conjugate>` of X(35523)

Construction
------------

.. literalinclude:: model.py
   :language: python
