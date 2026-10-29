:order: 738
:type: center
:canonical_id: X(738)
:dependencies: X(9), X(56), X(57), X(77), X(269), X(279), X(348), X(479), X(728), X(951), X(30693)

.. _X(738):

X(738) = ISOGONAL CONJUGATE OF X(728)
=====================================

.. figure:: x-00738.svg
   :alt: X(738) = ISOGONAL CONJUGATE OF X(728)
   :align: center

   **X(738) = ISOGONAL CONJUGATE OF X(728)** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`f(a,b,c) : f(b,c,a) : f(c,a,b)`, where f(a,b,c) = (b + c - a) :sup:`-3`
* :math:`\tan^{3}(A/2) : \tan^{3}(B/2) : \tan^{3}(C/2) (M. Iliev, 4/12/07)`

* **Kimberling (6, 9, 13) Search Value:** :math:`0.007065173776`

Notes
-----

.. container:: note-item

   Barycentrics g(a,b,c) : g(b,c,a) : g(c,a,b), where g(a,b,c) = af(a,b,c)

Incidence
---------

:ref:`X(738) <X(738)>` lies and on these lines:

{:ref:`9 <X(9)>`, :ref:`348 <X(348)>`}, {:ref:`56 <X(56)>`, :ref:`269 <X(269)>`}, {:ref:`57 <X(57)>`, :ref:`279 <X(279)>`}, {:ref:`77 <X(77)>`, :ref:`951 <X(951)>`}

Relations
---------

* :ref:`X(738) <X(738)>` = :term:`isogonal conjugate <isogonal-conjugate>` of :ref:`X(728) <X(728)>`
* :ref:`X(738) <X(738)>` = :term:`isotomic conjugate <isotomic-conjugate>` of X(30693)
* :ref:`X(738) <X(738)>` = :ref:`X(479) <X(479)>`-:term:`Ceva conjugate <ceva-conjugate>` of :ref:`X(269) <X(269)>`

Construction
------------

.. literalinclude:: model.py
   :language: python
