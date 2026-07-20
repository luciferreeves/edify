image
=====

**Software** · :doc:`Back to the library <index>`

A container image reference.

.. code-block:: python

   from edify.library import image


Edit the string, or the pattern itself:

.. edify-playground::

   from edify.library import image
   image

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^(?:(?:[a-z0-9\.\-]+(?::\d+)?/)?[a-z0-9]+(?:[._-][a-z0-9]+)*)(?:/[a-z0-9]+(?:[._-][a-z0-9]+)*)*(?::[a-zA-Z0-9_][a-zA-Z0-9\._\-]{0,127})?(?:@sha256:[a-f0-9]{64})?$

See the other validators in the :doc:`library <index>`.
