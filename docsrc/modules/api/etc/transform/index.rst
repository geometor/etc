etc.transform
=============

.. py:module:: etc.transform


Functions
---------

.. autoapisummary::

   etc.transform.format_rst_header
   etc.transform.wrap_refs
   etc.transform.transform_center_to_rst
   etc.transform.generate_rst_files


Module Contents
---------------

.. py:function:: format_rst_header(title, char='=')

   Create an RST header.


.. py:function:: wrap_refs(text)

   Wrap X(n) references in :ref:`X.n`.


.. py:function:: transform_center_to_rst(data, glossary_terms=None)

   Transform a center data dictionary into an RST string.


.. py:function:: generate_rst_files(centers, output_dir, glossary_terms=None)

   Generate RST files for a list of centers.


