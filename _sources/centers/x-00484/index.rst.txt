:order: 484
:type: center
:canonical_id: X(484)
:dependencies: X(1), X(3), X(4), X(10), X(12), X(13), X(14), X(30), X(35), X(36), X(46), X(63), X(74), X(79), X(80), X(100), X(186), X(191), X(499), X(535), X(650), X(758), X(759), X(901), X(962), X(1046), X(1048), X(1100), X(1138), X(1155), X(1276), X(1277), X(3065), X(3153), X(3245), X(3336), X(3464), X(3465), X(3466), X(3483), X(3484), X(5045), X(35631), X(37616)

.. _X(484):
.. _1st-EvansPerspector:

X(484) = 1st EVANS PERSPECTOR
=============================

.. figure:: x-00484.svg
   :alt: X(484) = 1st EVANS PERSPECTOR
   :align: center

   **X(484) = 1st EVANS PERSPECTOR** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`1 + 2(\cos A - \cos B - \cos C) : 1 + 2(\cos B - \cos C - \cos A) : 1 + 2(\cos C - \cos A - \cos B)`
* :math:`a^3 + a^2 (b + c) - a (b^2 + b c + c^2) - (b - c)^2 (b + c) : :`

Barycentrics
~~~~~~~~~~~~

* :math:`a[1 + 2(\cos A - \cos B - \cos C)] : b[1 + 2(\cos B - \cos C - \cos A)] : c[1 + 2(\cos C - \cos A - \cos B)]`

* **Kimberling (6, 9, 13) Search Value:** :math:`-6.840882082776`

Notes
-----

.. container:: note-item

   :ref:`X(484) <X(484)>` is the perspector of the :term:`excentral triangle <excentral-triangle>` and the triangle A'B'C', where A' is the reflection of vertex A in sideline BC and B', C' are determined cyclically. (Lawrence Evans, 10/22/98)

Incidence
---------

:ref:`X(484) <X(484)>` lies on the Neuberg cubic and on these lines:

{:ref:`1 <X(1)>`, :ref:`3 <X(3)>`}, {:ref:`4 <X(4)>`, 3483}, {:ref:`10 <X(10)>`, :ref:`191 <X(191)>`}, {:ref:`12 <X(12)>`, :ref:`79 <X(79)>`}, {:ref:`13 <X(13)>`, 1277}, {:ref:`14 <X(14)>`, 1276}, {:ref:`30 <X(30)>`, :ref:`80 <X(80)>`}, {:ref:`63 <X(63)>`, :ref:`535 <X(535)>`}, {:ref:`74 <X(74)>`, 3465}, {:ref:`100 <X(100)>`, :ref:`758 <X(758)>`}, {:ref:`499 <X(499)>`, :ref:`962 <X(962)>`}, {:ref:`759 <X(759)>`, :ref:`901 <X(901)>`}, {1046, 1048}, {1138, 3464}, {3466, 3484}

Relations
---------

* :ref:`X(484) <X(484)>` = midpoint of :ref:`X(36) <X(36)>` and X(3245)
* :ref:`X(484) <X(484)>` = reflection of X(i) in X(j) for these (i,j): (:ref:`1 <X(1)>`, :ref:`36 <X(36)>`), (:ref:`36 <X(36)>`, 1155)
* :ref:`X(484) <X(484)>` = :term:`isogonal conjugate <isogonal-conjugate>` of X(3065)
* :ref:`X(484) <X(484)>` = inverse-in-circumcircle of :ref:`X(35) <X(35)>`
* :ref:`X(484) <X(484)>` = inverse-in-Bevan-circle of :ref:`X(1) <X(1)>`
* :ref:`X(484) <X(484)>` = Conway-circle-inverse of X(35631)
* :ref:`X(484) <X(484)>` = :ref:`X(80) <X(80)>`-:term:`Ceva conjugate <ceva-conjugate>` of :ref:`X(1) <X(1)>`
* :ref:`X(484) <X(484)>` = :term:`crossdifference <crossdifference>` of every pair of points on line :ref:`X(650) <X(650)>`\ X(1100)
* :ref:`X(484) <X(484)>` = {:ref:`X(1) <X(1)>`\ \ :ref:`X(46) <X(46)>`}-harmonic conjugate of X(3336)
* :ref:`X(484) <X(484)>` = inverse-in-incircle of X(5045)
* :ref:`X(484) <X(484)>` = perspector of ABC and the reflection of the :term:`incentral triangle <incentral-triangle>` in the antiorthic axis (the reflection of the :term:`cevian triangle <cevian-triangle>` of :ref:`X(1) <X(1)>` in the :term:`trilinear polar <trilinear-polar>` of :ref:`X(1) <X(1)>`)
* :ref:`X(484) <X(484)>` = reflection of :ref:`X(36) <X(36)>` in the antiorthic axis
* :ref:`X(484) <X(484)>` = :ref:`X(30) <X(30)>`-Ceva conjugate of X(3465)
* :ref:`X(484) <X(484)>` = :ref:`X(186) <X(186)>`-of-excentral-triangle
* :ref:`X(484) <X(484)>` = {:ref:`X(1) <X(1)>`,\ :ref:`X(3) <X(3)>`}-harmonic conjugate of X(37616)
* :ref:`X(484) <X(484)>` = endo-homothetic center of Ehrmann vertex-triangle and dual of :term:`orthic triangle <orthic-triangle>`; the homothetic center of is X(3153)

Construction
------------

.. literalinclude:: model.py
   :language: python
