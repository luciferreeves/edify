git
===

**Software** · :doc:`Back to the library <index>`

A Git commit hash or ref.

.. code-block:: python

   from edify.library import git

   git('a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2')   # True
   git('!!')   # False

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2|!!| 

   from edify.library import git
   git

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^[a-f0-9]{7,40}$

How it reads
------------

.. code-block:: text

   - The text must start with between 7 and 40 of either one character from "a" through "f" or one character from "0" through "9".

See the other validators in the :doc:`library <index>`.
