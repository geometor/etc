:order: 839
:type: center
:canonical_id: X(839)
:dependencies: X(6), X(110), X(321), X(334), X(668), X(741), X(838)

.. _X(839):

X(839) = o-(3, 4) CIRCUMCIRCLE POINT
====================================

.. figure:: x-00839.svg
   :alt: X(839) = o-(3, 4) CIRCUMCIRCLE POINT
   :align: center

   **X(839) = o-(3, 4) CIRCUMCIRCLE POINT** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`f(a,b,c) : f(b,c,a) : f(c,a,b)`, where f(a,b,c) = 1/[a\ :sup:`2`\ (b\ :sup:`4` - c\ :sup:`4`) + a\ :sup:`3`\ (b\ :sup:`3` - c\ :sup:`3`)]

Barycentrics
~~~~~~~~~~~~

* :math:`g(a,b,c) : g(b,c,a) : g(c,a,b)`, where g(a,b,c) = af(a,b,c)

* **Kimberling (6, 9, 13) Search Value:** :math:`4.543806593145`

Incidence
---------

:ref:`X(839) <X(839)>` lies on the circumcircle.

:ref:`X(839) <X(839)>` lies and on these lines:

{:ref:`110 <X(110)>`, :ref:`668 <X(668)>`}, {:ref:`334 <X(334)>`, :ref:`741 <X(741)>`}

Relations
---------

* :ref:`X(839) <X(839)>` = :term:`isogonal conjugate <isogonal-conjugate>` of :ref:`X(838) <X(838)>`
* :ref:`X(839) <X(839)>` = :term:`trilinear pole <trilinear-pole>` of line :ref:`X(6) <X(6)>`\ \ :ref:`X(321) <X(321)>`
* :ref:`X(839) <X(839)>` = Ψ(:ref:`X(6) <X(6)>`, :ref:`X(321) <X(321)>`)

Construction
------------

.. literalinclude:: model.py
   :language: python
