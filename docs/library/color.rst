color
=====

**Color** · :doc:`Back to the library <index>`

A CSS color — hex, ``rgb()``, or a named color.

.. code-block:: python

   from edify.library import color

   color('#a3c113')   # True
   color('###')   # False

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: #a3c113|rgb(1,2,3)|###

   from edify.library import color
   color

Pattern
-------

The regex this validator emits:

.. code-block:: text

   (?:^\#(?:[0-9A-Fa-f]{3,4}|[0-9A-Fa-f]{6}|[0-9A-Fa-f]{8})$|^rgba?\(\s*\d{1,3}%?\s*,\s*\d{1,3}%?\s*,\s*\d{1,3}%?(?:\s*,\s*(?:\d|[\.])+)?\s*\)$|^hsla?\(\s*\d{1,3}(?:deg)?\s*,\s*\d{1,3}%\s*,\s*\d{1,3}%(?:\s*,\s*(?:\d|[\.])+)?\s*\)$|^[a-zA-Z]{3,20}$)

See the other validators in the :doc:`library <index>`.
