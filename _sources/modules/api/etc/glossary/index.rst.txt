etc.glossary
============

.. py:module:: etc.glossary


Functions
---------

.. autoapisummary::

   etc.glossary.extract_glossary_terms
   etc.glossary.generate_glossary_rst
   etc.glossary.wrap_glossary_terms


Module Contents
---------------

.. py:function:: extract_glossary_terms(html_content)

   Extracts glossary terms and definitions from the HTML content.
   Returns a dictionary {term: definition_rst}.


.. py:function:: generate_glossary_rst(terms)

   Generates the content for glossary.rst.


.. py:function:: wrap_glossary_terms(text, terms)

   Wraps occurrences of glossary terms in the text with :term:`term`.
   terms is a list of strings.


