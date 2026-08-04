Deprecation policy
==================

Edify follows `semantic versioning <https://semver.org>`_. This page is the
contract for how public API is removed, so you can upgrade with confidence.

What "public" means
-------------------

The public API is everything reachable from the top-level :mod:`edify` package
and :mod:`edify.library`, plus the documented sub-package entry points
(:mod:`edify.result`, :mod:`edify.introspect`, :mod:`edify.serialize`,
:mod:`edify.testing`, and the framework integrations). Anything under a private
module or a name with a leading underscore is internal and may change at any
time.

The committed public-surface snapshot is the source of truth: a change to it in
a pull request is exactly what changed for you.

How things are removed
----------------------

A public name is never deleted outright. It is **deprecated** for one full major
version before removal:

#. In the release that supersedes it, the old name keeps working but emits a
   ``DeprecationWarning`` when used.
#. The warning message states what to use instead and links to the matching
   section of the relevant upgrade guide.
#. The name is removed no earlier than the **next major version**.

So a name deprecated in 1.x keeps working through all of 1.x and is only removed
in 2.0 — you always have a full major cycle to migrate.

Behavior changes
----------------

A change to what an existing call *returns* or *matches* — not just its name — is
treated as breaking and only ships in a major release, documented in the upgrade
guide with a before/after. Bug fixes that bring behavior in line with documented
intent are the exception and can ship in a minor release.

Warnings point at the fix
-------------------------

Every deprecation warning ends in a URL to the upgrade-guide anchor for that
change, so the message you see at runtime links straight to the migration steps.
The docs build verifies that every such anchor actually exists, so those links
never rot.
