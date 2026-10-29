:order: 500
:type: center
:canonical_id: X(500)
:dependencies: X(1), X(3), X(6), X(30), X(35), X(79), X(582), X(651), X(942), X(943)

.. _X(500):

X(500) = ORTHOCENTER OF THE INCENTRAL TRIANGLE
==============================================

.. figure:: x-00500.svg
   :alt: X(500) = ORTHOCENTER OF THE INCENTRAL TRIANGLE
   :align: center

   **X(500) = ORTHOCENTER OF THE INCENTRAL TRIANGLE** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`a(b^{2} +c^{2} - a^{2} + bc)[2abc + (b + c)(a^{2} - (b - c)^{2})] : :`

* **Kimberling (6, 9, 13) Search Value:** :math:`3.085237628787`

Incidence
---------

:ref:`X(500) <X(500)>` lies and on these lines:

{:ref:`1 <X(1)>`, :ref:`30 <X(30)>`}, {:ref:`3 <X(3)>`, :ref:`6 <X(6)>`}, {:ref:`651 <X(651)>`, :ref:`943 <X(943)>`}

Relations
---------

* :ref:`X(500) <X(500)>` = inverse-in-Brocard-circle of :ref:`X(582) <X(582)>`
* :ref:`X(500) <X(500)>` = :term:`crosspoint <crosspoint>` of :ref:`X(1) <X(1)>` and :ref:`X(35) <X(35)>`
* :ref:`X(500) <X(500)>` = :term:`crosssum <crosssum>` of :ref:`X(1) <X(1)>` and :ref:`X(79) <X(79)>`
* :ref:`X(500) <X(500)>` = :ref:`X(1) <X(1)>`-:term:`Ceva conjugate <ceva-conjugate>` of :ref:`X(942) <X(942)>`

Construction
------------

.. literalinclude:: model.py
   :language: python
