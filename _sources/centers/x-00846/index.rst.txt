:order: 846
:type: center
:canonical_id: X(846)
:dependencies: X(1), X(2), X(3), X(6), X(9), X(21), X(35), X(37), X(43), X(55), X(100), X(171), X(228), X(275), X(333), X(405), X(661), X(740), X(756), X(982), X(984), X(986), X(1001), X(1051), X(1054), X(1281), X(4367)

.. _X(846):

X(846) = 4th SHARYGIN POINT
===========================

.. figure:: x-00846.svg
   :alt: X(846) = 4th SHARYGIN POINT
   :align: center

   **X(846) = 4th SHARYGIN POINT** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`f(a,b,c) : f(b,c,a) : f(c,a,b)`, where f(a,b,c) = - a\ :sup:`2` + b\ :sup:`2` + c\ :sup:`2` + bc + ca + ab

Barycentrics
~~~~~~~~~~~~

* :math:`g(a,b,c) : g(b,c,a) : g(c,a,b)`, where g(a,b,c) = a f(a,b,c)

* **Kimberling (6, 9, 13) Search Value:** :math:`2.519912547907`

Notes
-----

.. container:: note-item

   This point solves a problem posed by :person:`Antreas Hatzipolakis <antreas-hatzipolakis>` in :cite:`Hyacinthos #3001 <hyacinthos>`, June 11, 2001. For the construction as a Sharygin point, see the description at X(1281).

Incidence
---------

:ref:`X(846) <X(846)>` lies and on these lines:

{:ref:`1 <X(1)>`, :ref:`21 <X(21)>`}, {:ref:`2 <X(2)>`, 1054}, {:ref:`6 <X(6)>`, 1051}, {:ref:`9 <X(9)>`, :ref:`43 <X(43)>`}, {:ref:`35 <X(35)>`, :ref:`228 <X(228)>`}, {:ref:`37 <X(37)>`, :ref:`171 <X(171)>`}, {:ref:`55 <X(55)>`, :ref:`984 <X(984)>`}, {:ref:`100 <X(100)>`, :ref:`756 <X(756)>`}, {:ref:`333 <X(333)>`, :ref:`740 <X(740)>`}, {:ref:`405 <X(405)>`, :ref:`986 <X(986)>`}, {:ref:`982 <X(982)>`, 1001}

Relations
---------

* :ref:`X(846) <X(846)>` = X(i)-:term:`Ceva conjugate <ceva-conjugate>` of X(j) for these (i,j): (:ref:`37 <X(37)>`, :ref:`1 <X(1)>`), (:ref:`171 <X(171)>`, :ref:`43 <X(43)>`)
* :ref:`X(846) <X(846)>` = :term:`crossdifference <crossdifference>` of every pair of points on line :ref:`X(661) <X(661)>`\ X(4367)
* :ref:`X(846) <X(846)>` = homothetic center of the :term:`excentral triangle <excentral-triangle>` and the :term:`antipedal triangle <antipedal-triangle>`, wrt the :term:`incentral triangle <incentral-triangle>`, of :ref:`X(1) <X(1)>`
* :ref:`X(846) <X(846)>` = :ref:`X(275) <X(275)>`-of-excentral-triangle
* :ref:`X(846) <X(846)>` = excentral polar conjugate of :ref:`X(3) <X(3)>`
* :ref:`X(846) <X(846)>` = perspector of 1st Sharygin triangle and :term:`unary cofactor triangle <unary-cofactor-triangle>` of 2nd Sharygin triangle

Construction
------------

.. literalinclude:: model.py
   :language: python
