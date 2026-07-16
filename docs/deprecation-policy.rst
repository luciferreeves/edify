.. _deprecation-policy:

Deprecation Policy
==================

This policy governs how every removed, renamed, or behavior-changed public API
in Edify **1.0 and later** communicates the change to existing users. It does
not apply to the 0.3 → 1.0 transition, which is a clean redesign with no
deprecation stubs — see :ref:`upgrading-0-3-to-1-0` for that move.

The stub pattern
----------------

When a public symbol is renamed or removed, the old name stays importable for one
minor-release cycle as a **deprecation stub**. The stub forwards to the new
implementation (for a rename) or raises on use (for a removal), and always emits
a :class:`DeprecationWarning` on first use.

.. code-block:: python

    import warnings

    def old_name(*args, **kwargs):
        warnings.warn(
            "old_name is deprecated since 1.1; use new_name. "
            "See https://edify.readthedocs.io/en/latest/upgrading/1.0-to-1.1.html#new-name",
            DeprecationWarning,
            stacklevel=2,
        )
        return new_name(*args, **kwargs)

Message format
--------------

Every deprecation warning message follows this exact shape::

    <name> is deprecated since <version>; use <replacement>. See <docs-url>

* ``<name>`` — the deprecated symbol, spelled exactly as the user typed it.
* ``<version>`` — the release that introduced the deprecation.
* ``<replacement>`` — the symbol to use instead, or a one-clause instruction
  when there is no drop-in replacement.
* ``<docs-url>`` — an absolute URL into the upgrade guide, ending in the frozen
  ``#anchor`` for the relevant section. The anchor is a
  ``.. _label:`` target under ``docs/upgrading/``, decoupled from the heading
  text so rewording a heading never breaks the link.

Warning category and stacklevel
-------------------------------

* The category is always :class:`DeprecationWarning`.
* ``stacklevel=2`` so the warning points at the caller's line, not at the stub.
* Each stub fires its warning **exactly once per call site** — it never suppresses
  or batches, and it never fires at import time.

Removal cadence
---------------

* A symbol deprecated in release ``X.Y`` remains importable through the end of the
  ``X.(Y+1)`` line and is removed no earlier than ``X.(Y+2)``.
* Removals only land in a minor or major release, never a patch release.
* The removal is recorded as a breaking change in the CHANGELOG and gets its own
  section (with a frozen anchor) in the matching upgrade guide.

Behavior-change rule
--------------------

A change to what an existing, unchanged call *returns* or *raises* — with no
change to its name or signature — is a breaking change even though nothing looks
different at the call site. It is documented in the upgrade guide with a
before/after, cross-linked from the CHANGELOG, and (where technically possible)
announced with a :class:`DeprecationWarning` for one cycle before the new
behavior becomes the default.
