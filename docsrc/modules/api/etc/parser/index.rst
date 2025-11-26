etc.parser
==========

.. py:module:: etc.parser


Functions
---------

.. autoapisummary::

   etc.parser.remove_tags
   etc.parser.clean_text
   etc.parser.parse_coordinates
   etc.parser.parse_h3
   etc.parser.parse_notes
   etc.parser.parse_center


Module Contents
---------------

.. py:function:: remove_tags(text)

   Remove HTML tags from text.


.. py:function:: clean_text(text)

   Clean up text by removing tags and extra whitespace.


.. py:function:: parse_coordinates(coord_type, html)

   Parse coordinates (Trilinears, Barycentrics, etc.) from the HTML.
   Looks for patterns like "Trilinears ... <br>"


.. py:function:: parse_h3(html)

   Parse the <h3> tag to get the key (X number) and title.


.. py:function:: parse_notes(html)

   Extract paragraphs as notes.


.. py:function:: parse_center(html_content)

   Main function to parse a center's HTML content.


