password
========

**Auth** · :doc:`Back to the library <index>`

A password; the strength policy is configurable via keyword arguments.

.. code-block:: python

   from edify.library import password


Edit the string, or the pattern itself:

.. edify-playground::

   from edify.library import password
   password

Pattern
-------

The regex this validator emits:

.. code-block:: text

   (?:)

How it reads
------------

.. code-block:: text

   This pattern is empty and matches an empty string.

See the other validators in the :doc:`library <index>`.
