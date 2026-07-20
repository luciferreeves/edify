plus
====

**Geo** · :doc:`Back to the library <index>`

An Open Location (plus) code.

.. code-block:: python

   from edify.library import plus

   plus('23+23   eoa')   # True

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: 23+23   eoa|345+345

   from edify.library import plus
   plus

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^[23456789CFGHJMPQRVWX]{2,8}\+[23456789CFGHJMPQRVWX]{2,3}(?:\s+.+)?$

How it reads
------------

.. code-block:: text

   - The text must start with between 2 and 8 characters from the set "23456789CFGHJMPQRVWX".
   - Then the text must have "+".
   - Then the text must have between 2 and 3 characters from the set "23456789CFGHJMPQRVWX".
   - Optional: one or more whitespace characters (space, tab, newline, etc.), then one or more characters (any character).

See the other validators in the :doc:`library <index>`.
