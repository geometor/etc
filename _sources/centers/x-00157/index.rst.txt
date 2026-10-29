:order: 157
:type: center
:canonical_id: X(157)
:dependencies: X(3), X(6), X(22), X(25), X(53), X(66), X(127), X(161), X(183), X(206), X(216), X(248), X(264), X(418), X(520), X(2909), X(22391)

.. _X(157):

X(157) = X(6)-OF-TANGENTIAL-TRIANGLE
====================================

.. figure:: x-00157.svg
   :alt: X(157) = X(6)-OF-TANGENTIAL-TRIANGLE
   :align: center

   **X(157) = X(6)-OF-TANGENTIAL-TRIANGLE** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`f(a,b,c) : f(b,c,a) : f(c,a,b)`, where f(a,b,c) = a[b\ :sup:`3`\ cos B + c\ :sup:`3`\ cos C - a\ :sup:`3`\ cos A], = g(a,b,c) : g(b,c,a) : g(c,a,b), where, g(a,b,c) = a[a\ :sup:`6` - b\ :sup:`6` - c\ :sup:`6` - a\ :sup:`4`\ (b\ :sup:`2` + c\ :sup:`2`) + b\ :sup:`4`\ (c\ :sup:`2` + a\ :sup:`2`) + c\ :sup:`4`\ (a\ :sup:`2` + b\ :sup:`2`)]

* **Kimberling (6, 9, 13) Search Value:** :math:`-1.134813455477`

Notes
-----

.. container:: note-item

   Barycentrics af(a,b,c) : bf(b,c,a) : cf(c,a,b)

Incidence
---------

:ref:`X(157) <X(157)>` lies and on these lines:

{:ref:`3 <X(3)>`, :ref:`66 <X(66)>`}, {:ref:`6 <X(6)>`, :ref:`248 <X(248)>`}, {:ref:`22 <X(22)>`, :ref:`183 <X(183)>`}, {:ref:`25 <X(25)>`, :ref:`53 <X(53)>`}, {:ref:`161 <X(161)>`, :ref:`418 <X(418)>`}, {:ref:`206 <X(206)>`, :ref:`216 <X(216)>`}

Relations
---------

* :ref:`X(157) <X(157)>` = :term:`isogonal conjugate <isogonal-conjugate>` of :term:`anticomplement <anticomplement>` of X(22391)
* :ref:`X(157) <X(157)>` = :term:`isotomic conjugate <isotomic-conjugate>` of isogonal conjugate of X(2909)
* :ref:`X(157) <X(157)>` = :ref:`X(264) <X(264)>`-:term:`Ceva conjugate <ceva-conjugate>` of :ref:`X(6) <X(6)>`
* :ref:`X(157) <X(157)>` = :term:`crosssum <crosssum>` of :ref:`X(127) <X(127)>` and :ref:`X(520) <X(520)>`
* :ref:`X(157) <X(157)>` = :ref:`X(6) <X(6)>`-of-tangential-triangle
* :ref:`X(157) <X(157)>` = perspector of circumcircle wrt Schroeter triangle
* :ref:`X(157) <X(157)>` = perspector of polar circle wrt :term:`tangential triangle <tangential-triangle>`
* :ref:`X(157) <X(157)>` = intouch-to-ABC :term:`functional image <functional-image>` of :ref:`X(6) <X(6)>`

Construction
------------

.. literalinclude:: model.py
   :language: python
