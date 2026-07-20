component
=========

**Software** · :doc:`Back to the library <index>`

A semantic-version component.

.. code-block:: python

   from edify.library import component

   component('@aa0-/a@123-aA0')   # True

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: @aa0-/a@123-aA0|00@2345.2345

   from edify.library import component
   component

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^(?:@[a-z0-9][a-z0-9\-]*/)?[a-z0-9][a-z0-9\._\-]{0,213}@\d+(?:\.\d+){0,3}(?:[-.+][a-zA-Z0-9\.\-]+)?$

See the other validators in the :doc:`library <index>`.
