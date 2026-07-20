tld
===

**Address** · :doc:`Back to the library <index>`

A top-level domain such as ``com`` or ``io``.

.. code-block:: python

   from edify.library import tld

   tld('aA')   # True

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: aA|AaA

   from edify.library import tld
   tld

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^[a-zA-Z]{2,63}$

How it reads
------------

.. code-block:: text

   - The text must start with between 2 and 63 of either one character from "a" through "z" or one character from "A" through "Z".

See the other validators in the :doc:`library <index>`.
