:order: 769
:type: center
:canonical_id: X(769)
:dependencies: X(768), X(35553)

.. _X(769):

X(769) = o-(- 4, - 3) CIRCUMCIRCLE POINT
========================================

.. figure:: x-00769.svg
   :alt: X(769) = o-(- 4, - 3) CIRCUMCIRCLE POINT
   :align: center

   **X(769) = o-(- 4, - 3) CIRCUMCIRCLE POINT** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`f(a,b,c) : f(b,c,a) : f(c,a,b)`, where f(a,b,c) = 1/[a :sup:`-5`\ (b :sup:`-3` - c :sup:`-3`) + a :sup:`-4`\ (b :sup:`-4` - c :sup:`-4`)]

Barycentrics
~~~~~~~~~~~~

* :math:`g(a,b,c) : g(b,c,a) : g(c,a,b)`, where g(a,b,c) = af(a,b,c)

* **Kimberling (6, 9, 13) Search Value:** :math:`0.558566389944`

Notes
-----

.. container:: note-item

   1/[a\ :sup:`m-1`\ (b\ :sup:`n` - c\ :sup:`n`) + a\ :sup:`n-1`\ (b\ :sup:`m` - c\ :sup:`m`)],

   hence the name "(m, n)-circumcircle point".

Incidence
---------

:ref:`X(769) <X(769)>` lies on the circumcircle. This is one of several points of the form given by first trilinear

Relations
---------

* :ref:`X(769) <X(769)>` = :term:`isogonal conjugate <isogonal-conjugate>` of :ref:`X(768) <X(768)>`
* :ref:`X(769) <X(769)>` = :term:`isotomic conjugate <isotomic-conjugate>` of X(35553)

Construction
------------

.. literalinclude:: model.py
   :language: python
