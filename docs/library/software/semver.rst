Semver
======

`Semantic versioning <https://semver.org/>`__ gives a version number meaning: bump
the major for a breaking change, the minor for a feature, the patch for a fix.
**Semver** enforces the specification exactly — three numeric components, with
optional pre-release and build metadata.

Each core component is an :func:`~edify.any_of` of ``0`` or a non-zero-led digit run,
which is how the specification bans leading zeros. The three parts are exposed as
:meth:`~edify.RegexBuilder.named_capture` groups — ``major``, ``minor``, ``patch`` —
so a match can be destructured rather than re-parsed.

The three components
--------------------

All three are required, which is the difference from :doc:`version`:

.. edify-playground::

   from edify.library import semver

   semver("1.2.3")
   semver("0.1.0")
   semver("10.20.30")
   semver("1.2")       # only two components
   semver("1")         # only one

Pre-release and build metadata
------------------------------

A ``-`` introduces a pre-release, which sorts *before* the release; a ``+``
introduces build metadata, which is ignored when comparing:

.. edify-playground::

   from edify.library import semver

   semver("1.2.3-alpha")
   semver("1.2.3-alpha.1")
   semver("1.0.0-rc.1+build.42")   # both
   semver("1.2.3+20240115")        # build metadata alone

No leading zeros, no prefix
---------------------------

.. edify-playground::

   from edify.library import semver

   semver("1.2.3")     # canonical
   semver("01.2.3")    # a leading zero
   semver("v1.2.3")    # the v prefix is not part of semver
   semver("")          # empty

The ``v`` rejection is deliberate: ``v1.2.3`` is a common *tag* name but not a
version string, so strip the prefix before comparing. For the looser form that
accepts it see :doc:`version`; for the increment names, :doc:`bump`.
