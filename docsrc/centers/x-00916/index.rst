:order: 916
:type: center
:canonical_id: X(916)
:dependencies: X(3), X(4), X(19), X(30), X(48), X(72), X(103), X(185), X(511), X(917), X(1037), X(1069), X(2989), X(8608)

.. _X(916):

X(916) = X(103)-CEVA CONJUGATE OF X(3)
======================================

.. figure:: x-00916.svg
   :alt: X(916) = X(103)-CEVA CONJUGATE OF X(3)
   :align: center

   **X(916) = X(103)-CEVA CONJUGATE OF X(3)** constructed on acute reference triangle :math:`(a, b, c) = (5, 6, 7)` with unit baseline :math:`AB = 1`.

Coordinates
-----------

Trilinears
~~~~~~~~~~

* :math:`f(a,b,c) : f(b,c,a) : f(c,a,b),`, where f(a,b,c) = wb\ :sup:`2` + vc\ :sup:`2` - a(wb + vc), u : v : w = :ref:`X(4) <X(4)>`

Barycentrics
~~~~~~~~~~~~

* :math:`g(a,b,c) : g(b,c,a) : g(c,a,b)`, where g(a,b,c) = af(a,b,c)

Notes
-----

.. container:: note-item

   As the :term:`isogonal conjugate <isogonal-conjugate>` of a point on the circumcircle, :ref:`X(916) <X(916)>` lies on the line at infinity.

Incidence
---------

:ref:`X(916) <X(916)>` lies and on these lines:

{:ref:`3 <X(3)>`, :ref:`48 <X(48)>`}, {:ref:`30 <X(30)>`, :ref:`511 <X(511)>`}, {:ref:`72 <X(72)>`, :ref:`185 <X(185)>`}, {1037, 1069}

Relations
---------

* :ref:`X(916) <X(916)>` = isogonal conjugate of :ref:`X(917) <X(917)>`
* :ref:`X(916) <X(916)>` = :term:`isotomic conjugate <isotomic-conjugate>` of polar conjugate of X(8608)
* :ref:`X(916) <X(916)>` = :ref:`X(19) <X(19)>`-:term:`isoconjugate <isoconjugate>` of X(2989)
* :ref:`X(916) <X(916)>` = :ref:`X(103) <X(103)>`-:term:`Ceva conjugate <ceva-conjugate>` of :ref:`X(3) <X(3)>`

Construction
------------

.. literalinclude:: model.py
   :language: python
