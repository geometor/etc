:order: 156
:type: center
:canonical_id: X(156)
:dependencies: X(3), X(4), X(5), X(25), X(26), X(49), X(54), X(74), X(110), X(143), X(154), X(155), X(184), X(381), X(546), X(550), X(578), X(1092), X(1614)

.. _X(156):

X(156) = X(5)-OF-TANGENTIAL-TRIANGLE
====================================

.. figure:: x-00156.svg
   :alt: X(156) = X(5)-OF-TANGENTIAL-TRIANGLE
   :align: center

   **X(156) = X(5)-OF-TANGENTIAL-TRIANGLE** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`f(a,b,c) : f(b,c,a) : f(c,a,b)`, where f(a,b,c) = a[b\ :sup:`2`\ y/v + c\ :sup:`2`\ z/w - a\ :sup:`2`\ x/u],, u = u(A,B,C) = sin 2A, v = u(B,C,A), w = u(C,A,B);, x = x(A,B,C) = u\ :sup:`2`\ (v\ :sup:`2` + w\ :sup:`2`) - (v\ :sup:`2` - w\ :sup:`2`)\ :sup:`2`, y = x(B,C,A), z = x(C,A,B)

Barycentrics
~~~~~~~~~~~~

* :math:`a^2 (a^8 - 3 a^6 (b^2 + c^2) + a^4 (3 b^4 + 2 b^2 c^2 + 3 c^4) - a^2 (b^6 + c^6) + b^2 c^2 (b^2 - c^2)^2) : :`

* **Kimberling (6, 9, 13) Search Value:** :math:`-1.190548227388`

Notes
-----

.. container:: note-item

   Let O\ :sub:`A` be the reflection of :ref:`X(3) <X(3)>` in BC, and define O\ :sub:`B` and O\ :sub:`C` cyclically. Let O':sub:`A` be the circumcenter of AO\ :sub:`B`\ O\ :sub:`C`, and define O':sub:`B` and O':sub:`C` cyclically. :ref:`X(156) <X(156)>` is the circumcenter of O':sub:`A`\ O':sub:`B`\ O':sub:`C`. (:person:`Randy Hutson <randy-hutson>`, July 11, 2019)

.. container:: note-item

   Let A'B'C' be the triangle described in :cite:`ADGEOM #2697 <adgeom>` (8/26/2015, Tran Quang Hung). Then :ref:`X(156) <X(156)>` = :ref:`X(5) <X(5)>`-of-A'B'C'. (Randy Hutson, July 11, 2019)

.. container:: note-item

   :ref:`X(156) <X(156)>` is the {:ref:`X(154) <X(154)>`,\ :ref:`X(155) <X(155)>`}-harmonic conjugate of :ref:`X(26) <X(26)>`. For a list of harmonic conjugates, click **Tables** at the top of this page.

Incidence
---------

:ref:`X(156) <X(156)>` lies and on these lines:

{:ref:`3 <X(3)>`, :ref:`74 <X(74)>`}, {:ref:`4 <X(4)>`, :ref:`49 <X(49)>`}, {:ref:`5 <X(5)>`, :ref:`184 <X(184)>`}, {:ref:`25 <X(25)>`, :ref:`143 <X(143)>`}, {:ref:`26 <X(26)>`, :ref:`154 <X(154)>`}, {:ref:`54 <X(54)>`, :ref:`381 <X(381)>`}, {:ref:`546 <X(546)>`, :ref:`578 <X(578)>`}, {:ref:`550 <X(550)>`, 1092}

Relations
---------

* :ref:`X(156) <X(156)>` = midpoint of :ref:`X(26) <X(26)>` and :ref:`X(155) <X(155)>`
* :ref:`X(156) <X(156)>` = :ref:`X(5) <X(5)>`-of-tangential-triangle
* :ref:`X(156) <X(156)>` = {:ref:`X(110) <X(110)>`,X(1614)}-harmonic conjugate of :ref:`X(3) <X(3)>`
* :ref:`X(156) <X(156)>` = intouch-to-ABC :term:`functional image <functional-image>` of :ref:`X(5) <X(5)>`

Construction
------------

.. literalinclude:: model.py
   :language: python
