semver
======

**Software** · :doc:`Back to the library <index>`

A semantic version such as ``1.2.3``.

.. code-block:: python

   from edify.library import semver

   semver('1.2.3')   # True
   semver('1.2')   # False

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: 1.2.3|0.1.0|2.0.0-rc.1|1.2|v1

   from edify.library import semver
   semver

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^(?P<major>(?:[1-9]\d*|[0]))\.(?P<minor>(?:[1-9]\d*|[0]))\.(?P<patch>(?:[1-9]\d*|[0]))(?:\-(?P<prerelease>(?:[1-9]\d*|\d*[a-zA-Z\-][0-9a-zA-Z\-]*|[0])(?:\.(?:[1-9]\d*|\d*[a-zA-Z\-][0-9a-zA-Z\-]*|[0]))*))?(?:\+(?P<buildmetadata>[0-9a-zA-Z\-]+(?:\.[0-9a-zA-Z\-]+)*))?$

See the other validators in the :doc:`library <index>`.
