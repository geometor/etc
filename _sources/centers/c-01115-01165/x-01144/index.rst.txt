:order: 1144
:canonical_id: X_1144
:subtitle: EHRMANN CONGRUENT SQUARES POINT
:dependencies: X_1, X_6

.. _X_1144:

X_1144
======

.. rubric:: EHRMANN CONGRUENT SQUARES POINT

.. enunciation::

   Suppose that P is a point inside triangle :g:`ABC << A B C >>`. Let :math:`S_{A}` be the square inscribed in triangle :g:`PBC << P B C >>`, having two vertices on segment :g:`BC <[ B C ]>`, one on :g:`PB <[ P B ]>`, and one on :g:`PC <[ P C ]>`. Define :math:`S_{B}` and :math:`S_{C}` cyclically. Then :ref:`X_1144 <X_1144>` is the unique choice of :g:`P <P>` for which the three squares are congruent. The function L(a,b,c) is symmetric, homogeneous of degree 1, and satisfies 0 < L(a,b,c) < min{a,b,c}. Also, :ref:`X_1144 <X_1144>` lies on the hyperbola {:g:`A <A>`, :g:`B <B>`, :g:`C <C>`,\ :ref:`X_1 <X_1>`,\ :ref:`X_6 <X_6>`}; indeed, :ref:`X_1144 <X_1144>` lies on the open arc from :ref:`X_1 <X_1>` to the vertex of :g:`ABC << A B C >>` opposite the shortest side. L(a,b,c) is the common length of the sides of the three squares. (Jean-Pierre Ehrmann, 12/16/01)

.. figure:: x-01144.svg
   :alt: X_1144 — EHRMANN CONGRUENT SQUARES POINT
   :align: center

   **X_1144** (*EHRMANN CONGRUENT SQUARES POINT*) constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :g:`AB <[ A B ]>` = :math:`1`.

.. signature:: center

   | **Trilinears:** :math:`a/(a - L) : b/(b - L) : c/(c - L)`, where :g:`L <L>` = L(a,b,c) is the smallest root of :math:`a^{2}`/(a - L) + :math:`b^{2}`/(b - L) + :math:`c^{2}`/(c - L) = 2D/L, and :math:`D = \operatorname{area}(ABC)`
   | **Barycentrics:** :math:`a^{2}/(a - L) : b^{2}/(b - L) : c^{2}/(c - L)`
   | **Search Value (6, 9, 13):** :math:`1.872006645063`

Notes
-----

.. container:: note-item

   See **Jean-Pierre Ehrmann,** `Congruent Inscribed Rectangles <http://forumgeom.fau.edu/FG2002volume2/FG200203.pdf>`__.

.. toctree::
   :hidden:

   code
