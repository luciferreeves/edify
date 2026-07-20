ref
===

**Software** · :doc:`Back to the library <index>`

A Git ref name.

.. code-block:: python

   from edify.library import ref

   ref('a0a0a0a')   # True

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: a0a0a0a|refs/tags/oaiu

   from edify.library import ref
   ref

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^(?:[a-f0-9]{7,40}|refs/(?:(?:heads|tags|remotes))/(?:(?!(?:\s|[~^:?*[\\])).)+|(?!(?:\s|[~^:?*[\\/])).(?:(?!(?:\s|[~^:?*[\\])).){0,127})$

How it reads
------------

.. code-block:: text

   - The text must start with either between 7 and 40 of either one character from "a" through "f" or one character from "0" through "9", "refs/", then either "heads", "tags", or "remotes", then "/", then one or more of AssertNotAheadElement, then any single character, or AssertNotAheadElement, then any single character, then between 0 and 127 of AssertNotAheadElement, then any single character.

See the other validators in the :doc:`library <index>`.
