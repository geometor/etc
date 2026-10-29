:order: 598
:type: center
:canonical_id: X(598)
:dependencies: X(2), X(4), X(6), X(30), X(48), X(76), X(98), X(187), X(262), X(351), X(381), X(523), X(524), X(574), X(575), X(599), X(671), X(5094), X(38402)

.. _X(598):

X(598) = ISOGONAL CONJUGATE OF X(574)
=====================================

.. figure:: x-00598.svg
   :alt: X(598) = ISOGONAL CONJUGATE OF X(574)
   :align: center

   **X(598) = ISOGONAL CONJUGATE OF X(574)** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`bc/(a^{2} - 2b^{2} - 2c^{2}) : ca/(b^{2} - 2c^{2} - 2a^{2}) : ab/(c^{2} - 2a^{2} - 2b^{2})`

Barycentrics
~~~~~~~~~~~~

* :math:`1/(a^{2} - 2b^{2} - 2c^{2}) : 1/(b^{2} - 2c^{2} - 2a^{2}) : 1/(c^{2} - 2a^{2} - 2b^{2})`

* **Kimberling (6, 9, 13) Search Value:** :math:`0.826083882460`

Notes
-----

.. container:: note-item

   The Lemoine ellipse is the ellipse inscribed in triangle ABC having :ref:`X(2) <X(2)>` and :ref:`X(6) <X(6)>` as foci. Let A' be where this ellipse meets sideline BC, and define B' and C' cyclically. Then triangles ABC and A'B'C' are perspective, and their perspector is :ref:`X(598) <X(598)>`. (:person:`Bernard Gibert <bernard-gibert>`, 1/5/01, :cite:`Hyacinthos #2334 <hyacinthos>`)

Incidence
---------

:ref:`X(598) <X(598)>` lies and on these lines:

{:ref:`2 <X(2)>`, :ref:`187 <X(187)>`}, {:ref:`4 <X(4)>`, :ref:`575 <X(575)>`}, {:ref:`6 <X(6)>`, :ref:`671 <X(671)>`}, {:ref:`30 <X(30)>`, :ref:`262 <X(262)>`}, {:ref:`76 <X(76)>`, :ref:`524 <X(524)>`}, {:ref:`98 <X(98)>`, :ref:`381 <X(381)>`}

Relations
---------

* :ref:`X(598) <X(598)>` = :term:`isogonal conjugate <isogonal-conjugate>` of :ref:`X(574) <X(574)>`
* :ref:`X(598) <X(598)>` = :term:`isotomic conjugate <isotomic-conjugate>` of :ref:`X(599) <X(599)>`
* :ref:`X(598) <X(598)>` = :term:`cyclocevian conjugate <cyclocevian-conjugate>` of isogonal conjugate of X(38402)
* :ref:`X(598) <X(598)>` = :term:`trilinear pole <trilinear-pole>` of line :ref:`X(351) <X(351)>`\ \ :ref:`X(523) <X(523)>` (the Euler line of the 1st and 2nd Parry triangles)
* :ref:`X(598) <X(598)>` = pole wrt polar circle of :term:`trilinear polar <trilinear-polar>` of X(5094)
* :ref:`X(598) <X(598)>` = :ref:`X(48) <X(48)>`-:term:`isoconjugate <isoconjugate>` (polar conjugate) of X(5094)
* :ref:`X(598) <X(598)>` = perspector of ABC and anti-Artzt triangle
* :ref:`X(598) <X(598)>` = :ref:`X(262) <X(262)>`-of-anti-Artzt-triangle

Construction
------------

.. literalinclude:: model.py
   :language: python
