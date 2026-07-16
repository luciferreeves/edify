Change fragments
================

Every breaking change to Edify's public surface lands with a **change fragment**
in this directory. Fragments are the single source of truth for the CHANGELOG and
the upgrade guide: the release generator (``tools/changes.py``) concatenates them
into both outputs, then deletes them.

There is no external changelog tooling — the format is a small stdlib-parseable
INI, and the generator is a single stdlib script.

File format
-----------

One file per breaking change, named ``<fragment-id>.rst`` where ``<fragment-id>``
sorts into the order the fragment should appear in the release notes (for
example ``0010-char-class-escape.rst``). The file is an INI document with a single
``[change]`` section:

.. code-block:: ini

    [change]
    anchor = char-class-escape
    heading = Character-class escaping is the minimal correct form
    before = any_of_chars('#?!@$%^&*-')  ->  [\#\?!@$%\^\&\*\-]
    after = any_of_chars('#?!@$%^&*-')  ->  [#?!@$%^&*-]
    context = Only backslash, closing bracket, first-position caret, and interior
        dash are escaped inside a character class; every other metacharacter is a
        literal. Match behavior is unchanged.

Fields
------

``anchor`` (required)
    The frozen ``.. _<anchor>:`` label the upgrade-guide section carries. The
    deprecation-warning URL for this change ends in ``#<anchor>``.

``heading`` (required)
    The one-line human title of the change.

``before`` / ``after`` (optional)
    A before/after pair. Include both or neither. Rendered as a literal block when
    present.

``context`` (required)
    One or two sentences explaining what changed and what the caller should do.
    May span multiple indented lines.

Release flow
------------

On release, ``tools/changes.py`` slots each fragment into the matching section of
``CHANGELOG.rst`` and the active upgrade guide in fragment-id order, then removes
the fragment files. Adding a fragment is the only step a contributor takes; the
generator does the rest.
