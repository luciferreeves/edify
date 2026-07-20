swatch
======

**Color** · :doc:`Back to the library <index>`

A single color swatch.

.. code-block:: python

   from edify.library import swatch

   swatch('#0Aa')   # True

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: #0Aa|oaiu

   from edify.library import swatch
   swatch

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^(?:(?:\#[0-9A-Fa-f]{3,8})|[a-zA-Z]{3,20})$

How it reads
------------

.. code-block:: text

   - The text must start with either "#", then between 3 and 8 of either one character from "0" through "9", one character from "A" through "F", or one character from "a" through "f" or between 3 and 20 letters (a-z or A-Z).

See the other validators in the :doc:`library <index>`.
