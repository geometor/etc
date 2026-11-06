:order: 2055
:type: collection
:canonical_id: X_2055–X_2119
:subtitle: Orion Transforms, Circumcircle Inverses, PK/NK Transforms, Reflections & Kepler Points

.. _c-02055-02119:

X_2055–X_2119
=============

.. rubric:: Orion Transforms, Circumcircle Inverses, PK/NK Transforms, Reflections & Kepler Points

.. enunciation::

   Orion transforms OT(X) (:ref:`X_2055 <X_2055>`\ –\ :ref:`X_2065 <X_2065>`), Caroli and Cursa points, circumcircle inverses (:ref:`X_2070 <X_2070>`\ –\ :ref:`X_2080 <X_2080>`), PK and NK transforms (:ref:`X_2081 <X_2081>`\ –\ :ref:`X_2092 <X_2092>`), classical reflections (:ref:`X_2093 <X_2093>`\ –\ :ref:`X_2105 <X_2105>`), and Kepler points and their :term:`isotomic conjugates <isotomic-conjugate>` (:ref:`X_2106 <X_2106>`\ –\ :ref:`X_2119 <X_2119>`).

.. figure:: c-02055-02119.svg
   :alt: X_2055–X_2119 — Orion Transforms, Circumcircle Inverses, PK/NK Transforms, Reflections & Kepler Points
   :align: center

   **X_2055–X_2119** (*Orion Transforms, Circumcircle Inverses, PK/NK Transforms, Reflections & Kepler Points*) — 16 representative centers (from 65 in collection) constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :g:`AB <[ A B ]>` = :math:`1`.

.. _preamble-0031:

.. admonition:: Group Preamble — Orion Transforms, 2055 -2065
   :class: note

   On September 24, 2003, Jean-Pierre Ehrmann suggested in :cite:`Hyacinthos <hyacinthos>` 7999 a transformation: suppose :g:`P <P>` =\ :math:`x : y : z` (trilinears); the Orion transform of :g:`P <P>` is given by OT(P) =\ :math:`f(a,b,c) : f(b,c,a) : f(c,a,b)`, where

   :math:`f(a,b,c) = x[- y^{2}z^{2} + x^{2}(y^{2} + z^{2} + 2yz \cos A)]`.

   Among pairs (i,j) for which OT(X_j) = X_i are these:

   (1,35), (2,69), (4,24), (7,57), (99,249), (100,59), (110,250)

   Ehrmann's construction of OT(P) is as the perspector of triangles :g:`ABC << A B C >>` and :g:`A″B″C″ << A″ B″ C″ >>`, where :g:`A″ <A″>` is the reflection of :g:`P <P>` in the sideline :g:`B'C' <[ B' C' ]>` of the :term:`cevian triangle <cevian-triangle>` :g:`A'B'C' << A' B' C' >>` of :g:`P <P>`, and :g:`B″ <B″>` and :g:`C' <C'>` are defined cyclically. Alternative and related constructions are given in other :cite:`Hyacinthos <hyacinthos>` messages prompted by #7999.

.. _preamble-0032:

.. admonition:: Group Preamble — Inverses in Circumcircle, 2070 -2080
   :class: note

   Suppose X is a point in the plane of triangle :g:`ABC << A B C >>`, other than the circumcenter O and not on the line at infinity. The inverse-in-circumcircle of :g:`X <X>` is the point :g:`X' <X'>` on ray OX whose distance from :g:`O <O>` is :math:`R^{2}`/\|OX\|\ :sup:`2`. In **normalized** trilinears, if

   :g:`X <X>` = (x, y, z) :g:`O <O>` = (:math:`x_{3}`, :math:`y_{3}`, :math:`z_{3})`, R = circumradius,

   then :g:`X' <X'>` is given as (f(a,b,c), f(b,c,a), f(c,a,b)) by :math:`f(a,b,c) = x_{3} + (x - x_{3})(R/`\ \|OX\|)\ :sup:`2`.

   In this section, representations using the circumradius R, inradius r, Brocard angle ω and J as defined at :ref:`X_1113 <X_1113>`, were contributed by Peter J. C . Moses.

.. _preamble-0033:

