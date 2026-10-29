:order: 97
:type: center
:canonical_id: X(97)
:dependencies: X(2), X(3), X(51), X(53), X(54), X(77), X(92), X(95), X(110), X(216), X(276), X(288), X(324), X(401), X(418), X(577), X(7592), X(34433), X(34836)

.. _X(97):

X(97) = ISOGONAL CONJUGATE OF X(53)
===================================

.. figure:: x-00097.svg
   :alt: X(97) = ISOGONAL CONJUGATE OF X(53)
   :align: center

   **X(97) = ISOGONAL CONJUGATE OF X(53)** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`\cot A \sec(B - C) : \cot B \sec(C - A) : \cot C \sec(A - B)`

Barycentrics
~~~~~~~~~~~~

* :math:`\cos A \sec(B - C) : \cos B \sec(C - A) : \cos C \sec(A - B)`

* **Kimberling (6, 9, 13) Search Value:** :math:`-13.339586550833`

Notes
-----

.. container:: note-item

   In the plane of a triangle ABC, let

      * Ia = line through :ref:`X(3) <X(3)>` parallel to BC, and define Ib and Ic cyclically.
      * Ac = Ia∩AB, and define Ba and Cb cyclically.
      * Ab = Ia∩AC, and define Bc and Ca cyclically.
      * Oa = circumcircle of A, Bc, Cb, and define Ob and Oc cyclically.

   Then :ref:`X(97) <X(97)>` = radical center of Oa, Ob, Oc. See also :ref:`X(77) <X(77)>`. (Ivan Pavlov, April 1, 2022)

Incidence
---------

:ref:`X(97) <X(97)>` lies and on these lines:

{:ref:`2 <X(2)>`, :ref:`95 <X(95)>`}, {:ref:`3 <X(3)>`, :ref:`54 <X(54)>`}, {110, 418}, {216, 288}, {276, 401}

Relations
---------

* :ref:`X(97) <X(97)>` = :term:`isogonal conjugate <isogonal-conjugate>` of :ref:`X(53) <X(53)>`
* :ref:`X(97) <X(97)>` = :term:`isotomic conjugate <isotomic-conjugate>` of X(324)
* :ref:`X(97) <X(97)>` = :term:`anticomplement <anticomplement>` of X(34836)
* :ref:`X(97) <X(97)>` = :term:`complement <complement>` of isogonal conjugate of X(34433)
* :ref:`X(97) <X(97)>` = :ref:`X(95) <X(95)>`-:term:`Ceva conjugate <ceva-conjugate>` of :ref:`X(54) <X(54)>`
* :ref:`X(97) <X(97)>` = :ref:`X(3) <X(3)>`-:term:`cross conjugate <cross-conjugate>` of :ref:`X(95) <X(95)>`
* :ref:`X(97) <X(97)>` = :term:`cevapoint <cevapoint>` of :ref:`X(3) <X(3)>` and X(577)
* :ref:`X(97) <X(97)>` = :ref:`X(51) <X(51)>`-:term:`isoconjugate <isoconjugate>` of :ref:`X(92) <X(92)>`
* :ref:`X(97) <X(97)>` = Cundy-Parry Phi transform of X(7592)

Construction
------------

.. literalinclude:: model.py
   :language: python
