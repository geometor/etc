:order: 727
:type: center
:canonical_id: X(727)
:dependencies: X(1), X(6), X(31), X(32), X(43), X(58), X(99), X(101), X(190), X(238), X(726), X(789), X(932), X(934), X(985), X(1106), X(35538)

.. _X(727):

X(727) = EVEN (- 2, -1) CIRCUMCIRCLE POINT
==========================================

.. figure:: x-00727.svg
   :alt: X(727) = EVEN (- 2, -1) CIRCUMCIRCLE POINT
   :align: center

   **X(727) = EVEN (- 2, -1) CIRCUMCIRCLE POINT** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`f(a,b,c) : f(b,c,a) : f(c,a,b)`, where f(a,b,c) = 1/[a :sup:`-3`\ (b :sup:`-1` + c :sup:`-1`) - a :sup:`-2`\ (b :sup:`-2` + c :sup:`-2`)]

Barycentrics
~~~~~~~~~~~~

* :math:`g(a,b,c) : g(b,c,a) : g(c,a,b)`, where g(a,b,c) = af(a,b,c)

* **Kimberling (6, 9, 13) Search Value:** :math:`-0.618761834841`

Incidence
---------

:ref:`X(727) <X(727)>` lies on the circumcircle.

:ref:`X(727) <X(727)>` lies and on these lines:

{:ref:`1 <X(1)>`, :ref:`932 <X(932)>`}, {:ref:`31 <X(31)>`, :ref:`43 <X(43)>`}, {:ref:`32 <X(32)>`, :ref:`101 <X(101)>`}, {:ref:`58 <X(58)>`, :ref:`99 <X(99)>`}, {:ref:`789 <X(789)>`, :ref:`985 <X(985)>`}, {:ref:`934 <X(934)>`, 1106}

Relations
---------

* :ref:`X(727) <X(727)>` = :term:`isogonal conjugate <isogonal-conjugate>` of :ref:`X(726) <X(726)>`
* :ref:`X(727) <X(727)>` = :term:`isotomic conjugate <isotomic-conjugate>` of X(35538)
* :ref:`X(727) <X(727)>` = :ref:`X(238) <X(238)>`-:term:`cross conjugate <cross-conjugate>` of :ref:`X(58) <X(58)>`
* :ref:`X(727) <X(727)>` = Ψ(:ref:`X(190) <X(190)>`, :ref:`X(6) <X(6)>`)

Construction
------------

.. literalinclude:: model.py
   :language: python
