bump
====

**Software** · :doc:`Back to the library <index>`

A version bump keyword.

.. code-block:: python

   from edify.library import bump

   bump('major')   # True

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: major|minor

   from edify.library import bump
   bump

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^(?:major|minor|patch|premajor|preminor|prepatch|prerelease|release)$

How it reads
------------

.. code-block:: text

   - The text must start with either "major", "minor", "patch", "premajor", "preminor", "prepatch", "prerelease", or "release".

See the other validators in the :doc:`library <index>`.
