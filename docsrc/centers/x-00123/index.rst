:order: 123
:type: center
:canonical_id: X(123)
:dependencies: X(2), X(4), X(108), X(521), X(1415), X(2443), X(3436), X(6332), X(6588), X(7004), X(15385), X(34455), X(38972)

.. _X(123):

X(123) = X(108)-OF-MEDIAL-TRIANGLE
==================================

.. figure:: x-00123.svg
   :alt: X(123) = X(108)-OF-MEDIAL-TRIANGLE
   :align: center

   **X(123) = X(108)-OF-MEDIAL-TRIANGLE** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`(\csc A)(\sec B - \sec C)[(\sec A)(\sin^{2}B - \sin^{2}C) + \sin C \tan C - \sin B \tan B] : :`

Barycentrics
~~~~~~~~~~~~

* :math:`(\sec B - \sec C)[(\sec A)(\sin^{2}B - \sin^{2}C) + \sin C \tan C - \sin B \tan B]`
* :math:`(a - b - c)(b - c)^2(a^2 - b^2 - c^2)(a^4 - b^4 - c^4 + 2a^2bc - 2ab^2c - 2abc^2 + 2b^2c^2) : :`

* **Kimberling (6, 9, 13) Search Value:** :math:`3.984933555176`

Incidence
---------

:ref:`X(123) <X(123)>` lies on the nine-point circle and hese lines: 2,108 3,119 10,117 113,960

Relations
---------

* :ref:`X(123) <X(123)>` = :term:`isogonal conjugate <isogonal-conjugate>` of X(15385)
* :ref:`X(123) <X(123)>` = :term:`complement <complement>` of :ref:`X(108) <X(108)>`
* :ref:`X(123) <X(123)>` = :term:`complementary conjugate <complementary-conjugate>` of :ref:`X(521) <X(521)>`
* :ref:`X(123) <X(123)>` = :ref:`X(2) <X(2)>`-:term:`Ceva conjugate <ceva-conjugate>` of X(6588)
* :ref:`X(123) <X(123)>` = :ref:`X(4) <X(4)>`-Ceva conjugate of :ref:`X(521) <X(521)>`
* :ref:`X(123) <X(123)>` = Spieker-radical-circle-inverse of X(34455)
* :ref:`X(123) <X(123)>` = :ref:`X(108) <X(108)>`-of-:term:`medial triangle <medial-triangle>`
* :ref:`X(123) <X(123)>` = Stevanovic-circle-inverse of X(38972)
* :ref:`X(123) <X(123)>` = :term:`crossdifference <crossdifference>` of every pair of points on line X(1415)X(2443)
* :ref:`X(123) <X(123)>` = trilinear product X(i)\*X(j) for these {i,j}: {3436, 7004}, {6332, 6588}

Construction
------------

.. literalinclude:: model.py
   :language: python
