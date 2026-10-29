:order: 79
:type: center
:canonical_id: X(79)
:dependencies: X(1), X(2), X(3), X(8), X(9), X(12), X(21), X(30), X(33), X(34), X(35), X(36), X(46), X(55), X(57), X(65), X(80), X(90), X(104), X(191), X(226), X(314), X(319), X(320), X(388), X(442), X(481), X(482), X(484), X(592), X(650), X(758), X(946), X(1000), X(1030), X(1061), X(1063), X(2914), X(3065), X(3647), X(4802), X(6152)

.. _X(79):

X(79) = ISOGONAL CONJUGATE OF X(35)
===================================

.. figure:: x-00079.svg
   :alt: X(79) = ISOGONAL CONJUGATE OF X(35)
   :align: center

   **X(79) = ISOGONAL CONJUGATE OF X(35)** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`1/(1 + 2 \cos A) : :`
* :math:`bc/(b^{2} + c^{2} - a^{2} + bc)`
* :math:`(\sin A/2)(\sin 3B/2)(\sin 3C/2) : :`
* :math:`\sin(A/2) \csc(3A/2) : :`

Barycentrics
~~~~~~~~~~~~

* :math:`1/(b^{2} + c^{2} - a^{2} + bc) : :`
* :math:`1/(b c + 2 SA) : :`

* **Kimberling (6, 9, 13) Search Value:** :math:`0.046914305978`

Linear Combinations
-------------------

* :ref:`X(79) <X(79)>` = (2r + 3R)\*\ :ref:`X(1) <X(1)>` + 6r\*\ :ref:`X(2) <X(2)>` - 6r\*\ :ref:`X(3) <X(3)>` (:person:`Peter Moses <peter-moses>`, April 2, 2013)

Notes
-----

.. container:: note-item

   Let A' be the reflection of :ref:`X(1) <X(1)>` in sideline BC, and define B' and C' cyclically. Then the lines AA', BB', CC' concur in :ref:`X(79) <X(79)>`. (Eric Danneels, :cite:`Hyacinthos <hyacinthos>` 7892, 9/13/03)

.. container:: note-item

   A'B'C' is also the reflection triangle of :ref:`X(1) <X(1)>`. The lines AA', BB', CC' concur in :ref:`X(79) <X(79)>`. (:person:`Randy Hutson <randy-hutson>`, July 20, 2016)

.. container:: note-item

   Let P and Q be the intersections of line BC and circle {:ref:`X(1) <X(1)>`,2r}. Let X = :ref:`X(1) <X(1)>`. Let A' be the circumcenter of triangle PQX, and define B' and C' cyclically. The lines AA', BB', CC' concur in :ref:`X(79) <X(79)>`. (Compare to X(592), where the circle is the 1st Lemoine circle) (Randy Hutson, July 20, 2016)

.. container:: note-item

   Let A\ :sub:`25`\ B\ :sub:`25`\ C\ :sub:`25` be Gemini triangle 25. Let A' be the perspector of conic {A,B,C,B\ :sub:`25`,C\ :sub:`25`}}, and define B' and C' cyclically. The lines AA', BB', CC' concur in :ref:`X(79) <X(79)>`. (Randy Hutson, January 15, 2019)

.. container:: note-item

   A construction for :ref:`X(79) <X(79)>` appears in :person:`Dasari Naga Vijay Krishna <dasari-naga-vijay-krishna>`, `On the Feuerbach Triangle <http://forumgeom.fau.edu/FG2017volume17/FG201731.pdf>`__.

Incidence
---------

:ref:`X(79) <X(79)>` lies and on these lines:

{:ref:`1 <X(1)>`, :ref:`30 <X(30)>`}, {:ref:`2 <X(2)>`, 3647}, {:ref:`8 <X(8)>`, 758}, {:ref:`9 <X(9)>`, :ref:`46 <X(46)>`}, {:ref:`12 <X(12)>`, 484}, {:ref:`21 <X(21)>`, :ref:`36 <X(36)>`}, {:ref:`33 <X(33)>`, 1063}, {:ref:`34 <X(34)>`, 1061}, {:ref:`35 <X(35)>`, 226}, {:ref:`57 <X(57)>`, :ref:`90 <X(90)>`}, {:ref:`65 <X(65)>`, :ref:`80 <X(80)>`}, {104, 946}, {314, 320}, {388, 1000}

Relations
---------

* :ref:`X(79) <X(79)>` = reflection of X(191) in X(442)
* :ref:`X(79) <X(79)>` = :term:`isogonal conjugate <isogonal-conjugate>` of :ref:`X(35) <X(35)>`
* :ref:`X(79) <X(79)>` = :term:`isotomic conjugate <isotomic-conjugate>` of X(319)
* :ref:`X(79) <X(79)>` = :term:`cevapoint <cevapoint>` of X(481) and X(482)
* :ref:`X(79) <X(79)>` = :term:`crosssum <crosssum>` of :ref:`X(55) <X(55)>` and X(1030)
* :ref:`X(79) <X(79)>` = :term:`anticomplement <anticomplement>` of X(3647)
* :ref:`X(79) <X(79)>` = X(2914) of Fuhrmann triangle
* :ref:`X(79) <X(79)>` = :term:`antigonal image <antigonal-image>` of X(3065)
* :ref:`X(79) <X(79)>` = :term:`trilinear pole <trilinear-pole>` of line X(650)X(4802)
* :ref:`X(79) <X(79)>` = perspector of ABC and extraversion triangle of :ref:`X(80) <X(80)>`
* :ref:`X(79) <X(79)>` = Hofstadter -1/2 point
* :ref:`X(79) <X(79)>` = trilinear pole of line X(650)X(4802)
* :ref:`X(79) <X(79)>` = trilinear product of vertices of reflection triangle of :ref:`X(1) <X(1)>`
* :ref:`X(79) <X(79)>` = X(6152)-of-excentral-triangle

Construction
------------

.. literalinclude:: model.py
   :language: python
