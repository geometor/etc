:order: 641
:type: center
:canonical_id: X(641)
:dependencies: X(2), X(3), X(39), X(140), X(141), X(371), X(372), X(485), X(488), X(492), X(590), X(615), X(639)

.. _X(641):

X(641) = COMPLEMENT OF X(485)
=============================

.. figure:: x-00641.svg
   :alt: X(641) = COMPLEMENT OF X(485)
   :align: center

   **X(641) = COMPLEMENT OF X(485)** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`f(a,b,c) : f(b,c,a) : f(c,a,b)`, where f(a,b,c) = [2S\ :sub:`B`\ S\ :sub:`C` + 3S\ :sub:`A`\ a\ :sup:`2` + 2(b\ :sup:`2` + c\ :sup:`2`) area]/a

Barycentrics
~~~~~~~~~~~~

* :math:`g(a,b,c) : g(b,c,a) : g(c,a,b)`, where g(a,b,c) = af(a,b,c)

* **Kimberling (6, 9, 13) Search Value:** :math:`3.535230763926`

Notes
-----

.. container:: note-item

   Erect squares outwards on the sides of triangle ABC; the circumcenter of the centers of the squares is :ref:`X(641) <X(641)>`. (:person:`Peter Moses <peter-moses>`, 7/16,2003)

Incidence
---------

:ref:`X(641) <X(641)>` lies and on these lines:

{:ref:`2 <X(2)>`, :ref:`372 <X(372)>`}, {:ref:`3 <X(3)>`, :ref:`639 <X(639)>`}, {:ref:`39 <X(39)>`, :ref:`615 <X(615)>`}, {:ref:`140 <X(140)>`, :ref:`141 <X(141)>`}, {:ref:`371 <X(371)>`, :ref:`492 <X(492)>`}

Relations
---------

* :ref:`X(641) <X(641)>` = midpoint of :ref:`X(485) <X(485)>` and :ref:`X(488) <X(488)>`
* :ref:`X(641) <X(641)>` = :term:`complement <complement>` of :ref:`X(485) <X(485)>`
* :ref:`X(641) <X(641)>` = :term:`complementary conjugate <complementary-conjugate>` of :ref:`X(639) <X(639)>`
* :ref:`X(641) <X(641)>` = :term:`crosspoint <crosspoint>` of :ref:`X(2) <X(2)>` and :ref:`X(492) <X(492)>`
* :ref:`X(641) <X(641)>` = :ref:`X(3) <X(3)>`-of-outer-Vecten-triangle
* :ref:`X(641) <X(641)>` = outer-Vecten-:term:`isogonal conjugate <isogonal-conjugate>` of :ref:`X(485) <X(485)>`
* :ref:`X(641) <X(641)>` = perspector of circumconic centered at :ref:`X(590) <X(590)>`
* :ref:`X(641) <X(641)>` = center of circumconic that is locus of :term:`trilinear poles <trilinear-pole>` of lines passing through :ref:`X(590) <X(590)>`
* :ref:`X(641) <X(641)>` = :ref:`X(2) <X(2)>`-:term:`Ceva conjugate <ceva-conjugate>` of :ref:`X(590) <X(590)>`
* :ref:`X(641) <X(641)>` = perspector of :term:`medial triangle <medial-triangle>` and outer Vecten of outer Vecten triangle (note: the medial triangle is the inner Vecten of outer Vecten triangle.)

Construction
------------

.. literalinclude:: model.py
   :language: python
