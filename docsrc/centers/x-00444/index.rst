:order: 444
:type: center
:canonical_id: X(444)
:dependencies: X(2), X(3), X(19), X(232), X(256)

.. _X(444):

X(444) = EULER LINE INTERCEPT OF LINE X(19)X(232)
=================================================

.. figure:: x-00444.svg
   :alt: X(444) = EULER LINE INTERCEPT OF LINE X(19)X(232)
   :align: center

   **X(444) = EULER LINE INTERCEPT OF LINE X(19)X(232)** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`(v + w)\tan A : (w + u)\tan B : (u + v)\tan C`, where, u : v : w = :ref:`X(256) <X(256)>`; e.g., u(a,b,c) = 1/(a\ :sup:`2` + bc)

* **Kimberling (6, 9, 13) Search Value:** :math:`-1.132256340988`

Notes
-----

.. container:: note-item

   Barycentrics (v + w)(sin A tan A) : (w + u)(sin B tan B) : (u + v)(sin C tan C)

.. container:: note-item

   As a point on the Euler line, :ref:`X(444) <X(444)>` has Shinagawa coefficients ([$a$(E + F) + $aS\ :sub:`A`\ $ - abc]F,-(E + F)[$a$(E + F) + $aS\ :sub:`A`\ $ + abc]).

Incidence
---------

:ref:`X(444) <X(444)>` lies and on these lines:

{:ref:`2 <X(2)>`, :ref:`3 <X(3)>`}, {:ref:`19 <X(19)>`, :ref:`232 <X(232)>`}

Construction
------------

.. literalinclude:: model.py
   :language: python
