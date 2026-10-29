:order: 875
:type: center
:canonical_id: X(875)
:dependencies: X(1), X(31), X(42), X(213), X(239), X(291), X(295), X(350), X(512), X(649), X(659), X(667), X(669), X(740), X(798), X(812), X(874), X(926), X(1084)

.. _X(875):

X(875) = ISOGONAL CONJUGATE OF X(874)
=====================================

.. figure:: x-00875.svg
   :alt: X(875) = ISOGONAL CONJUGATE OF X(874)
   :align: center

   **X(875) = ISOGONAL CONJUGATE OF X(874)** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`f(a,b,c) : f(b,c,a) : f(c,a,b),`, where f(a,b,c) = a\ :sup:`2`\ u(bv - cw)/(a\ :sup:`2`\ u\ :sup:`2` - bcvw), u : v : w = :ref:`X(1) <X(1)>`

Barycentrics
~~~~~~~~~~~~

* :math:`g(a,b,c) : g(b,c,a) : g(c,a,b)`, where g(a,b,c) = af(a,b,c)

* **Kimberling (6, 9, 13) Search Value:** :math:`0.050859622864`

Incidence
---------

:ref:`X(875) <X(875)>` lies and on these lines:

{:ref:`1 <X(1)>`, :ref:`512 <X(512)>`}, {:ref:`31 <X(31)>`, :ref:`669 <X(669)>`}, {:ref:`42 <X(42)>`, :ref:`649 <X(649)>`}, {:ref:`213 <X(213)>`, :ref:`667 <X(667)>`}, {:ref:`291 <X(291)>`, :ref:`659 <X(659)>`}, {:ref:`295 <X(295)>`, :ref:`926 <X(926)>`}

Relations
---------

* :ref:`X(875) <X(875)>` = :term:`isogonal conjugate <isogonal-conjugate>` of :ref:`X(874) <X(874)>`
* :ref:`X(875) <X(875)>` = :term:`crosssum <crosssum>` of X(i) and X(j) for these (i,j): (:ref:`239 <X(239)>`, :ref:`659 <X(659)>`), (:ref:`740 <X(740)>`, :ref:`812 <X(812)>`)
* :ref:`X(875) <X(875)>` = :term:`crossdifference <crossdifference>` of every pair of points on line :ref:`X(239) <X(239)>`\ \ :ref:`X(350) <X(350)>`
* :ref:`X(875) <X(875)>` = :term:`trilinear pole <trilinear-pole>` of line :ref:`X(798) <X(798)>`\ X(1084)

Construction
------------

.. literalinclude:: model.py
   :language: python
