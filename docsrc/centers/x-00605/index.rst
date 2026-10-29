:order: 605
:type: center
:canonical_id: X(605)
:dependencies: X(6), X(31), X(371), X(372), X(590), X(601), X(602), X(615), X(748), X(750), X(3083), X(6212), X(37881), X(40651)

.. _X(605):

X(605) = INTERSECTION OF LINES X(371)X(602) AND X(372)X(601)
============================================================

.. figure:: x-00605.svg
   :alt: X(605) = INTERSECTION OF LINES X(371)X(602) AND X(372)X(601)
   :align: center

   **X(605) = INTERSECTION OF LINES X(371)X(602) AND X(372)X(601)** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`a(1 + \sin A) : b(1 + \sin B) : c(1 + \sin c)`
* :math:`a^{2}(S + bc) : b^{2}(S + ca) : c^{2}(S + ab)`

Barycentrics
~~~~~~~~~~~~

* :math:`a^{2}(1 + \sin A) : b^{2}(1 + \sin B) : c^{2}(1 + \sin C)`

* **Kimberling (6, 9, 13) Search Value:** :math:`0.801159897202`

Incidence
---------

:ref:`X(605) <X(605)>` lies and on these lines:

{:ref:`6 <X(6)>`, :ref:`31 <X(31)>`}, {:ref:`371 <X(371)>`, :ref:`602 <X(602)>`}, {:ref:`372 <X(372)>`, :ref:`601 <X(601)>`}, {:ref:`590 <X(590)>`, :ref:`748 <X(748)>`}, {:ref:`615 <X(615)>`, :ref:`750 <X(750)>`}

Relations
---------

* :ref:`X(605) <X(605)>` = :term:`isogonal conjugate <isogonal-conjugate>` of :term:`isotomic conjugate <isotomic-conjugate>` of X(3083)
* :ref:`X(605) <X(605)>` = isogonal conjugate of polar conjugate of X(6212)
* :ref:`X(605) <X(605)>` = isogonal conjugate of :term:`complement <complement>` of X(37881)
* :ref:`X(605) <X(605)>` = isogonal conjugate of :term:`anticomplement <anticomplement>` of X(40651)

Construction
------------

.. literalinclude:: model.py
   :language: python
