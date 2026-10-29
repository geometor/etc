:order: 256
:type: center
:canonical_id: X(256)
:dependencies: X(1), X(3), X(4), X(7), X(8), X(9), X(21), X(37), X(40), X(43), X(55), X(84), X(104), X(171), X(192), X(238), X(239), X(240), X(291), X(314), X(350), X(511), X(573), X(650), X(694), X(846), X(894), X(904), X(981), X(982), X(983), X(987), X(988), X(989), X(1064), X(1281), X(1909), X(3250), X(3287), X(3805)

.. _X(256):

X(256) = 1st SHARYGIN POINT
===========================

.. figure:: x-00256.svg
   :alt: X(256) = 1st SHARYGIN POINT
   :align: center

   **X(256) = 1st SHARYGIN POINT** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`1/(a^{2} + bc) : 1/(b^{2} + ca) : 1/(c^{2} + ab)`

Barycentrics
~~~~~~~~~~~~

* :math:`a/(a^{2} + bc) : b/(b^{2} + ca) : c/(c^{2} + ab)`

* **Kimberling (6, 9, 13) Search Value:** :math:`2.007180702620`

Notes
-----

.. container:: note-item

   See the description at X(1281). The lines AD, BE, CF defined there concur in :ref:`X(256) <X(256)>`.

Incidence
---------

:ref:`X(256) <X(256)>` lies and on these lines:

{:ref:`1 <X(1)>`, :ref:`511 <X(511)>`}, {:ref:`3 <X(3)>`, :ref:`987 <X(987)>`}, {:ref:`4 <X(4)>`, :ref:`240 <X(240)>`}, {:ref:`7 <X(7)>`, :ref:`982 <X(982)>`}, {:ref:`8 <X(8)>`, :ref:`192 <X(192)>`}, {:ref:`9 <X(9)>`, :ref:`43 <X(43)>`}, {:ref:`21 <X(21)>`, :ref:`238 <X(238)>`}, {:ref:`37 <X(37)>`, :ref:`694 <X(694)>`}, {:ref:`40 <X(40)>`, :ref:`989 <X(989)>`}, {:ref:`55 <X(55)>`, :ref:`983 <X(983)>`}, {:ref:`84 <X(84)>`, :ref:`988 <X(988)>`}, {:ref:`104 <X(104)>`, 1064}, {:ref:`291 <X(291)>`, :ref:`894 <X(894)>`}, {:ref:`314 <X(314)>`, :ref:`350 <X(350)>`}, {:ref:`573 <X(573)>`, :ref:`981 <X(981)>`}

Relations
---------

* :ref:`X(256) <X(256)>` = :term:`isogonal conjugate <isogonal-conjugate>` of :ref:`X(171) <X(171)>`
* :ref:`X(256) <X(256)>` = :term:`isotomic conjugate <isotomic-conjugate>` of X(1909)
* :ref:`X(256) <X(256)>` = :ref:`X(239) <X(239)>`-:term:`cross conjugate <cross-conjugate>` of :ref:`X(291) <X(291)>`
* :ref:`X(256) <X(256)>` = :term:`crosssum <crosssum>` of :ref:`X(43) <X(43)>` and :ref:`X(846) <X(846)>`
* :ref:`X(256) <X(256)>` = :ref:`X(238) <X(238)>`-:term:`Hirst inverse <hirst-inverse>` of :ref:`X(904) <X(904)>`
* :ref:`X(256) <X(256)>` = :term:`cevapoint <cevapoint>` of PU(6)
* :ref:`X(256) <X(256)>` = :term:`trilinear pole <trilinear-pole>` of line :ref:`X(650) <X(650)>`\ X(3250)
* :ref:`X(256) <X(256)>` = :term:`crossdifference <crossdifference>` of every pair of points on line X(3287)X(3805) (the perspectrix of ABC and Gemini triangle 34)

Construction
------------

.. literalinclude:: model.py
   :language: python
