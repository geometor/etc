:order: 369
:type: center
:canonical_id: X(369)

.. _X(369):
.. _1st-TrisectedPerimeterPoint:

X(369) = 1st TRISECTED PERIMETER POINT
======================================

.. enunciation::

   There exist points :g:`A' <A'>`, :g:`B' <B'>`, :g:`C' <C'>` on segments :g:`BC <[ B C ]>`, :g:`CA <[ C A ]>`, :g:`AB <[ A B ]>`, respectively, such that :g:`AB' <[ A B' ]>` + :g:`AC' <[ A C' ]>` = :g:`BC' <[ B C' ]>` + :g:`BA' <[ B A' ]>` = :g:`CA' <[ C A' ]>` + :g:`CB' <[ C B' ]>` = (a + b + c)/3, and the lines :g:`AA' <[ A A' ]>`, :g:`BB' <[ B B' ]>`, :g:`CC' <[ C C' ]>` concur in :ref:`X(369) <X(369)>`. Near the end of the 20th century, Yff found trilinears for :ref:`X(369) <X(369)>` in terms of the unique real root, r, of the cubic polynomial

.. figure:: x-00369.svg
   :alt: X(369) = 1st TRISECTED PERIMETER POINT
   :align: center

   **X(369) = 1st TRISECTED PERIMETER POINT** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :g:`AB <[ A B ]>` = :math:`1`.

.. signature:: center

   | **Trilinears:** :math:`x : y : z (see below)`
   | **Barycentrics:** :math:`ax : by : cz`
   | **Search Value (6, 9, 13):** :math:`2.053651811125`

Notes
-----

.. container:: note-item

   :math:`2t^{3}` - 3(a + b + c)\ :math:`t^{2}` + (:math:`a^{2}` + :math:`b^{2}` + :math:`c^{2}` + 8bc + 8ca + 8ab)t - (:math:`cb^{2}` + :math:`ac^{2}` + :math:`ba^{2}` + :math:`5bc^{2}` + :math:`5ca^{2}` + :math:`5ab^{2}` + 9abc),

      as follows: x = bc(r - c + a)(r - a + b). Here x(a,c,b) ≠ x(a,b,c), so that y and z are not obtained from x by cyclically permutating a,b,c. At the geometry conference held at Miami University of Ohio, October 2, 2004, Yff, proved that :ref:`X(369) <X(369)>` is also given by :math:`x_{1} : y_{1} : z_{1}` where :math:`y_{1}` : :math:`z_{1}` *are* given by cyclic permutations of a,b,c, in :math:`x_{1}`, where

   :math:`x_{1}` = bc[:math:`r^{2}` - (2c + a)r + (- :math:`a^{2}` + :math:`b^{2}` + :math:`2c^{2}` + 2bc + 3ca + 2ab].

.. container:: note-item

   His presentation included a proof that there is only one point for which :g:`AB' <[ A B' ]>` + :g:`AC' <[ A C' ]>` = :g:`BC' <[ B C' ]>` + :g:`BA' <[ B A' ]>` = :g:`CA' <[ C A' ]>` + :g:`CB' <[ C B' ]>` .

.. toctree::
   :hidden:

   code
