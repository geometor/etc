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

Member Centers
--------------

:ref:`Open Interactive 7-Triangle Constellation & Explorer ↗ <family-c-02055-02119>`

.. list-table::
   :class: etc-table etc-mode-relations
   :header-rows: 1
   :widths: 12 56 18 14

   * - Center
     - Name
     - Search (6,9,13)
     - Precision
   * - :ref:`X_2055 <X_2055>`
     - ORION TRANSFORM OF X\_3
     - ``-0.172128``
     - Exact
   * - :ref:`X_2056 <X_2056>`
     - ORION TRANSFORM OF X\_6
     - ``0.272844``
     - Exact
   * - :ref:`X_2057 <X_2057>`
     - ORION TRANSFORM OF X\_8
     - ``5.505360``
     - Exact
   * - :ref:`X_2058 <X_2058>`
     - ORION TRANSFORM OF X\_15
     - —
     - Catalog
   * - :ref:`X_2059 <X_2059>`
     - ORION TRANSFORM OF X\_16
     - —
     - Catalog
   * - :ref:`X_2060 <X_2060>`
     - ORION TRANSFORM OF X\_20
     - —
     - Catalog
   * - :ref:`X_2061 <X_2061>`
     - ORION TRANSFORM OF X\_40
     - —
     - Catalog
   * - :ref:`X_2062 <X_2062>`
     - ORION TRANSFORM OF X\_63
     - ``2.232092``
     - Exact
   * - :ref:`X_2063 <X_2063>`
     - ORION TRANSFORM OF X\_69
     - ``1.302512``
     - Exact
   * - :ref:`X_2064 <X_2064>`
     - ORION TRANSFORM OF X\_75
     - ``6.634077``
     - Exact
   * - :ref:`X_2065 <X_2065>`
     - ORION TRANSFORM OF X\_98
     - ``7.386450``
     - Exact
   * - :ref:`X_2066 <X_2066>`
     - POINT CAROLI I
     - ``2.045278``
     - Exact
   * - :ref:`X_2067 <X_2067>`
     - POINT CAROLI II
     - ``-6.463549``
     - Exact
   * - :ref:`X_2068 <X_2068>`
     - POINT CURSA I
     - ``1.513378``
     - 50-digit
   * - :ref:`X_2069 <X_2069>`
     - POINT CURSA II
     - ``-4.946728``
     - 50-digit
   * - :ref:`X_2070 <X_2070>`
     - INVERSE-IN-CIRCUMCIRCLE OF X\_5
     - ``0.225077``
     - Exact
   * - :ref:`X_2071 <X_2071>`
     - INVERSE-IN-CIRCUMCIRCLE OF X\_20
     - ``10.061006``
     - Exact
   * - :ref:`X_2072 <X_2072>`
     - INVERSE-IN-CIRCUMCIRCLE OF X\_26
     - ``2.192193``
     - Exact
   * - :ref:`X_2073 <X_2073>`
     - INVERSE-IN-CIRCUMCIRCLE OF X\_27
     - ``2.427130``
     - Exact
   * - :ref:`X_2074 <X_2074>`
     - INVERSE-IN-CIRCUMCIRCLE OF X\_28
     - ``1.443426``
     - Exact
   * - :ref:`X_2075 <X_2075>`
     - INVERSE-IN-CIRCUMCIRCLE OF X\_29
     - ``-20.375745``
     - Exact
   * - :ref:`X_2076 <X_2076>`
     - INVERSE-IN-CIRCUMCIRCLE OF X\_39
     - ``-2.785481``
     - Exact
   * - :ref:`X_2077 <X_2077>`
     - INVERSE-IN-CIRCUMCIRCLE OF X\_40
     - ``16.140013``
     - Exact
   * - :ref:`X_2078 <X_2078>`
     - INVERSE-IN-CIRCUMCIRCLE OF X\_57
     - ``-0.660678``
     - Exact
   * - :ref:`X_2079 <X_2079>`
     - INVERSE-IN-CIRCUMCIRCLE OF X\_115
     - ``-5.211781``
     - Exact
   * - :ref:`X_2080 <X_2080>`
     - INVERSE-IN-CIRCUMCIRCLE OF X\_182
     - ``-10.464130``
     - Exact
   * - :ref:`X_2081 <X_2081>`
     - PK-TRANSFORM OF X\_5
     - ``4.853034``
     - Exact
   * - :ref:`X_2082 <X_2082>`
     - NK-TRANSFORM OF X\_9
     - ``1.846971``
     - Exact
   * - :ref:`X_2083 <X_2083>`
     - NK-TRANSFORM OF X\_19
     - ``5.088304``
     - Exact
   * - :ref:`X_2084 <X_2084>`
     - PK-TRANSFORM OF X\_31
     - ``-10.538232``
     - Exact
   * - :ref:`X_2085 <X_2085>`
     - NK-TRANSFORM OF X\_31
     - ``1.283778``
     - Exact
   * - :ref:`X_2086 <X_2086>`
     - PK-TRANSFORM OF X\_99
     - ``-4.538534``
     - Exact
   * - :ref:`X_2087 <X_2087>`
     - PK-TRANSFORM OF X\_100
     - ``66.426159``
     - Exact
   * - :ref:`X_2088 <X_2088>`
     - PK-TRANSFORM OF X\_110
     - ``3.181584``
     - Exact
   * - :ref:`X_2089 <X_2089>`
     - 3rd MID-ARC POINT
     - ``0.522882``
     - 50-digit
   * - :ref:`X_2090 <X_2090>`
     - 1st STEVANOVIC PERSPECTOR
     - ``3.356487``
     - 50-digit
   * - :ref:`X_2091 <X_2091>`
     - 2nd STEVANOVIC PERSPECTOR
     - ``0.435726``
     - 50-digit
   * - :ref:`X_2092 <X_2092>`
     - DANNEELS-APOLLONIUS PERSPECTOR
     - ``1.427223``
     - Exact
   * - :ref:`X_2093 <X_2093>`
     - REFLECTION OF X\_1 IN X\_57
     - ``-0.929398``
     - Exact
   * - :ref:`X_2094 <X_2094>`
     - REFLECTION OF X\_2 IN X\_57
     - ``-1.868458``
     - Exact
   * - :ref:`X_2095 <X_2095>`
     - REFLECTION OF X\_3 IN X\_57
     - ``-6.021452``
     - Exact
   * - :ref:`X_2096 <X_2096>`
     - REFLECTION OF X\_4 IN X\_57
     - ``6.437530``
     - Exact
   * - :ref:`X_2097 <X_2097>`
     - REFLECTION OF X\_6 IN X\_57
     - ``-0.231998``
     - Exact
   * - :ref:`X_2098 <X_2098>`
     - REFLECTION OF X\_56 IN X\_1
     - ``3.193498``
     - Exact
   * - :ref:`X_2099 <X_2099>`
     - REFLECTION OF X\_55 IN X\_1
     - ``0.745148``
     - Exact
   * - :ref:`X_2100 <X_2100>`
     - REFLECTION OF X\_1 IN X\_1113
     - ``-0.908158``
     - 50-digit
   * - :ref:`X_2101 <X_2101>`
     - REFLECTION OF X\_1 IN X\_1114
     - ``24.656992``
     - 50-digit
   * - :ref:`X_2102 <X_2102>`
     - REFLECTION OF X\_1113 IN X\_1
     - ``2.989542``
     - 50-digit
   * - :ref:`X_2103 <X_2103>`
     - REFLECTION OF X\_1114 IN X\_1
     - ``-9.793033``
     - 50-digit
   * - :ref:`X_2104 <X_2104>`
     - REFLECTION OF X\_1113 IN X\_6
     - ``1.594742``
     - 50-digit
   * - :ref:`X_2105 <X_2105>`
     - REFLECTION OF X\_1114 IN X\_6
     - ``-11.187833``
     - 50-digit
   * - :ref:`X_2106 <X_2106>`
     - POINT KEPLER I
     - ``-3.198363``
     - Exact
   * - :ref:`X_2107 <X_2107>`
     - X\_2-ISOCONJUGATE OF X\_2106
     - ``-0.708443``
     - Exact
   * - :ref:`X_2108 <X_2108>`
     - POINT KEPLER I
     - ``5.319074``
     - Exact
   * - :ref:`X_2109 <X_2109>`
     - X\_2-ISOCONJUGATE OF X\_2108
     - ``1.991483``
     - Exact
   * - :ref:`X_2110 <X_2110>`
     - POINT KEPLER III
     - ``2.583869``
     - Exact
   * - :ref:`X_2111 <X_2111>`
     - X\_2-ISOCONJUGATE OF X\_2110
     - ``4.286092``
     - Exact
   * - :ref:`X_2112 <X_2112>`
     - POINT KEPLER IV
     - ``1.161253``
     - Exact
   * - :ref:`X_2113 <X_2113>`
     - X\_2-ISOCONJUGATE OF X\_2112
     - ``7.588781``
     - Exact
   * - :ref:`X_2114 <X_2114>`
     - POINT KEPLER V
     - ``0.079434``
     - Exact
   * - :ref:`X_2115 <X_2115>`
     - X\_2-ISOCONJUGATE OF X\_2114
     - ``10.436590``
     - Exact
   * - :ref:`X_2116 <X_2116>`
     - POINT KEPLER VI
     - ``0.391784``
     - Exact
   * - :ref:`X_2117 <X_2117>`
     - X\_2-ISOCONJUGATE OF X\_2116
     - ``10.682539``
     - Exact
   * - :ref:`X_2118 <X_2118>`
     - POINT KEPLER VII
     - ``-4.025763``
     - 50-digit
   * - :ref:`X_2119 <X_2119>`
     - X\_2-ISOCONJUGATE OF X\_2118
     - ``0.300281``
     - 50-digit
