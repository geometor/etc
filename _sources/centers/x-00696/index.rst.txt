:order: 696
:type: center
:canonical_id: X(696)
:dependencies: X(30), X(98), X(105), X(106), X(111), X(313), X(511), X(518), X(519), X(524), X(536), X(538), X(561), X(674), X(675), X(697), X(768)

.. _X(696):

X(696) = EVEN (- 4, - 3) INFINITY POINT
=======================================

.. figure:: x-00696.svg
   :alt: X(696) = EVEN (- 4, - 3) INFINITY POINT
   :align: center

   **X(696) = EVEN (- 4, - 3) INFINITY POINT** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`f(a,b,c) : f(b,c,a) : f(c,a,b)`, where f(a,b,c) = a :sup:`-5`\ (b :sup:`-3` + c :sup:`-3`) - a :sup:`-4`\ (b :sup:`-4` + c :sup:`-4`)

Barycentrics
~~~~~~~~~~~~

* :math:`g(a,b,c) : g(b,c,a) : g(c,a,b)`, where g(a,b,c) = af(a,b,c)

Notes
-----

.. container:: note-item

   As the :term:`isogonal conjugate <isogonal-conjugate>` of a point on the circumcircle, :ref:`X(696) <X(696)>` lies on the line at infinity. The first trilinear coordinate has the form

      a\ :sup:`m-1`\ (b\ :sup:`n` + c\ :sup:`n`) - a\ :sup:`n-1`\ (b\ :sup:`m` + c\ :sup:`m`).

.. container:: note-item

   If m and n are distinct integers, this form fits the definition of **even** :term:`polynomial center <polynomial-center>` as in :person:`Clark Kimberling <clark-kimberling>`, "Functional equations associated with triangle geometry," *Aequationes Mathematicae* 45 (1993) 127-152. This form, perhaps appearing initially here (July 7, 2001) defines a :term:`triangle center <triangle-center>` for arbitrary distinct real numbers m and n. Selected even infinity and circumcircle points begin at :ref:`X(696) <X(696)>`; odd ones begin at :ref:`X(768) <X(768)>`.

.. container:: note-item

   Certain points of this type occur prior to this section. They are as follows:

Incidence
---------

:ref:`X(696) <X(696)>` lies and on these lines:

{:ref:`30 <X(30)>`, :ref:`511 <X(511)>`}, {:ref:`313 <X(313)>`, :ref:`561 <X(561)>`}

Relations
---------

* :ref:`X(538) <X(538)>` = even (- 2, 0) infinity point
* :ref:`X(536) <X(536)>` = even (- 1, 0) infinity point
* :ref:`X(519) <X(519)>` = even (0, 1) infinity point
* :ref:`X(106) <X(106)>` = even (0, 1) circumcircle point
* :ref:`X(524) <X(524)>` = even (0, 2) infinity point
* :ref:`X(111) <X(111)>` = even (0, 2) circumcircle point
* :ref:`X(518) <X(518)>` = even (1, 2) infinity point
* :ref:`X(105) <X(105)>` = even (1, 2) circumcircle point
* :ref:`X(674) <X(674)>` = even (2, 3) infinity point
* :ref:`X(675) <X(675)>` = even (2, 3) circumcircle point
* :ref:`X(511) <X(511)>` = even (2, 4) infinity point
* :ref:`X(98) <X(98)>` = even (2, 4) circumcircle point
* :ref:`X(696) <X(696)>` = isogonal conjugate of :ref:`X(697) <X(697)>`\ \

Construction
------------

.. literalinclude:: model.py
   :language: python
