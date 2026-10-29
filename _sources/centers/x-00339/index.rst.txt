:order: 339
:type: center
:canonical_id: X(339)
:dependencies: X(3), X(25), X(69), X(76), X(115), X(125), X(127), X(250), X(264), X(265), X(305), X(338), X(381), X(525), X(1101), X(3267)

.. _X(339):

X(339) = ISOTOMIC CONJUGATE OF X(250)
=====================================

.. figure:: x-00339.svg
   :alt: X(339) = ISOTOMIC CONJUGATE OF X(250)
   :align: center

   **X(339) = ISOTOMIC CONJUGATE OF X(250)** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`(b^{2} - c^{2})^{2}(\cos A)/a^{4} : (c^{2} - a^{2})^{2}(\cos B)/b^{4} : (a^{2} - b^{2})^{2}(\cos C)/c^{4}, = \csc A \cot A \sin^{2}(B - C) : \csc B \cot B \sin^{2}(C - A) : \csc C \cot C \sin^{2}(A - B)`

* **Kimberling (6, 9, 13) Search Value:** :math:`5.009222601597`

Notes
-----

.. container:: note-item

   Barycentrics (b\ :sup:`2` - c\ :sup:`2`)\ :sup:`2`\ (cos A)/a\ :sup:`3` : (c\ :sup:`2` - a\ :sup:`2`)\ :sup:`2`\ (cos B)/b\ :sup:`3` : (a\ :sup:`2` - b\ :sup:`2`)\ :sup:`2`\ (cos C)/c\ :sup:`3`

   = cot A sin\ :sup:`2`\ (B - C) : cot B sin\ :sup:`2`\ (C - A) : cot C sin\ :sup:`2`\ (A - B)

   Barycentrics b^2 c^2 (b^2 - c^2)^2 (b^2 + c^2 - a^2) : :

Incidence
---------

:ref:`X(339) <X(339)>` lies on the MacBeath inconic and on these lines:

{:ref:`3 <X(3)>`, :ref:`76 <X(76)>`}, {:ref:`69 <X(69)>`, :ref:`265 <X(265)>`}, {:ref:`115 <X(115)>`, :ref:`127 <X(127)>`}, {:ref:`264 <X(264)>`, :ref:`381 <X(381)>`}

Relations
---------

* :ref:`X(339) <X(339)>` = :term:`isotomic conjugate <isotomic-conjugate>` of :ref:`X(250) <X(250)>`
* :ref:`X(339) <X(339)>` = X(i)-:term:`Ceva conjugate <ceva-conjugate>` of X(j) for these (i,j): (:ref:`76 <X(76)>`, :ref:`525 <X(525)>`), (:ref:`305 <X(305)>`, 3267)
* :ref:`X(339) <X(339)>` = :ref:`X(125) <X(125)>`-:term:`cross conjugate <cross-conjugate>` of :ref:`X(338) <X(338)>`
* :ref:`X(339) <X(339)>` = :ref:`X(25) <X(25)>`-:term:`isoconjugate <isoconjugate>` of X(1101)
* :ref:`X(339) <X(339)>` = :term:`crosspoint <crosspoint>` of :ref:`X(305) <X(305)>` and X(3267)

Construction
------------

.. literalinclude:: model.py
   :language: python
