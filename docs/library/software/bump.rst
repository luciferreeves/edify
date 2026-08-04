Bump
====

**Bump** matches the name of a release increment — the word you pass to a release
tool to say *which* part of a `semantic version <https://semver.org/>`__ should move.

The construction is a single :func:`~edify.any_of` over the eight names release
tooling uses: the three core increments, their pre-release forms, and the two
release verbs.

Increment names
---------------

.. edify-playground::

   from edify.library import bump

   bump("major")     # a breaking change
   bump("minor")     # a new feature
   bump("patch")     # a fix

Pre-release increments
----------------------

.. edify-playground::

   from edify.library import bump

   bump("premajor")
   bump("preminor")
   bump("prepatch")
   bump("prerelease")   # advance an existing pre-release
   bump("release")      # promote a pre-release to final

A closed set
------------

.. edify-playground::

   from edify.library import bump

   bump("patch")    # a known increment
   bump("Major")    # names are lowercase
   bump("hotfix")   # not an increment name
   bump("1.2.3")    # a version, not an increment
   bump("")         # empty

For the version these names operate on see :doc:`semver`.
