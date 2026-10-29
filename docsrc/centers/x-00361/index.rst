:order: 361
:type: center
:canonical_id: X(361)
:dependencies: X(1), X(164), X(188), X(266), X(503), X(978)

.. _X(361):

X(361) = X(266)-CEVA CONJUGATE OF X(1)
======================================

.. figure:: x-00361.svg
   :alt: X(361) = X(266)-CEVA CONJUGATE OF X(1)
   :align: center

   **X(361) = X(266)-CEVA CONJUGATE OF X(1)** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`\csc B/2 + \csc C/2 - \csc A/2 : \csc C/2 + \csc A/2 - \csc B/2 : \csc A/2 + \csc B/2 - \csc C/2`

Barycentrics
~~~~~~~~~~~~

* :math:`f(A,B,C) : f(B,C,A) : f(C,A,B)`, where f(A,B,C) = (sin A)(csc B/2 + csc C/2 - csc A/2)

* **Kimberling (6, 9, 13) Search Value:** :math:`-0.235887433544`

Notes
-----

.. container:: note-item

   The :term:`isoscelizer <isoscelizer>` equation au(X) = bv(X) = cw(X) has solution X = :ref:`X(361) <X(361)>`.

Incidence
---------

:ref:`X(361) <X(361)>` lies and on these lines:

{:ref:`1 <X(1)>`, :ref:`188 <X(188)>`}, {:ref:`164 <X(164)>`, :ref:`503 <X(503)>`}, {:ref:`266 <X(266)>`, :ref:`978 <X(978)>`}

Relations
---------

* :ref:`X(361) <X(361)>` = :ref:`X(266) <X(266)>`-:term:`Ceva conjugate <ceva-conjugate>` of :ref:`X(1) <X(1)>`

Construction
------------

.. literalinclude:: model.py
   :language: python
