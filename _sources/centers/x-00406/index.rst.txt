:order: 406
:type: center
:canonical_id: X(406)
:dependencies: X(2), X(3), X(8), X(10), X(33), X(37), X(92), X(108), X(158), X(208), X(226), X(261), X(317), X(388), X(475), X(1061), X(1068), X(34120), X(36744)

.. _X(406):

X(406) = EULER LINE INTERCEPT OF LINE X(10)X(33)
================================================

.. figure:: x-00406.svg
   :alt: X(406) = EULER LINE INTERCEPT OF LINE X(10)X(33)
   :align: center

   **X(406) = EULER LINE INTERCEPT OF LINE X(10)X(33)** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`f(a,b,c) : f(b,c,a) : f(c,a,b)`, where f(a,b,c) = bc(a + b + c) + abc sec A

Barycentrics
~~~~~~~~~~~~

* :math:`b + c + a(1 + \sec A) : c + a + b(1 + \sec B) : a + b + c(1 + \sec C)`

* **Kimberling (6, 9, 13) Search Value:** :math:`3.640581424626`

Notes
-----

.. container:: note-item

   As a point on the Euler line, :ref:`X(406) <X(406)>` has Shinagawa coefficients ($a$F, abc).

Incidence
---------

:ref:`X(406) <X(406)>` lies and on these lines:

{:ref:`2 <X(2)>`, :ref:`3 <X(3)>`}, {:ref:`8 <X(8)>`, 1061}, {:ref:`10 <X(10)>`, :ref:`33 <X(33)>`}, {:ref:`37 <X(37)>`, :ref:`158 <X(158)>`}, {:ref:`92 <X(92)>`, 1068}, {:ref:`108 <X(108)>`, :ref:`388 <X(388)>`}, {:ref:`208 <X(208)>`, :ref:`226 <X(226)>`}, {:ref:`261 <X(261)>`, :ref:`317 <X(317)>`}

Relations
---------

* :ref:`X(406) <X(406)>` = :term:`anticomplement <anticomplement>` of X(34120)
* :ref:`X(406) <X(406)>` = polar conjugate of :term:`isogonal conjugate <isogonal-conjugate>` of X(36744)
* :ref:`X(406) <X(406)>` = inverse-in-orthocentroidal-circle of :ref:`X(475) <X(475)>`

Construction
------------

.. literalinclude:: model.py
   :language: python
