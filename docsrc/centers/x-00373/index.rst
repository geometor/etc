:order: 373
:type: center
:canonical_id: X(373)
:dependencies: X(2), X(5), X(51), X(110), X(113), X(181), X(216), X(352), X(354), X(375), X(575), X(597), X(748), X(852), X(1499), X(2854), X(3917), X(11169), X(33842)

.. _X(373):

X(373) = CENTROID OF THE PEDAL TRIANGLE OF THE CENTROID
=======================================================

.. figure:: x-00373.svg
   :alt: X(373) = CENTROID OF THE PEDAL TRIANGLE OF THE CENTROID
   :align: center

   **X(373) = CENTROID OF THE PEDAL TRIANGLE OF THE CENTROID** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`f(a,b,c) : f(b,c,a) : f(c,a,b)`, where f(a,b,c) = 2bc + ac cos C + ab cos B, = g(a,b,c) : g(b,c,a) : g(c,a,b), where g(a,b,c) = a(b\ :sup:`4` + c\ :sup:`4` - a\ :sup:`2`\ b\ :sup:`2` - a\ :sup:`2`\ c\ :sup:`2` - 6b\ :sup:`2`\ c\ :sup:`2`)

Barycentrics
~~~~~~~~~~~~

* :math:`h(a,b,c) : h(b,c,a) : h(c,a,b)`, where h(a,b,c) = 2abc + ca\ :sup:`2`\ cos C + ba\ :sup:`2`\ cos B, :ref:`X(373) <X(373)>` = 2\*\ :ref:`X(2) <X(2)>` + :ref:`X(51) <X(51)>`

* **Kimberling (6, 9, 13) Search Value:** :math:`1.793121055895`

Incidence
---------

:ref:`X(373) <X(373)>` lies and on these lines:

{:ref:`2 <X(2)>`, :ref:`51 <X(51)>`}, {:ref:`5 <X(5)>`, :ref:`113 <X(113)>`}, {:ref:`110 <X(110)>`, :ref:`575 <X(575)>`}, {:ref:`181 <X(181)>`, :ref:`748 <X(748)>`}, {:ref:`216 <X(216)>`, :ref:`852 <X(852)>`}, {:ref:`354 <X(354)>`, :ref:`375 <X(375)>`}, {:ref:`597 <X(597)>`, 2854}

Relations
---------

* :ref:`X(373) <X(373)>` = :term:`isogonal conjugate <isogonal-conjugate>` of X(11169)
* :ref:`X(373) <X(373)>` = :term:`isotomic conjugate <isotomic-conjugate>` of polar conjugate of X(33842)
* :ref:`X(373) <X(373)>` = :term:`crossdifference <crossdifference>` of every pair of points on line :ref:`X(352) <X(352)>`\ X(1499)
* :ref:`X(373) <X(373)>` = {:ref:`X(2) <X(2)>`,\ :ref:`X(51) <X(51)>`}-harmonic conjugate of X(3917)

Construction
------------

.. literalinclude:: model.py
   :language: python
