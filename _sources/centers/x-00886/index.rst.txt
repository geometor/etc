:order: 886
:type: center
:canonical_id: X(886)
:dependencies: X(2), X(99), X(512), X(538), X(669), X(670), X(880), X(887), X(888), X(892), X(3228), X(39010)

.. _X(886):

X(886) = INTERSECTION OF LINES X(99)X(669) AND X(512)X(670)
===========================================================

.. figure:: x-00886.svg
   :alt: X(886) = INTERSECTION OF LINES X(99)X(669) AND X(512)X(670)
   :align: center

   **X(886) = INTERSECTION OF LINES X(99)X(669) AND X(512)X(670)** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`(a^{2}u^{2} - bcvw)/[a^{2}u(bv - cw)] : :`, where u : v : w = :ref:`X(512) <X(512)>`

Barycentrics
~~~~~~~~~~~~

* :math:`b^2 c^2/((b^2 - c^2) (a^2 b^2 + a^2 c^2 - 2 b^2 c^2)) : :`

* **Kimberling (6, 9, 13) Search Value:** :math:`4.726589555271`

Incidence
---------

:ref:`X(886) <X(886)>` lies on the Steiner circumellipse and on these lines:

{:ref:`99 <X(99)>`, :ref:`669 <X(669)>`}, {:ref:`512 <X(512)>`, :ref:`670 <X(670)>`}, {:ref:`538 <X(538)>`, 3228}, {:ref:`880 <X(880)>`, :ref:`892 <X(892)>`}

Relations
---------

* :ref:`X(886) <X(886)>` = :term:`isogonal conjugate <isogonal-conjugate>` of :ref:`X(887) <X(887)>`
* :ref:`X(886) <X(886)>` = :term:`isotomic conjugate <isotomic-conjugate>` of :ref:`X(888) <X(888)>`
* :ref:`X(886) <X(886)>` = :term:`anticomplement <anticomplement>` of X(39010)
* :ref:`X(886) <X(886)>` = :term:`trilinear pole <trilinear-pole>` of line :ref:`X(2) <X(2)>`\ \ :ref:`X(670) <X(670)>`

Construction
------------

.. literalinclude:: model.py
   :language: python
