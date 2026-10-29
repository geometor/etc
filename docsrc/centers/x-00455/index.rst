:order: 455
:type: center
:canonical_id: X(455)
:dependencies: X(2), X(3), X(25), X(159), X(1370), X(2386), X(3162), X(13575), X(17407), X(23115), X(39733), X(40009), X(40144), X(41361), X(41766), X(52041)

.. _X(455):

X(455) = EULER X(159)-11th-SUBSTITUTION POINT
=============================================

.. figure:: x-00455.svg
   :alt: X(455) = EULER X(159)-11th-SUBSTITUTION POINT
   :align: center

   **X(455) = EULER X(159)-11th-SUBSTITUTION POINT** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`u^{2}\sec A : v^{2}\sec B : w^{2}\sec C`, where u : v : w = :ref:`X(159) <X(159)>`

Barycentrics
~~~~~~~~~~~~

* :math:`u^{2}\tan A : v^{2}\tan B : w^{2}\tan C`
* :math:`a^2*(a^2 + b^2 - c^2)*(a^2 - b^2 + c^2)*(a^6 + a^4*b^2 - a^2*b^4 - b^6 + a^4*c^2 - 2*a^2*b^2*c^2 + b^4*c^2 - a^2*c^4 + b^2*c^4 - c^6)^2 : :`

* **Kimberling (6, 9, 13) Search Value:** :math:`-0.233349250637`

Notes
-----

.. container:: note-item

   As a point on the Euler line, :ref:`X(455) <X(455)>` has Shinagawa coefficients (4(E + F)\ :sup:`3`\ F\ :sup:`2` - E\ :sup:`2`\ FS\ :sup:`2`, -4(E + F)\ :sup:`4`\ F + (E + F)(E + 4F)ES\ :sup:`2`).

Incidence
---------

:ref:`X(455) <X(455)>` lies and on these lines:

{:ref:`2 <X(2)>`, :ref:`3 <X(3)>`}, {:ref:`159 <X(159)>`, 17407}, {2386, 40144}

Relations
---------

* :ref:`X(455) <X(455)>` = X(1370)-:term:`Ceva conjugate <ceva-conjugate>` of X(3162)
* :ref:`X(455) <X(455)>` = X(39733)-:term:`isoconjugate <isoconjugate>` of X(52041)
* :ref:`X(455) <X(455)>` = :ref:`X(25) <X(25)>`-Dao conjugate of X(13575)
* :ref:`X(455) <X(455)>` = barycentric product X(i)\*X(j) for these {i,j}: {:ref:`159 <X(159)>`, 41361}, {1370, 3162}, {23115, 41766}
* :ref:`X(455) <X(455)>` = barycentric quotient X(i)/X(j) for these {i,j}: {3162, 13575}, {41361, 40009}
* :ref:`X(455) <X(455)>` = {X(i),X(j)}-harmonic conjugate of X(k) for these (i,j,k): {}

Construction
------------

.. literalinclude:: model.py
   :language: python
