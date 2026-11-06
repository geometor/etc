:order: 3001
:type: collection
:canonical_id: X_3001–X_3118
:subtitle: Central Line Intersections, Stevanović Points & T/G Mappings

.. _c-03001-03118:

X_3001–X_3118
=============

.. rubric:: Central Line Intersections, Stevanović Points & T/G Mappings

.. enunciation::

   Pairwise intersections of the Brocard, de Longchamps, Gergonne, Lemoine, Nagel, orthic, Soddy, and Fermat axes (:ref:`X_3001 <X_3001>`\ –\ :ref:`X_3019 <X_3019>`), the 4th–10th Stevanović points (:ref:`X_3020 <X_3020>`\ –\ :ref:`X_3026 <X_3026>`), antipodal circle mappings and :term:`complements <complement>` (:ref:`X_3027 <X_3027>`\ –\ :ref:`X_3111 <X_3111>`), and Quang Tuan Bui's TgX and GtX mappings (:ref:`X_3112 <X_3112>`\ –\ :ref:`X_3118 <X_3118>`).

.. figure:: c-03001-03118.svg
   :alt: X_3001–X_3118 — Central Line Intersections, Stevanović Points & T/G Mappings
   :align: center

   **X_3001–X_3118** (*Central Line Intersections, Stevanović Points & T/G Mappings*) — 16 representative centers (from 118 in collection) constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :g:`AB <[ A B ]>` = :math:`1`.

.. _preamble-0047:

