:order: 3310
:type: collection
:canonical_id: X_3310–X_3414
:subtitle: Incircle Transforms T(U), Trigonometric Offset Points & Kiepert Cusps

.. _c-03310-03414:

X_3310–X_3414
=============

.. rubric:: Incircle Transforms T(U), Trigonometric Offset Points & Kiepert Cusps

.. enunciation::

   Barycentric products of perpendicular directions (:ref:`X_3310 <X_3310>`), incircle transforms T(U) lying on the incircle (:ref:`X_3318 <X_3318>`\ –\ :ref:`X_3328 <X_3328>`), Darboux-cubic reflections and conjugates (:ref:`X_3341 <X_3341>`\ –\ :ref:`X_3358 <X_3358>`), trigonometric phase-shifted centers cos/sin/sec/csc/tan/cot(A ± θ) (:ref:`X_3364 <X_3364>`\ –\ :ref:`X_3409 <X_3409>`), and the Brocard-Kiepert-Fermat cusps (:ref:`X_3411 <X_3411>`\ –\ :ref:`X_3414 <X_3414>`).

.. figure:: c-03310-03414.svg
   :alt: X_3310–X_3414 — Incircle Transforms T(U), Trigonometric Offset Points & Kiepert Cusps
   :align: center

   **X_3310–X_3414** (*Incircle Transforms T(U), Trigonometric Offset Points & Kiepert Cusps*) — 16 representative centers (from 105 in collection) constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :g:`AB <[ A B ]>` = :math:`1`.

.. _preamble-0051:

.. admonition:: Group Preamble — Barycentric Products of Perpendicular Directions
   :class: note

   Suppose P and U are points on the line at infinity, given in barycentric coordinates by :g:`P <P>` =\ :math:`p : q : r` and :g:`U <U>` =\ :math:`u : v : w`. We call P and U *perpendicular directions* if for every point X not in the line at infinity, the lines XP and XU are perpendicular. (It is well known that if P and U are an antipodal pair on the circumcircle, then their :term:`isogonal conjugates <isogonal-conjugate>` are perpendicular directions.)

   Theorem: If P and U are perpendicular directions, then their barycentric product lies on the orthic axis.

   An outline of a proof follows. For given P on the line at infinity, the direction perpendicular to :g:`P <P>` is given by

   | a/:math:`d_{1}` : b/:math:`d_{2}` : c/:math:`d_{3}`,
   | where

   | :math:`d_{1}` = :math:`a^{2}`\ qr cos B cos C - :math:`p(b_{2}`\ r + :math:`c_{2}`\ q) cos A
   | :math:`d_{2}` = :math:`b^{2}`\ rp cos C cos A - :math:`q(c_{2}`\ p + :math:`a_{2}`\ r) cos B
   | :math:`d_{3}` = :math:`c^{2}`\ pq cos A cos B - :math:`r(a_{2}`\ q + :math:`b_{2}`\ p) cos C,

   and the barycentric product :g:`P*U <[ P* U ]>` is the point :math:`x : y : z` given by

   ap/:math:`d_{1}` : bq/:math:`d_{2}` : cr/:math:`d_{3}`.

   For P to lie on the line at infinity means that r = - p - q. Substitution for r, a computer quickly shows that

   x cot A + y cot B + z cot :g:`C <C>` = 0,

   as desired.

   The orthic axis is perpendicular to the Euler line. For this and other properties, visit MathWorld. The appearance of (I, J, K) in the following list means that X(K) is the barycentric product of perpendicular directions X_i and X_j.

   | (30,1511,1637)
   | (511,523,2491)
   | (514,516,676)
   | (2574,2575,647)
   | (513,517,3310)

.. _preamble-0052:

