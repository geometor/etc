etc.ingest
==========

.. py:module:: etc.ingest


Functions
---------

.. autoapisummary::

   etc.ingest.slugify
   etc.ingest.unique_filename
   etc.ingest.split_html_file
   etc.ingest.ingest_folder


Module Contents
---------------

.. py:function:: slugify(text)

   Simple slugify function to create safe filenames.


.. py:function:: unique_filename(output_folder, base_name)

   Return the filename, allowing overwrites.


.. py:function:: split_html_file(input_path, output_folder)

   Splits a single HTML file into multiple files based on <h3> tags.


.. py:function:: ingest_folder(input_folder, output_folder)

   Ingests all HTML files in the input folder.


