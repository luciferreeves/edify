sso
===

**Auth** · :doc:`Back to the library <index>`

A single-sign-on token.

.. code-block:: python

   from edify.library import sso

   sso('Aa0_Aa0/Aa0.Aa0_Aa0/')   # True

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: Aa0_Aa0/Aa0.Aa0_Aa0/|a0_Aa0/Aa0.Aa0_Aa0/Aa

   from edify.library import sso
   sso

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^[A-Za-z0-9+/=_\-.]{20,2048}$

How it reads
------------

.. code-block:: text

   - The text must start with between 20 and 2048 of either one character from "A" through "Z", one character from "a" through "z", one character from "0" through "9", or one character from the set "+/=_\-.".

See the other validators in the :doc:`library <index>`.
