:order: 150
:type: center
:canonical_id: X(150)
:dependencies: X(1), X(2), X(4), X(7), X(20), X(69), X(80), X(85), X(101), X(103), X(116), X(147), X(152), X(295), X(334), X(348), X(355), X(514), X(664), X(668), X(944), X(952), X(1565), X(20999), X(22145), X(34179), X(39026)

.. _X(150):

X(150) = REFLECTION OF X(20) IN X(103)
======================================

.. figure:: x-00150.svg
   :alt: X(150) = REFLECTION OF X(20) IN X(103)
   :align: center

   **X(150) = REFLECTION OF X(20) IN X(103)** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`f(a,b,c) : f(b,c,a) : f(c,a,b)`, where, f(a,b,c) = bc[b\ :sup:`4` + c\ :sup:`4` - a\ :sup:`4` + a(bc\ :sup:`2` +cb\ :sup:`2` - b\ :sup:`3` - c\ :sup:`3`) - bc(a\ :sup:`2` + b\ :sup:`2` + c\ :sup:`2`) + (b + c)a\ :sup:`3`]

* **Kimberling (6, 9, 13) Search Value:** :math:`5.247092904763`

Notes
-----

.. container:: note-item

   Barycentrics g(a,b,c) : g(b,c,a) : g(c,a,b), where

      * g(a,b,c) = b\ :sup:`4` + c\ :sup:`4` - a\ :sup:`4` + a(bc\ :sup:`2` +cb\ :sup:`2` - b\ :sup:`3` - c\ :sup:`3`) - bc(a\ :sup:`2` + b\ :sup:`2` + c\ :sup:`2`) + (b + c)a\ :sup:`3`

Incidence
---------

:ref:`X(150) <X(150)>` lies on the anticomplementary circle and on these lines:

{:ref:`1 <X(1)>`, :ref:`147 <X(147)>`}, {:ref:`2 <X(2)>`, :ref:`101 <X(101)>`}, {:ref:`4 <X(4)>`, :ref:`152 <X(152)>`}, {:ref:`7 <X(7)>`, :ref:`80 <X(80)>`}, {:ref:`20 <X(20)>`, :ref:`103 <X(103)>`}, {:ref:`69 <X(69)>`, :ref:`668 <X(668)>`}, {:ref:`85 <X(85)>`, :ref:`355 <X(355)>`}, {:ref:`295 <X(295)>`, :ref:`334 <X(334)>`}, {:ref:`348 <X(348)>`, :ref:`944 <X(944)>`}, {:ref:`664 <X(664)>`, :ref:`952 <X(952)>`}

Relations
---------

* :ref:`X(150) <X(150)>` = :ref:`X(101) <X(101)>`-of-:term:`anticomplementary triangle <anticomplementary-triangle>`
* :ref:`X(150) <X(150)>` = reflection of X(i) in X(j) for these (i,j): (:ref:`20 <X(20)>`, :ref:`103 <X(103)>`), (:ref:`101 <X(101)>`, :ref:`116 <X(116)>`), (:ref:`152 <X(152)>`, :ref:`4 <X(4)>`), (:ref:`664 <X(664)>`, 1565)
* :ref:`X(150) <X(150)>` = :term:`isogonal conjugate <isogonal-conjugate>` of X(34179)
* :ref:`X(150) <X(150)>` = :term:`isotomic conjugate <isotomic-conjugate>` of isogonal conjugate of X(20999)
* :ref:`X(150) <X(150)>` = isotomic conjugate of :term:`anticomplement <anticomplement>` of X(39026)
* :ref:`X(150) <X(150)>` = polar conjugate of isogonal conjugate of X(22145)
* :ref:`X(150) <X(150)>` = :term:`anticomplementary conjugate <anticomplementary-conjugate>` of :ref:`X(514) <X(514)>`

Construction
------------

.. literalinclude:: model.py
   :language: python