.. admonition:: Group Preamble — PK and NK Transforms, 2081 - 2088
   :class: note

   On October 1, 2003, :person:`Bernard Gibert <bernard-gibert>` described two transforms, given for :g:`X <X>` =\ :math:`u : v : w` (barycentrics) by

   PK(X) = :math:`a^{2}(c^{2}v^{2} - b^{2}w^{2})`\ u : :math:`b^{2}(a^{2}w^{2} - c^{2}u^{2})`\ v : :math:`c^{2}(b^{2}u^{2} - a^{2}v^{2})`\ w;

   NK(X) = :math:`a^{2}(c^{2}v^{2} + b^{2}w^{2})`\ u : :math:`b^{2}(a^{2}w^{2} + c^{2}u^{2})`\ v : :math:`c^{2}(b^{2}u^{2} + a^{2}v^{2})`\ w.

   Let :math:`X ^{-1}` denote the :term:`isogonal conjugate <isogonal-conjugate>` of X. Then PK(X) is the point of intersection of the :term:`trilinear polar <trilinear-polar>` of :g:`X <X>` and the trilinear polar of :math:`X ^{-1}`, and NK(P) is the pole of the line :math:`XX ^{-1}` with respect to the conic that passes through points :g:`A <A>`, :g:`B <B>`, :g:`C <C>`, :g:`X <X>`, and :math:`X ^{-1}`.

   Also, PK(X) is the :term:`crossdifference <crossdifference>`, and NK(X) the :term:`crosssum <crosssum>`, of :g:`X <X>` and :math:`X ^{-1}`.

   The transform PK carries any point on the cubic pK(X6,X) to the trilinear polar of :math:`X ^{-1}`, and NK carries any point on the cubic nK0(X6,X) to the trilinear polar of :math:`X ^{-1}`. (The notations for these cubics are given at Bernard Gibert's Cubics in the Triangle Plane.)

   | PK(X_i) = X_j for these (i,j):
   | (2,512), (3,647), (4,647), (6,512), (9,663), (19,810), (57,663), (63,810)

   | NK(X_i) = X_j for these (i,j):
   | (1,1), (2,30), (3,185), (4,185), (6,39), (98,446), (511,446)

   In trilinears: suppose :g:`X <X>` =\ :math:`x : y : z`; then

   PK(X) = (:math:`y^{2}` - :math:`z^{2})`\ x : (:math:`z^{2}` - :math:`x^{2})`\ y : (:math:`x^{2}` - :math:`y^{2})`\ z;

   NK(X) = (:math:`y^{2}` + :math:`z^{2})`\ x : (:math:`z^{2}` + :math:`x^{2})`\ y : (:math:`x^{2}` + :math:`y^{2})`\ z.

   The self-isogonal cubic pK(X6,X) is denoted as Z(X) in :cite:`TCCT <tcct>` (p. 240), and nK0(:g:`K_{6} <K_6>`,\ :g:`X <X>`), as :math:`Z^{+}(L)`. Extending examples on p. 240-241,

   | Z(:g:`X_{2} <X_2>`) passes through X_i for I = 1,2,3,4,6,9,57, 223, 282, 1073, 1249.
   | Z(:g:`X_{4} <X_4>`) passes through X_i for I = 1,3,4,46,90,155,254,371,372,485,486,487,488.
   | Z(:g:`X_{5} <X_5>`) passes through X_i for I = 1,3,4,5,17,18,54,61,62,195,627,628.
   | Z(:g:`X_{20} <X_20>`) passes through X_i for I = 1,3,4,20,40,64,84,1490,1498.
   | Z(:g:`X_{30} <X_30>`) passes through X_i for I = 1,3,4,13,14,15,16, 30, 74, 399, 484, 616,617,1138,1157,1263,1276,1277,1337,1338.
   | Z(:g:`X_{98} <X_98>`) passes through X_i for I = 1,98,511,1687,1688,1756,2009,2010.
   | Z(:g:`X_{99} <X_99>`) passes through X_i for I = 1,39,83,99,512,1018,1019,1379,1380.
   | Z(:g:`X_{100} <X_100>`) passes through X_i for I = 1,100,513,1381,1382.
   | Z(:g:`X_{110} <X_110>`) passes through X_i for I = 1,5,54,110,523,\ **1113,1114**.

   | Z\ :sup:`+`\ (:g:`X_{1}X_{6} <[ X_1 X_6 ]>`) passes through X_i for I = 1,44,88,239,241,292,294,1931.
   | Z\ :sup:`+`\ (:g:`X_{3}X_{6} <[ X_3 X_6 ]>`) passes through X_i for I = 2,6,13,14,15,16,111,524
   | Z\ :sup:`+`\ (:g:`X_{1}X_{2} <[ X_1 X_2 ]>`) passes through X_i for I = 1,238,291,899
   | Z\ :sup:`+`\ (:g:`X_{1}X_{3} <[ X_1 X_3 ]>`) passes through X_i for I = 1,105,243,296,518,1155,1156

   Additional pass-through points for these and other cubics are given at `Bernard Gibert's Cubics in the Triangle Plane <http://perso.wanadoo.fr/bernard.gibert/index.html>`__.

.. _preamble-0034:

.. admonition:: Group Preamble — Reflections, 2093 - 2105
   :class: note

   Suppose :g:`X <X>` =\ :math:`x : y : z` and :g:`U <U>` =\ :math:`u : v : w` (trilinears). Then the reflection of :g:`X <X>` in :g:`U <U>` is the point

   (au - bv - cw)x + 2u(by + cz) : (bv - cw - au)y + 2v(cz + ax) : (cw - au - bv)z + 2w(ax + by).

   Thus, if x = x(a,b,c), y = x(b,c,a), z = x(c,a,b) and u = u(a,b,c), v = u(b,c,a), w = u(c,a,b), then the reflection of :g:`X <X>` in :g:`U <U>` is given by :math:`f(a,b,c) : f(b,c,a) : f(c,a,b)`, where :math:`f(a,b,c) = (au - bv - cw)x + 2u(by + cz)`.

   In this section, several coordinate representations were contributed by Peter J. C . Moses.

.. _preamble-0035:

.. admonition:: Group Preamble — Centers 2106 -2119 (points on the 2nd equal-areas cubic, EAC2)
   :class: note

   are on the 2nd equal-areas cubic, EAC2. (For the definition, click Tables and then Bicentric Pairs.)

   For any point :g:`P <P>` on EAC2, the :ref:`X_2 <X_2>`-:term:`isoconjugate <isoconjugate>` of :g:`P <P>` is also on EAC2. In the following table, for each (i,j), the centers X_i and X_j are on EAC2 and are an :ref:`X_2 <X_2>`-isoconjugate pair. Each pair are collinear with the pivot :ref:`X_238 <X_238>`.

   I J 1 6 2 31 105 672 238 292 365 365 1423 2053 1931 2054 2106 2107 2108 2109 2110 2111 2112 2113 2114 2115 2116 2117 2118 2119 2144 2145 2146 2147 3009 20332

   :term:`Triangle centers <triangle-center>` on a cubic yield non-central points on the cubic; e.g., if P and :g:`P' <P'>` are on EAC2, then the line of :g:`PP' <[ P P' ]>` meets EAC2 in third point, L(P,\ :g:`P' <P'>`), on EAC2. (Possibly L(P,\ :g:`P' <P'>`) is P or :g:`P' <P'>`.) If :g:`A' <A'>`, :g:`B' <B'>`, :g:`C' <C'>` are :term:`central triangle <central-triangle>` vertices and X is a triangle center, and all four points :g:`A' <A'>`, :g:`B' <B'>`, :g:`C' <C'>`, and X lie on EAC2, then the points

   L(:g:`A' <A'>`,\ :g:`X <X>`), L(:g:`B' <B'>`,\ :g:`X <X>`), L(:g:`C' <C'>`,\ :g:`X <X>`)

   are central triangle vertices on EAC2. (A definition of central triangle is given in the Glossary.) In the following table, column 1 indicates the :g:`A <A>`-vertex of such a triangle; column 2 two points collinear with that vertex; and column 3, the :g:`A <A>`-vertex of the :ref:`X_2 <X_2>`-isoconjugate of the triangle. Taking row 1 as an example, **- a : c :** represents the point :math:`-a : c : b`, which is the :g:`A <A>`-vertex of the central triangle with :g:`B <B>`-vertex :math:`c : - b : a` and :g:`C <C>`-vertex :math:`b : a : - c`. The :g:`A <A>`-vertex is collinear with :g:`A <A>` and :ref:`X_2 <X_2>` (so that the :g:`B <B>`-vertex is collinear with :g:`B <B>` and :ref:`X_2 <X_2>`, etc.). Then, in column 3, - bc : :math:`a^{2}`\ b : represents the :g:`A <A>`-vertex of the :ref:`X_2 <X_2>`-isoconjugate of **- a : c :** . The vertices **- a : c :** and - bc : :math:`a^{2}`\ b : are collinear with the pivot, :ref:`X_238 <X_238>`.

   | :g:`A <A>`-vertex Line :g:`A <A>`-vertex (iso-) - a : c : A, :ref:`X_2 <X_2>` - bc : :math:`b^{2}` : - :math:`a^{1/2}` : :math:`b^{1/2}` : A, :ref:`X_365 <X_365>` - :math:`a^{1/2}` : :math:`b^{1/2}` : - a(a + b + c) : bc + ca + ab : A, :ref:`X_1 <X_1>` - 1/(a + b + c) : b/(bc + ca + ab) : bc + ab + ac : - (a + b + c)b : A, :ref:`X_6 <X_6>` a/(bc + ab + ac) : - 1/(a + b + c) : - bc : :math:`b^{2}` : A, :ref:`X_31 <X_31>` - a : c : a(a + b + c) : :math:`a^{2}` + :math:`b^{2}` - (a + b)c: :ref:`X_6 <X_6>`, - a : c : 1/(a + b + c) : b/[:math:`a^{2}` + :math:`b^{2}` - (a + b)c] : 2\ :math:`a(b^{2}` + ca)(:math:`c^{2}` + ab) :
   | (:math:`b^{2}` + ca)(:math:`a^{3}` + :math:`b^{3}` - :math:`c^{3}` - abc) : :ref:`X_31 <X_31>`, - a : c : 1/[2\ :math:`a(b^{2}` + ca)(:math:`c^{2}` + ab)] :
   | b/[(:math:`b^{2}` + ca)(:math:`a^{3}` + :math:`b^{3}` - :math:`c^{3}` - abc)] : (a+b)(a+c)(:math:`a^{2}`\ +\ :math:`b^{2}`\ +\ :math:`c^{2}`\ +bc+ca+ab) :
   | b(a+c)(:math:`a^{2}`\ +\ :math:`b^{2}`\ +ab-c(a+b+c)) : :ref:`X_1 <X_1>`, - a : c : a/[(a+b)(a+c)(:math:`a^{2}`\ +\ :math:`b^{2}`\ +\ :math:`c^{2}`\ +bc+ca+ab)] :
   | 1/[(a+c)(:math:`a^{2}`\ +\ :math:`b^{2}`\ +ab-c(a+b+c))] : a(bc + ab + ac) : (c - b)\ :math:`a^{2}` - :math:`b^{2}`\ a + :math:`b^{2}`\ c : :ref:`X_1 <X_1>`, - bc : :math:`b^{2}` : 1/[(bc + ab + ac) : b/[(c - b)\ :math:`a^{2}` - :math:`b^{2}`\ a + :math:`b^{2}`\ c] : :math:`2a^{2}`\ :math:`bc(b^{2}` + ca)(:math:`c^{2}` + ba) :
   | (:math:`b^{2}` + ca)(:math:`b^{3}`\ :math:`c^{3}` + :math:`a^{3}`\ :math:`c^{3}` - :math:`a^{3}`\ :math:`b^{3}` - :math:`a^{2}`\ :math:`b^{2}`\ :math:`c^{2})` : :ref:`X_2 <X_2>`, - bc : :math:`b^{2}` : 1/[2\ :math:`abc(b^{2}` + ca)(:math:`c^{2}` + ba)] :
   | b/[(:math:`b^{2}` + ca)(:math:`b^{3}`\ :math:`c^{3}` + :math:`a^{3}`\ :math:`c^{3}` - :math:`a^{3}`\ :math:`b^{3}` - :math:`a^{2}`\ :math:`b^{2}`\ :math:`c^{2})`] : (a+b)(a+c)[(:math:`b^{2}`\ +bc+\ :math:`c^{2})`\ :math:`a^{2}` + abc(b+c) + :math:`b^{2}`\ :math:`c^{2}`] :
   | b(a+c)[(:math:`c^{2}`-bc-:math:`b^{2})`\ :math:`a^{2}` + abc(c-b) + :math:`b^{2}`\ :math:`c^{2}`] : :ref:`X_6 <X_6>`, - bc : :math:`b^{2}` : 1/[(a+b)(a+c)[(:math:`b^{2}`\ +bc+\ :math:`c^{2})`\ :math:`a^{2}` + abc(b+c) + :math:`b^{2}`\ :math:`c^{2}`]] :
   | 1/[(a+c)[(:math:`c^{2}`-bc-:math:`b^{2})`\ :math:`a^{2}` + abc(c-b) + :math:`b^{2}`\ :math:`c^{2}`]] :

.. collection::
   :sort: order
