version
=======

**Software** · :doc:`Back to the library <index>`

A version string.

.. code-block:: python

   from edify.library import version

   version('v123-aA0')   # True

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: v123-aA0|2345.2345

   from edify.library import version
   version

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^v?\d+(?:\.\d+){0,3}(?:[-.+][a-zA-Z0-9\.\-]+)?$

How it reads
------------

.. code-block:: text

   - Optional: "v".
   - Then the text must have one or more digits (0-9).
   - Then the text must have between 0 and 3 of ".", then one or more digits (0-9).
   - Optional: one character from the set "-.+", then one or more of either one character from "a" through "z", one character from "A" through "Z", one character from "0" through "9", ".", or "-".

See the other validators in the :doc:`library <index>`.
