:order: 235
:type: center
:canonical_id: X(235)
:dependencies: X(2), X(3), X(4), X(11), X(12), X(24), X(33), X(34), X(48), X(52), X(55), X(56), X(113), X(133), X(136), X(155), X(185), X(427), X(523), X(801), X(1092), X(2071), X(11413), X(16196), X(37917)

.. _X(235):

X(235) = X(4)-CEVA CONJUGATE OF X(185)
======================================

.. figure:: x-00235.svg
   :alt: X(235) = X(4)-CEVA CONJUGATE OF X(185)
   :align: center

   **X(235) = X(4)-CEVA CONJUGATE OF X(185)** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`\sec A - \cos(B - C) : :`
* :math:`(\sec A)(\cos^{2}B + \cos^{2}C) : :`

Barycentrics
~~~~~~~~~~~~

* :math:`(\tan A)(\cos^{2}B + \cos^{2}C) : :`
* :math:`(a^4 (b^2 + c^2) - 2 a^2 (b^2 - c^2)^2 + (b^2 - c^2)^2 (b^2 + c^2))/(a^2 - b^2 - c^2) : :`

* **Kimberling (6, 9, 13) Search Value:** :math:`-2.042726748267`

Notes
-----

.. container:: note-item

   As a point on the Euler line, :ref:`X(235) <X(235)>` has Shinagawa coefficients (F, F - E).

Incidence
---------

:ref:`X(235) <X(235)>` lies and on these lines:

{:ref:`2 <X(2)>`, :ref:`3 <X(3)>`}, {:ref:`11 <X(11)>`, :ref:`34 <X(34)>`}, {:ref:`12 <X(12)>`, :ref:`33 <X(33)>`}, {:ref:`52 <X(52)>`, :ref:`113 <X(113)>`}, {:ref:`133 <X(133)>`, :ref:`136 <X(136)>`}

Relations
---------

* :ref:`X(235) <X(235)>` = midpoint of :ref:`X(4) <X(4)>` and :ref:`X(24) <X(24)>`
* :ref:`X(235) <X(235)>` = :term:`complement <complement>` of X(11413)
* :ref:`X(235) <X(235)>` = :term:`anticomplement <anticomplement>` of X(16196)
* :ref:`X(235) <X(235)>` = circumcircle-inverse of X(37917)
* :ref:`X(235) <X(235)>` = excentral-to-ABC :term:`functional image <functional-image>` of :ref:`X(55) <X(55)>`
* :ref:`X(235) <X(235)>` = :ref:`X(4) <X(4)>`-:term:`Ceva conjugate <ceva-conjugate>` of :ref:`X(185) <X(185)>`
* :ref:`X(235) <X(235)>` = :term:`crosssum <crosssum>` of :ref:`X(3) <X(3)>` and X(1092)
* :ref:`X(235) <X(235)>` = orthic-:term:`isogonal conjugate <isogonal-conjugate>` of :ref:`X(185) <X(185)>`
* :ref:`X(235) <X(235)>` = :ref:`X(56) <X(56)>` of :term:`orthic triangle <orthic-triangle>` if ABC is acute
* :ref:`X(235) <X(235)>` = insimilicenter of nine-point circle and incircle of orthic triangle if ABC is acute; the exsimilicenter is :ref:`X(427) <X(427)>`
* :ref:`X(235) <X(235)>` = pole wrt polar circle of :term:`trilinear polar <trilinear-polar>` of :ref:`X(801) <X(801)>` (line :ref:`X(523) <X(523)>`\ X(2071))
* :ref:`X(235) <X(235)>` = :ref:`X(48) <X(48)>`-:term:`isoconjugate <isoconjugate>` (polar conjugate) of :ref:`X(801) <X(801)>`
* :ref:`X(235) <X(235)>` = perspector of ABC and cross-triangle of ABC and 2nd Hyacinth triangle
* :ref:`X(235) <X(235)>` = radical center of the polar-circle-inverses of the power circles
* :ref:`X(235) <X(235)>` = intersection of tangents to Hatzipolakis-Lozada hyperbola at :ref:`X(4) <X(4)>` and :ref:`X(155) <X(155)>`
* :ref:`X(235) <X(235)>` = :term:`crosspoint <crosspoint>`, wrt orthic triangle, of :ref:`X(4) <X(4)>` and :ref:`X(155) <X(155)>`

Construction
------------

.. literalinclude:: model.py
   :language: python
