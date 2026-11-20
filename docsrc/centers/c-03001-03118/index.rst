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

Member Centers
--------------

:ref:`Open Interactive 7-Triangle Constellation & Explorer ↗ <family-c-03001-03118>`

.. list-table::
   :class: etc-table etc-mode-relations
   :header-rows: 1
   :widths: 12 56 18 14

   * - Center
     - Name
     - Search (6,9,13)
     - Precision
   * - :ref:`X_3001 <X_3001>`
     - (BROCARD AXIS)∩(DE LONGCHAMPS LINE)
     - ``5.295530``
     - Exact
   * - :ref:`X_3002 <X_3002>`
     - (BROCARD AXIS)∩(GERGONNE LINE)
     - ``-1.062689``
     - Exact
   * - :ref:`X_3003 <X_3003>`
     - (BROCARD AXIS)∩(ORTHIC AXIS)
     - ``0.463617``
     - Exact
   * - :ref:`X_3004 <X_3004>`
     - (DE LONGCHAMPS LINE)∩(GERGONNE LINE)
     - ``-71.744206``
     - Exact
   * - :ref:`X_3005 <X_3005>`
     - (DE LONGCHAMPS LINE)∩(LEMOINE AXIS)
     - ``-11.861814``
     - Exact
   * - :ref:`X_3006 <X_3006>`
     - (DE LONGCHAMPS LINE)∩(NAGEL LINE)
     - ``7.932609``
     - Exact
   * - :ref:`X_3007 <X_3007>`
     - (DE LONGCHAMPS LINE)∩(SODDY LINE)
     - ``5.120109``
     - Exact
   * - :ref:`X_3008 <X_3008>`
     - (GERGONNE LINE)∩(NAGEL LINE)
     - ``-2.345113``
     - Exact
   * - :ref:`X_3009 <X_3009>`
     - (LEMOINE AXIS)∩(NAGEL LINE)
     - ``-2.750146``
     - Exact
   * - :ref:`X_3010 <X_3010>`
     - (LEMOINE AXIS)∩(SODDY LINE)
     - ``-1.533330``
     - Exact
   * - :ref:`X_3011 <X_3011>`
     - (NAGEL LINE)∩(ORTHIC AXIS)
     - ``-0.022251``
     - Exact
   * - :ref:`X_3012 <X_3012>`
     - (ORTHIC AXIS)∩(SODDY LINE)
     - ``0.749351``
     - Exact
   * - :ref:`X_3013 <X_3013>`
     - (ANTIORTHIC AXIS)∩(FERMAT AXIS)
     - ``-3.582657``
     - Exact
   * - :ref:`X_3014 <X_3014>`
     - (DE LONGCHAMPS LINE)∩(FERMAT AXIS)
     - ``3.978407``
     - Exact
   * - :ref:`X_3015 <X_3015>`
     - (GERGONNE LINE)∩(FERMAT AXIS)
     - ``-0.470397``
     - Exact
   * - :ref:`X_3016 <X_3016>`
     - (LEMOINE AXIS)∩(FERMAT AXIS)
     - ``-1.260296``
     - Exact
   * - :ref:`X_3017 <X_3017>`
     - (NAGEL LINE)∩(FERMAT AXIS)
     - ``1.097655``
     - Exact
   * - :ref:`X_3018 <X_3018>`
     - (ORTHIC AXIS)∩(FERMAT AXIS)
     - ``0.625644``
     - Exact
   * - :ref:`X_3019 <X_3019>`
     - (SODDY LINE)∩(FERMAT AXIS)
     - ``0.218216``
     - Exact
   * - :ref:`X_3020 <X_3020>`
     - 4th STEVANOVIC POINT
     - ``2.856936``
     - Exact
   * - :ref:`X_3021 <X_3021>`
     - 5th STEVANOVIC POINT
     - ``2.622145``
     - Exact
   * - :ref:`X_3022 <X_3022>`
     - 6th STEVANOVIC POINT
     - ``2.935176``
     - Exact
   * - :ref:`X_3023 <X_3023>`
     - 7th STEVANOVIC POINT
     - ``2.452390``
     - Exact
   * - :ref:`X_3024 <X_3024>`
     - 8th STEVANOVIC POINT
     - ``3.029294``
     - Exact
   * - :ref:`X_3025 <X_3025>`
     - 9th STEVANOVIC POINT
     - ``3.338604``
     - Exact
   * - :ref:`X_3026 <X_3026>`
     - 10th STEVANOVIC POINT
     - ``2.570624``
     - Exact
   * - :ref:`X_3027 <X_3027>`
     - INCIRCLE-ANTIPODE OF X\_3023
     - ``0.928227``
     - Exact
   * - :ref:`X_3028 <X_3028>`
     - INCIRCLE-ANTIPODE OF X\_3024
     - ``0.351323``
     - Exact
   * - :ref:`X_3029 <X_3029>`
     - INTERSECTION X\_10X\_115∩X\_98X\_573
     - ``10.032808``
     - Exact
   * - :ref:`X_3030 <X_3030>`
     - INTERSECTION X\_10X\_11∩X\_43X\_57
     - ``-1.977975``
     - Exact
   * - :ref:`X_3031 <X_3031>`
     - INTERSECTION X\_10X\_125∩X\_74X\_573
     - ``-0.005323``
     - Exact
   * - :ref:`X_3032 <X_3032>`
     - INTERSECTION X\_10X\_11∩X\_100X\_386
     - ``6.713846``
     - Exact
   * - :ref:`X_3033 <X_3033>`
     - INTERSECTION X\_10X\_116∩X\_43X\_57
     - ``1.632335``
     - Exact
   * - :ref:`X_3034 <X_3034>`
     - INTERSECTION X\_10X\_116∩X\_105X\_386
     - ``7.079070``
     - Exact
   * - :ref:`X_3035 <X_3035>`
     - COMPLEMENT OF X\_11
     - ``2.622486``
     - Exact
   * - :ref:`X_3036 <X_3036>`
     - COMPLEMENT OF X\_1317
     - ``3.575312``
     - Exact
   * - :ref:`X_3037 <X_3037>`
     - COMPLEMENT OF X\_1356
     - ``3.883934``
     - Exact
   * - :ref:`X_3038 <X_3038>`
     - COMPLEMENT OF X\_1357
     - ``3.825077``
     - Exact
   * - :ref:`X_3039 <X_3039>`
     - COMPLEMENT OF X\_1358
     - ``3.564817``
     - Exact
   * - :ref:`X_3040 <X_3040>`
     - COMPLEMENT OF X\_1361
     - ``3.853479``
     - Exact
   * - :ref:`X_3041 <X_3041>`
     - COMPLEMENT OF X\_1362
     - ``3.721333``
     - Exact
   * - :ref:`X_3042 <X_3042>`
     - COMPLEMENT OF X\_1364
     - ``2.344319``
     - Exact
   * - :ref:`X_3043 <X_3043>`
     - INTERSECTION X\_4X\_110∩X\_74X\_184
     - ``4.565356``
     - Exact
   * - :ref:`X_3044 <X_3044>`
     - INTERSECTION X\_54X\_114∩X\_99X\_184
     - ``-0.555875``
     - Exact
   * - :ref:`X_3045 <X_3045>`
     - INTERSECTION X\_54X\_119∩X\_100X\_184
     - ``-1.020805``
     - Exact
   * - :ref:`X_3046 <X_3046>`
     - INTERSECTION X\_54X\_118∩X\_101X\_184
     - ``-1.732638``
     - Exact
   * - :ref:`X_3047 <X_3047>`
     - INTERSECTION X\_54X\_113∩X\_2X\_98
     - ``-1.962046``
     - Exact
   * - :ref:`X_3048 <X_3048>`
     - INTERSECTION X\_110X\_126∩X\_111X\_184
     - ``-1.795451``
     - Exact
   * - :ref:`X_3049 <X_3049>`
     - INTERSECTION X\_6X\_523∩X\_520X\_647
     - ``-1.278090``
     - Exact
   * - :ref:`X_3050 <X_3050>`
     - INTERSECTION X\_6X\_523∩X\_50X\_647
     - ``-3.549088``
     - Exact
   * - :ref:`X_3051 <X_3051>`
     - INTERSECTION X\_2X\_6∩X\_32X\_184
     - ``0.510064``
     - Exact
   * - :ref:`X_3052 <X_3052>`
     - INTERSECTION X\_31X\_42∩X\_32X\_220
     - ``-0.249098``
     - Exact
   * - :ref:`X_3053 <X_3053>`
     - INTERSECTION X\_3X\_6∩X\_4X\_230
     - ``-0.631286``
     - Exact
   * - :ref:`X_3054 <X_3054>`
     - CENTER OF EVANS CONIC
     - ``-113.162938``
     - Exact
   * - :ref:`X_3055 <X_3055>`
     - {X\_2,X\_6}-HARMONIC CONJUGATE OF X\_3054
     - ``1.805316``
     - Exact
   * - :ref:`X_3056 <X_3056>`
     - INTERSECTION OF LINES X\_1X\_256 AND X\_6X\_31
     - ``3.009842``
     - Exact
   * - :ref:`X_3057 <X_3057>`
     - INTERSECTION OF LINES X\_1X\_3 AND X\_10X\_11
     - ``2.850891``
     - Exact
   * - :ref:`X_3058 <X_3058>`
     - INTERSECTION OF LINES X\_1X\_30 AND X\_2X\_11
     - ``2.636860``
     - Exact
   * - :ref:`X_3059 <X_3059>`
     - INTERSECTION OF LINES X\_7X\_8 AND X\_9X\_55
     - ``4.721924``
     - Exact
   * - :ref:`X_3060 <X_3060>`
     - INTERSECTION OF LINES X\_2X\_51 AND X\_4X\_52
     - ``-2.388118``
     - Exact
   * - :ref:`X_3061 <X_3061>`
     - INTERSECTION OF LINES X\_1X\_6 AND X\_2X\_257
     - ``3.898256``
     - Exact
   * - :ref:`X_3062 <X_3062>`
     - ISOGONAL CONJUGATE OF X\_165
     - ``-11.151252``
     - Exact
   * - :ref:`X_3063 <X_3063>`
     - CROSSDIFFERENCE OF X\_7 AND X\_8
     - ``-4.539010``
     - Exact
   * - :ref:`X_3064 <X_3064>`
     - ISOGONAL CONJUGATE OF X\_1813
     - ``-6.194436``
     - Exact
   * - :ref:`X_3065 <X_3065>`
     - ISOGONAL CONJUGATE OF X\_484
     - ``5.239356``
     - Exact
   * - :ref:`X_3066 <X_3066>`
     - 2nd LEMOINE HOMOTHETIC CENTER
     - ``0.950790``
     - Exact
   * - :ref:`X_3067 <X_3067>`
     - HOFSTADTER ELLIPSE INTERSECTION
     - ``1.445571``
     - 50-digit
   * - :ref:`X_3068 <X_3068>`
     - INTERSECTION OF X\_2X\_6 AND X\_4X\_371
     - ``1.535810``
     - Exact
   * - :ref:`X_3069 <X_3069>`
     - INTERSECTION OF X\_2X\_6 AND X\_4X\_372
     - ``-0.620505``
     - Exact
   * - :ref:`X_3070 <X_3070>`
     - INTERSECTION OF X\_4X\_6 AND X\_5X\_372
     - ``-0.665590``
     - Exact
   * - :ref:`X_3071 <X_3071>`
     - INTERSECTION OF X\_4X\_6 AND X\_5X\_371
     - ``4.292325``
     - Exact
   * - :ref:`X_3072 <X_3072>`
     - INTERSECTION OF X\_1X\_3 AND X\_4X\_31
     - ``-0.593433``
     - Exact
   * - :ref:`X_3073 <X_3073>`
     - INTERSECTION OF X\_3X\_238 AND X\_4X\_31
     - ``2.331483``
     - Exact
   * - :ref:`X_3074 <X_3074>`
     - INTERSECTION OF X\_1X\_6 AND X\_2X\_255
     - ``2.780224``
     - Exact
   * - :ref:`X_3075 <X_3075>`
     - INTERSECTION OF X\_1X\_3 AND X\_2X\_255
     - ``3.476896``
     - Exact
   * - :ref:`X_3076 <X_3076>`
     - INTERSECTION OF X\_1X\_606 AND X\_47X\_605
     - ``1.779658``
     - Exact
   * - :ref:`X_3077 <X_3077>`
     - INTERSECTION OF X\_1X\_605 AND X\_47X\_606
     - ``-3.673557``
     - Exact
   * - :ref:`X_3078 <X_3078>`
     - DANNEELS POINT OF X\_5
     - ``2.017202``
     - Exact
   * - :ref:`X_3079 <X_3079>`
     - DANNEELS POINT OF X\_20
     - ``-0.644259``
     - Exact
   * - :ref:`X_3080 <X_3080>`
     - DANNEELS POINT OF X\_25
     - ``-0.079537``
     - Exact
   * - :ref:`X_3081 <X_3081>`
     - DANNEELS POINT OF X\_30
     - ``-0.704134``
     - Exact
   * - :ref:`X_3082 <X_3082>`
     - RADICAL CENTER OF EXTERNAL MALFATTI CIRCLES
     - ``4.611476``
     - 50-digit
   * - :ref:`X_3083 <X_3083>`
     - INTERSECTION OF LINES X\_1X\_2 AND X\_37X\_494
     - ``2.266684``
     - Exact
   * - :ref:`X_3084 <X_3084>`
     - INTERSECTION OF LINES X\_1X\_2 AND X\_37X\_493
     - ``4.223180``
     - Exact
   * - :ref:`X_3085 <X_3085>`
     - INTERSECTION OF LINES X\_1X\_2 AND X\_4X\_12
     - ``1.929560``
     - Exact
   * - :ref:`X_3086 <X_3086>`
     - INTERSECTION OF LINES X\_1X\_2 AND X\_4X\_11
     - ``1.202485``
     - Exact
   * - :ref:`X_3087 <X_3087>`
     - INTERSECTION OF LINES X\_2X\_95 AND X\_4X\_6
     - ``1.748108``
     - Exact
   * - :ref:`X_3088 <X_3088>`
     - INTERSECTION OF LINES X\_2X\_3 AND X\_33X\_3086
     - ``168.696563``
     - Exact
   * - :ref:`X_3089 <X_3089>`
     - INTERSECTION OF LINES X\_2X\_3 AND X\_33X\_3085
     - ``-1.422301``
     - Exact
   * - :ref:`X_3090 <X_3090>`
     - INTERSECTION OF LINES X\_2X\_3 AND X\_11X\_1058
     - ``1.442799``
     - Exact
   * - :ref:`X_3091 <X_3091>`
     - INTERSECTION OF LINES X\_2X\_3 AND X\_11X\_153
     - ``-0.693026``
     - Exact
   * - :ref:`X_3092 <X_3092>`
     - INTERSECTION OF LINES X\_2X\_1579 AND X\_4X\_6
     - ``6.974385``
     - Exact
   * - :ref:`X_3093 <X_3093>`
     - INTERSECTION OF LINES X\_2X\_1578 AND X\_4X\_6
     - ``-1.148171``
     - Exact
   * - :ref:`X_3094 <X_3094>`
     - INTERSECTION OF LINES X\_2X\_694 AND X\_3X\_6
     - ``2.136051``
     - Exact
   * - :ref:`X_3095 <X_3095>`
     - INTERSECTION OF LINES X\_3X\_6 AND X\_5X\_76
     - ``-3.653404``
     - Exact
   * - :ref:`X_3096 <X_3096>`
     - INTERSECTION OF LINES X\_2X\_32 AND X\_76X\_141
     - ``3.236406``
     - Exact
   * - :ref:`X_3097 <X_3097>`
     - INTERSECTION OF LINES X\_1X\_39 AND X\_43X\_63
     - ``1.522537``
     - Exact
   * - :ref:`X_3098 <X_3098>`
     - INTERSECTION OF LINES X\_3X\_6 AND X\_69X\_74
     - ``9.677090``
     - Exact
   * - :ref:`X_3099 <X_3099>`
     - INTERSECTION OF LINES X\_1X\_32 AND X\_846X\_902
     - ``-5.787974``
     - Exact
   * - :ref:`X_3100 <X_3100>`
     - INTERSECTION OF LINES X\_1X\_7 AND X\_2X\_33
     - ``4.147545``
     - Exact
   * - :ref:`X_3101 <X_3101>`
     - INTERSECTION OF LINES X\_2X\_19 AND X\_8X\_20
     - ``31.699209``
     - Exact
   * - :ref:`X_3102 <X_3102>`
     - INNER VERTEX OF THE BROCARD SQUARE
     - ``3.291440``
     - Exact
   * - :ref:`X_3103 <X_3103>`
     - OUTER VERTEX OF THE BROCARD SQUARE
     - ``-0.162481``
     - Exact
   * - :ref:`X_3104 <X_3104>`
     - INNER VERTEX OF 1st BROCARD EQUILATERAL TRIANGLE
     - ``4.555662``
     - Exact
   * - :ref:`X_3105 <X_3105>`
     - OUTER VERTEX OF 2nd BROCARD EQUILATERAL TRIANGLE
     - ``-1.426703``
     - Exact
   * - :ref:`X_3106 <X_3106>`
     - CENTER OF 1st BROCARD EQUILATERAL TRIANGLE
     - ``2.561541``
     - Exact
   * - :ref:`X_3107 <X_3107>`
     - CENTER OF 2nd BROCARD EQUILATERAL TRIANGLE
     - ``0.567419``
     - Exact
   * - :ref:`X_3108 <X_3108>`
     - DC(X\_83)
     - ``1.252809``
     - Exact
   * - :ref:`X_3109 <X_3109>`
     - ORTHOGONAL PROJECTION OF X\_1 ON EULER LINE
     - ``2.126222``
     - Exact
   * - :ref:`X_3110 <X_3110>`
     - ORTHOGONAL PROJECTION OF X\_1 ON BROCARD AXIS
     - ``1.581408``
     - Exact
   * - :ref:`X_3111 <X_3111>`
     - ORTHOGONAL PROJECTION OF X\_2 ON BROCARD AXIS
     - ``2.305148``
     - Exact
   * - :ref:`X_3112 <X_3112>`
     - TgX(31)
     - ``2.817985``
     - Exact
   * - :ref:`X_3113 <X_3113>`
     - GtX(31)
     - ``1.145037``
     - Exact
   * - :ref:`X_3114 <X_3114>`
     - TgX(32)
     - ``3.070797``
     - Exact
   * - :ref:`X_3115 <X_3115>`
     - GtX(32)
     - ``2.148033``
     - Exact
   * - :ref:`X_3116 <X_3116>`
     - ISOGONAL CONJUGATE OF GtX(31)
     - ``1.376632``
     - Exact
   * - :ref:`X_3117 <X_3117>`
     - ISOGONAL CONJUGATE OF TgX(32)
     - ``0.822397``
     - Exact
   * - :ref:`X_3118 <X_3118>`
     - ISOGONAL CONJUGATE OF GtX(32)
     - ``1.153875``
     - Exact
