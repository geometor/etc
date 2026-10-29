:order: 167
:type: center
:canonical_id: X(167)
:dependencies: X(1), X(8), X(9), X(164), X(165), X(166), X(174), X(188)

.. _X(167):

X(167) = NAGEL POINT OF EXCENTRAL TRIANGLE
==========================================

.. figure:: x-00167.svg
   :alt: X(167) = NAGEL POINT OF EXCENTRAL TRIANGLE
   :align: center

   **X(167) = NAGEL POINT OF EXCENTRAL TRIANGLE** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`f(A,B,C) : f(B,C,A) : f(C,A,B)`, where, f(A,B,C) = s(B,C,A)t(B,C,A) + s(C,A,B)t(C,A,B) - s(A,B,C)t(A,B,C),, where s(A,B,C) = sin(A/2) and t(A,B,C) = (cos B/2 + cos C/2 - cos A/2) sec A/2

* **Kimberling (6, 9, 13) Search Value:** :math:`14.236467851795`

Notes
-----

.. container:: note-item

   Barycentrics g(A,B,C) : g(B,C,A) : g(C,A,B), where g(A,B,C) = (sin A)f(A,B,C)

Incidence
---------

:ref:`X(167) <X(167)>` lies and on these lines:

{:ref:`1 <X(1)>`, :ref:`174 <X(174)>`}, {:ref:`164 <X(164)>`, :ref:`165 <X(165)>`}, {:ref:`166 <X(166)>`, :ref:`188 <X(188)>`}

Relations
---------

* :ref:`X(167) <X(167)>` = :ref:`X(8) <X(8)>`-of-:term:`excentral triangle <excentral-triangle>`
* :ref:`X(167) <X(167)>` = :ref:`X(9) <X(9)>`-:term:`aleph conjugate <aleph-conjugate>` of :ref:`X(166) <X(166)>`

Construction
------------

.. literalinclude:: model.py
   :language: python
