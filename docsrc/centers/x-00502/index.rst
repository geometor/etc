:order: 502
:type: center
:canonical_id: X(502)
:dependencies: X(1), X(10), X(12), X(42), X(58), X(191), X(313), X(501), X(594), X(1089), X(3678), X(3969), X(14873), X(14874), X(17791), X(21043)

.. _X(502):

X(502) = ISOGONAL CONJUGATE OF X(501)
=====================================

.. figure:: x-00502.svg
   :alt: X(502) = ISOGONAL CONJUGATE OF X(501)
   :align: center

   **X(502) = ISOGONAL CONJUGATE OF X(501)** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`f(a,b,c) : f(b,c,a) : f(c,a,b)`, where f(a,b,c) = bc(b + c)/[a\ :sup:`3` - b\ :sup:`3` - c\ :sup:`3` - bc(a + b + c) + ab(a - b) + ac(a - c)]

Barycentrics
~~~~~~~~~~~~

* :math:`af(a,b,c) : bf(b,c,a) : cf(c,a,b)`

* **Kimberling (6, 9, 13) Search Value:** :math:`-2.150446441377`

Notes
-----

.. container:: note-item

   Let A'B'C' be the :term:`incentral triangle <incentral-triangle>`. Let BCA'' be the triangle similar to A'B'C' such that the segment AA'' crosses the line BC. Define B'' and C'' cyclically. The lines AA'', BB'', CC'' concur in :ref:`X(502) <X(502)>`. (:person:`Randy Hutson <randy-hutson>`, 9/23/2011)

Incidence
---------

:ref:`X(502) <X(502)>` lies and on these lines:

{:ref:`10 <X(10)>`, :ref:`191 <X(191)>`}, {:ref:`12 <X(12)>`, 14873}, {:ref:`42 <X(42)>`, 14874}, {:ref:`58 <X(58)>`, 21043}, {:ref:`313 <X(313)>`, 17791}, {:ref:`594 <X(594)>`, 3678}, {1089, 3969}

Relations
---------

* :ref:`X(502) <X(502)>` = :term:`isogonal conjugate <isogonal-conjugate>` of :ref:`X(501) <X(501)>`
* :ref:`X(502) <X(502)>` = :ref:`X(1) <X(1)>`-:term:`cross conjugate <cross-conjugate>` of :ref:`X(10) <X(10)>`

Construction
------------

.. literalinclude:: model.py
   :language: python
