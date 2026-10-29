:order: 173
:type: center
:canonical_id: X(173)
:dependencies: X(1), X(2), X(9), X(19), X(57), X(164), X(168), X(174), X(177), X(180), X(188), X(258), X(361), X(362), X(366), X(483), X(503), X(504), X(505), X(507), X(508), X(509), X(844), X(845), X(1130), X(1485), X(1486), X(34849)

.. _X(173):
.. _CongruentIsoscelizersPoint:

X(173) = CONGRUENT ISOSCELIZERS POINT
=====================================

.. figure:: x-00173.svg
   :alt: X(173) = CONGRUENT ISOSCELIZERS POINT
   :align: center

   **X(173) = CONGRUENT ISOSCELIZERS POINT** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`\cos B/2 + \cos C/2 - \cos A/2 : :`
* :math:`\tan A/2 + \sec A/2 : \tan B/2 + \sec B/2 : \tan C/2 + \sec C/2 (M. Iliev, 4/12/07)`
* :math:`b(\csc B/2) + c(\csc C/2) - a(\csc A/2) : :`
* :math:`\cot A'/2 : :`, where A'B'C' = :term:`excentral triangle <excentral-triangle>`
* :math:`b' + c' - a' : :`, where a', b', c' are sidelengths of excentral triangle
* :math:`\cot A' + \csc A' : :`, where A'B'C' = excentral triangle
* [distance from A to far side of A-excircle] : :

* **Kimberling (6, 9, 13) Search Value:** :math:`0.865451887564`

Notes
-----

.. container:: note-item

   Let P\ :sub:`B` on sideline AC and Q\ :sub:`C` be equidistant from A, so that AP\ :sub:`B`\ Q\ :sub:`C` is an isosceles triangle. The line P\ :sub:`B`\ Q\ :sub:`C` is called an :term:`isoscelizer <isoscelizer>`. The lines P\ :sub:`B`\ Q\ :sub:`C`, P\ :sub:`C`\ Q\ :sub:`A`, P\ :sub:`A`\ Q\ :sub:`B` concur in :ref:`X(173) <X(173)>`. (P. Yff, unpublished notes, 1989)

.. container:: note-item

   The :term:`intouch triangle <intouch-triangle>` of the intouch triangle of triangle ABC is perspective to triangle ABC, and :ref:`X(173) <X(173)>` is the perspector. (Eric Danneels, :cite:`Hyacinthos <hyacinthos>` 7892, 9/13/03)

.. container:: note-item

   Also, :ref:`X(173) <X(173)>` = X(1486)-of-the-intouch-triangle. (:person:`Darij Grinberg <darij-grinberg>`; see notes at X(1485) and X(1486).)

Incidence
---------

:ref:`X(173) <X(173)>` lies and on these lines:

{:ref:`1 <X(1)>`, :ref:`168 <X(168)>`}, {:ref:`9 <X(9)>`, :ref:`177 <X(177)>`}, {:ref:`57 <X(57)>`, :ref:`174 <X(174)>`}, {:ref:`164 <X(164)>`, :ref:`504 <X(504)>`}, {:ref:`180 <X(180)>`, :ref:`483 <X(483)>`}, {:ref:`503 <X(503)>`, :ref:`844 <X(844)>`}, {:ref:`505 <X(505)>`, 1130}

Relations
---------

* :ref:`X(173) <X(173)>` = :term:`isogonal conjugate <isogonal-conjugate>` of :ref:`X(258) <X(258)>`
* :ref:`X(173) <X(173)>` = :term:`anticomplement <anticomplement>` of X(34849)
* :ref:`X(173) <X(173)>` = :ref:`X(174) <X(174)>`-:term:`Ceva conjugate <ceva-conjugate>` of :ref:`X(1) <X(1)>`
* :ref:`X(173) <X(173)>` = SS(A→A')-of-:ref:`X(9) <X(9)>`, where A'B'C' is the excentral triangle
* :ref:`X(173) <X(173)>` = :ref:`X(19) <X(19)>`-of-excentral triangle
* :ref:`X(173) <X(173)>` = :ref:`X(19) <X(19)>`-of-Yff :term:`central triangle <central-triangle>`
* :ref:`X(173) <X(173)>` = homothetic center of excentral triangle and Yff central triangle
* :ref:`X(173) <X(173)>` = homothetic center of ABC and :term:`orthic triangle <orthic-triangle>` of Yff central triangle
* :ref:`X(173) <X(173)>` = homothetic center of ABC and extangents triangle of excentral triangle
* :ref:`X(173) <X(173)>` = excentral isogonal conjugate of :ref:`X(845) <X(845)>`
* :ref:`X(173) <X(173)>` = X(i)-:term:`aleph conjugate <aleph-conjugate>` of X(j) for these (i,j): (:ref:`1 <X(1)>`, :ref:`503 <X(503)>`), (:ref:`2 <X(2)>`, :ref:`504 <X(504)>`), (:ref:`174 <X(174)>`, :ref:`173 <X(173)>`), (:ref:`188 <X(188)>`, :ref:`845 <X(845)>`), (:ref:`366 <X(366)>`, :ref:`164 <X(164)>`), (:ref:`507 <X(507)>`, :ref:`1 <X(1)>`), (:ref:`508 <X(508)>`, :ref:`362 <X(362)>`), (:ref:`509 <X(509)>`, :ref:`361 <X(361)>`)

Construction
------------

.. literalinclude:: model.py
   :language: python
