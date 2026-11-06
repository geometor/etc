:order: 3078
:canonical_id: X_3078
:subtitle: DANNEELS POINT OF X_5
:dependencies: X_2, X_3, X_5, X_233, X_288, X_2167, X_8012

.. _X_3078:

X_3078
======

.. rubric:: DANNEELS POINT OF X_5

.. enunciation::

   Let :g:`A'B'C' << A' B' C' >>` be the :term:`cevian triangle <cevian-triangle>` of a point :g:`X <X>` =\ :math:`x : y : z` (trilinears), let L(A) be the line through :g:`A <A>` parallel to :g:`B'C' <[ B' C' ]>`, and define L(B) and L(C) cyclically. The lines L(A), L(B), L(C) form a triangle homothetic to :g:`A'B'C' << A' B' C' >>`, with homothetic center

.. figure:: x-03078.svg
   :alt: X_3078 — DANNEELS POINT OF X_5
   :align: center

   **X_3078** (*DANNEELS POINT OF X_5*) constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :g:`AB <[ A B ]>` = :math:`1`.

.. admonition:: Constructed Elements
   :class: note

   * **Central Lines:** :g:`{2, 3} <{ 2, 3 }>` (:term:`Euler line <euler line>`)
   * **Related Centers:** :g:`X_5 <X_5>` (:ref:`NINE-POINT CENTER <X_5>`), :g:`X_233 <X_233>` (:ref:`-CEVA CONJUGATE OF X(140) <X_233>`), :g:`X_2 <X_2>` (:ref:`CENTROID <X_2>`), :g:`X_3 <X_3>` (:ref:`CIRCUMCENTER <X_3>`)

.. signature:: center

   | **Trilinears:** :math:`a[\cos^{2}(B - C)][b \cos(C - A) + c \cos (A - B)] : :`
   | **Barycentrics:** :math:`a^{2}[\cos^{2}(B - C)][b \cos(C - A) + c \cos (A - B)] : :`
   | **Search Value (6, 9, 13):** :math:`2.017201680077`

.. collapse:: Incident Central Lines
   :badge: 1 line
   :class: line-catalog

   {:ref:`2 <X_2>`, :ref:`3 <X_3>`}

.. collapse:: Functional Relations
   :badge: 2 relations

   * :ref:`X_3078 <X_3078>` = :ref:`X_5 <X_5>`-:term:`Ceva conjugate <ceva-conjugate>` of :ref:`X_233 <X_233>`
   * :ref:`X_3078 <X_3078>` = :ref:`X_288 <X_288>`-:term:`isoconjugate <isoconjugate>` of :ref:`X_2167 <X_2167>`

Notes
-----

.. container:: note-item

   :math:`ax^{2}(by + cz)` : :math:`by^{2}(cz + ax)` : :math:`cz^{2}(ax + by)`.

.. container:: note-item

   We denote this point by D(X) and call it the Danneels point of :g:`X <X>`. (Eric Danneels, :cite:`Hyacinthos <hyacinthos>`, Jan. 28, 2005). In addition to the discussion below, see the preamble to X_8012 and the Danneels points beginning at X_8012.

.. container:: note-item

   If X lies on the line at infinity, then D(X) = :ref:`X_2 <X_2>` of cevian triangle of :g:`X <X>`. (:person:`Randy Hutson <randy-hutson>`, Jul 23, 2015)

.. container:: note-item

   The formula is simpler in barycentrics: if :g:`U <U>` =\ :math:`u : v : w`, then

      D(U) = :math:`u^{2}(v + w)` : :math:`v^{2}(w + u)` : :math:`w^{2}(u + v)`.

.. container:: note-item

   If X is line the Euler line, then D(X) is on the Euler line. A proof follows. Let :math:`a_{1}`, :math:`b_{1}`, :math:`c_{1}` be cos A, cos B, cos C, respectively, so that the Euler line is given parametrically as :math:`x(t) : y(t) : z` (t) by

   x = :math:`b_{1}`\ :math:`c_{1}` + :math:`ta_{1}`

   y = :math:`c_{1}`\ :math:`a_{1}` + :math:`tb_{1}`

   z = :math:`a_{1}`\ :math:`b_{1}` + :math:`tc_{1}`,

   where t is an arbitrary function homogenous of degree 0 in a, b, c. Then D(X) is the point :g:`U <U>` =\ :math:`u : v : w` given by

   u = :math:`ax^{2}(by + cz)`

   v = :math:`by^{2}(cz + ax)`

   w = :math:`cz^{2}(ax + by)`.

.. container:: note-item

   A point :g:`P <P>` =\ :math:`p : q : r` is on the Euler line if

   :math:`a(b^{2}` - :math:`c^{2})`\ (:math:`b^{2}` + :math:`c^{2}` - :math:`a^{2})`\ p

   + :math:`b(c^{2}` - :math:`a^{2})`\ (:math:`c^{2}` + :math:`a^{2}` - :math:`b^{2})`\ q

   + :math:`c(a^{2}` - :math:`b^{2})`\ (:math:`a^{2}` + :math:`b^{2}` -:math:`c^{2})`\ r = 0.

.. container:: note-item

   It is easy to check that the point U satisfies this equation. (This sort of algebraic proof is more inclusive than a geometric proof, because here, a,b,c are indeterminates or variables. They can, for example, take values that are not sidelengths of a triangle. Here, cos A is defined as (:math:`b^{2}` + :math:`c^{2}` - :math:`a^{2})`/(2bc), so that no dependence on a geometric angle is necessary.)

.. container:: note-item

   The appearance of (i,j) in the following list means that D(X_i) = X_j:

      * (1,42) (2,2) (3,418) (4,25) 6,3051 (7,57) (8,200) (69,394) (75,321) (100,55) (110,84) (264,324) (366,367) (651,222) (653,196) (1113,25) (1114,25) (1370,455) For an extension of this list, see the preamble to X_8012.

.. toctree::
   :hidden:

   code
