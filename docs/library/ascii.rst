ascii
=====

**Text** · :doc:`Back to the library <index>`

ASCII-only text.

.. code-block:: python

   from edify.library import ascii

   ascii('hello')   # True
   ascii('café')   # False

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: hello|ABC123|café|😀

   from edify.library import ascii
   ascii

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^[ -~]+$

How it reads
------------

.. code-block:: text

   - The text must start with one or more characters from " " through "~".

See the other validators in the :doc:`library <index>`.