.. admonition:: Group Preamble — Antipodal Pairs on Circles
   :class: note

   In response to Stevanovic's findings (:ref:`X_3000 <X_3000>` to :ref:`X_3006 <X_3006>`), :person:`Peter Moses <peter-moses>` noted (:cite:`Hyacinthos <hyacinthos>`, 12/9/2004) a method for mapping a pair of antipodal points on one circle to an antipodal pair on another circle. The method depends on centers of similitude:

   Suppose :g:`O_{1} <O_1>` and :g:`O_{2} <O_2>` are circles, that P is on :g:`O_{1} <O_1>` and that :g:`P' <P'>` is the antipode of :g:`P <P>` on :g:`O_{1} <O_1>`. Let :g:`U <U>` be the internal center of similitude (insimilicenter) of :g:`O_{1} <O_1>` and :g:`O_{2} <O_2>`, and V the exsimilicenter. Define :g:`Q <Q>` = :g:`PU <[ P U ]>` ∩\ :g:`P' <P'>` V and :g:`Q' <Q'>` = PV ∩\ :g:`P' <P'>` U. Then on :g:`O_{2} <O_2>`, point :g:`Q' <Q'>` is the antipode of Q. Moreover, the lines :g:`PP' <[ P P' ]>` and :g:`QQ' <[ Q Q' ]>` are parallel.

   The method follows from introductory material on centers of similitude (e.g., **H. S. M. Coxeter,** *Introduction to Geometry, 2nd edition*, page 70, which cites **Nathan Altshiller-Court,** *College Geometry, 2nd edition,* page 184). If you have The Geometer's Sketchpad, you can view **Antipodal Pairs** (``AntipodalPairs.gsp``).

   In the following examples, suppose :g:`P <P>` =\ :math:`p : q : r` (trilinears).

   Example 1. :g:`O_{1} <O_1>` = circumcircle and :g:`O_{2} <O_2>` = incircle. In this case, insimilicenter(:g:`O_{1} <O_1>`, :g:`O_{2} <O_2>`) = :ref:`X_55 <X_55>`, and exsimilicenter(:g:`O_{1} <O_1>`, :g:`O_{2} <O_2>`) = :ref:`X_56 <X_56>`. The antipodal points on :g:`O_{2} <O_2>` given by the Moses mapping are

   :g:`Q <Q>` = ((b - c)\ :sup:`2`\ p + a(bq + cr))(b + c - a) : :

   :g:`Q' <Q'>` = ((b + c)\ :sup:`2`\ p + a(bq + cr))/(b + c - a) : : .

   Example 2. :g:`O_{1} <O_1>` = circumcircle and :g:`O_{2} <O_2>` = Apollonius circle, with center :ref:`X_970 <X_970>`. Here, insimilicenter(:g:`O_{1} <O_1>`, :g:`O_{2} <O_2>`) = :ref:`X_573 <X_573>`, and exsimilicenter(:g:`O_{1} <O_1>`, :g:`O_{2} <O_2>`) = :ref:`X_386 <X_386>`. A point on :g:`O_{2} <O_2>` is

   :g:`Q' <Q'>` = (a + b)(a + c)(b + c)\ :sup:`2`\ p - a(bc + ca + ab + :math:`b^{2}` + :math:`c^{2})`\ (bq + cr) : : .

   Example 3. :g:`O_{1} <O_1>` = circumcircle and :g:`O_{2} <O_2>` = Spieker circle. In this case, insimilicenter(:g:`O_{1} <O_1>`, :g:`O_{2} <O_2>`) = :ref:`X_958 <X_958>`, and exsimilicenter(:g:`O_{1} <O_1>`, :g:`O_{2} <O_2>`) = :ref:`X_1376 <X_1376>`.

   :g:`Q <Q>` = (a - b - c)[((b + c)(b - c)\ :sup:`2` + :math:`a(b^{2}` + :math:`c^{2})`)p + (ab + ac + 2bc + :math:`a^{2})`\ (bq + cr)] : :

   :g:`Q' <Q'>` = (:math:`b^{3}` + :math:`c^{3}` - :math:`ab^{2}` - :math:`ac^{2}` - :math:`bc^{2}` - :math:`b^{2}`\ c)p + (ab + ac - 2bc - :math:`a^{2})`\ (bq + cr) : :

   Example 4. :g:`O_{1} <O_1>` = incircle and :g:`O_{2} <O_2>` = Spieker circle. In this case, insimilicenter(:g:`O_{1} <O_1>`, :g:`O_{2} <O_2>`) = :ref:`X_2 <X_2>`, and exsimilicenter(:g:`O_{1} <O_1>`, :g:`O_{2} <O_2>`) = :ref:`X_8 <X_8>`.

   :g:`Q <Q>` = (bp + cq)/a : (cr + ap)/b : (ap + bq)/c = complement of :g:`P <P>`

   :g:`Q' <Q'>` = 2abc(b + c)p - bc(a - b - c)(bq + cr) : :

   Example 5. :g:`O_{1} <O_1>` = circumcircle and :g:`O_{2} <O_2>` = sine-triple-angle circle. In this case, insimilicenter(:g:`O_{1} <O_1>`, :g:`O_{2} <O_2>`) = :ref:`X_1147 <X_1147>`, and exsimilicenter(:g:`O_{1} <O_1>`, :g:`O_{2} <O_2>`) = :ref:`X_184 <X_184>`. A point on :g:`O_{2} <O_2>` is

   :g:`Q <Q>` = a[:math:`a(a^{2}` - :math:`b^{2})`\ (:math:`a^{2}` - :math:`c^{2})`\ p - :math:`a^{2}(b^{2} -a^{2} + c^{2})`\ (bq + cr)] : :

.. _preamble-0048:

.. admonition:: Group Preamble — T and G Mappings (Centers X_3112-X_3118)
   :class: note

   This section presents points :ref:`X_3112 <X_3112>` to :ref:`X_3118 <X_3118>` as representative of points introduced by Quang Tuan Bui in :cite:`Hyacinthos <hyacinthos>`, August 5, 2006.

   Suppose X is a point not on a sideline of :g:`ABC << A B C >>`. Let

   | gX = :term:`isogonal conjugate <isogonal-conjugate>` of X
   | tX = :term:`isotomic conjugate <isotomic-conjugate>` of X
   | tgX = isotomic conjugate of gX
   | gtX = isogonal conjugate of tX
   | Gt = intersection of lines X(tX) and (gX)(gtX)
   | Tg = intersection of lines X(gX) and (tX)(tgX)

   Then the points :g:`A <A>`, :g:`B <B>`, :g:`C <C>`, gX, tX, Tg, Gt are on a conic. As a circumconic, it is the image under the isogonal conjugate mapping of line X(gtX). It is also the image under the isotomic conjugate mapping of line X(tgX).

   If :g:`X <X>` =\ :math:`x : y : z` (trilinears), then

   Gt = (:math:`b^{2}` - :math:`c^{2})`/(:math:`x(b^{2}`\ :math:`y^{2}` - :math:`c^{2}`\ :math:`z^{2})`) : (:math:`c^{2}` - :math:`a^{2})`/(:math:`y(c^{2}`\ :math:`z^{2}` - :math:`a^{2}`\ :math:`x^{2})`) : (:math:`a^{2}` - :math:`b^{2})`/(:math:`z(a^{2}`\ :math:`x^{2}` - :math:`b^{2}`\ :math:`y^{2})`)

   Tg = (:math:`b^{2}` - :math:`c^{2})`/(:math:`x(y^{2}` - :math:`z^{2})`) : (:math:`c^{2}` - :math:`a^{2})`/(:math:`y(z^{2}` - :math:`x^{2})`) : (:math:`a^{2}` - :math:`b^{2})`/(:math:`z(x^{2}` - :math:`y^{2})`)

   | The :ref:`X_31 <X_31>`-conic passes through X_i for I = 75, 92, 313, 321, 561, 1441, 1821, 1934, 2995, 2997.
   | The :ref:`X_32 <X_32>`-conic passes through X_i for I = 76, 264, 276, 290, 300, 301, 308, 313, 327, 349, 1502, 2367.
   | The :ref:`X_76 <X_76>`-conic passes through X_i for I = 6, 32, 83, 213, 729, 981, 1918, 1974, 2207, 2281, 2422.

.. collection::
   :sort: order
