:order: 973
:type: center
:canonical_id: X(973)
:dependencies: X(3), X(5), X(6), X(24), X(51), X(52), X(68), X(442), X(568), X(974), X(1209)

.. _X(973):
.. _FirstEhrmannPoint:

X(973) = 1st EHRMANN POINT
==========================

.. figure:: x-00973.svg
   :alt: X(973) = 1st EHRMANN POINT
   :align: center

   **X(973) = 1st EHRMANN POINT** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`u[a^{10} - 3a^{8}s + a^{6}(2b^{4} + 3b^{2}c^{2} + 2c^{4}) + a^{4}s(2b^{4} - b^{2}c^{2} + 2c^{4}) - a^{2}(b^{2} - c^{2})^{2}(3b^{4} + 5b^{2}c^{2} + s(b^{2} - c^{2})^{2}(b^{4} - b^{2}c^{2} + c^{4})] : : ,`, where u : v : w = :ref:`X(51) <X(51)>` and s = b\ :sup:`2` + c\ :sup:`2`

* **Kimberling (6, 9, 13) Search Value:** :math:`3.147032989910`

Notes
-----

.. container:: note-item

   For constructions of :ref:`X(973) <X(973)>` and :ref:`X(974) <X(974)>`, see :cite:`Hyacinthos <hyacinthos>` message 3695, Sept. 1, 2001, and related messages.

.. container:: note-item

   Let A'B'C' be the :term:`orthic triangle <orthic-triangle>`. :ref:`X(973) <X(973)>` is the radical center of the nine-point circles of AB'C', BC'A', CA'B'. (:person:`Randy Hutson <randy-hutson>`, January 29, 2018)

Incidence
---------

:ref:`X(973) <X(973)>` lies and on these lines:

{:ref:`5 <X(5)>`, :ref:`51 <X(51)>`}, {:ref:`6 <X(6)>`, :ref:`24 <X(24)>`}, {:ref:`68 <X(68)>`, :ref:`568 <X(568)>`}

Relations
---------

* :ref:`X(973) <X(973)>` = midpoint of :ref:`X(52) <X(52)>` and X(1209)
* :ref:`X(973) <X(973)>` = :term:`crosssum <crosssum>` of :ref:`X(3) <X(3)>` and X(1209)
* :ref:`X(973) <X(973)>` = :ref:`X(442) <X(442)>`-of-orthic-triangle if ABC is acute

Construction
------------

.. literalinclude:: model.py
   :language: python
