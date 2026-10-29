:order: 304
:type: center
:canonical_id: X(304)
:dependencies: X(1), X(6), X(8), X(19), X(25), X(48), X(63), X(69), X(72), X(75), X(76), X(85), X(92), X(255), X(279), X(293), X(305), X(306), X(309), X(312), X(322), X(326), X(337), X(341), X(345), X(346), X(348), X(560), X(561), X(662), X(668), X(742), X(799), X(811), X(1096), X(1102), X(1565), X(1895), X(1921), X(1958), X(1973), X(2172), X(2176), X(2349), X(3061), X(3263), X(16583), X(21216)

.. _X(304):

X(304) = ISOTOMIC CONJUGATE OF X(19)
====================================

.. figure:: x-00304.svg
   :alt: X(304) = ISOTOMIC CONJUGATE OF X(19)
   :align: center

   **X(304) = ISOTOMIC CONJUGATE OF X(19)** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`(\cot A)\csc^{2}A : (\cot B)\csc^{2}B : (\cot C)\csc^{2}C`
* :math:`\cos A \csc(A - \omega ) : \cos B \csc(B - \omega ) : \cos C \csc(C - \omega )`

Barycentrics
~~~~~~~~~~~~

* :math:`(\cos A)\csc^{2}A : (\cos B)\csc^{2}B : (\cos C)\csc^{2}C`

* **Kimberling (6, 9, 13) Search Value:** :math:`6.190909895273`

Notes
-----

.. container:: note-item

   Let AaBaCa, AbBbCb, AcBcCc be the A-, B-, and C-anti-altimedial triangles, resp. :ref:`X(304) <X(304)>` is the trilinear product Ba\*Ca\*Cb\*Ab\*Ac\*Bc. (:person:`Randy Hutson <randy-hutson>`, November 2, 2017)

Incidence
---------

:ref:`X(304) <X(304)>` lies and on these lines:

{:ref:`1 <X(1)>`, :ref:`75 <X(75)>`}, {:ref:`8 <X(8)>`, 3263}, {:ref:`63 <X(63)>`, 1102}, {:ref:`69 <X(69)>`, :ref:`72 <X(72)>`}, {:ref:`76 <X(76)>`, :ref:`85 <X(85)>`}, {:ref:`92 <X(92)>`, :ref:`561 <X(561)>`}, {:ref:`255 <X(255)>`, :ref:`293 <X(293)>`}, {:ref:`279 <X(279)>`, :ref:`346 <X(346)>`}, {:ref:`305 <X(305)>`, :ref:`306 <X(306)>`}, {:ref:`309 <X(309)>`, :ref:`322 <X(322)>`}, {:ref:`337 <X(337)>`, 1565}, {:ref:`341 <X(341)>`, :ref:`668 <X(668)>`}, {:ref:`345 <X(345)>`, :ref:`348 <X(348)>`}, {:ref:`662 <X(662)>`, 2172}, {:ref:`742 <X(742)>`, 2176}, {:ref:`799 <X(799)>`, 2349}, {:ref:`811 <X(811)>`, 1895}, {1921, 3061}, {1958, 1973}

Relations
---------

* :ref:`X(304) <X(304)>` = :term:`isogonal conjugate <isogonal-conjugate>` of X(1973)
* :ref:`X(304) <X(304)>` = :term:`isotomic conjugate <isotomic-conjugate>` of :ref:`X(19) <X(19)>`
* :ref:`X(304) <X(304)>` = :term:`complement <complement>` of X(21216)
* :ref:`X(304) <X(304)>` = :term:`anticomplement <anticomplement>` of X(16583)
* :ref:`X(304) <X(304)>` = :term:`cevapoint <cevapoint>` of X(i) and X(j) for these (i,j): (:ref:`63 <X(63)>`, :ref:`326 <X(326)>`), (:ref:`69 <X(69)>`, :ref:`345 <X(345)>`), (:ref:`312 <X(312)>`, :ref:`322 <X(322)>`)
* :ref:`X(304) <X(304)>` = X(i)-:term:`cross conjugate <cross-conjugate>` of X(j) for these (i,j): (:ref:`63 <X(63)>`, :ref:`75 <X(75)>`), (:ref:`306 <X(306)>`, :ref:`69 <X(69)>`)
* :ref:`X(304) <X(304)>` = X(i)-:term:`isoconjugate <isoconjugate>` of X(j) for these (i,j): (:ref:`6 <X(6)>`, :ref:`25 <X(25)>`), (:ref:`48 <X(48)>`, 1096), (:ref:`92 <X(92)>`, :ref:`560 <X(560)>`)
* :ref:`X(304) <X(304)>` = polar conjugate of X(1096)
* :ref:`X(304) <X(304)>` = trilinear product of vertices of Gemini triangle 35
* :ref:`X(304) <X(304)>` = trilinear product of vertices of Gemini triangle 36

Construction
------------

.. literalinclude:: model.py
   :language: python
