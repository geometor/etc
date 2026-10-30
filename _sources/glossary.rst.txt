:navigation: header
:order: 2
:layout: book
:book_title: Encyclopedia of Triangle Centers

.. _glossary:

Glossary
========

An extension of this Glossary, contributed by César Lozada, can be accessed here: `Extended Glossary <https://faculty.evansville.edu/ck6/encyclopedia/ext_glossary.html>`__.

Many of the terms used in triangle geometry are presented in Eric Weisstein's `MathWorld <https://mathworld.wolfram.com/>`__, including topics contributed by `Darij Grinberg <http://mathworld.wolfram.com/topics/Grinberg.html>`__, `Floor Lamoen <http://mathworld.wolfram.com/topics/vanLamoen.html>`__, and `Peter Moses <http://mathworld.wolfram.com/topics/Moses.html>`__.

A number of terms defined at MathWorld originated in this Glossary, using trilinear coordinates. The need for definitions using barycentric coordinates has led to P. L. Douillet's highly recommended `Translation of Kimberling's Glossary into barycentrics, "Le Glossaire de Pierre" <https://vixra.org/pdf/2504.0039v1.pdf>`__

In 2012, links to `Tables <https://faculty.evansville.edu/ck6/encyclopedia/Tables.html>`__ were added to ETC. These tables include many examples of conjugates of various kinds (e.g., aleph, beth, gimel, he, waw, zayin, complementary, and anticomplementary), introduced in C. Kimberling, `Collineations, Conjugacies, and Cubics <http://forumgeom.fau.edu/FG2002volume2/FG200204.pdf>`__, *Forum Geometricorum* 2 (2002) 21-32. Those definitions are included below.

In 2016, an Index of Triangles Referenced in ETC was provided by César Lozada. You can access it `here <https://faculty.evansville.edu/ck6/encyclopedia/IndexOfTrianglesReferencedInETC.html>`__, and also from `Tables <https://faculty.evansville.edu/ck6/encyclopedia/Tables.html>`__.

In this Glossary, points and lines are given in homogeneous coordinates. The coordinates are assumed to be trilinear unless otherwise indicated (as barycentric or polar coordinates), and they are used here to **define** points, lines, circles, triangle centers, etc. Likewise, zero determinants **define** collinearity and concurrence, etc. Consequently, triangle geometry is presented here at a much more general level than a single euclidean triangle. In this treatment, the symbols a,b,c are regarded as algebraic indeterminates or variables, so that points, as functions of a,b,c, are quite different from points in a two-dimensional plane. When (a,b,c) are real numbers restricted by the "triangle inequalities" for sidelengths (i.e., :math:`a \leq b + c`, :math:`b \leq c + a`, :math:`c \leq a + b`), the result is traditional triangle geometry. In favor of the greater generality, in this Glossary, algebraic definitions take precedence over traditional geometric construction-definitions. (For more in this vein, see the definitions of line, point, and symbolic substitution.)

The words "defined cyclically" apply after an "A-object" has been defined: if the A-object is F(:g:`A <A>`, :g:`B <B>`, :g:`C <C>`), then the B-object is F(:g:`B <B>`, :g:`C <C>`, :g:`A <A>`), obtained by the cyclic permutation :g:`ABC << A B C >>` → :g:`BCA << B C A >>`, and the C-object is, likewise, F(:g:`C <C>`, :g:`A <A>`, :g:`B <B>`). Example: If :g:`A' <A'>` is the point where lines :g:`AP <[ A P ]>` and :g:`BC <[ B C ]>` meet, and :g:`B' <B'>` and :g:`C' <C'>` are defined cyclically, then :g:`B' <B'>` is where lines :g:`BP <[ B P ]>` and :g:`CA <[ C A ]>` meet, and :g:`C' <C'>` is where lines :g:`CP <[ C P ]>` and :g:`AB <[ A B ]>` meet.

----

.. _aleph-conjugate:
.. _term-aleph-conjugate:

aleph conjugate
---------------

Let :g:`P <P>` =\ :math:`p : q : r` and :g:`U <U>` =\ :math:`u : v : w` be points, neither lying on a sideline of :g:`ABC << A B C >>`. The :g:`P <P>`-aleph conjugate of :g:`U <U>` is the point

   :math:`h(p,q,r,u,v,w) : h(q,r,p,v,w,u) : h(r,p,q,w,u,v)`,

where

   :math:`h(p,q,r,u,v,w) = - q^{2}r^{2}u^{2} + r^{2}p^{2}v^{2} + p^{2}q^{2}w^{2} + (vw + wu + uv)( - q^{2}r^{2} + r^{2}p^{2} + p^{2}q^{2})`.

Let g be the mapping given by

   :math:`g(x : y : z) = -x/p + y/q + z/r : x/p - y/q + z/r : x/p + y/q - z/r`.

The :g:`P <P>`-aleph conjugate of :g:`U <U>` is "what you do to g(X) to make :math:`g(X^{-1})` when :math:`f(X) = U`." (Hyacinthos #4111, Oct. 11, 2001.)

.. _anticevian-triangle:
.. _term-anticevian-triangle:

anticevian triangle
-------------------

Let :g:`P <P>` be a point not on a sideline of :g:`ABC << A B C >>`. Let :g:`A' <A'>` = :g:`AP <[ A P ]>`\ ∩\ :g:`BC <[ B C ]>`. Let :g:`A″ <A″>` be the harmonic conjugate of :g:`P <P>` with respect to :g:`A <A>` and :g:`A' <A'>`. Define :g:`B″ <B″>` and :g:`C″ <C″>` cyclically. Triangle :g:`A″B″C″ << A″ B″ C″ >>` is the anticevian triangle of triangle :g:`ABC << A B C >>`. (The lines :g:`AP <[ A P ]>`, :g:`BP <[ B P ]>`, :g:`CP <[ C P ]>` are the *cevians* of :g:`P <P>`, and :g:`A'B'C' << A' B' C' >>`, the *cevian triangle* of :g:`P <P>`.)

   If :g:`P <P>` =\ :math:`p : q : r`, then :g:`A″ <A″>` = :math:`- p : q : r`, :g:`B″ <B″>` =\ :math:`p : - q : r`, :g:`C″ <C″>` =\ :math:`p : q : - r`.

Examples of anticevian triangles

* excentral; :g:`P <P>` = incenter = :ref:`X(1) <X(1)>` =\ :math:`1 : 1 : 1`
* anticomplementary; :g:`P <P>` = centroid = :ref:`X(2) <X(2)>` =\ :math:`1/a : 1/b : 1/c`
* tangential; :g:`P <P>` = symmedian point = :ref:`X(6) <X(6)>` =\ :math:`a : b : c`

.. _anticomplement:
.. _term-anticomplement:

anticomplement
--------------

If points :g:`P <P>` and :g:`Q <Q>` are collinear with the centroid G, then P is the anticomplement of Q if G trisects segment :g:`PQ <[ P Q ]>` and is closer to Q than to P. See also :term:`complement <complement>`. (According to Court, p. 297, the term *anticomplementary point* dates from 1886.)

.. _anticomplementary-conjugate:
.. _term-anticomplementary-conjugate:

anticomplementary conjugate
---------------------------

Let :g:`P <P>` =\ :math:`p : q : r` and :g:`U <U>` =\ :math:`u : v : w` be points, neither lying on a sideline of :g:`ABC << A B C >>`. The P-anticomplementary conjugate of :g:`U <U>` is the point

   :math:`h(a,b,c,p,q,r,u,v,w) : h(b,c,a,q,r,p,v,w,u) : h(c,a,b,r,p,q,w,u,v)`,

where

   :math:`h(a,b,c,p,q,r,u,v,w) = [b^{2}/q(au + cw) + c^{2}/r(au + bv) - a^{2}/p(bv + cw)]/a`.

Let f(X) be the anticomplement of :g:`X <X>`, given by

   :math:`f(x : y : z) = (- ax + by + cz)/a : (ax - by + cz)/b : (ax + by - cz)/c`,

and let k be P-isoconjugation. The P-anticomplementary conjugate of :g:`U <U>` is "what you do to f(X) to make f(k(X)) when :math:`f(X) = U`."

If :g:`P <P>` = incenter, then P-anticomplementary conjugate is shortened to "anticomplementary conjugate."

.. _anticomplementary-triangle:
.. _term-anticomplementary-triangle:

anticomplementary triangle
--------------------------

Let L(A) be the line through vertex :g:`A <A>` parallel to side :g:`BC <[ B C ]>`, and define L(B) and L(C) cyclically. Let :g:`A' <A'>` = L(B)∩L(C), and define :g:`B' <B'>` and :g:`C' <C'>` cyclically. Then :g:`A'B'C' << A' B' C' >>` is the anticomplementary triangle of :g:`ABC << A B C >>`. (Efforts to replace this name have encountered the fact that :g:`A' <A'>` is the anticomplement of :g:`A <A>`.)

.. _antigonal-image:
.. _term-antigonal-image:

antigonal image
---------------

Let :g:`P <P>` =\ :math:`p : q : r` (barycentric coordinates) be a point not on a sideline of :g:`ABC << A B C >>` and not :ref:`X(4) <X(4)>`. The antigonal image of :g:`P <P>` is the point h(P) given by barycentyrics

   :math:`h(a,b,c,p,q,r) : h(b,c,a,q,r,p) : h(c,a,b,r,p,q)`,

where

   :math:`h(a,b,c,p,q,r) = p/[(b^{2} + c^{2} - a^{2})p^{2} - a^{2}qr + (b^{2} - a^{2})pq + (c^{2} - a^{2})pr]`.

The point h(P) is the isogonal conjugate of the inverse-in-circumcircle of the isogonal conjugate of P. If P lies on the circumcircle then h(P)=\ :ref:`X(4) <X(4)>`; otherwise, h(h(P))=P, so that h(P), in such a case, is called the antigonal conjugate of P. If P lies on the line at infinity, then :math:`h(P)=P`.

Antigonal pairs of points are discussed in Jan Van Yzeren, "Pairs of Points: Antigonal, Isogonal, and Inverse," *Mathematics Magazine* 65 (1992) 339-347.

Subsequent developments occur in Hyacinthos, beginning with #7825.

.. _antipedal-triangle:
.. _term-antipedal-triangle:

antipedal triangle
------------------

For a point :g:`P <P>`, the triangle :g:`A'B'C' << A' B' C' >>` formed by the lines through :g:`A <A>`, :g:`B <B>`, :g:`C <C>` perpendicular to :g:`AP <[ A P ]>`, :g:`BP <[ B P ]>`, :g:`CP <[ C P ]>` respectively. (See :term:`central triangle <central-triangle>`.)

.. _antitomic-conjugate:
.. _term-antitomic-conjugate:

antitomic conjugate
-------------------

Let :g:`P <P>` be a point not on a sideline of :g:`ABC << A B C >>`. Let :g:`T <T>` = isotomic conjugate and S = Steiner- circumellipse-inverse (this ellipse is T of the line at infinity). The antitomic conjugate of :g:`P <P>` is the point T(S(T(P))). Source: Preamble just before X(14941).

.. _barycentric-image:
.. _term-barycentric-image:

barycentric image
-----------------

See :term:`homologous images <homologous>`)

