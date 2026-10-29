:order: 161
:type: center
:canonical_id: X(161)
:dependencies: X(6), X(22), X(25), X(26), X(63), X(68), X(157), X(343), X(418)

.. _X(161):

X(161) = X(63)-OF-TANGENTIAL-TRIANGLE
=====================================

.. figure:: x-00161.svg
   :alt: X(161) = X(63)-OF-TANGENTIAL-TRIANGLE
   :align: center

   **X(161) = X(63)-OF-TANGENTIAL-TRIANGLE** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`f(a,b,c) : f(b,c,a) : f(c,a,b)`, where, f(a,b,c) = a[(a\ :sup:`2` + b\ :sup:`2` + c\ :sup:`2`)sin\ :sup:`2`\ (2A) + (c\ :sup:`2` - b\ :sup:`2` - a\ :sup:`2`)sin\ :sup:`2`\ (2B) + (b\ :sup:`2` - c\ :sup:`2` - a\ :sup:`2`)sin\ :sup:`2`\ (2C)]

* **Kimberling (6, 9, 13) Search Value:** :math:`6.599863926710`

Notes
-----

.. container:: note-item

   Barycentrics g(a,b,c) : g(b,c,a) : g(c,a,b), where g(a,b,c) = af(a,b,c)

Incidence
---------

:ref:`X(161) <X(161)>` lies and on these lines:

{:ref:`6 <X(6)>`, :ref:`25 <X(25)>`}, {:ref:`22 <X(22)>`, :ref:`343 <X(343)>`}, {:ref:`26 <X(26)>`, :ref:`68 <X(68)>`}, {:ref:`157 <X(157)>`, :ref:`418 <X(418)>`}

Relations
---------

* :ref:`X(161) <X(161)>` = :ref:`X(63) <X(63)>`-of-:term:`tangential triangle <tangential-triangle>` if ABC is acute
* :ref:`X(161) <X(161)>` = :ref:`X(68) <X(68)>`-:term:`Ceva conjugate <ceva-conjugate>` of :ref:`X(6) <X(6)>`

Construction
------------

.. literalinclude:: model.py
   :language: python
