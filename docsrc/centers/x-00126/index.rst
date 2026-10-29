:order: 126
:type: center
:canonical_id: X(126)
:dependencies: X(2), X(4), X(6), X(99), X(111), X(125), X(141), X(524), X(625), X(858), X(2374), X(3258), X(3291)

.. _X(126):

X(126) = X(111)-OF-MEDIAL-TRIANGLE
==================================

.. figure:: x-00126.svg
   :alt: X(126) = X(111)-OF-MEDIAL-TRIANGLE
   :align: center

   **X(126) = X(111)-OF-MEDIAL-TRIANGLE** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`f(a,b,c) : f(b,c,a) : f(c,a,b)`, where, f(a,b,c) = bc(2a\ :sup:`2` - b\ :sup:`2` - c\ :sup:`2`)[b\ :sup:`4` + c\ :sup:`4` + a\ :sup:`2`\ (b\ :sup:`2` + c\ :sup:`2`) - 4b\ :sup:`2`\ c\ :sup:`2`]

* **Kimberling (6, 9, 13) Search Value:** :math:`3.340332250420`

Notes
-----

.. container:: note-item

   Barycentrics g(a,b,c) : g(b,c,a) : g(c,a,b) where g(a,b,c) = (2a\ :sup:`2` - b\ :sup:`2` - c\ :sup:`2`)[b\ :sup:`4` + c\ :sup:`4` + a\ :sup:`2`\ (b\ :sup:`2` + c\ :sup:`2`) - 4b\ :sup:`2`\ c\ :sup:`2`]

Incidence
---------

:ref:`X(126) <X(126)>` lies on the nine-point circle

:ref:`X(126) <X(126)>` lies and on these lines:

{:ref:`2 <X(2)>`, :ref:`99 <X(99)>`}, {:ref:`125 <X(125)>`, :ref:`141 <X(141)>`}, {:ref:`625 <X(625)>`, :ref:`858 <X(858)>`}

Relations
---------

* :ref:`X(126) <X(126)>` = :ref:`X(111) <X(111)>`-of-:term:`medial triangle <medial-triangle>`.
* :ref:`X(126) <X(126)>` = :term:`complement <complement>` of :ref:`X(111) <X(111)>`
* :ref:`X(126) <X(126)>` = :term:`complementary conjugate <complementary-conjugate>` of :ref:`X(524) <X(524)>`
* :ref:`X(126) <X(126)>` = :ref:`X(4) <X(4)>`-:term:`Ceva conjugate <ceva-conjugate>` of :ref:`X(524) <X(524)>`
* :ref:`X(126) <X(126)>` = perspector of circumconic centered at X(3291)
* :ref:`X(126) <X(126)>` = center of circumconic that is locus of :term:`trilinear poles <trilinear-pole>` of lines passing through X(3291)
* :ref:`X(126) <X(126)>` = :ref:`X(2) <X(2)>`-Ceva conjugate of X(3291)
* :ref:`X(126) <X(126)>` = one of two intersections (X(3258) is the other) of the nine-point circle of ABC and the Parry circle of the :ref:`X(2) <X(2)>`-Brocard triangle
* :ref:`X(126) <X(126)>` = inverse-in-polar-circle of X(2374)
* :ref:`X(126) <X(126)>` = inverse-in-{circumcircle, nine-point circle}-inverter of :ref:`X(99) <X(99)>`
* :ref:`X(126) <X(126)>` = Λ(:ref:`X(2) <X(2)>`, :ref:`X(6) <X(6)>`), wrt :term:`orthic triangle <orthic-triangle>`

Construction
------------

.. literalinclude:: model.py
   :language: python
