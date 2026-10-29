:order: 917
:type: center
:canonical_id: X(917)
:dependencies: X(3), X(4), X(27), X(63), X(92), X(100), X(101), X(109), X(110), X(118), X(278), X(516), X(916), X(1305), X(2989), X(5190), X(8608)

.. _X(917):

X(917) = X(516)-CROSS CONJUGATE OF X(4)
=======================================

.. figure:: x-00917.svg
   :alt: X(917) = X(516)-CROSS CONJUGATE OF X(4)
   :align: center

   **X(917) = X(516)-CROSS CONJUGATE OF X(4)** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`(\sec A)/((a - b) \sin 2B + (a - c) \sin 2C) : :`

Barycentrics
~~~~~~~~~~~~

* :math:`1/((a^2 - b^2 - c^2) (a^3 (b^2 + c^2) - a^2 (b^3 + c^3) - a (b^2 - c^2)^2 + b^5 - b^3 c^2 - b^2 c^3 + c^5)) : :`

* **Kimberling (6, 9, 13) Search Value:** :math:`14.158875247015`

Notes
-----

.. container:: note-item

   Let A'B'C' be the 1st circumperp triangle. Let A″ be the pole, wrt the polar circle, of line B'C', and define B″and C″ cyclically. The lines A'A″, B'B″, C'C″ concur in :ref:`X(917) <X(917)>`. (:person:`Randy Hutson <randy-hutson>`, July 11, 2019)

Incidence
---------

:ref:`X(917) <X(917)>` lies on the circumcircle and on these lines:

{:ref:`4 <X(4)>`, :ref:`101 <X(101)>`}, {:ref:`27 <X(27)>`, :ref:`110 <X(110)>`}, {:ref:`92 <X(92)>`, :ref:`100 <X(100)>`}, {:ref:`109 <X(109)>`, :ref:`278 <X(278)>`}

Relations
---------

* :ref:`X(917) <X(917)>` = reflection of X(1305) in :ref:`X(3) <X(3)>`
* :ref:`X(917) <X(917)>` = reflection of :ref:`X(4) <X(4)>` in X(5190)
* :ref:`X(917) <X(917)>` = :term:`isogonal conjugate <isogonal-conjugate>` of :ref:`X(916) <X(916)>`
* :ref:`X(917) <X(917)>` = :ref:`X(516) <X(516)>`-:term:`cross conjugate <cross-conjugate>` of :ref:`X(4) <X(4)>`
* :ref:`X(917) <X(917)>` = polar conjugate of :term:`isotomic conjugate <isotomic-conjugate>` of X(2989)
* :ref:`X(917) <X(917)>` = :ref:`X(63) <X(63)>`-:term:`isoconjugate <isoconjugate>` of X(8608)
* :ref:`X(917) <X(917)>` = antipode of :ref:`X(4) <X(4)>` in hyperbola {A,B,C,\ :ref:`X(4) <X(4)>`,\ :ref:`X(27) <X(27)>`}
* :ref:`X(917) <X(917)>` = polar-circle-inverse of :ref:`X(118) <X(118)>`
* :ref:`X(917) <X(917)>` = the point of intersection, other than A, B, and C, of the circumcircle and hyperbola {A,B,C,\ :ref:`X(4) <X(4)>`,\ :ref:`X(27) <X(27)>`}

Construction
------------

.. literalinclude:: model.py
   :language: python
