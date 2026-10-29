:order: 501
:type: center
:canonical_id: X(501)
:dependencies: X(1), X(10), X(21), X(35), X(36), X(58), X(110), X(214), X(215), X(229), X(284), X(502), X(572), X(595), X(662), X(759), X(942), X(992), X(1326), X(1364), X(1385)

.. _X(501):

X(501) = MIQUEL ASSOCIATE OF INCENTER
=====================================

.. figure:: x-00501.svg
   :alt: X(501) = MIQUEL ASSOCIATE OF INCENTER
   :align: center

   **X(501) = MIQUEL ASSOCIATE OF INCENTER** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`f(a,b,c) : f(b,c,a) : f(c,a,b)`, where, f(a,b,c) = a[a\ :sup:`3` - b\ :sup:`3` - c\ :sup:`3` - bc(a + b + c) + ab(a - b) + ac(a - c)]/(b + c)

* **Kimberling (6, 9, 13) Search Value:** :math:`4.266239413525`

Notes
-----

.. container:: note-item

   Barycentrics af(a,b,c) : bf(b,c,a) : cf(c,a,b)

.. container:: note-item

   Miquel's theorem states that if A', B', C' are points (other than A, B, C) on sidelines BC, CA, AB, respectively, then the circles AB'C', BC'A', CA'B' meet at a point. Suppose P is a point and A' = P∩BC, B' = P∩CA, C' = P∩AB; the point in which the three circles is the *Miquel associate* of P. (:person:`Paul Yiu <paul-yiu>`, 7/6/99)

Incidence
---------

:ref:`X(501) <X(501)>` lies and on these lines:

{:ref:`1 <X(1)>`, :ref:`229 <X(229)>`}, {:ref:`10 <X(10)>`, :ref:`662 <X(662)>`}, {:ref:`21 <X(21)>`, :ref:`214 <X(214)>`}, {:ref:`35 <X(35)>`, :ref:`110 <X(110)>`}, {:ref:`36 <X(36)>`, :ref:`58 <X(58)>`}, {:ref:`215 <X(215)>`, 1364}, {:ref:`284 <X(284)>`, :ref:`942 <X(942)>`}, {:ref:`572 <X(572)>`, :ref:`992 <X(992)>`}, {:ref:`595 <X(595)>`, 1326}, {:ref:`759 <X(759)>`, 1385}

Relations
---------

* :ref:`X(501) <X(501)>` = :term:`isogonal conjugate <isogonal-conjugate>` of :ref:`X(502) <X(502)>`

Construction
------------

.. literalinclude:: model.py
   :language: python
