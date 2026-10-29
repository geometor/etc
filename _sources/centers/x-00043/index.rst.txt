:order: 43
:type: center
:canonical_id: X(43)
:dependencies: X(1), X(2), X(6), X(8), X(9), X(31), X(35), X(40), X(42), X(46), X(55), X(57), X(58), X(63), X(72), X(75), X(81), X(87), X(100), X(165), X(169), X(170), X(174), X(181), X(192), X(210), X(218), X(238), X(256), X(259), X(312), X(330), X(362), X(365), X(366), X(507), X(509), X(518), X(573), X(660), X(740), X(750), X(851), X(872), X(970), X(979), X(982), X(984), X(986), X(995), X(1011), X(1018), X(1695), X(1766), X(3741), X(3840), X(5121), X(6384), X(22370)

.. _X(43):

X(43) = -CEVA CONJUGATE OF X(1)
===============================

.. figure:: x-00043.svg
   :alt: X(43) = -CEVA CONJUGATE OF X(1)
   :align: center

   **X(43) = -CEVA CONJUGATE OF X(1)** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`ab + ac - bc : bc + ba - ca : ca + cb - ab`
* :math:`\csc B + \csc C - \csc A : \csc C + \csc A - \csc B : \csc A + \csc B - \csc C`

Barycentrics
~~~~~~~~~~~~

* :math:`a(ab + ac - bc) : b(bc + ba - ca) : c(ca + cb - ab)`

* **Kimberling (6, 9, 13) Search Value:** :math:`0.257220860135`

Notes
-----

.. container:: note-item

   Let A' be the inverse-in-excircles-radical-circle of the midpoint of BC, and define B' and C' cyclically. Triangle A'B'C' is inscribed in the Apollonius circle and homothetic to the :term:`excentral triangle <excentral-triangle>` at :ref:`X(43) <X(43)>`. (:person:`Randy Hutson <randy-hutson>`, November 30, 2018)

.. container:: note-item

   :ref:`X(43) <X(43)>` is the {:ref:`X(2) <X(2)>`,\ :ref:`X(42) <X(42)>`}-harmonic conjugate of :ref:`X(1) <X(1)>`. :ref:`X(43) <X(43)>` is the external center of similitude of the Bevan circle and Apollonius circle; the internal center is X(1695).

Incidence
---------

:ref:`X(43) <X(43)>` lies on the Kiepert hyperbola of the excentral triangle and on these lines:

{:ref:`1 <X(1)>`, :ref:`2 <X(2)>`}, {:ref:`6 <X(6)>`, :ref:`87 <X(87)>`}, {:ref:`9 <X(9)>`, 256}, {:ref:`31 <X(31)>`, :ref:`100 <X(100)>`}, {:ref:`35 <X(35)>`, 1011}, {:ref:`40 <X(40)>`, 970}, {:ref:`46 <X(46)>`, 851}, {:ref:`55 <X(55)>`, 238}, {:ref:`57 <X(57)>`, 181}, {:ref:`58 <X(58)>`, 979}, {:ref:`72 <X(72)>`, 986}, {:ref:`75 <X(75)>`, 872}, {:ref:`81 <X(81)>`, 750}, {165, 573}, {170, 218}, {210, 984}, {312, 740}, {518, 982}

Relations
---------

* :ref:`X(43) <X(43)>` = reflection of :ref:`X(1) <X(1)>` in X(995)
* :ref:`X(43) <X(43)>` = :term:`isogonal conjugate <isogonal-conjugate>` of :ref:`X(87) <X(87)>`
* :ref:`X(43) <X(43)>` = :term:`isotomic conjugate <isotomic-conjugate>` of X(6384)
* :ref:`X(43) <X(43)>` = :term:`anticomplement <anticomplement>` of X(3840)
* :ref:`X(43) <X(43)>` = :ref:`X(6) <X(6)>`-:term:`Ceva conjugate <ceva-conjugate>` of :ref:`X(1) <X(1)>`
* :ref:`X(43) <X(43)>` = X(192)-:term:`cross conjugate <cross-conjugate>` of :ref:`X(1) <X(1)>`
* :ref:`X(43) <X(43)>` = :term:`crosssum <crosssum>` of :ref:`X(2) <X(2)>` and X(330)
* :ref:`X(43) <X(43)>` = :ref:`X(55) <X(55)>`-:term:`Hirst inverse <hirst-inverse>` of X(238)
* :ref:`X(43) <X(43)>` = inverse-in-excircles-radical-circle of X(5121)
* :ref:`X(43) <X(43)>` = perspector of ABC and extraversion triangle of :ref:`X(87) <X(87)>`
* :ref:`X(43) <X(43)>` = trilinear product of extraversions of :ref:`X(87) <X(87)>`
* :ref:`X(43) <X(43)>` = excentral-isogonal conjugate of X(1766)
* :ref:`X(43) <X(43)>` = polar conjugate of isotomic conjugate of X(22370)
* :ref:`X(43) <X(43)>` = perspector of Gemini triangle 5 and cross-triangle of Gemini triangles 3 and 5
* :ref:`X(43) <X(43)>` = X(i)-:term:`aleph conjugate <aleph-conjugate>` of X(j) for these (i,j): (:ref:`1 <X(1)>`, :ref:`9 <X(9)>`), (:ref:`6 <X(6)>`, :ref:`43 <X(43)>`), (:ref:`55 <X(55)>`, 170), (:ref:`100 <X(100)>`, 1018), (174, 169), (259, 165), (365, :ref:`1 <X(1)>`), (366, :ref:`63 <X(63)>`), (507, 362), (509, :ref:`57 <X(57)>`)
* :ref:`X(43) <X(43)>` = X(660)-:term:`beth conjugate <beth-conjugate>` of :ref:`X(43) <X(43)>`
* :ref:`X(43) <X(43)>` = {:ref:`X(2) <X(2)>`,\ :ref:`X(8) <X(8)>`}-harmonic conjugate of X(3741)

Construction
------------

.. literalinclude:: model.py
   :language: python
