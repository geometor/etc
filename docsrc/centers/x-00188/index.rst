:order: 188
:type: center
:canonical_id: X(188)
:dependencies: X(1), X(2), X(4), X(9), X(40), X(65), X(164), X(166), X(167), X(173), X(174), X(178), X(236), X(259), X(266), X(361), X(4146), X(5451)

.. _X(188):

X(188) = 2nd MID-ARC POINT OF ANTICOMPLEMENTARY TRIANGLE
========================================================

.. figure:: x-00188.svg
   :alt: X(188) = 2nd MID-ARC POINT OF ANTICOMPLEMENTARY TRIANGLE
   :align: center

   **X(188) = 2nd MID-ARC POINT OF ANTICOMPLEMENTARY TRIANGLE** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`\csc A/2 : \csc B/2 : \csc C/2`
* :math:`[bc(b + c - a)]^{1/2} : :`
* :math:`\csc A \cos A/2 : :`
* :math:`|AX(1)| : |BX(1)| : |CX(1)|`
* :math:`\sec A' : \sec B', \sec C'`, where A'B'C' = :term:`excentral triangle <excentral-triangle>`

Barycentrics
~~~~~~~~~~~~

* 1/(sin(B/2) sin(C/2) + sin(A/2)) : : c.f., X(5451)
* 1/(csc(B/2) csc(C/2) + csc(A/2)) : : c.f., X(5451)
* :math:`\cos A/2 : \cos B/2 : \cos C/2`

* **Kimberling (6, 9, 13) Search Value:** :math:`3.169616971348`

Notes
-----

.. container:: note-item

   Let A'B'C' be the excentral triangle of ABC, so that A' = -1 : 1 : 1 (trilinears). Let A'' be the point where the bisector of angle BA'C meets the line BC. Define B'' and C'' cyclically. The lines AA'', BB'', CC'' concur in :ref:`X(188) <X(188)>`. (Seiichi Kirikami, February 14, 2010)

.. container:: note-item

   Let Ea be the ellipse with B and C as foci and passing through the A-excenter, and define Eb and Ec cyclically. Let La be the line tangent to Ea at the A-excenter, and define Lb and Lc cyclically. Let A' = La∩BC, B' = Lb∩CA, C' = Lc∩AB. Then A', B', C' are collinear, and the :term:`trilinear pole <trilinear-pole>` of line A'B'C' = :ref:`X(188) <X(188)>`. Note: The triangle formed by La, Lb, Lc is also the excentral triangle of the excentral triangle. Alternately, let A″ be the trilinear pole of line La, and define B″, C″ cyclically. The lines AA″, BB″ and CC″ concur at :ref:`X(188) <X(188)>`; see also :ref:`X(174) <X(174)>`. (:person:`Randy Hutson <randy-hutson>`, December 2, 2017)

Incidence
---------

:ref:`X(188) <X(188)>` lies and on these lines:

{:ref:`1 <X(1)>`, :ref:`361 <X(361)>`}, {:ref:`2 <X(2)>`, :ref:`178 <X(178)>`}, {:ref:`9 <X(9)>`, :ref:`173 <X(173)>`}, {:ref:`40 <X(40)>`, :ref:`164 <X(164)>`}, {:ref:`166 <X(166)>`, :ref:`167 <X(167)>`}, {:ref:`174 <X(174)>`, :ref:`266 <X(266)>`}

Relations
---------

* :ref:`X(188) <X(188)>` = :term:`isogonal conjugate <isogonal-conjugate>` of :ref:`X(266) <X(266)>`
* :ref:`X(188) <X(188)>` = :term:`isotomic conjugate <isotomic-conjugate>` of X(4146)
* :ref:`X(188) <X(188)>` = :term:`anticomplement <anticomplement>` of :ref:`X(178) <X(178)>`
* :ref:`X(188) <X(188)>` = :ref:`X(2) <X(2)>`-:term:`Ceva conjugate <ceva-conjugate>` of :ref:`X(236) <X(236)>`
* :ref:`X(188) <X(188)>` = :term:`cevapoint <cevapoint>` of :ref:`X(1) <X(1)>` and :ref:`X(164) <X(164)>`
* :ref:`X(188) <X(188)>` = :ref:`X(259) <X(259)>`-:term:`cross conjugate <cross-conjugate>` of :ref:`X(174) <X(174)>`
* :ref:`X(188) <X(188)>` = :term:`crosssum <crosssum>` of :ref:`X(1) <X(1)>` and :ref:`X(361) <X(361)>`
* :ref:`X(188) <X(188)>` = :ref:`X(188) <X(188)>`-:term:`beth conjugate <beth-conjugate>` of :ref:`X(266) <X(266)>`
* :ref:`X(188) <X(188)>` = SS(A→A') of :ref:`X(4) <X(4)>`, where A'B'C' is the excentral triangle
* :ref:`X(188) <X(188)>` = isotomic conjugate of X(4146)
* :ref:`X(188) <X(188)>` = :ref:`X(65) <X(65)>`-of-excentral-triangle
* :ref:`X(188) <X(188)>` = perspector of circumconic centered at :ref:`X(236) <X(236)>`
* :ref:`X(188) <X(188)>` = center of circumconic that is locus of trilinear poles of lines passing through :ref:`X(236) <X(236)>`
* :ref:`X(188) <X(188)>` = excentral-to-ABC :term:`trilinear image <trilinear-image>` of :ref:`X(1) <X(1)>`
* :ref:`X(188) <X(188)>` = excentral-to-ABC :term:`barycentric image <barycentric-image>` of :ref:`X(164) <X(164)>`

Construction
------------

.. literalinclude:: model.py
   :language: python
