:order: 215
:type: center
:canonical_id: X(215)
:dependencies: X(1), X(11), X(12), X(49), X(50), X(54), X(55), X(110), X(184)

.. _X(215):

X(215) = X(1)-CEVA CONJUGATE OF X(50)
=====================================

.. figure:: x-00215.svg
   :alt: X(215) = X(1)-CEVA CONJUGATE OF X(50)
   :align: center

   **X(215) = X(1)-CEVA CONJUGATE OF X(50)** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`f(A,B,C) : f(B,C,A) : f(C,A,B)`, where f(A,B,C) = (sin 3A)(sin 3B + sin 3C - sin 3A)
* :math:`\cos^{2}(3A/2) : \cos^{2}(3B/2) : \cos^{2}(3C/2) (M. Iliev, 4/12/07)`
* :math:`1 + \cos 3A : 1 + \cos 3B : 1+ \cos 3C (M. Iliev, 4/12/07)`
* :math:`a^3 (a^2 - b^2 - c^2 + b c)^2 (a - b - c) : :`

* **Kimberling (6, 9, 13) Search Value:** :math:`1.577243820289`

Notes
-----

.. container:: note-item

   :ref:`X(215) <X(215)>` is the insimilicenter of the incircle and the sine-triple-angle circle. (:person:`Randy Hutson <randy-hutson>`, December 14, 2014)

.. container:: note-item

   Barycentrics (sin A)f(A,B,C) : (sin B)f(B,C,A) : (sin C)f(C,A,B)

Incidence
---------

:ref:`X(215) <X(215)>` lies and on these lines:

{:ref:`1 <X(1)>`, :ref:`49 <X(49)>`}, {:ref:`11 <X(11)>`, :ref:`110 <X(110)>`}, {:ref:`12 <X(12)>`, :ref:`54 <X(54)>`}, {:ref:`55 <X(55)>`, :ref:`184 <X(184)>`}

Relations
---------

* :ref:`X(215) <X(215)>` = X(i)-:term:`Ceva conjugate <ceva-conjugate>` of X(j) for these (i,j): (:ref:`1 <X(1)>`, :ref:`50 <X(50)>`)

Construction
------------

.. literalinclude:: model.py
   :language: python
