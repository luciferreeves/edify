package
=======

**Software** · :doc:`Back to the library <index>`

A package name.

.. code-block:: python

   from edify.library import package

   package('@aa0-/a')   # True

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: @aa0-/a|00

   from edify.library import package
   package

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^(?:@[a-z0-9][a-z0-9\-]*/)?[a-z0-9][a-z0-9\._\-]{0,213}$

How it reads
------------

.. code-block:: text

   - Optional: "@", then either one character from "a" through "z" or one character from "0" through "9", then zero or more of either one character from "a" through "z", one character from "0" through "9", or "-", then "/".
   - Then the text must have either one character from "a" through "z" or one character from "0" through "9".
   - Then the text must have between 0 and 213 of either one character from "a" through "z", one character from "0" through "9", ".", "_", or "-".

See the other validators in the :doc:`library <index>`.