.. _beth-conjugate:
.. _term-beth-conjugate:

beth conjugate
--------------

Let :g:`P <P>` =\ :math:`p : q : r` and :g:`U <U>` =\ :math:`u : v : w` be points, neither lying on a sideline of :g:`ABC << A B C >>`. The :g:`P <P>`-beth conjugate of :g:`U <U>` is the point

   :math:`h(a,b,c,p,q,r,u,v,w) : h(b,c,a,q,r,p,v,w,u) : h(c,a,b,r,p,q,w,u,v)`,

where

   :math:`h(a,b,c,p,q,r,u,v,w) = 2abcp(\cos B + \cos C)(ua'/p + vb'/q + wc'/r) - (a+b+c)a'b'c'u`,

where a', b', c' are - a + b + c, a - b + c, a + b - c, respectively. Let f by the mapping given by

   :math:`f(x : y : z) = p(y + z) : q(z + x) : r(x + y)`,

| and let k be the mapping "reflection in the circumcenter." The :g:`P <P>`-beth conjugate of :g:`U <U>` is "what you do to f(X) to make
| f(k(X)) when :math:`f(X) = U`." (Hyacinthos #4146, Oct. 26, 2001.)

.. _bicentric-points:
.. _term-bicentric-points:

bicentric points
----------------

Let :math:`f(a,b,c) : f(b,c,a) : f(c,a,b)` be a point that satisfies (1) in the definition of triangle center, but that \|f(a,b,c)\| ≠ \|f(a,c,b)\|. Then

   :math:`f(a,c,b) : f(b,a,c) : f(c,b,a)` and :math:`f(a,b,c) : f(b,c,a) : f(c,a,b)`

are bicentric points, together comprising a *bicentric pair*. Example: the Brocard points,\ :math:`c/b : a/c : b/a` and :math:`b/c : c/a : a/b`.

.. _center:
.. _term-center:

center
------

See :term:`triangle center <triangle-center>`.

.. _central-triangle:
.. _term-central-triangle:

central triangle
----------------

Let each of f(a,b,c) and g(a,b,c) be a center function (i.e., as in the definition of triangle center) or the zero function, such that one of these conditions holds:

   | (1) the degree of homogeneity of g equals that of f;
   | (2) f is the zero function and g is not the zero function;
   | (3) g is the zero function and f is not the zero function.

Let

   | :g:`A' <A'>` =\ :math:`f(a,b,c) : g(b,c,a) : g(c,a,b)`
   | :g:`B' <B'>` =\ :math:`g(a,b,c) : f(b,c,a) : g(c,a,b)`
   | :g:`C' <C'>` =\ :math:`g(a,b,c) : g(b,c,a) : f(c,a,b)`.

Then :g:`A'B'C' << A' B' C' >>` is the *(f,g)-central triangle of type 1*. A *central triangle of type 1* is any triangle :g:`A'B'C' << A' B' C' >>` for which equations (1)-(3) hold for some choice of center functions f and g.

Next, suppose f and g are as for type 1 except that g(a,b,c) ≠ g(a,c,b). Let

   | :g:`A' <A'>` =\ :math:`f(a,b,c) : g(b,c,a) : g(c,b,a)`
   | :g:`B' <B'>` =\ :math:`g(a,c,b) : f(b,c,a) : g(c,a,b)`
   | :g:`C' <C'>` =\ :math:`g(a,b,c) : g(b,a,c) : f(c,a,b)`.

Then :g:`A'B'C' << A' B' C' >>` is the *(f,g)-central triangle of type 2*. A *central triangle of type 2* is any triangle :g:`A'B'C' << A' B' C' >>` for some choice of center function f and function g as described. Note that the coordinates in the definitions can be read as barycentrics without changing the classes of triangles called central, central of type 1, and central of type 2.

A form for compact notation for a central triangle is T(f(a,b,c), g(b,c,a)), where the triangle is of type 1 if :math:`g(b,c,a ) = g(b`,a,c) and of type 2 otherwise; see the preamble to X(3758) in ETC.

Examples: :g:`ABC << A B C >>`, the medial, orthic, excentral, anticomplementary, and tangential triangles are central of type 1; in fact, if X is a center, then the cevian and anticevian triangles of :g:`X <X>` are central of type 1. The pedal triangle of :g:`X <X>` is of type 2 if the triangle is not also a cevian triangle.

.. _ceva-conjugate:
.. _term-ceva-conjugate:

Ceva conjugate
--------------

Let :g:`P <P>` =\ :math:`p : q : r` and :g:`U <U>` =\ :math:`u : v : w` be points, neither lying on a sideline of :g:`ABC << A B C >>`. The P-Ceva conjugate of :g:`U <U>` is the point

   :math:`u(- qru + rpv + pqw) : v(qru - rpv + pqw) : w(qru + rpv - pqw)`,

which is the perspector of the cevian triangle of :g:`P <P>` and the anticevian triangle of :g:`U <U>`. (See :term:`cevian nest <cevian-nest>` and :term:`cross conjugate <cross-conjugate>`.)

Ceva conjugate and cevapoint are related thus: :g:`X <X>` = P©U if and only if :g:`P <P>` = cevapoint(U,X), and in this case, :g:`U <U>` = P©X.