.. admonition:: Group Preamble — Points on the Incircle (Incircle transforms)
   :class: note

   Suppose that :g:`U <U>` =\ :math:`u : v : w` (trilinears) is a point other than the symmedian point, :ref:`X_6 <X_6>`. Then the *incircle transform of :g:`U* <U*>` is the point.

   T(U) = a (a - b + c) (a + b - c) (c v - b w)^2 : : ,

   which lies on the incircle. Geometrically, T(U) is the Brisse transform of the psi transform of :ref:`X_6 <X_6>` and U. (Brisse transform is described just before :ref:`X_1254 <X_1254>`, and psi transform, also called the "Psi mapping" elsewhere in ETC, and :cite:`TCCT <tcct>`, p. 80, is defined in the preamble just before :ref:`X_98 <X_98>`.

Member Centers
--------------

:ref:`Open Interactive 7-Triangle Constellation & Explorer ↗ <family-c-03310-03414>`

.. list-table::
   :class: etc-table etc-mode-relations
   :header-rows: 1
   :widths: 12 56 18 14

   * - Center
     - Name
     - Search (6,9,13)
     - Precision
   * - :ref:`X_3310 <X_3310>`
     - BARYCENTRIC PRODUCT X\_513\*X\_517
     - ``-1.339464``
     - Exact
   * - :ref:`X_3311 <X_3311>`
     - INTERSECTION OF LINES X\_3X\_6 AND X\_4X\_1131
     - ``1.814941``
     - Exact
   * - :ref:`X_3312 <X_3312>`
     - INTERSECTION OF LINES X\_3X\_6 AND X\_4X\_1132
     - ``-0.155143``
     - Exact
   * - :ref:`X_3313 <X_3313>`
     - INTERSECTION OF LINES X\_3X\_6 AND X\_66X\_69
     - ``8.519138``
     - Exact
   * - :ref:`X_3314 <X_3314>`
     - INTERSECTION OF LINES X\_2X\_6 AND X\_76X\_115
     - ``4.030634``
     - Exact
   * - :ref:`X_3315 <X_3315>`
     - INTERSECTION OF LINES X\_1X\_88 AND X\_105X\_110
     - ``1.484271``
     - Exact
   * - :ref:`X_3316 <X_3316>`
     - ISOGONAL CONJUGATE OF X\_3311
     - ``1.509856``
     - Exact
   * - :ref:`X_3317 <X_3317>`
     - ISOGONAL CONJUGATE OF X\_3312
     - ``15.176523``
     - Exact
   * - :ref:`X_3318 <X_3318>`
     - INCIRCLE TRANSFORM T(X\_603)
     - ``3.254781``
     - Exact
   * - :ref:`X_3319 <X_3319>`
     - INCIRCLE TRANSFORM T(X\_654)
     - ``0.066441``
     - Exact
   * - :ref:`X_3320 <X_3320>`
     - INCIRCLE TRANSFORM T(X\_656)
     - ``0.098781``
     - Exact
   * - :ref:`X_3321 <X_3321>`
     - INCIRCLE TRANSFORM T(X\_663)
     - ``0.294314``
     - Exact
   * - :ref:`X_3322 <X_3322>`
     - INCIRCLE TRANSFORM T(X\_665)
     - ``0.000026``
     - Exact
   * - :ref:`X_3323 <X_3323>`
     - INCIRCLE TRANSFORM T(X\_692)
     - ``2.338565``
     - Exact
   * - :ref:`X_3324 <X_3324>`
     - INCIRCLE TRANSFORM T(X\_822)
     - ``0.200393``
     - Exact
   * - :ref:`X_3325 <X_3325>`
     - INCIRCLE TRANSFORM T(X\_896)
     - ``0.419671``
     - Exact
   * - :ref:`X_3326 <X_3326>`
     - INCIRCLE TRANSFORM T(X\_909)
     - ``3.314176``
     - Exact
   * - :ref:`X_3327 <X_3327>`
     - INCIRCLE TRANSFORM T(X\_2290)
     - ``0.013445``
     - Exact
   * - :ref:`X_3328 <X_3328>`
     - INCIRCLE TRANSFORM T(X\_2291)
     - ``3.380591``
     - Exact
   * - :ref:`X_3329 <X_3329>`
     - INTERSECTION OF LINES X\_2X\_6 AND X\_39X\_83
     - ``1.736180``
     - Exact
   * - :ref:`X_3330 <X_3330>`
     - INTERSECTION OF LINES X\_4X\_6 AND X\_44X\_513
     - ``-4.107444``
     - Exact
   * - :ref:`X_3331 <X_3331>`
     - INTERSECTION OF LINES X\_4X\_6 AND X\_187X\_237
     - ``-1.480212``
     - Exact
   * - :ref:`X_3332 <X_3332>`
     - INTERSECTION OF LINES X\_1X\_7 AND X\_4X\_6
     - ``-0.810586``
     - Exact
   * - :ref:`X_3333 <X_3333>`
     - POHOATA POINT
     - ``1.074955``
     - Exact
   * - :ref:`X_3334 <X_3334>`
     - PERSPECTOR OF TRIANGLES T1T2T3 AND J1J2J3
     - ``2.640439``
     - 50-digit
   * - :ref:`X_3335 <X_3335>`
     - PERSPECTOR OF TRIANGLES N1N2N3 AND J1J2J3
     - ``-0.059584``
     - 50-digit
   * - :ref:`X_3336 <X_3336>`
     - INTERSECTION OF LINES X\_1X\_3 AND X\_7X\_498
     - ``-0.134392``
     - Exact
   * - :ref:`X_3337 <X_3337>`
     - INTERSECTION OF LINES X\_1X\_3 AND X\_7X\_499
     - ``0.668705``
     - Exact
   * - :ref:`X_3338 <X_3338>`
     - INTERSECTION OF LINES X\_1X\_3 AND X\_7X\_90
     - ``0.852972``
     - Exact
   * - :ref:`X_3339 <X_3339>`
     - INTERSECTION OF LINES X\_1X\_3 AND X\_7X\_10
     - ``0.459601``
     - Exact
   * - :ref:`X_3340 <X_3340>`
     - INTERSECTION OF LINES X\_1X\_3 AND X\_7X\_145
     - ``0.648456``
     - Exact
   * - :ref:`X_3341 <X_3341>`
     - X\_2-CEVA CONJUGATE OF X\_282
     - ``1.234001``
     - Exact
   * - :ref:`X_3342 <X_3342>`
     - ISOGONAL CONJUGATE OF X\_3341
     - ``2.244041``
     - Exact
   * - :ref:`X_3343 <X_3343>`
     - X\_2-CEVA CONJUGATE OF X\_1073
     - ``2.054606``
     - Exact
   * - :ref:`X_3344 <X_3344>`
     - ISOGONAL CONJUGATE OF X\_3343
     - ``1.371322``
     - Exact
   * - :ref:`X_3345 <X_3345>`
     - ISOGONAL CONJUGATE OF X\_1490
     - ``15.553223``
     - Exact
   * - :ref:`X_3346 <X_3346>`
     - ISOGONAL CONJUGATE OF X\_1498
     - ``9.801005``
     - Exact
   * - :ref:`X_3347 <X_3347>`
     - ISOGONAL CONJUGATE OF X\_3182
     - ``4.762941``
     - Exact
   * - :ref:`X_3348 <X_3348>`
     - ISOGONAL CONJUGATE OF X\_3183
     - ``-0.628930``
     - Exact
   * - :ref:`X_3349 <X_3349>`
     - INTERSECTION OF LINES X\_3X\_2130 AND X\_4X\_2131
     - ``-0.199660``
     - Exact
   * - :ref:`X_3350 <X_3350>`
     - INTERSECTION OF LINES X\_3X\_2131 AND X\_4X\_1073
     - ``4.108122``
     - Exact
   * - :ref:`X_3351 <X_3351>`
     - X\_2-CEVA CONJUGATE OF X\_3342
     - ``3.002384``
     - Exact
   * - :ref:`X_3352 <X_3352>`
     - ISOGONAL CONJUGATE OF X\_3351
     - ``0.779700``
     - Exact
   * - :ref:`X_3353 <X_3353>`
     - X\_20-CEVA CONJUGATE OF X\_84
     - ``-52.770375``
     - Exact
   * - :ref:`X_3354 <X_3354>`
     - ISOGONAL CONJUGATE OF X\_3353
     - ``11.874417``
     - Exact
   * - :ref:`X_3355 <X_3355>`
     - REFLECTION OF X\_2131 IN X\_3
     - ``-169.876745``
     - Exact
   * - :ref:`X_3356 <X_3356>`
     - X\_6-CROSS CONJUGATE OF X\_3350
     - ``3.803387``
     - Exact
   * - :ref:`X_3357 <X_3357>`
     - MIDPOINT OF X\_3 AND X\_64
     - ``19.204843``
     - Exact
   * - :ref:`X_3358 <X_3358>`
     - MIDPOINT OF X\_9 AND X\_84
     - ``-24.599201``
     - Exact
   * - :ref:`X_3359 <X_3359>`
     - MIDPOINT OF X\_2096 AND X\_3421
     - ``6.127436``
     - Exact
   * - :ref:`X_3360 <X_3360>`
     - SS(a → bc) OF X\_20
     - ``-2.826342``
     - Exact
   * - :ref:`X_3361 <X_3361>`
     - INTERSECTION OF LINES X\_1X\_3 AND X\_7X\_1125
     - ``0.290431``
     - Exact
   * - :ref:`X_3362 <X_3362>`
     - ISOGONAL CONJUGATE OF X\_1745
     - ``5.868808``
     - Exact
   * - :ref:`X_3363 <X_3363>`
     - X\_6 OF PEDAL TRIANGLE OF X\_2
     - ``1.602164``
     - Exact
   * - :ref:`X_3364 <X_3364>`
     - COS(A - 5π/12) POINT
     - ``1.464512``
     - Exact
   * - :ref:`X_3365 <X_3365>`
     - SIN(A - 5π/12) POINT
     - ``31.397915``
     - Exact
   * - :ref:`X_3366 <X_3366>`
     - SEC(A - 5π/12) POINT
     - ``1.937388``
     - Exact
   * - :ref:`X_3367 <X_3367>`
     - CSC(A - 5π/12) POINT
     - ``16.637410``
     - Exact
   * - :ref:`X_3368 <X_3368>`
     - COS(A - 2π/5) POINT
     - ``1.555046``
     - 50-digit
   * - :ref:`X_3369 <X_3369>`
     - SIN(A - 2π/5) POINT
     - ``317.719436``
     - 50-digit
   * - :ref:`X_3370 <X_3370>`
     - SEC(A - 2π/5) POINT
     - ``1.822510``
     - 50-digit
   * - :ref:`X_3371 <X_3371>`
     - COS(A - 3π/8) POINT
     - ``1.690907``
     - 50-digit
   * - :ref:`X_3372 <X_3372>`
     - SIN(A - 3π/8) POINT
     - ``-22.025343``
     - 50-digit
   * - :ref:`X_3373 <X_3373>`
     - SEC(A - 3π/8) POINT
     - ``1.656403``
     - 50-digit
   * - :ref:`X_3374 <X_3374>`
     - CSC(A - 3π/8) POINT
     - ``6.889028``
     - 50-digit
   * - :ref:`X_3375 <X_3375>`
     - TAN(A - π/3) POINT
     - ``-2.595788``
     - Exact
   * - :ref:`X_3376 <X_3376>`
     - COT(A - π/3) POINT
     - ``2.957649``
     - Exact
   * - :ref:`X_3377 <X_3377>`
     - TAN(A - π/4) POINT
     - ``-0.444525``
     - Exact
   * - :ref:`X_3378 <X_3378>`
     - COT(A - π/4) POINT
     - ``1.553319``
     - Exact
   * - :ref:`X_3379 <X_3379>`
     - COS(A - π/5) POINT
     - ``2.804834``
     - 50-digit
   * - :ref:`X_3380 <X_3380>`
     - SIN(A - π/5) POINT
     - ``-0.839988``
     - 50-digit
   * - :ref:`X_3381 <X_3381>`
     - SEC(A - π/5) POINT
     - ``0.408158``
     - 50-digit
   * - :ref:`X_3382 <X_3382>`
     - CSC(A - π/5) POINT
     - ``-0.617220``
     - 50-digit
   * - :ref:`X_3383 <X_3383>`
     - TAN(A - π/6) POINT
     - ``-0.008317``
     - Exact
   * - :ref:`X_3384 <X_3384>`
     - COT(A - π/6) POINT
     - ``-30.987829``
     - Exact
   * - :ref:`X_3385 <X_3385>`
     - COS(A - π/8) POINT
     - ``3.564267``
     - 50-digit
   * - :ref:`X_3386 <X_3386>`
     - SIN(A - π/8) POINT
     - ``0.073125``
     - 50-digit
   * - :ref:`X_3387 <X_3387>`
     - SEC(A - π/8) POINT
     - ``-0.457458``
     - 50-digit
   * - :ref:`X_3388 <X_3388>`
     - CSC(A - π/8) POINT
     - ``6.624679``
     - 50-digit
   * - :ref:`X_3389 <X_3389>`
     - COS(A - π/12) POINT
     - ``4.192229``
     - Exact
   * - :ref:`X_3390 <X_3390>`
     - SIN(A - π/12) POINT
     - ``0.429519``
     - Exact
   * - :ref:`X_3391 <X_3391>`
     - SEC(A - π/12) POINT
     - ``-1.235668``
     - Exact
   * - :ref:`X_3392 <X_3392>`
     - CSC(A - π/12) POINT
     - ``4.042937``
     - Exact
   * - :ref:`X_3393 <X_3393>`
     - COS(A + π/5) POINT
     - ``-3.851034``
     - 50-digit
   * - :ref:`X_3394 <X_3394>`
     - SIN(A + π/5) POINT
     - ``2.115192``
     - 50-digit
   * - :ref:`X_3395 <X_3395>`
     - COS(A + 2π/5) POINT
     - ``0.295299``
     - 50-digit
   * - :ref:`X_3396 <X_3396>`
     - SIN(A + 2π/5) POINT
     - ``3.914336``
     - 50-digit
   * - :ref:`X_3397 <X_3397>`
     - SEC(A + 2π/5) POINT
     - ``4.674851``
     - 50-digit
   * - :ref:`X_3398 <X_3398>`
     - COS(A - 2ω) POINT
     - ``2.776457``
     - Exact
   * - :ref:`X_3399 <X_3399>`
     - SEC(A - 2ω) POINT
     - ``0.439523``
     - Exact
   * - :ref:`X_3400 <X_3400>`
     - TAN(A - 2ω) POINT
     - ``-0.115143``
     - Exact
   * - :ref:`X_3401 <X_3401>`
     - COT(A - 2ω) POINT
     - ``-0.306871``
     - Exact
   * - :ref:`X_3402 <X_3402>`
     - TAN(A - ω) POINT
     - ``-0.068962``
     - Exact
   * - :ref:`X_3403 <X_3403>`
     - COT(A - ω) POINT
     - ``5.702764``
     - Exact
   * - :ref:`X_3404 <X_3404>`
     - TAN(A + ω) POINT
     - ``6.564259``
     - Exact
   * - :ref:`X_3405 <X_3405>`
     - COT(A + ω) POINT
     - ``-42.899104``
     - Exact
   * - :ref:`X_3406 <X_3406>`
     - SEC(A + 2ω) POINT
     - ``3.149957``
     - Exact
   * - :ref:`X_3407 <X_3407>`
     - CSC(A + 2ω) POINT
     - ``1.145037``
     - Exact
   * - :ref:`X_3408 <X_3408>`
     - TAN(A + 2ω) POINT
     - ``2.322401``
     - 50-digit
   * - :ref:`X_3409 <X_3409>`
     - COT(A + 2ω) POINT
     - ``-1.194716``
     - 50-digit
   * - :ref:`X_3410 <X_3410>`
     - INTERSECTION OF LINES X\_2X\_98 AND X\_4X\_93
     - ``-3.318868``
     - Exact
   * - :ref:`X_3411 <X_3411>`
     - 1st BROCARD-KIEPERT-FERMAT CUSP
     - ``-0.801182``
     - Exact
   * - :ref:`X_3412 <X_3412>`
     - 2nd BROCARD-KIEPERT-FERMAT CUSP
     - ``1.680501``
     - Exact
   * - :ref:`X_3413 <X_3413>`
     - 1st KIEPERT INFINITY POINT
     - —
     - 50-digit
   * - :ref:`X_3414 <X_3414>`
     - 2nd KIEPERT INFINITY POINT
     - —
     - 50-digit
