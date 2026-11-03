:canonical_id: X_428
:type: code
:subtitle: EULER X_38-5th-SUBSTITUTION POINT

X_428
=====

.. rubric:: EULER X_38-5th-SUBSTITUTION POINT

.. enunciation::

   Let H = :ref:`X_4 <X_4>` and let :g:`A'B'C' << A' B' C' >>` be the :term:`pedal triangle <pedal-triangle>` of :g:`H <H>` in the plane of a triangle :g:`ABC << A B C >>`. Let

      * :g:`B_{c} <B_c>` = reflection of :g:`B' <B'>` in :g:`HC' <[ H C' ]>`, and define :g:`C_{a} <C_a>` and :g:`A_{b} <A_b>` cyclically;
      * :g:`C_{b} <C_b>` = reflection of :g:`C' <C'>` in :g:`HB' <[ H B' ]>`, and define :g:`A_{c} <A_c>` and :g:`B_{a} <B_a>` cyclically;
      * :g:`H_{a} <H_a>` = orthogonal projecton of :g:`A <A>` on :g:`B_{c}C_{b} <[ B_c C_b ]>`, and define :g:`H_{b} <H_b>` and :g:`H_{c} <H_c>` cyclically.

   Then :ref:`X_428 <X_428>` = centroid of triangle :g:`H_{a}H_{b}H_{c} << H_a H_b H_c >>`. See :person:`Antreas Hatzipolakis <antreas-hatzipolakis>` and :person:`Peter Moses <peter-moses>`, `Hyacinthos 27169 <http://www.hyacinthos.epizy.com/message.php?msg=27169>`__

.. figure:: x-00428.svg
   :alt: X_428 — EULER X_38-5th-SUBSTITUTION POINT
   :align: center

   **X_428** (*EULER X_38-5th-SUBSTITUTION POINT*) constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :g:`AB <[ A B ]>` = :math:`1`.

.. literalinclude:: model.py
   :language: python
