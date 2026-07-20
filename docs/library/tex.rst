tex
===

**Documents** · :doc:`Back to the library <index>`

A LaTeX ``.tex`` file name.

.. code-block:: python

   from edify.library import tex

   tex('\\documentclass[aaa]{aaa}eoa')   # True

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: \documentclass[aaa]{aaa}eoa|\documentclass{aaaa}oaiu

   from edify.library import tex
   tex

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^\\documentclass(?:\[[^\]]*\])?\{[^}]+\}.*$

How it reads
------------

.. code-block:: text

   - The text must start with "\documentclass".
   - Optional: "[", then zero or more characters NOT from the set "\]", then "]".
   - Then the text must have "{".
   - Then the text must have one or more characters NOT from the set "}".
   - Then the text must have "}".
   - Then the text must have zero or more characters (any character).

See the other validators in the :doc:`library <index>`.
