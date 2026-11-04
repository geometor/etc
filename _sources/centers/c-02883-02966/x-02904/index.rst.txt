:order: 2904
:canonical_id: X_2904
:subtitle: ORTHIC-ISOGONAL CONJUGATE OF X_24
:dependencies: X_3, X_4, X_6, X_24, X_25, X_52, X_70, X_90, X_155, X_156, X_185, X_195, X_378, X_403, X_576, X_648, X_847, X_1112, X_1843, X_1986, X_1994, X_2883, X_2888, X_2914, X_14111

.. _X_2904:

X_2904
======

.. rubric:: ORTHIC-ISOGONAL CONJUGATE OF X_24

.. enunciation::

   Let :g:`P <P>` be an arbitrary point of the circumcircle , O, and let S(P) be the Simson-Wallace line of :g:`P <P>`, and :g:`P' <P'>` the reflection of :g:`P <P>` in S(P). The locus of :g:`P' <P'>` as P ranges through :g:`O <O>` is a bicircular circumquartic that meets the sidelines of :g:`ABC << A B C >>` in 6 points other than :g:`A <A>`, :g:`B <B>`, :g:`C <C>`. The 6 points lie on a conic, here called the **Montesdeoca conic**, M. The center of M is :ref:`X_2904 <X_2904>`, and the perspector of M is X_14111. Let u = :math:`S_{A}`, v = :math:`S_{B}`, w = :math:`S_{C}`, :math:`f(a,b,c) = u^{2}(S^{2} - v^{2})(S^{2} - w^{2})`, :math:`g(a,b,c) = 2vw(u^{2} - S^{2})(S^{2} + vw)`. A barycentric equation for M is

.. figure:: x-02904.svg
   :alt: X_2904 — ORTHIC-ISOGONAL CONJUGATE OF X_24
   :align: center

   **X_2904** (*ORTHIC-ISOGONAL CONJUGATE OF X_24*) constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :g:`AB <[ A B ]>` = :math:`1`.

.. admonition:: Constructed Elements
   :class: note

   * **Central Lines:** :g:`{6, 70} <{ 6, 70 }>`, :g:`{24, 52} <{ 24, 52 }>`
   * **Related Centers:** :g:`X_4 <X_4>` (:ref:`ORTHOCENTER <X_4>`), :g:`X_24 <X_24>` (:ref:`PERSPECTOR OF ABC AND ORTHIC-OF-ORTHIC TRIANGLE <X_24>`), :g:`X_6 <X_6>` (:ref:`SYMMEDIAN POINT <X_6>`), :g:`X_70 <X_70>` (:ref:`ISOGONAL CONJUGATE OF X(26) <X_70>`), :g:`X_52 <X_52>` (:ref:`ORTHOCENTER OF ORTHIC TRIANGLE <X_52>`)

.. signature:: center

   | **Trilinears:** :math:`f(a,b,c) : f(b,c,a) : f(c,a,b)`, where f(a,b,c) is as described just before :ref:`X_2883 <X_2883>`
   | **Barycentrics:** :math:`a^{2}(a^{4} + b^{4} + c^{4} - 2a^{2}b^{2} - 2a^{2}c^{2})[a^{6} - 3a^{4}(b^{2} + c^{2}) + 3a^{2}(b^{4} + c^{4}) - (b^{2} - c^{2})^{2}(b^{2} + c^{2})]/(b^{2} + c^{2} - a^{2}) : :`
   | **Search Value (6, 9, 13):** :math:`-1.962230807342`

.. collapse:: Incident Central Lines
   :badge: 11 lines
   :class: line-catalog

   {:ref:`3 <X_3>`, :ref:`1986 <X_1986>`}, {:ref:`4 <X_4>`, :ref:`1994 <X_1994>`}, {:ref:`6 <X_6>`, :ref:`70 <X_70>`}, {:ref:`24 <X_24>`, :ref:`52 <X_52>`}, {:ref:`25 <X_25>`, :ref:`195 <X_195>`}, {:ref:`155 <X_155>`, :ref:`403 <X_403>`}, {:ref:`156 <X_156>`, :ref:`1112 <X_1112>`}, {:ref:`185 <X_185>`, :ref:`378 <X_378>`}, {:ref:`576 <X_576>`, :ref:`1843 <X_1843>`}, {:ref:`648 <X_648>`, :ref:`847 <X_847>`}, {:ref:`2888 <X_2888>`, :ref:`2914 <X_2914>`}

.. collapse:: Functional Relations
   :badge: 2 relations

   * :ref:`X_2904 <X_2904>` = :ref:`X_4 <X_4>`-:term:`Ceva conjugate <ceva-conjugate>` of :ref:`X_24 <X_24>`
   * :ref:`X_2904 <X_2904>` = :ref:`X_90 <X_90>`-of-orthic-triangle if :g:`ABC << A B C >>` is acute

Notes
-----

.. container:: note-item

   Let :g:`O <O>` be the circumcircle of a triangle :g:`ABC << A B C >>`. Let

      * :g:`A' <A'>` = perpendicular bisector of segment :g:`OA <[ O A ]>`, and define :g:`B' <B'>` and :g:`C' <C'>` cyclically
      * :g:`A″ <A″>` = :g:`B' <B'>`\ ∩\ :g:`C' <C'>`, and define :g:`B″ <B″>` and :g:`C″ <C″>` cyclically
      * :g:`A* <A*>` = reflection of :g:`A* <A*>` in :g:`BC <[ B C ]>`, and define :g:`B* <B*>` and :g:`C* <C*>` cyclically.

   Then :g:`A*B*C* << A* B* C* >>` is perspective to the :term:`orthic triangle <orthic-triangle>` of :g:`ABC << A B C >>`, and the perspector is :ref:`X_2904 <X_2904>`. (:person:`Angel Montesdeoca <angel-montesdeoca>`, November 12, 2016).

.. container:: note-item

   f(a,b,c)\ :math:`x^{2}` + f(b,c,a)\ :math:`y^{2}` + (f,c,a,b)\ :math:`z^{2}` + g(a,b,c)yz + g(b,c,a)zx + g(c,b,a)xy = 0.

.. container:: note-item

   See `HG121017 <http://amontes.webs.ull.es/otrashtm/HGT2017.htm#HG121017>`__ and :ref:`X_2904 <X_2904>`.

.. toctree::
   :hidden:

   code
