digest
======

**Software** · :doc:`Back to the library <index>`

A content digest such as ``sha256:...``.

.. code-block:: python

   from edify.library import digest

   digest('sha256:aA0aA0aA0aA0aA0aA0aA0aA0aA0aA0aA')   # True

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: sha256:aA0aA0aA0aA0aA0aA0aA0aA0aA0aA0aA|sha512-A0aA0aA0aA0aA0aA0aA0aA0aA0aA0aA0a

   from edify.library import digest
   digest

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^(?:(?:sha256|sha512|sha1|md5|blake2[bs]?))[:-][a-fA-F0-9]{32,128}$

How it reads
------------

.. code-block:: text

   - The text must start with either "sha256", "sha512", "sha1", "md5", or "blake2", then an optional one character from the set "bs".
   - Then the text must have one character from the set ":-".
   - Then the text must have between 32 and 128 of either one character from "a" through "f", one character from "A" through "F", or one character from "0" through "9".

See the other validators in the :doc:`library <index>`.
