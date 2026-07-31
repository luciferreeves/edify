Component
=========

**Component** matches a
`package name <https://docs.npmjs.com/cli/commands/npm-install>`__ **pinned to a
version** — ``react@18.2.0``,
``@babel/core@7.23.0`` — the notation an install command or a lockfile entry uses.
The ``@version`` is required, which is the whole difference from :doc:`package`.

The construction is the same optional ``@scope/`` and name as :doc:`package`,
followed by a required :meth:`~edify.RegexBuilder.char`\ ``("@")`` and one to four
dotted numeric components with an :meth:`~edify.RegexBuilder.optional` suffix.

Pinned components
-----------------

.. edify-playground::

   from edify.library import component

   component("react@18.2.0")
   component("lodash@4")             # a partial version pins loosely
   component("@babel/core@7.23.0")   # a scoped package
   component("@scope/pkg@1.0.0-rc.1")  # a pre-release

The version is required
-----------------------

.. edify-playground::

   from edify.library import component

   component("react@18.2.0")   # pinned
   component("react")          # unpinned: see package
   component("react@")         # no version
   component("react@latest")   # a tag, not a numeric version

Note that ``@latest`` and other dist-tags are not matched — this is for *numeric*
pins. Pinning exactly is what makes an install reproducible; a floating range does
not. For the unpinned name see :doc:`package`.
