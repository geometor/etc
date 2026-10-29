:order: 129
:type: center
:canonical_id: X(129)
:dependencies: X(5), X(51), X(52), X(53), X(98), X(115), X(130), X(137), X(139), X(389), X(1298), X(32428), X(34838)

.. _X(129):

X(129) = X(98)-OF-ORTHIC-TRIANGLE
=================================

.. figure:: x-00129.svg
   :alt: X(129) = X(98)-OF-ORTHIC-TRIANGLE
   :align: center

   **X(129) = X(98)-OF-ORTHIC-TRIANGLE** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`f(A,B,C) : f(B,C,A) : f(C,A,B)`, where, f(A,B,C) = (sec A)(sin 2A)(sin 2B + sin 2C) s(A,B,C) t(A,B,C),, s(A,B,C) = sin\ :sup:`4`\ (2B) + sin\ :sup:`4`\ (2C) - sin\ :sup:`2`\ (2A) sin\ :sup:`2`\ (2B) - sin\ :sup:`2`\ (2A) sin\ :sup:`2`\ (2C),, t(A,B,C) = sin\ :sup:`4`\ (2A) + sin\ :sup:`2`\ (2A) u(A,B,C) + v(A,B,C),, u(A,B,C) = sin 2B sin 2C - sin\ :sup:`2`\ (2B) - sin\ :sup:`2`\ (2C),, v(A,B,C) = (sin 2B sin 2C)(sin 2B - sin 2C)\ :sup:`2`

* **Kimberling (6, 9, 13) Search Value:** :math:`3.956071987550`

Notes
-----

.. container:: note-item

   Barycentrics g(A,B,C) : g(B,C,A) : g(C,A,B) where g(A,B,C) = (sin A) f(A,B,C)

Incidence
---------

:ref:`X(129) <X(129)>` lies on the nine-point circle

:ref:`X(129) <X(129)>` lies and on these lines:

{:ref:`5 <X(5)>`, :ref:`130 <X(130)>`}, {:ref:`51 <X(51)>`, :ref:`137 <X(137)>`}, {:ref:`52 <X(52)>`, :ref:`139 <X(139)>`}, {:ref:`115 <X(115)>`, :ref:`389 <X(389)>`}

Relations
---------

* :ref:`X(129) <X(129)>` = :ref:`X(98) <X(98)>`-of-:term:`orthic triangle <orthic-triangle>`.
* :ref:`X(129) <X(129)>` = reflection of :ref:`X(130) <X(130)>` in :ref:`X(5) <X(5)>`
* :ref:`X(129) <X(129)>` = :term:`complement <complement>` of X(1298)
* :ref:`X(129) <X(129)>` = :term:`anticomplement <anticomplement>` of X(34838)
* :ref:`X(129) <X(129)>` = :term:`complementary conjugate <complementary-conjugate>` of X(32428)
* :ref:`X(129) <X(129)>` = Λ(:ref:`X(5) <X(5)>`, :ref:`X(53) <X(53)>`), wrt orthic triangle
* :ref:`X(129) <X(129)>` = excentral-to-ABC :term:`functional image <functional-image>` of :ref:`X(98) <X(98)>`

Construction
------------

.. literalinclude:: model.py
   :language: python
