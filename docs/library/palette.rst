palette
=======

**Color** · :doc:`Back to the library <index>`

A palette of colors.

.. code-block:: python

   from edify.library import palette

   palette('#0Aa   ,   #0Aa')   # True

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: #0Aa   ,   #0Aa|oaiu    ,    oaiu     ,     #a0Aa0

   from edify.library import palette
   palette

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^(?:(?:\#[0-9A-Fa-f]{3,8})|[a-zA-Z]{3,20})(?:\s*,\s*(?:(?:\#[0-9A-Fa-f]{3,8})|[a-zA-Z]{3,20})){1,15}$

See the other validators in the :doc:`library <index>`.