Let f(:math:`x : y : z`) =\ :math:`p(y + z) : q(z + x) : r(x + y)`. The P-Ceva conjugate of :g:`U <U>` is "what you do to f(X) to make :math:`f(X^{-1})` when :math:`f(X) = U`." (Hyacinthos #3966, Sept. 26, 2001.)

.. _cevapoint:
.. _term-cevapoint:

cevapoint
---------

Let :g:`P <P>` =\ :math:`p : q : r` and :g:`U <U>` =\ :math:`u : v : w` be distinct points, neither lying on a sideline of :g:`ABC << A B C >>`. The cevapoint of :g:`P <P>` and U is the point

   :math:`(pv + qu)(pw + ru) : (qw + rv)(qu + pv) : (ru + pw)(rv + qw)`.

Let :g:`A″B″C″ << A″ B″ C″ >>` be the anticevian triangle of U. Let :g:`A' <A'>` =\ :g:`PA″ <[ P A″ ]>`\ ∩\ :g:`BC <[ B C ]>`, and define :g:`B' <B'>` and :g:`C' <C'>` cyclically. The cevapoint of :g:`P <P>` and U is the perspector, X, of triangles :g:`ABC << A B C >>` and :g:`A'B'C' << A' B' C' >>`. Moreover, P is the X-Ceva conjugate of :g:`U <U>`, and U is the X-Ceva conjugate of :g:`P <P>`. (See :term:`cevian nest <cevian-nest>` and :term:`Ceva conjugate <ceva-conjugate>`.) As a comparison of cevapoint(P,U) and crosspoint(P,U), note that their trilinears can be written as

   :math:`1/(qw + rv) : 1/(ru + pw) : 1/(pv + qu)` and :math:`1/qw + 1/rv : 1/ru + 1/pw : 1/pv + 1/qu`.

Floor Van Lamoen contributed the following two constructions of cevapoint(P,U). Let :g:`A_{p}B_{p}C_{p} << A_p B_p C_p >>` be the cevian triangle of :g:`P <P>`, and let :g:`A_{u}B_{u}C_{u} << A_u B_u C_u >>` be the cevian triangle of U. Define

   | :g:`A_{pu} <A_pu>` = :g:`C_{p}A_{u} <[ C_p A_u ]>`\ ∩\ :g:`A_{p}B_{u} <[ A_p B_u ]>`   —   :g:`A_{up} <A_up>` = :g:`C_{u}A_{p} <[ C_u A_p ]>`\ ∩\ :g:`A_{u}B_{p} <[ A_u B_p ]>`
   | :g:`B_{pu} <B_pu>` = :g:`A_{p}B_{u} <[ A_p B_u ]>`\ ∩\ :g:`B_{p}C_{u} <[ B_p C_u ]>`   —   :g:`B_{up} <B_up>` = :g:`A_{u}B_{p} <[ A_u B_p ]>`\ ∩\ :g:`B_{u}C_{p} <[ B_u C_p ]>`
   | :g:`C_{pu} <C_pu>` = :g:`B_{p}C_{u} <[ B_p C_u ]>`\ ∩\ :g:`C_{p}A_{u} <[ C_p A_u ]>`   —   :g:`C_{up} <C_up>` = :g:`B_{u}C_{p} <[ B_u C_p ]>`\ ∩\ :g:`C_{u}A_{p} <[ C_u A_p ]>`

Then triangle :g:`ABC << A B C >>` is perspective to both triangles :g:`A_{pu}B_{pu}C_{pu} << A_pu B_pu C_pu >>` and :g:`A_{up}B_{up}C_{up} << A_up B_up C_up >>`, and the perspector in both cases is the cevapoint of :g:`P <P>` and U. (Received 10/17/2003)

| Randy Hutson noted that cevapoint(P,U) is given by the following constructions:
| \* The intersection of tangents at :g:`P <P>` and U to the bianticevian conic of :g:`P <P>` and U;
| \* The crosspoint of :g:`P <P>` and U wrt both the anticevian triangle of :g:`P <P>` and anticevian triangle of :g:`U <U>`;
| \* The pole of line :g:`PU <[ P U ]>` wrt the bianticevian conic of :g:`P <P>` and U. (Received 7/14/2019)

.. _cevian:
.. _term-cevian:

cevian
------

Let :g:`P <P>` be a point not on a sideline of :g:`ABC << A B C >>`. The lines :g:`AP <[ A P ]>`, :g:`BP <[ B P ]>`, :g:`CP <[ C P ]>` are the *cevians* of :g:`P <P>`.

.. _cevian-nest:
.. _term-cevian-nest:

cevian nest
-----------

Let :g:`D <D>`, :g:`E <E>`, :g:`F <F>` be triangles, where F is inscribed in :g:`E <E>`, and E is inscribed in D. If any two of the three triangles are perspective, then the ordered triple (:g:`D <D>`, :g:`E <E>`, :g:`F <F>`) is a cevian nest. (It is well known that if any two of the three triangles are perspective, then each is perspective to the third; in particular, E is a cevian triangle of :g:`D <D>`, and F is a cevian triangle of :g:`E <E>`.)

Cevian nests in which one of the triangles is :g:`ABC << A B C >>` beget three families of conjugates: *Ceva conjugates,* *cross conjugates,* and *isoconjugates*. See also :term:`crosspoint <crosspoint>`.

.. _cevian-triangle:
.. _term-cevian-triangle:

cevian triangle
---------------

Let :g:`P <P>` be a point not on a sideline of :g:`ABC << A B C >>`. Let :g:`A' <A'>` = :g:`AP <[ A P ]>`\ ∩\ :g:`BC <[ B C ]>` meet. Define :g:`B' <B'>` and :g:`C' <C'>` cyclically. Triangle :g:`A'B'C' << A' B' C' >>` is the cevian triangle of triangle :g:`ABC << A B C >>`.

   If :g:`P <P>` =\ :math:`p : q : r`, then :g:`A' <A'>` =\ :math:`0 : q : r`, :g:`B' <B'>` =\ :math:`p : 0 : r`, :g:`C' <C'>` =\ :math:`p : q : 0`.

Examples of cevian triangles:

   | incentral triangle; :g:`P <P>` = incenter = :ref:`X(1) <X(1)>` =\ :math:`1 : 1 : 1`
   | medial triangle; :g:`P <P>` = centroid = :ref:`X(2) <X(2)>` =\ :math:`1/a : 1/b : 1/c`
   | orthic triangle; :g:`P <P>` = orthocenter = :ref:`X(4) <X(4)>` = sec A : sec B : sec C
   | intouch triangle; :g:`P <P>` = Gergonne point = :ref:`X(7) <X(7)>` = :math:`\sec^{2}(A/2)` : :math:`\sec^{2}(B/2)` : :math:`\sec^{2}(C/2)`
   | extouch triangle; :g:`P <P>` = Nagel point = :ref:`X(8) <X(8)>` = :math:`\csc^{2}(A/2)` : :math:`\csc^{2}(B/2)` : :math:`\csc^{2}(C/2)`

.. _circumperp-conjugate:
.. _term-circumperp-conjugate:

circumperp conjugate
--------------------

Let :g:`P <P>` =\ :math:`p : q : r` be a point distinct from :ref:`X(3) <X(3)>`. The circumperp conjugate of :g:`P <P>` is the point

   :math:`f(p,q,r,a,b,c,S_{A},S_{B},S_{C}) : f(q,r,p,b,c,a,S_{B},S_{C},S_{A}) : f(r,p,q,c,a,b,S_{C},S_{A},S_{B})`,

where

   :math:`f(p,q,r,a,b,c,S_{A},S_{B},S_{C}) = (-a (-b c S_{C} S_{B} p^{2}+2 r q S_{A}^{3})-S_{A} a b c (b^{2} q^{2}+c^{2} r^{2})+b ((S_{A}+S_{B}) S^{2}-2 S_{A} S_{B}^{2}) r p+c ((S_{C}+S_{A}) S^{2}-2 S_{A} S_{C}^{2}) p q) a`.

Let :g:`ABC << A B C >>` be a triangle and P a point. The perpendicular bisectors of :g:`BC <[ B C ]>`, :g:`CA <[ C A ]>`, :g:`AB <[ A B ]>` intersect the circumcircle at (:g:`A_{1} <A_1>`, :g:`A_{2} <A_2>`), (:g:`B_{1} <B_1>`, :g:`B_{2} <B_2>`), (:g:`C_{1} <C_1>`, :g:`C_{2} <C_2>`), respectively. Then the circumcircles of :g:`PA_{1}A_{2} << P A_1 A_2 >>`, :g:`PB_{1}B_{2} << P B_1 B_2 >>`, :g:`PC_{1}C_{2} << P C_1 C_2 >>` are coaxial. The other than P point of intersection of these circles is the circumperp conjugate of :g:`P <P>`, as :g:`A_{1} <A_1>`, :g:`A_{2} <A_2>`, :g:`B_{1} <B_1>`, :g:`B_{2} <B_2>`, :g:`C_{1} <C_1>`, :g:`C_{2} <C_2>` are the vertices of the circumperp triangles. (See preamble just before X(18859))

.. _cocevian-triangle:
.. _term-cocevian-triangle:

cocevian triangle
-----------------

Let :g:`P <P>` be a point not on a sideline of :g:`ABC << A B C >>`, and let :g:`A'B'C' << A' B' C' >>` be the anticevian triangle of P. Let :g:`A″ <A″>` be the harmonic conjugate of :g:`A' <A'>` with respect to :g:`B <B>` and :g:`C <C>`, and define :g:`B″ <B″>` and :g:`C″ <C″>` cyclically. (If :g:`P <P>` =\ :math:`p : q : r`, then :g:`A″ <A″>` =\ :math:`0 : y : - z`.). The cocevian triangle of :g:`P <P>` is the triangle :g:`A″B″C″ << A″ B″ C″ >>`. The vertices are collinear and the triangle degenerate. For a discussion, see TCCT, page 200.

.. _combo:
.. _term-combo:

combo
-----

Let :g:`P <P>` and U be finite points having normalized barycentric coordinates (p,q,r) and (u,v,w). Suppose that f = f(a,b,c) and g = g(a,b,c) are nonzero homogeneous functions having the same degree of homogeneity. Let x = fp + gu, y = fq + gv, z = fr + gw. The (f,g) combo of :g:`P <P>` and U, denoted by f\*P + g\*U, is the point :g:`X <X>` =\ :math:`x : y : z`; the normalized barycentric coordinates of :g:`X <X>` are (kx,ky,kz), where k=1/(x+y+z).

The definition of combo readily extends to finite sets of finite points. In particular, the (f,g,h) combo of :g:`P <P>` = (p,q,r), :g:`U <U>` = (u,v,w), J = (j,k,m) is given by fp + gu + hj : fq + gv + hk : fr + gw + hm and denoted by f\*P + g\*U + h\*J. Suppose that T is a (central) triangle with vertices :g:`A' <A'>`,\ :g:`B' <B'>`,\ :g:`C' <C'>` given by normalize barycentrics. Then T is represented by a 3x3 matrix with row sums equal to 1. Let NT denote the set of these matrices and let \* denote matrix multiplication. Then NT is closed under \*. Also, NT is closed under matrix inversion, so that (NT, \*) is a group. Once normalized, any central T can be used to produce triangle centers as combos of the form Xcom(nT); see the preambles to X(3663), X(3739), and X(3758) in ETC.

.. _complement:
.. _term-complement:

complement
----------

If points :g:`P <P>` and U are collinear with the centroid G, then P is the complement of U if G trisects segment :g:`PU <[ P U ]>` and is closer to P than to U. See also :term:`anticomplement <anticomplement>`. (According to Court, p. 297, the term *complementary point* dates from 1885.)

.. _complementary-conjugate:
.. _term-complementary-conjugate:

complementary conjugate
-----------------------

Let :g:`P <P>` =\ :math:`p : q : r` and :g:`U <U>` =\ :math:`u : v : w` be points, neither lying on a sideline of :g:`ABC << A B C >>`. The P-complementary conjugate of :g:`U <U>` is the point

   :math:`h(a,b,c,p,q,r,u,v,w) : h(b,c,a,q,r,p,v,w,u) : h(c,a,b,r,p,q,w,u,v)`,

where

   :math:`h(a,b,c,p,q,r,u,v,w) = [b^{2}/q(au - bv + cw) + c^{2}/r(au + bv - cw)]/a`.

Let f(X) be the complement of :g:`X <X>`, given by

   :math:`f(x : y : z) = (bv + cw)/a : (cw + au)/b : (au + bv)/c`,

and let k be P-isoconjugation. The P-complementary conjugate of :g:`U <U>` is "what you do to f(X) to make f(k(X)) when :math:`f(X) = U`."

If :g:`P <P>` = incenter, then P-complementary conjugate is shortened to "complementary conjugate."

.. _cross-conjugate:
.. _term-cross-conjugate:

cross conjugate
---------------

Let :g:`P <P>` =\ :math:`p : q : r` and :g:`U <U>` =\ :math:`u : v : w` be distinct points, neither lying on a sideline of :g:`ABC << A B C >>`. The P-cross conjugate of :g:`U <U>` is the point

   :math:`u/(- pvw + qwu + ruv) : v/(pvw - qwu + ruv) : w/(pvw + qwu - ruv)`.

Let :g:`A'B'C' << A' B' C' >>` be the cevian triangle of U. Let :g:`A″ <A″>` be where line :g:`PA' <[ P A' ]>` crosses line :g:`B'C' <[ B' C' ]>`, and define :g:`B″ <B″>` and :g:`C″ <C″>` cyclically - so that :g:`A″B″C″ << A″ B″ C″ >>` is the cevian triangle (in triangle :g:`A'B'C' << A' B' C' >>`, not :g:`ABC << A B C >>`) of P. The perspector of triangles :g:`ABC << A B C >>` and :g:`A″B″C″ << A″ B″ C″ >>` is the P-cross conjugate of :g:`U <U>`. (See :term:`cevian nest. <cevian-nest>`)

As a transformation, P-cross conjugate is an involution; i.e., if PxU = P-cross conjugate of :g:`U <U>`, then Px(PxU) = U. Properties of cross conjugates arise from those of Ceva conjugates; for, on writing :g:`P_{c}U <[ P_c U ]>` for the P-Ceva conjugate of :g:`U <U>`,

   :math:`PxU = (U/P) \cdot (UcP)` and :math:`PcU = (U/P)*` (UxP)

   where / and \* denote trilinear division and multiplication.

Cross conjugate and crosspoint are related thus: :g:`X <X>` = PxU if and only if :g:`P <P>` = crosspoint(X,U).

.. _crossdifference:
.. _term-crossdifference:

crossdifference
---------------

Let :g:`P <P>` =\ :math:`p : q : r` and :g:`U <U>` =\ :math:`u : v : w` be distinct points, neither lying on a sideline of :g:`ABC << A B C >>`. The crossdifference of :g:`P <P>` and U is the point X defined by trilinears

   :math:`qw - rv : ru - pw : pv - qu`,

constructible as the isogonal conjugate of the trilinear pole of the line :g:`PU <[ P U ]>`. Thus, U is the crossdifference of :g:`P <P>` and X, and P is the crossdifference of :g:`U <U>` and X. In order to see that the crossdifference of :g:`P <P>` and X is a solution for :g:`U <U>` of the equation

:math:`x : y : z` = qw - rv : ru - pw : pv - qu,

| note first that this equation implies px + qy + rz = 0. Thus, if :math:`u : v : w` = qz - ry : rx - pz : py - qx, then
| qw - rv = q(py - qx) - r(rx - pz) = - (:math:`p^{2}` + :math:`q^{2}` + :math:`r^{2})`\ x, so that
| qw - rv : ru - pw : pv - qu =\ :math:`x : y : z`.

A point :g:`X <X>` is the crossdifference of distinct points :g:`P <P>` and U if and only if the line :g:`PU <[ P U ]>` is the trilinear polar of the isogonal conjugate of X. Examples:

| :ref:`X(1) <X(1)>` = crossdifference of :ref:`X(44) <X(44)>` and :ref:`X(513) <X(513)>`
| :ref:`X(2) <X(2)>` = crossdifference of :ref:`X(187) <X(187)>` and :ref:`X(512) <X(512)>`
| :ref:`X(3) <X(3)>` = crossdifference of :ref:`X(230) <X(230)>` and :ref:`X(231) <X(231)>`.

Let W be the side-triangle of these two triangles: the cevian triangle of the isogonal conjugate of :g:`P <P>` and the cevian triangle of the isogonal conjugate of U. Then W is perspective to :g:`ABC << A B C >>`, and the perspector is the crossdifference of :g:`P <P>` and U; see also :term:`crosspoint <crosspoint>`. (Randy Hutson, April 9, 2016)

.. _crosspoint:
.. _term-crosspoint:

crosspoint
----------

Let :g:`P <P>` =\ :math:`p : q : r` and :g:`U <U>` =\ :math:`u : v : w` be distinct points, neither lying on a sideline of :g:`ABC << A B C >>`. The crosspoint of :g:`P <P>` and U is the point

   :math:`pu(rv + qw) : qv(pw + ru) : rw(qu + pv)`.

This point is introduced in `TCCT <http://faculty.evansville.edu/ck6/tcenters/tcct.html>`__ with the notation C(P,Q). Here, ":g:`Q″ <Q″>` is replaced by ":g:`U″ <U″>`, and C(P,U) is abbreviated as X. The construction for X given in TCCT follows. Let :g:`A'B'C' << A' B' C' >>` be the cevian triangle of :g:`P <P>` and :g:`A″B″C″ << A″ B″ C″ >>` that of U. Let A''' = :g:`AA″ <[ A A″ ]>`\ ∩\ :g:`B'C' <[ B' C' ]>`, and define B''' and C''' cyclically. Then X is the perspector of triangles :g:`A'B'C' << A' B' C' >>` and A'''B'''C'''. Moreover, U is the X-cross conjugate of :g:`P <P>`, and P is the X-cross conjugate of :g:`U <U>`. (See :term:`cevian nest <cevian-nest>` and :term:`cross conjugate <cross-conjugate>`.) The following properties of X were noted by Jean-Pierre Ehrmann (5/29/03):

:g:`X <X>` = perspector of :g:`A'B'C' << A' B' C' >>` and the triangle with vertices :g:`AU <[ A U ]>`\ ∩\ :g:`B'C' <[ B' C' ]>`, :g:`BU <[ B U ]>`\ ∩\ :g:`C'A' <[ C' A' ]>`, :g:`CU <[ C U ]>`\ ∩\ :g:`A'B' <[ A' B' ]>`;

:g:`X <X>` = perspector of :g:`A″B″C″ << A″ B″ C″ >>` and the triangle with vertices :g:`AP <[ A P ]>`\ ∩\ :g:`B″C″ <[ B″ C″ ]>`, :g:`BP <[ B P ]>`\ ∩\ :g:`C″A″ <[ C″ A″ ]>`, :g:`CP <[ C P ]>`\ ∩\ :g:`A″B″ <[ A″ B″ ]>`;

| :g:`X <X>` = the point of concurrence of these three lines:
| the line of points :g:`AP <[ A P ]>`\ ∩\ :g:`BU <[ B U ]>` and :g:`AU <[ A U ]>`\ ∩\ :g:`BP <[ B P ]>`
| the line of points :g:`BP <[ B P ]>`\ ∩\ :g:`CU <[ C U ]>` and :g:`BU <[ B U ]>`\ ∩\ :g:`CP <[ C P ]>`
| the line of points :g:`CP <[ C P ]>`\ ∩\ :g:`AU <[ A U ]>` and :g:`CU <[ C U ]>`\ ∩\ :g:`AP <[ A P ]>`

Figure 7.3 in TCCT with ":g:`Q″ <Q″>` replaced by ":g:`U″ <U″>` can be used to visualize the nine lines concurring in :g:`X <X>`.

The lines tangent to the conic {:g:`A <A>`, :g:`B <B>`, :g:`C <C>`,P,U} at :g:`P <P>` and U intersect in :g:`X <X>`. (Randy Hutson, September 10, 2012)

Let W be the side-triangle of these two triangles: the cevian triangle of :g:`P <P>` and the cevian triangle of U. Let :g:`W' <W'>` be the vertex-triangle of the anticevian triangle of :g:`P <P>` and the anticevian triangle of U. Then W is perspective to :g:`W' <W'>`, and the perspector is the crosspoint of :g:`P <P>` and U; see also :term:`crossdifference <crossdifference>`. (Randy Hutson, April 9, 2016)

.. _crosssum:
.. _term-crosssum:

crosssum
--------

Let :g:`P <P>` =\ :math:`p : q : r` and :g:`U <U>` =\ :math:`u : v : w` be distinct points, neither lying on a sideline of :g:`ABC << A B C >>`. The crosssum of :g:`P <P>` and U is the point X defined by trilinears

   :math:`qw + rv : ru + pw : pv + qu`,

constructible as the crosspoint of the isogonal conjugates of :g:`P <P>` and U. Thus, U is the isogonal conjugate of the X-cross conjugate of the isogonal conjugate of :g:`P <P>`, and P is the isogonal conjugate of the X-cross conjugate of the isogonal conjugate of :g:`U <U>`. (Regarding the neologism "crosssum" placed here on 5/28/03, what words in the English language have spellings containing three consecutive identical letters?)

.. _cubic:
.. _term-cubic:

cubic
-----

A cubic is a curve of degree 3 in a,b,c. For a catalog with sketches, visit `Bernard Gibert's site <http://perso.wanadoo.fr/bernard.gibert/index.html>`__.

.. _cyclocevian-conjugate:
.. _term-cyclocevian-conjugate:

cyclocevian conjugate
---------------------

Let :g:`P <P>` =\ :math:`p : q : r` be a point not on a sideline of :g:`ABC << A B C >>`, and let :g:`A'B'C' << A' B' C' >>` be the cevian triangle of P. The circumcircle of :g:`A'B'C' << A' B' C' >>` meets line :g:`BC <[ B C ]>` in two points: :g:`A' <A'>` and :g:`A″ <A″>`; pairs :g:`B' <B'>`, :g:`B″ <B″>`, and :g:`C' <C'>`,\ :g:`C″ <C″>` are obtained cyclically. The lines :g:`AA″ <[ A A″ ]>`, :g:`BB″ <[ B B″ ]>`, :g:`CC″ <[ C C″ ]>` concur in the cyclocevian conjugate of P. Let

   :math:`g(a,b,c) = a/[p(qb + r_{c})]` and :math:`f(a,b,c) = bc/[g(b,c,a) + g(c,a,b) - g(a,b,c)]`.

The cyclocevian conjugate of :g:`P <P>` is given by

   :math:`f(a,b,c) : f(b,c,a) : f(c,a,b)`.

In Hyacinthos #6423 (January 24, 2003), Darij Grinberg states nine theorems, of which the last is as follows:

| The cyclocevian conjugate of a point is the
| isotomic conjugate
| of the anticomplement
| of the isogonal conjugate
| of the complement
| of the isotomic conjugate
| of the point.

.. _daleth-conjugate:
.. _term-daleth-conjugate:

daleth conjugate
----------------

Let :g:`P <P>` =\ :math:`p : q : r` and :g:`U <U>` =\ :math:`u : v : w` be points, neither lying on a sideline of :g:`ABC << A B C >>`. The P-daleth conjugate of :g:`U <U>` is the point

   :math:`h(p,q,r,u,v,w) : h(q,r,p,v,w,u) : h(r,p,q,w,u,v)`,

where

   :math:`h(p,q,r,u,v,w) = p(y/q - z/r)^{2} + x(2x/p - y/q - z/r)`.

.. _dual-triangle:
.. _term-dual-triangle:

dual triangle
-------------

Let :g:`DEF << D E F >>` be a triangle in the plane of triangle :g:`ABC << A B C >>`. Let :g:`D' <D'>` be the isogonal conjugate of the point of intersection of line :g:`EF <[ E F ]>` and the line at infinity. Define :g:`E' <E'>` and :g:`F' <F'>` cyclically. The triangle :g:`D'E'F' << D' E' F' >>` is the *dual* of :g:`DEF << D E F >>`. The vertices of :g:`D'E'F' << D' E' F' >>` lie on the circumcircle, and :g:`D'E'F' << D' E' F' >>` is similar to :g:`DEF << D E F >>`. The duality is between the sidelines :g:`EF <[ E F ]>`, :g:`FD <[ F D ]>`, :g:`DE <[ D E ]>` and the points :g:`D' <D'>`, :g:`E' <E'>`, :g:`F' <F'>`, respectively. For example, if :g:`E <E>` and :g:`F <F>` remain fixed and D varies, then :g:`D' <D'>` remains fixed, while :g:`E'F' <[ E' F' ]>` varies. (From the preamble to X(2979) in ETC.)

.. _eigencenter:
.. _term-eigencenter:

eigencenter
-----------

Let :g:`T <T>` be a central triangle, and let U(T) be the unary cofactor triangle of T. Then T and U(T) are perspective, and their perspector is the eigencenter of :g:`T <T>`.

Suppose the A-, B-, C- vertices of :g:`T <T>` are :g:`P_{i} <P_i>` =\ :math:`x_{i} : y_{i} : z_{i}`, for i = 1,2,3. Let

   :math:`s = y_{3}(x_{1}x_{2} + z_{1}z_{2}) - y_{1}(x_{2}x_{3} + z_{2}z_{3})`

   :math:`t = z_{1}(x_{2}x_{3} + y_{2}y_{3}) - z_{2}(x_{1}x_{3} + y_{1}y_{3})`

   :math:`u = z_{3}(x_{1}x_{2} + y_{1}y_{2}) - z_{1}(x_{2}x_{3} + y_{2}y_{3})`

   :math:`v = y_{1}(x_{2}x_{3} + z_{2}z_{3}) - y_{2}(x_{1}x_{3} + z_{1}z_{3})`

Let x = st - uv, and define y and z cyclically. Then the eigencenter of :g:`T <T>` is the point :math:`x : y : z`.

.. _excentral-triangle:
.. _term-excentral-triangle:

excentral triangle
------------------

The anticevian triangle of the incenter :ref:`X(1) <X(1)>` =\ :math:`1 : 1 : 1`, whose vertices are the three excenters of :g:`ABC << A B C >>`. (See :term:`anticevian triangle <anticevian-triangle>`.)

.. _extouch-triangle:
.. _term-extouch-triangle:

extouch triangle
----------------

The cevian triangle of the Nagel point :ref:`X(8) <X(8)>`, whose vertices are the points of tangency of the A-, B-, :g:`C <C>`-excircles with sides :g:`BC <[ B C ]>`, :g:`CA <[ C A ]>`, :g:`AB <[ A B ]>`. (See :term:`cevian triangle <cevian-triangle>`.)

.. _functional-image:
.. _term-functional-image:

functional image
----------------

see :term:`homologous images <homologous>`

.. _gimel-conjugate:
.. _term-gimel-conjugate:

gimel conjugate
---------------

Let :g:`P <P>` =\ :math:`p : q : r` and :g:`U <U>` =\ :math:`u : v : w` be points, neither lying on a sideline of :g:`ABC << A B C >>`. The :g:`P <P>`-gimel conjugate of :g:`U <U>` is the point

   :math:`h(a,b,c,p,q,r,u,v,w) : h(b,c,a,q,r,p,v,w,u) : h(c,a,b,r,p,q,w,u,v)`,

where

   :math:`h(a,b,c,p,q,r,u,v,w) = abc[- (\cos A)/p + (\cos B)/q + (\cos C)/r]S - 8u\sigma ^{2}`,

where S = (bq + cr)u + (cr + ap)v + (ap + bq)w and σ = area of :g:`ABC << A B C >>`.

.. _he-conjugate:
.. _term-he-conjugate:

he conjugate
------------

Let :g:`P <P>` =\ :math:`p : q : r` and :g:`U <U>` =\ :math:`u : v : w` be points, neither lying on a sideline of :g:`ABC << A B C >>`. The :g:`P <P>`-he conjugate of :g:`U <U>` is the point

   :math:`h(p,q,r,u,v,w) : h(q,r,p,v,w,u) : h(r,p,q,w,u,v)`,

where

   :math:`h(p,q,r,u,v,w) = -p(y + z)^{2} + q(z + x)^{2} + r(x + y)^{2} + (qr/p)(x + y)(x + z) - (rp/q)(y + z)(y + x) - (pq/r)(z + x)(z + y)`.

.. _hirst-inverse:
.. _term-hirst-inverse:

Hirst inverse
-------------

Let :g:`P <P>` =\ :math:`p : q : r` and :g:`U <U>` =\ :math:`u : v : w` be distinct points, neither lying on a sideline of :g:`ABC << A B C >>`. The :g:`P <P>`-Hirst inverse of :g:`U <U>` is the point

   :math:`qru^{2} - vwp^{2} : rpv^{2} - wuq^{2} : pqw^{2} - uvr^{2}`.

Geometrically, this is the point of intersection of the line :g:`PU <[ P U ]>` and the polar of :g:`U <U>` with respect to the conic.

   :math:`pyz + qzx + rxy = 0`.

As a transformation, :g:`P <P>`-Hirst inverse is an involution; i.e., if PhU = :g:`P <P>`-Hirst inverse of :g:`U <U>`, then Ph(PhU) = U. Concerning the designation "Hirst inverse," see the `information <http://mathforum.org/kb/message.jspa?messageID=1178474&tstart=0>`__ contributed by Gunter Weiss.

.. _homologous:
.. _term-homologous:

homologous images: similarity image, trilinear image, barycentric image, and functional image
---------------------------------------------------------------------------------------------

The term *homologous* means *having the same relation or relative position to*. Let :g:`T_{1} <T_1>` and :g:`T_{2} <T_2>` be two triangles, and P a point in the plane of triangle :g:`T_{1} <T_1>`. The point :g:`P' <P'>` in the plane of triangle :g:`T_{2} <T_2>` is a :g:`T_{1} <T_1>`-to-:g:`T_{2} <T_2>` homologous image of P if :g:`P' <P'>` has the same relation or relative position to :g:`T_{2} <T_2>` as P has to :g:`T_{1} <T_1>`. However, the words "relation or relative position" are subject to different meanings, as discussed here.

If :g:`T_{1} <T_1>` and :g:`T_{2} <T_2>` are similar triangles, then :g:`P' <P'>` is the :g:`T_{1} <T_1>`-to-:g:`T_{2} <T_2>` similarity image of :g:`P <P>`.

Suppose that P has trilinears :math:`x : y : z` wrt :g:`T_{1} <T_1>`. Then the :g:`T_{1} <T_1>`-to-:g:`T_{2} <T_2>` trilinear image of :g:`P <P>` is the point :g:`P' <P'>` with trilinears :math:`x : y : z` wrt :g:`T_{2} <T_2>`. This is a non-affine collineation, preserving collinearities, but not ratios of distances between collinear points. Parallel lines do not remain parallel under this mapping, so that points on the line at infinity map to finite points. Circumconics of :g:`T_{1} <T_1>` map to circumconics of :g:`T_{2} <T_2>` and inconics of :g:`T_{1} <T_1>` map to inconics of :g:`T_{2} <T_2>`.

Suppose that P has barycentrics :math:`x : y : z` wrt :g:`T_{1} <T_1>`. Then the :g:`T_{1} <T_1>`-to-:g:`T_{2} <T_2>` barycentric image of :g:`P <P>` is the point :g:`P' <P'>` with barycentrics :math:`x : y : z` wrt :g:`T_{2} <T_2>`. This is an affine collineation, preserving collinearities as well as ratios of distances between collinear points. Parallel lines remain parallel under this mapping, so that the line at infinity maps to itself. Conics map to conics of the same type (ellipses, including circles, map to ellipses, parabolas to parabolas, hyperbolas to hyperbolas). Circumconics of :g:`T_{1} <T_1>` map to circumconics of :g:`T_{2} <T_2>` and inconics of :g:`T_{1} <T_1>` map to inconics of :g:`T_{2} <T_2>`.

Let the sidelengths of :g:`T_{1} <T_1>` be denoted :math:`a_{1}`, :math:`b_{1}`, :math:`c_{1}` and the sidelengths of :g:`T_{2} <T_2>` be denoted :math:`a_{2}`, :math:`b_{2}`, :math:`c_{2}`. Suppose that P has coordinates :math:`f(a_{1},b_{1},c_{1}) : g(b_{1},c_{1},a_{1}) : h(c_{1},a_{1},b_{1})` with respect to :g:`T_{1} <T_1>`, where f, g, h either have the same degree of homogeneity, or else one is the zero function and the other two have the same degree of homogeneity. (If P is a center of :g:`T_{1} <T_1>`, then f = g = h.) Then the :g:`T_{1} <T_1>`-to-:g:`T_{2} <T_2>`-functional image of :g:`P <P>` is the point :g:`P' <P'>` with coordinates :math:`f(a_{2},b_{2},c_{2}) : g(b_{2},c_{2},a_{2}) : h(c_{2},a_{2},b_{2})` with respect to :g:`T_{2} <T_2>`. Coordinates here can be trilinears or barycentrics, as long as the same system is used for :g:`T_{1} <T_1>` and :g:`T_{2} <T_2>`. :g:`P' <P'>` serves the same 'function' wrt :g:`T_{2} <T_2>` (e.g., centroid, circumcenter, 1st Brocard point, :g:`A <A>`-vertex of orthic triangle, etc.) as P serves wrt :g:`T_{1} <T_1>`. For example, the orthic-to-excentral functional image of :ref:`X(5) <X(5)>` is :ref:`X(40) <X(40)>`, since :ref:`X(5) <X(5)>` and :ref:`X(40) <X(40)>` are the respective circumcenters of the orthic and excentral triangles. This is a non-affine collineation, preserving collinearities, but not ratios of distances between collinear points (except where these distance ratios define the point, such as midpoints, reflections, etc.). Parallel lines remain parallel under this mapping, so that the line at infinity maps to itself. Circles map to circles. Other conics map to conics, but not necessarily of the same type (e.g., the MacBeath circumconic of :g:`T_{1} <T_1>` may be an ellipse, but maps to the MacBeath circumconic of :g:`T_{2} <T_2>`, which may be a hyperbola.) Circumconics of :g:`T_{1} <T_1>` map to circumconics of :g:`T_{2} <T_2>` and inconics of :g:`T_{1} <T_1>` map to inconics of :g:`T_{2} <T_2>`.

.. _incentral-triangle:
.. _term-incentral-triangle:

incentral triangle
------------------

The cevian triangle of the incenter :ref:`X(1) <X(1)>` =\ :math:`1 : 1 : 1`, whose vertices are the points where the interior angle bisectors of :g:`ABC << A B C >>` meet the opposite sidelines. (See :term:`cevian triangle <cevian-triangle>`.)

.. _intouch-triangle:
.. _term-intouch-triangle:

intouch triangle
----------------

The cevian triangle of the Gergonne point :ref:`X(7) <X(7)>` (also the pedal triangle of the incenter :ref:`X(1) <X(1)>`), whose vertices are the points of tangency of the incircle with the sides of :g:`ABC << A B C >>`. (See :term:`cevian triangle <cevian-triangle>`.)

.. _isoconjugate:
.. _term-isoconjugate:

isoconjugate
------------

Let :g:`P <P>` =\ :math:`p : q : r` and :g:`U <U>` =\ :math:`u : v : w` be points, neither on a sideline of :g:`ABC << A B C >>`. The P-isoconjugate of :g:`U <U>` is the point

   :math:`qrvw : rpwu : pquv`.

Examples: the *isogonal conjugate* of :g:`U <U>` is the :ref:`X(1) <X(1)>`-isoconjugate of :g:`U <U>`, and the *isotomic conjugate* of :g:`U <U>` is the :ref:`X(31) <X(31)>`-isoconjugate of :g:`U <U>`.

As suggested by the meaning of the prefix "iso",

P-isoconjugate of :g:`U <U>` = U-isoconjugate of :g:`P <P>`.

Let :g:`A'B'C' << A' B' C' >>` be the anticevian triangle of :g:`U <U>`, and let :g:`A″B″C″ << A″ B″ C″ >>` be the anticevian triangle of P *with respect to A'B'C'*. The perspector of :g:`A'B'C' << A' B' C' >>` and :g:`A″B″C″ << A″ B″ C″ >>` is the :math:`U^{-2}`-isoconjugate of :g:`P <P>`, where :math:`U^{-2}` =\ :math:`u^{-2} : v^{-2}: w^{-2}`. (See :term:`cevian nest <cevian-nest>`.)

The earliest appearance of the term "isoconjugate" in triangle geometry may be its inclusion in this Glossary as early as 1998. Isoconjugates are also discussed in C. Kimberling, "Conjugacies in the plane of a triangle," *Aequationes Mathematicae* 63 (2002) 158-167, submitted April 27, 1999, and "Conics associated with a cevian nest," *Forum Geometricorum* 1 (2001) 141-150.

Thereafter the term "isoconjugate" was sometimes used for *reciprocal conjugate*, a term defined in this Glossary, with a reference to probable earliest usage.

.. _isogonal-conjugate:
.. _term-isogonal-conjugate:

isogonal conjugate
------------------

Let :g:`P <P>` =\ :math:`p : q : r` be a point not on a sideline of :g:`ABC << A B C >>`. Let L(A) be the line obtained by reflecting line :g:`AP <[ A P ]>` in the internal bisector of angle A. Define L(B) and L(B) cyclically. The lines L(A), L(B), L(C) concur in the isogonal conjugate of :g:`P <P>`, which has trilinears :math:`1/p : 1/q : 1/r` and is denoted by :math:`P^{-1}`. See :term:`isoconjugate <isoconjugate>`.

.. _isoscelizer:
.. _term-isoscelizer:

isoscelizer
-----------

An isoscelizer is a line perpendicular to an angle bisector. If P is a point, then the A-isoscelizer of :g:`P <P>` is the line L(P,A) through :g:`P <P>` perpendicular to the line that bisects vertex angle :g:`A <A>`; the B- and C- isoscelizers are defined cyclically. Let :g:`D <D>` and E be the points where L(P,A) meets sidelines :g:`AB <[ A B ]>` and :g:`AC <[ A C ]>`. Unless :g:`D <D>` = :g:`E <E>` = A, the triangle :g:`ADE << A D E >>` is isosceles.

In ETC, there are several triangle centers defined in terms of isoscelizers. These were discovered or invented by Peter Yff, in whose notebooks the word *isoscelizer* dates back to 1963.

.. _isotomic-conjugate:
.. _term-isotomic-conjugate:

isotomic conjugate
------------------

Let :g:`P <P>` =\ :math:`p : q : r` be a point not on a sideline of :g:`ABC << A B C >>`. Let :g:`A' <A'>`, :g:`B' <B'>`, :g:`C' <C'>` be the points where lines :g:`AP <[ A P ]>`, :g:`BP <[ B P ]>`, :g:`CP <[ C P ]>` meet lines :g:`BC <[ B C ]>`, :g:`CA <[ C A ]>`, :g:`AB <[ A B ]>`, respectively. Reflect :g:`A' <A'>`, :g:`B' <B'>`, :g:`C' <C'>` about the midpoints of sides :g:`BC <[ B C ]>`, :g:`CA <[ C A ]>`, :g:`AB <[ A B ]>`, respectively, to obtain points :g:`A″ <A″>`, :g:`B″ <B″>`, :g:`C″ <C″>`. Then lines :g:`AA″ <[ A A″ ]>`, :g:`BB″ <[ B B″ ]>`, :g:`CC″ <[ C C″ ]>` concur in the isotomic conjugate of :g:`P <P>`, which has trilinears 1/(:math:`pa^{2})` : 1/(:math:`qb^{2})` : 1/(:math:`r_{c}^{2})`. See :term:`isoconjugate <isoconjugate>`.

.. _line:
.. _term-line:

line
----

A line is the set of points :math:`x : y : z` satisfying the equation

   :math:`f(a,b,c)x + g(a,b,c)y + h(a,b,c)z = 0`

for some point :math:`f(a,b,c) : g(a,b,c) : h(a,b,c)`. If this point is a triangle center, then the corresponding line is a *central line.*

| Three lines dx + ey + fz = 0, rx + sy + tz = 0, ux + vy + wz = 0 are concurrent if and only the following determinant equation holds:
| See also :term:`point <point>`. Chapter 5 of `TCCT <http://faculty.evansville.edu/ck6/tcenters/tcct.html>`__ discusses central lines.

.. _line-conjugate:
.. _term-line-conjugate:

line conjugate
--------------

Let :g:`P <P>` =\ :math:`p : q : r` and :g:`U <U>` =\ :math:`u : v : w` be distinct points, neither equal to :g:`A <A>`, :g:`B <B>`, or :g:`C <C>`. The :g:`P <P>`-line conjugate of :g:`U <U>` is the point

   :math:`p(v^{2} + w^{2}) - u(qv + rw) : q(w^{2} + u^{2}) - v(rw + pu) : r(u^{2} + v^{2}) - w(pu + qv)`,

or, equivalently,

   :math:`hp - ku : hq - kv : hr - kw`,

where h = :math:`u^{2}` + :math:`v^{2}` + :math:`w^{2}` and k = pu + qv + rw.

This is the point of intersection of line :g:`PU <[ P U ]>` and the trilinear polar of the isogonal conjugate of :g:`U <U>`.

.. _line-polar-triangle:
.. _term-line-polar-triangle:

line-polar triangle
-------------------

Let :g:`P_{i} <P_i>` =\ :math:`x_{i} : y_{i} : z_{i}`, for i=1,2,3, be noncollinear points. An equation for line :g:`P_{2}P_{3} <[ P_2 P_3 ]>` is then

   :math:`a_{1}x + b_{1}y + c_{1}z = 0`,

where :math:`a_{1}` = :math:`y_{2}`\ :math:`z_{3}` - :math:`z_{2}`\ :math:`y_{3}`, and :math:`b_{1}` and :math:`c_{1}` are defined cyclically. The trilinear pole of this line is the point

   :math:`1/a_{1} : 1/b_{1} : 1/c_{1}`.

This point is the :g:`A <A>`-vertex of the line-polar triangle. The B- and C- vertices are defined cyclically.

.. _major-center:
.. _term-major-center:

major center
------------

A major center is a triangle center X for which there exists a function f(A) such that :g:`X <X>` =\ :math:`f(A) : f(B) : f(C)`. Examples: :ref:`X(1) <X(1)>`, :ref:`X(2) <X(2)>`, :ref:`X(3) <X(3)>`, :ref:`X(4) <X(4)>`, :ref:`X(6) <X(6)>`. Major centers solve certain problems in functional equations; click `here (AeqMath) <http://www.link.springer.de/link/service/journals/00010/bibs/8055003/80550251.htm>`__ or `here (AMM) <http://www.maa.org/pubs/monthly_may97_toc.html>`__ for more.

.. _medial-triangle:
.. _term-medial-triangle:

medial triangle
---------------

The cevian triangle of the centroid :ref:`X(2) <X(2)>` =\ :math:`1/a : 1/b : 1/c`, whose vertices are the midpoints of sides :g:`BC <[ B C ]>`, :g:`CA <[ C A ]>`, :g:`AB <[ A B ]>`. (See :term:`cevian triangle <cevian-triangle>`.)

.. _orthic-triangle:
.. _term-orthic-triangle:

orthic triangle
---------------

The cevian (and pedal) triangle of the orthocenter :ref:`X(4) <X(4)>` = sec A : sec B : sec C, whose vertices are the feet of the altitudes of :g:`ABC << A B C >>`. (See :term:`cevian triangle <cevian-triangle>`.)

.. _orthojoin:
.. _term-orthojoin:

orthojoin
---------

Let :g:`X <X>` =\ :math:`x : y : z` be a point, and let

| :math:`a_{1}` = (:math:`b^{2}` + :math:`c^{2}` - :math:`a^{2})`/(2bc) = cos A,
| :math:`b_{1}` = (:math:`c^{2}` + :math:`a^{2}` - :math:`b^{2})`/(2ca) = cos B,
| :math:`c_{1}` = (:math:`a^{2}` + :math:`b^{2}` - :math:`c^{2})`/(2ab) = cos C,

| :math:`u_{1}` = :math:`b_{1}`\ :math:`c_{1}`\ :math:`x^{3}` - :math:`b_{1}`\ :math:`y^{3}` - :math:`c_{1}`\ :math:`z^{3}`,
| :math:`u_{2}` = - (1 + :math:`2c_{1}^{2})`\ :math:`b_{1}`\ :math:`x^{2}`\ y - (1 + :math:`2b_{1}^{2})`\ :math:`c_{1}`\ :math:`x^{2}`\ z,
| :math:`u_{3}` = (:math:`2a_{1}`\ :math:`b_{1}` - :math:`c_{1})`\ :math:`y^{2}`\ z + (:math:`2a_{1}`\ :math:`c_{1}` - :math:`b_{1})`\ :math:`yz^{2}`,
| :math:`u_{4}` = :math:`3b_{1}`\ :math:`c_{1}`\ :math:`xy^{2}` + :math:`3b_{1}`\ :math:`c_{1}`\ :math:`xz^{2}`,
| :math:`u_{5}` = (1 + :math:`b_{1}^{2}` + :math:`c_{1}^{2}` - :math:`a_{1}^{2}` - :math:`4a_{1}`\ :math:`b_{1}`\ :math:`c_{1})`\ xyz,

:math:`f(a,b,c) = (- x + yc_{1} + zb_{1})(u_{1} + u_{2} + u_{3} + u_{4} + u_{5})`.

The orthojoin of :g:`X <X>` is the point :math:`f(a,b,c) : f(b,c,a) : f(c,a,b)`.

| The above formula for f(a,b,c) can be written out explicitly in terms of a,b,c and simplified to the form
| :math:`g(a,b,c) : g(b,c,a) : g(c,a,b)`, where

:math:`g(a,b,c) = bc[2abcx + c_{3}y + b_{3}z - (a_{2} + bc)(cy + bz)]F`,

where :math:`F = x[a_{4} - (b_{2} - c_{2})_{2}] + 2a[by(b_{2} - a_{2} - c_{2}) + cz(c_{2} - b_{2} - a_{2})]`

The orthojoin of :g:`X <X>`, defined (6/16/03) as above, can be described geometrically (when a,b,c are sidelengths of a triangle) as the orthopole of the trilinear polar of the isogonal conjugate of X. The orthopole of a line :g:`L <L>` is constructed as follows. Let :g:`A' <A'>` be the foot of the perpendicular from vertex :g:`A <A>` on :g:`L <L>`, and define :g:`B' <B'>` and :g:`C' <C'>` cyclically. Then the perpendiculars from :g:`A' <A'>` to :g:`BC <[ B C ]>`, from :g:`B' <B'>` to :g:`CA <[ C A ]>`, and from :g:`C' <C'>` to :g:`AB <[ A B ]>` concur in the orthopole of L. For a proof and link to further information, see `Orthopole - a new proof by Darij Grinberg <http://mathforum.org/epigone/geom.college/cexprylox>`__.

.. _orthopoint:
.. _term-orthopoint:

orthopoint
----------

Each point :g:`X <X>` on the line at infinity is the point common to every line in a family F(X) of pairwise parallel lines. That is, X may be regarded as the direction common to the lines in F(X). Let :g:`L <L>` be any line in F(X), and let :g:`L' <L'>` be any line perpendicular to L. Let G be the family of lines parallel to :g:`L' <L'>`. The orthopoint of :g:`X <X>` is the point H(X) in which :g:`L' <L'>` meets the line at infinity. If :g:`X <X>` =\ :math:`x : y : z`, then

   :math:`H(X) = cy \cos B - bz \cos C : az \cos C - cx \cos A : bx \cos A - ay \cos B`.

For any X on the line at infinity, the isogonal conjugates of :g:`X <X>` and H(X) are circumcircle-antipodes; i.e., each is the :ref:`X(3) <X(3)>`-reflection of the other.

.. _pedal-triangle:
.. _term-pedal-triangle:

pedal triangle
--------------

For a point :g:`P <P>`, the triangle :g:`A'B'C' << A' B' C' >>` whose vertices are the orthogonal projections (feet of perpendiculars) of P onto the sidelines :g:`BC <[ B C ]>`, :g:`CA <[ C A ]>`, :g:`AB <[ A B ]>`. (See :term:`central triangle <central-triangle>`.)

.. _perspective:
.. _term-perspective:

perspective
-----------

Triangles :g:`DEF << D E F >>` and :g:`UVW << U V W >>` are perspective triangles if one of the following six triples of lines concur in a point:

   {:g:`DU <[ D U ]>`,\ :g:`EV <[ E V ]>`,\ :g:`FW <[ F W ]>`}, {:g:`DV <[ D V ]>`,\ :g:`EW <[ E W ]>`,\ :g:`FU <[ F U ]>`}, {:g:`DW <[ D W ]>`,\ :g:`EU <[ E U ]>`,\ :g:`FV <[ F V ]>`}; {:g:`DU <[ D U ]>`,\ :g:`EW <[ E W ]>`,\ :g:`FV <[ F V ]>`}, {:g:`DV <[ D V ]>`,\ :g:`EU <[ E U ]>`,\ :g:`FW <[ F W ]>`}, {:g:`DW <[ D W ]>`,\ :g:`EV <[ E V ]>`,\ :g:`FU <[ F U ]>`}

The point of concurrence is called a *perspector* (replacing *center of perspective*). If, for example, lines :g:`DU <[ D U ]>`,\ :g:`EV <[ E V ]>`,\ :g:`FW <[ F W ]>` concur in a point, then by Desargues's theorem, the points

   :g:`EF <[ E F ]>` intersect :g:`VW <[ V W ]>`, :g:`FD <[ F D ]>` intersect :g:`WU <[ W U ]>`, :g:`DE <[ D E ]>` intersect :g:`UV <[ U V ]>`

are collinear, and their line is the *perspectrix* (replacing *axis of perspective*.)

In case :g:`DEF << D E F >>` is the reference triangle, :g:`ABC << A B C >>`, and :g:`UVW << U V W >>` is a central triangle, it is sometimes tacitly understood that perspectivity of the two triangles refers to only one of the six possibilities, namely, the concurrence of lines :g:`DU <[ D U ]>`,\ :g:`EV <[ E V ]>`,\ :g:`FW <[ F W ]>`. In this case, if :g:`UVW << U V W >>` is the cevian triangle, :g:`A'B'C' << A' B' C' >>`, of a point :g:`P <P>`, then P is the perspector of :g:`ABC << A B C >>` and :g:`A'B'C' << A' B' C' >>`, and the perspectrix is the trilinear polar of :g:`P <P>`.

.. _point:
.. _term-point:

point
-----

In traditional euclidean geometry, *point* is not subject to definition, much as an axiom is not subject to proof. However, when (a,b,c) is variable or indeterminate, a point is defined informally by :math:`f(a,b,c) : g(a,b,c) : h(a,b,c)` for all (a,b,c) for which at least one of the values f(a,b,c), g(a,b,c), h(a,b,c) is not zero. A formal definition is given in `TCCT. <http://faculty.evansville.edu/ck6/tcenters/tcct.html>`__ See also :term:`triangle center <triangle-center>`.

Three points :math:`x : y : z`,\ :math:`r : s : t`,\ :math:`u : v : w` are collinear if and only the following determinant equation holds:

Thus, if :math:`x : y : z` is a variable point, this equation gives the line determined by the points :math:`r : s : t` and :math:`u : v : w`.

.. _point-polar-triangle:
.. _term-point-polar-triangle:

point-polar triangle
--------------------

Let :g:`P_{i} <P_i>` =\ :math:`x_{i} : y_{i} : z_{i}`, for i = 1,2,3, be noncollinear points, none lying on a sideline of :g:`ABC << A B C >>`. The trilinear polar of :g:`P_{1} <P_1>` is the line

   :math:`x/x_{1} + y/y_{1} + z/z_{1} = 0`,

and the trilinear polars of :g:`P_{2} <P_2>` and :g:`P_{3} <P_3>` are defined cyclically. These last two lines meet in the point

   :math:`1/y_{2}z_{3} - 1/z_{2}y_{3} : 1/z_{2}x_{3} - 1/x_{2}z_{3} : 1/x_{2}y_{3} - 1/y_{2}x_{3}`.

This point is the :g:`A <A>`-vertex of the point-polar triangle. The B- and C- vertices are defined cyclically.

.. _polar:
.. _term-polar:

polar
-----

Let W be a conic, P a point, and :g:`XX' <[ X X' ]>` and :g:`YY' <[ Y Y' ]>` chords of W that meet in P. As X and Y vary, the locus of the point :g:`X'Y <[ X' Y ]>`\ ∩\ :g:`XY' <[ X Y' ]>` is a line, called the polar of :g:`P <P>` with respect to W. If W is a circumconic, it has an equation uyz + vzx + wxy = 0, and the polar of a point :g:`Q <Q>` =\ :math:`p : q : r` is the line

   :math:`(vr + wq)x + (wp + ur)y + (uq + vp)z = 0`.

.. _polynomial-center:
.. _term-polynomial-center:

polynomial center
-----------------

A triangle center X is a polynomial center if there exists a polynomial f(a,b,c) such that

   :math:`X = f(a,b,c) : f(b,c,a) : f(c,a,b)`.

Examples: :ref:`X(1) <X(1)>`, :ref:`X(2) <X(2)>`, . . . , :ref:`X(12) <X(12)>`, but not :ref:`X(13) <X(13)>`.

.. _radical-trace:
.. _term-radical-trace:

radical trace
-------------

The radical trace of two nonconcentric circles is the point of intersection of the radical axis of the circles and the line of the centers of the circles. (For examples, see X(I) for I = 6, 187, 1570, 2021-2025, 2030-2032.)

.. _reciprocal-conjugate:
.. _term-reciprocal-conjugate:

reciprocal conjugate
--------------------

Let :g:`P <P>` and U be points, neither on a sideline of :g:`ABC << A B C >>`, given in barycentric coordinates by :g:`P <P>` =\ :math:`p : q : r` and :g:`U <U>` =\ :math:`u : v : w`. The P-reciprocal conjugate of :g:`U <U>` is the point

   :math:`pvw : qwu : ruv`. (barycentrics)

As suggested by the meaning of "reciprocal",

   P-reciprocal conjugate of :g:`U <U>` = G/(U-reciprocal conjugate of :g:`P <P>`),

in accord with the fact that G, the centroid, is the identity corresponding to barycentric division.

The term *reciprocal conjugate* was introduced in Keith Dean and Floor van Lamoen, "Geometric construction of reciprocal conjugations," *Forum Geometricorum* 1 (2001) 115-120.

See also :term:`isoconjugate. <isoconjugate>`

.. _similarity-image:
.. _term-similarity-image:

similarity image
----------------

see :term:`homologous images <homologous>`

.. _symbolic-substitution:
.. _term-symbolic-substitution:

symbolic substitution
---------------------

Let p(a, b, c), q(a, b, c), r(a, b, c) be functions of a, b, c, all of the same degree of homogeneity. As the plane consists of points [functions of the form :g:`X <X>` =\ :math:`x(a, b, c) : y(a, b, c) : z(a, b, c)`], the substitution indicated by

   :math:`a \to p(a, b, c), b \to q(a, b, c), c \to r(a, b, c)`

maps the set of all points - that is, the plane - into itself. Such a substitution has no clear geometric meaning, as suggested by the name, *symbolic* substitution. On the other hand, symbolic substitutions are of geometric interest because they map lines to lines, conics to conics, cubics to cubics, and they preserve incidence.

Example: The symbolic substitution (a, b, c) →(1/a, 1/b, 1/c) maps every triangle center to a triangle center, every pair of bicentric points to a pair of bicentric points, every circumconic to a circumconic, etc. However, when (a, b, c) = (2, 4, 5), for example, then a, b, c are sidelengths of a euclidean triangle, but 1/a, 1/b, 1/c are not.

Symbolic substitutions are introduced in C. Kimberling, "Symbolic substitutions in the transfigured plane of a triangle," *Aequationes Mathematicae* 73 (2007) 156-171.

.. _syngonal-image:
.. _term-syngonal-image:

syngonal image
--------------

Let :g:`P <P>` =\ :math:`p : q : r` (barycentric coordinates) be a point not on a sideline of :g:`ABC << A B C >>`, not :ref:`X(3) <X(3)>`, and not on the circumcircle of :g:`ABC << A B C >>`. The syngonal image of :g:`P <P>` is the point k(P) given by barycentyrics

   :math:`k(a,b,c,p,q,r) : k(b,c,a,q,r,p) : k(c,a,b,r,p,q)`,

where

   :math:`k(a,b,c,p,q,r) = (q + r - p)/[2a^{2}qr - (q + r - p)(b^{2}r + c^{2}q)]`.

The point k(P) is the antigonal image of the anticomplement of P. For further developments, search Hyacinthos for "symgonal" - however, following Hyacinthos #9881, the spelling "syngonal" is used here.

.. _tangential-triangle:
.. _term-tangential-triangle:

tangential triangle
-------------------

The anticevian triangle of the symmedian point :ref:`X(6) <X(6)>` =\ :math:`a : b : c`, formed by the lines tangent to the circumcircle of :g:`ABC << A B C >>` at vertices :g:`A <A>`, :g:`B <B>`, :g:`C <C>`. (See :term:`anticevian triangle <anticevian-triangle>`.)

.. _term-transcendental-center:
.. _transcendental-center:

transcendental center
---------------------

A triangle center X is a transcendental center if there exists no algebraic function f(a,b,c) such that :g:`X <X>` =\ :math:`f(a,b,c) : f(b,c,a) : f(c,a,b)`. Examples: :ref:`X(359) <X(359)>` and :ref:`X(360) <X(360)>`.

.. _term-triangle-center:
.. _triangle-center:

triangle center
---------------

A triangle center is a point of the form :math:`f(a,b,c) : f(b,c,a) : f(c,a,b)`, where f is a nonzero function satisfying two conditions:

   | (1) f is homogeneous in a,b,c; i.e., there is a nonnegative real number h such that

   :math:`f(ta,tb,tc) = t^{h}f(a,b,c)` for all (a,b,c) in the domain of f;

   | (2) f is symmetric in b and c; i.e., :math:`f(a,c,b) = f(a`,b,c).

A formal definition of triangle center is given in `TCCT. <http://faculty.evansville.edu/ck6/tcenters/tcct.html>`__ See also :term:`polynomial center <polynomial-center>`, :term:`transcendental center <transcendental-center>`, :term:`central triangle <central-triangle>`, :term:`bicentric points <bicentric-points>`.

.. _term-trilinear-image:
.. _trilinear-image:

trilinear image
---------------

see :term:`homologous images <homologous>`

.. _term-trilinear-polar:
.. _trilinear-polar:

trilinear polar
---------------

The trilinear polar of a point :math:`p : q : r` is the line

   :math:`qrx + rpy + pqz = 0`.

.. _term-trilinear-pole:
.. _trilinear-pole:

trilinear pole
--------------

The trilinear pole of the line ux + vy + wz = 0 is the point :math:`wv : uw : uv`.

Geometrically, the trilinear pole of a line :g:`PU <[ P U ]>` is the perspector of :g:`ABC << A B C >>` and the vertex-triangle of the anticevian triangles of :g:`P <P>` and U. (Randy Hutson, April 9, 2016)

.. _term-unary-cofactor-triangle:
.. _unary-cofactor-triangle:

unary cofactor triangle
-----------------------

Let :g:`P_{i} <P_i>` =\ :math:`x_{i} : y_{i} : z_{i}`, for i=1,2,3, be points. The :g:`A <A>`-vertex of the unary cofactor triangle is the point

   :math:`y_{2}z_{3} - z_{2}y_{3} : z_{2}x_{3} - x_{2}z_{3} : x_{2}y_{3} - y_{2}x_{3}`.

The :g:`B <B>`-vertex and :g:`C <C>`-vertex are defined cyclically. The vertices are the isogonal conjugates of the the vertices of the line-polar triangle of the points :g:`P_{i} <P_i>`.

If T is a triangle and U(T) its unary cofactor triangle, then U(U(T)) = T, and T and U(T) are perspective; see :term:`eigencenter <eigencenter>`.

.. _term-vertex-conjugate:
.. _vertex-conjugate:

vertex conjugate
----------------

The :g:`U <U>`-vertex conjugate of :g:`X <X>` is defined for distinct points :g:`U <U>` =\ :math:`u : v : w` and :g:`X <X>` = x : y : z: (trilinears) as the point P given by

   :math:`P = a/[a^{2}vwyz - ux(bw + cv)(bz + cy)] : b/[b^{2}wuzx - vy(cu + aw)(cx + az)] : c/[c^{2}uvxy - wz(av + bu)(ay + bx)]`.

Suppose that :g:`T <T>` = :g:`DEF << D E F >>` and :g:`T' <T'>` = :g:`D'E'F' << D' E' F' >>` are triangles. The vertex triangle of :g:`T <T>` and :g:`T' <T'>` is the triangle V(T,\ :g:`T' <T'>`) having sidelines :g:`DD' <[ D D' ]>`, :g:`EE' <[ E E' ]>`, :g:`FF' <[ F F' ]>`. Thus, V(T,\ :g:`T' <T'>`) generalizes "perspector", since V(T,\ :g:`T' <T'>`) is a single point if and only if T is perspective to :g:`T' <T'>`. If U and X are distinct points, then (vertex triangle of the circumcevian triangles of :g:`U <U>` and X) is perspective to :g:`ABC << A B C >>`, and the perspector is the :g:`U <U>`-vertex conjugate of :g:`X <X>`, which equals the :g:`X <X>`-vertex conjugate of U. See C. Kimberling, `Mappings Associated with Vertex Triangles <http://forumgeom.fau.edu/FG2009volume9/FG200903.pdf>`__, *Forum Geometricorum,* 2 (2002) 21-32.

.. _term-waw-conjugate:
.. _waw-conjugate:

waw conjugate
-------------

Let :g:`P <P>` =\ :math:`p : q : r` and :g:`U <U>` =\ :math:`u : v : w` be points, neither lying on a sideline of :g:`ABC << A B C >>`. The :g:`P <P>`-waw conjugate of :g:`U <U>` is the point

   :math:`h(p,q,r,u,v,w) : h(q,r,p,v,w,u) : h(r,p,q,w,u,v)`,

where

   :math:`h(p,q,r,u,v,w) = p[x^{2}q^{2}r^{2} + 2p^{2}(ry - qz)^{2} - pqr^{2}xy - pq^{2}rxz]`

.. _term-zayin-conjugate:
.. _zayin-conjugate:

zayin conjugate
---------------

Let :g:`P <P>` =\ :math:`p : q : r` and :g:`U <U>` =\ :math:`u : v : w` be points, neither lying on a sideline of :g:`ABC << A B C >>`. The :g:`P <P>`-zayin conjugate of :g:`U <U>` is the point

   :math:`h(p,q,r,u,v,w) : h(q,r,p,v,w,u) : h(r,p,q,w,u,v)`,

where

   :math:`h(p,q,r,u,v,w) = p(y + z)^{2} - ry^{2} - qz^{2} + (p - r)xy + (p - q)xz`.

Note that :ref:`X(1) <X(1)>`-zayin conjugacy is simply isogonal conjugacy.
