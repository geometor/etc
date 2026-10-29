:order: 212
:type: center
:canonical_id: X(212)
:dependencies: X(1), X(3), X(4), X(6), X(7), X(9), X(11), X(31), X(33), X(34), X(35), X(40), X(41), X(47), X(48), X(55), X(56), X(57), X(63), X(73), X(78), X(92), X(109), X(154), X(165), X(184), X(198), X(201), X(219), X(228), X(238), X(273), X(278), X(283), X(312), X(497), X(514), X(582), X(643), X(748), X(939), X(942), X(1040), X(1946), X(3064)

.. _X(212):

X(212) = X(9)-CEVA CONJUGATE OF X(41)
=====================================

.. figure:: x-00212.svg
   :alt: X(212) = X(9)-CEVA CONJUGATE OF X(41)
   :align: center

   **X(212) = X(9)-CEVA CONJUGATE OF X(41)** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`(\cos A)(1 + \cos A) : (\cos B)(1 + \cos B) : (\cos C)(1 + \cos C), = (\cos A)\cos^{2}(A/2) : (\cos B)\cos^{2}(B/2) : (\cos C)\cos^{2}(C/2), = a^{2}(b + c - a)(b^{2} + c^{2} - a^{2}) : b^{2}(c + a - b)(c^{2} + a^{2} - b^{2}) : c^{2}(a + b - c)(a^{2} + b^{2} - c^{2})`

* **Kimberling (6, 9, 13) Search Value:** :math:`4.122746567678`

Notes
-----

.. container:: note-item

   Barycentrics (sin 2A)(1 + cos A) : (sin 2B)(1 + cos B) : (sin 2C)(1 + cos C)

.. container:: note-item

   The :term:`trilinear polar <trilinear-polar>` of :ref:`X(212) <X(212)>` passes through X(1946). (:person:`Randy Hutson <randy-hutson>`, June 7, 2019)

Incidence
---------

:ref:`X(212) <X(212)>` lies and on these lines:

{:ref:`1 <X(1)>`, :ref:`201 <X(201)>`}, {:ref:`3 <X(3)>`, :ref:`73 <X(73)>`}, {:ref:`6 <X(6)>`, :ref:`31 <X(31)>`}, {:ref:`9 <X(9)>`, :ref:`33 <X(33)>`}, {:ref:`11 <X(11)>`, :ref:`748 <X(748)>`}, {:ref:`34 <X(34)>`, :ref:`40 <X(40)>`}, {:ref:`35 <X(35)>`, :ref:`47 <X(47)>`}, {:ref:`48 <X(48)>`, :ref:`184 <X(184)>`}, {:ref:`56 <X(56)>`, :ref:`939 <X(939)>`}, {:ref:`63 <X(63)>`, 1040}, {:ref:`78 <X(78)>`, :ref:`283 <X(283)>`}, {:ref:`109 <X(109)>`, :ref:`165 <X(165)>`}, {:ref:`154 <X(154)>`, :ref:`198 <X(198)>`}, {:ref:`238 <X(238)>`, :ref:`497 <X(497)>`}, {:ref:`312 <X(312)>`, :ref:`643 <X(643)>`}, {:ref:`582 <X(582)>`, :ref:`942 <X(942)>`}

Relations
---------

* :ref:`X(212) <X(212)>` = :term:`isogonal conjugate <isogonal-conjugate>` of :ref:`X(273) <X(273)>`
* :ref:`X(212) <X(212)>` = :term:`crossdifference <crossdifference>` of every pair of points on line :ref:`X(514) <X(514)>`\ X(3064)
* :ref:`X(212) <X(212)>` = :ref:`X(4) <X(4)>`-:term:`isoconjugate <isoconjugate>` of :ref:`X(7) <X(7)>`
* :ref:`X(212) <X(212)>` = :ref:`X(57) <X(57)>`-isoconjugate of :ref:`X(92) <X(92)>`
* :ref:`X(212) <X(212)>` = X(i)-:term:`Ceva conjugate <ceva-conjugate>` of X(j) for these (i,j): (:ref:`3 <X(3)>`, :ref:`48 <X(48)>`), (:ref:`9 <X(9)>`, :ref:`41 <X(41)>`), (:ref:`283 <X(283)>`, :ref:`219 <X(219)>`)
* :ref:`X(212) <X(212)>` = :ref:`X(228) <X(228)>`-:term:`cross conjugate <cross-conjugate>` of :ref:`X(55) <X(55)>`
* :ref:`X(212) <X(212)>` = :term:`crosspoint <crosspoint>` of X(i) and X(j) for these (i,j): (:ref:`3 <X(3)>`, :ref:`219 <X(219)>`), (:ref:`9 <X(9)>`, :ref:`78 <X(78)>`)
* :ref:`X(212) <X(212)>` = :term:`crosssum <crosssum>` of X(i) and X(j) for these (i,j): (:ref:`4 <X(4)>`, :ref:`278 <X(278)>`), (:ref:`34 <X(34)>`, :ref:`57 <X(57)>`)
* :ref:`X(212) <X(212)>` = :ref:`X(212) <X(212)>`-:term:`beth conjugate <beth-conjugate>` of :ref:`X(184) <X(184)>`

Construction
------------

.. literalinclude:: model.py
   :language: python
