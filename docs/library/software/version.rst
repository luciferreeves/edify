Version
=======

**Version** is the permissive counterpart to :doc:`semver`, covering the
`version numbering <https://en.wikipedia.org/wiki/Software_versioning>`__ schemes
real projects use: one to four dotted
numeric components, an optional ``v`` prefix, and an optional suffix. It is the
validator for real-world version strings, which frequently ignore the semantic
versioning contract.

The construction is an :meth:`~edify.RegexBuilder.optional` ``v``, digits, then
:meth:`~edify.RegexBuilder.between`\ ``(0, 3)`` further ``.digits`` groups, and an
optional ``-``/``.``/``+`` suffix.

Dotted versions
---------------

Anything from one to four components:

.. edify-playground::

   from edify.library import version

   version("1")          # a single component
   version("1.2")        # two
   version("1.2.3")      # three
   version("1.2.3.4")    # four, as Windows and Java builds use

With a prefix or suffix
-----------------------

.. edify-playground::

   from edify.library import version

   version("v1.2.3")           # the tag-style prefix
   version("1.2.3-beta")       # a pre-release suffix
   version("1.2.3+build.1")    # build metadata
   version("v2.0")             # both conventions at once

Numeric components only
-----------------------

.. edify-playground::

   from edify.library import version

   version("1.2.3")     # valid
   version("1.2.x")     # a wildcard component
   version("latest")    # a tag, not a version
   version("")          # empty

Being permissive has a cost: these strings do not compare reliably, because ``1.2``
and ``1.2.0`` and ``v1.2`` all mean the same release but differ as text. Normalise to
:doc:`semver` when you need ordering.
