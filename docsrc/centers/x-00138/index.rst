:order: 138
:type: center
:canonical_id: X(138)
:dependencies: X(51), X(53), X(111), X(122), X(130), X(137), X(233)

.. _X(138):

X(138) = X(111)-OF-ORTHIC-TRIANGLE
==================================

.. figure:: x-00138.svg
   :alt: X(138) = X(111)-OF-ORTHIC-TRIANGLE
   :align: center

   **X(138) = X(111)-OF-ORTHIC-TRIANGLE** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`(v + w) \sec A : (w + u) \sec B : (u + v) \sec C`, where, u = u(A,B,C) = (sin 2A)/(2 sin\ :sup:`2`\ 2A - sin\ :sup:`2`\ 2B - sin\ :sup:`2`\ 2C), v = u(B,C,A), w = u(C,A,B)

* **Kimberling (6, 9, 13) Search Value:** :math:`3.323272182949`

Notes
-----

.. container:: note-item

   Barycentrics (v + w) tan A : (w + u) tan B : (u + v) tan C

Incidence
---------

:ref:`X(138) <X(138)>` lies on the nine-point circle

:ref:`X(138) <X(138)>` lies and on these lines:

{:ref:`51 <X(51)>`, :ref:`130 <X(130)>`}, {:ref:`53 <X(53)>`, :ref:`137 <X(137)>`}, {:ref:`122 <X(122)>`, :ref:`233 <X(233)>`}

Relations
---------

* :ref:`X(138) <X(138)>` = :ref:`X(111) <X(111)>`-of-:term:`orthic triangle <orthic-triangle>`
* :ref:`X(138) <X(138)>` = Λ(:ref:`X(51) <X(51)>`, :ref:`X(53) <X(53)>`), wrt orthic triangle

Construction
------------

.. literalinclude:: model.py
   :language: python
