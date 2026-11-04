:order: 1285
:canonical_id: X_1285
:subtitle: LEMOINE HOMOTHETIC CENTER
:dependencies: X_2, X_4, X_6, X_32, X_99, X_172, X_193, X_376, X_497, X_609, X_631, X_1003, X_1056, X_1058, X_1384, X_1914, X_1992, X_3053, X_3066

.. _X_1285:

X_1285
======

.. rubric:: LEMOINE HOMOTHETIC CENTER

.. enunciation::

   :ref:`X_1285 <X_1285>` is the homothetic center of the :term:`antipedal triangle <antipedal-triangle>` of :ref:`X_2 <X_2>` and the :term:`pedal triangle <pedal-triangle>` of :ref:`X_6 <X_6>`. (:person:`Darij Grinberg <darij-grinberg>`, :cite:`Hyacinthos #6577 <hyacinthos>`, 2/21/03). See also X_3066.

.. figure:: x-01285.svg
   :alt: X_1285 — LEMOINE HOMOTHETIC CENTER
   :align: center

   **X_1285** (*LEMOINE HOMOTHETIC CENTER*) constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :g:`AB <[ A B ]>` = :math:`1`.

.. admonition:: Constructed Elements
   :class: note

   * **Central Lines:** :g:`{4, 32} <{ 4, 32 }>`, :g:`{6, 376} <{ 6, 376 }>`
   * **Related Centers:** :g:`X_4 <X_4>` (:ref:`ORTHOCENTER <X_4>`), :g:`X_32 <X_32>` (:ref:`3rd POWER POINT <X_32>`), :g:`X_6 <X_6>` (:ref:`SYMMEDIAN POINT <X_6>`), :g:`X_376 <X_376>` (:ref:`CENTROID OF THE ANTIPEDAL TRIANGLE OF X <X_376>`)

.. signature:: center

   | **Trilinears:** :math:`f(a,b,c) : f(b,c,a) : f(c,a,b)`, where :math:`f(a,b,c) = bc(3a^{2} + b^{2} - c^{2})(3a^{2} - b^{2} + c^{2})`
   | **Barycentrics:** :math:`af(a,b,c) : bf(b,c,a) : cf(c,a,b)`
   | **Search Value (6, 9, 13):** :math:`0.102966916856`

.. collapse:: Incident Central Lines
   :badge: 9 lines
   :class: line-catalog

   {:ref:`2 <X_2>`, :ref:`1384 <X_1384>`}, {:ref:`4 <X_4>`, :ref:`32 <X_32>`}, {:ref:`6 <X_6>`, :ref:`376 <X_376>`}, {:ref:`99 <X_99>`, :ref:`1992 <X_1992>`}, {:ref:`172 <X_172>`, :ref:`1058 <X_1058>`}, {:ref:`193 <X_193>`, :ref:`1003 <X_1003>`}, {:ref:`497 <X_497>`, :ref:`609 <X_609>`}, {:ref:`631 <X_631>`, 3053}, {:ref:`1056 <X_1056>`, :ref:`1914 <X_1914>`}

Notes
-----

.. container:: note-item

   Let :g:`T <T>` denote the antipedal triangle of :ref:`X_2 <X_2>`, and let T(m) denote X(m)-of-T. Then T(m) is a :term:`triangle center <triangle-center>` of the reference triangle :g:`ABC << A B C >>`. The appearance of (m,n) in the following list means that T(m) = X_n. Note the special case m = 1285.

      (2,376), (6,2), (115,99), (125,1296), (597,3), (599,20), (1285,1285), (1992,4), (2030,187), (2549,69)

.. container:: note-item

   Let :g:`U <U>` denote the pedal triangle of :ref:`X_6 <X_6>`, and let U(m) denote X(m)-of-U. Then U(m) is a triangle center of the reference triangle :g:`ABC << A B C >>`. The appearance of (m,n) in the following list means that U(m) = X_n. (This list and the one just above were contributed by :person:`Peter Moses <peter-moses>`, 11/15/2007.)

      (2,6), (3,597), (4,1992), (20,599), (69,2549), (99,115), (187,2030), (376,2), (1285, 1285), (1296, 125)

.. container:: note-item

   Let :g:`A'B'C' << A' B' C' >>` be the antipedal triangle of :ref:`X_2 <X_2>`. The centroid of :g:`A'B'C' << A' B' C' >>` is :ref:`X_376 <X_376>`. Let :g:`A″B″C″ << A″ B″ C″ >>` be the antipedal triangle, wrt :g:`A'B'C' << A' B' C' >>`, of :ref:`X_376 <X_376>`. :g:`A″B″C″ << A″ B″ C″ >>` is homothetic to :g:`ABC << A B C >>`, and the center of homothety is :ref:`X_1285 <X_1285>`. (:person:`Randy Hutson <randy-hutson>`, March 21, 2019)

.. container:: note-item

   Let :g:`A'B'C' << A' B' C' >>` be the pedal triangle of :ref:`X_6 <X_6>`. Let :g:`K' <K'>` be :ref:`X_6 <X_6>` of :g:`A'B'C' << A' B' C' >>`. Let :g:`A″B″C″ << A″ B″ C″ >>` be the pedal triangle, wrt :g:`A'B'C' << A' B' C' >>`, of :g:`K' <K'>`. :g:`A″B″C″ << A″ B″ C″ >>` is homothetic to :g:`ABC << A B C >>`, and the center of homothety is :ref:`X_1285 <X_1285>`. (Randy Hutson, March 21, 2019)

.. toctree::
   :hidden:

   code
