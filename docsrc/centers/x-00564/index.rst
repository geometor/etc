:order: 564
:type: center
:canonical_id: X(564)
:dependencies: X(1), X(47), X(91), X(92), X(1048)

.. _X(564):

X(564) = INTERSECTION OF LINES X(1)X(1048) AND X(47,91)
=======================================================

.. figure:: x-00564.svg
   :alt: X(564) = INTERSECTION OF LINES X(1)X(1048) AND X(47,91)
   :align: center

   **X(564) = INTERSECTION OF LINES X(1)X(1048) AND X(47,91)** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`\cos(2B - 2C) : \cos(2C - 2A) : \cos(2A - 2B)`
* :math:`b^2 c^2 (a^4 (b^4 + c^4) - 2 a^2 (b^2 - c^2)^2 (b^2 + c^2) + (b^2 - c^2)^4) : :`

Barycentrics
~~~~~~~~~~~~

* :math:`\sin A \cos(2B - 2C) : \sin B \cos(2C - 2A) : \sin C \cos(2A - 2B)`

* **Kimberling (6, 9, 13) Search Value:** :math:`14.990638600206`

Notes
-----

.. container:: note-item

   **Clark Kimberling and Cyril Parry,** "Products, Square Roots, and Layers in Triangle Geometry," *Mathematics and Informatics Quarterly* 10 (2000) 9-22; on page 21, section 8.

Incidence
---------

:ref:`X(564) <X(564)>` lies and on these lines:

{:ref:`1 <X(1)>`, 1048}, {:ref:`47 <X(47)>`, :ref:`91 <X(91)>`}

Relations
---------

* :ref:`X(564) <X(564)>` = {:ref:`X(91) <X(91)>`,\ :ref:`X(92) <X(92)>`}-harmonic conjugate of :ref:`X(47) <X(47)>`

Construction
------------

.. literalinclude:: model.py
   :language: python
