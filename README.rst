=====
Edify
=====

.. image:: https://raw.githubusercontent.com/luciferreeves/edify/main/images/cover.png
    :alt: Edify — simple regular expressions

|

.. image:: https://readthedocs.org/projects/edify/badge/?style=flat&version=latest
    :target: https://edify.readthedocs.io/
    :alt: Documentation

.. image:: https://github.com/luciferreeves/edify/actions/workflows/github-actions.yml/badge.svg?branch=main
    :target: https://github.com/luciferreeves/edify/actions
    :alt: Build status

.. image:: https://codecov.io/gh/luciferreeves/edify/branch/main/graph/badge.svg?branch=main
    :target: https://codecov.io/github/luciferreeves/edify
    :alt: Coverage

.. image:: https://img.shields.io/pypi/v/edify
    :target: https://pypi.org/project/edify
    :alt: PyPI

.. image:: https://img.shields.io/pypi/pyversions/edify
    :target: https://pypi.org/project/edify
    :alt: Python versions

.. image:: https://img.shields.io/badge/license-MIT-blue
    :target: https://github.com/luciferreeves/edify/blob/main/LICENSE
    :alt: MIT License

.. end-badges

|

**Edify builds regular expressions you can actually read.** It's a fluent,
immutable regex builder for Python: you describe a pattern step by step in plain
English, and Edify hands you a compiled regex — one your teammates can review in
a pull request instead of squinting at.

Why Edify
=========

A regular expression is easy to write and hard to read. Six months later nobody
remembers what ``^(?:0x)?([0-9a-fA-F]{4})$`` was meant to accept, and the person
reviewing the change that touches it has no way to be sure either. The syntax
gives you nowhere to put a name, a comment, or a seam.

Edify moves the pattern into ordinary Python, where all three fit:

- Methods say what they do. ``.one_or_more().digit()`` needs no decoding.
- The quantity comes before the thing it counts, the way you say it aloud —
  ``.exactly(4).digit()`` is *exactly four digits*.
- Every call returns a new builder, so a pattern you share can be extended in
  two directions without either one disturbing the other.
- A mistake raises an error that points at the call that caused it and names the
  fix, rather than emitting a regex that is subtly wrong.

A first pattern
===============

.. code-block:: python

    from edify import RegexBuilder

    # A 16-bit hex literal like "0xC0DE" — with the four hex digits captured.
    hex_literal = (
        RegexBuilder()
        .start_of_input()
        .optional().string("0x")
        .capture()
            .exactly(4).any_of().range("0", "9").range("a", "f").range("A", "F").end()
        .end()
        .end_of_input()
    )

    hex_literal.to_regex_string()   # '^(?:0x)?([0-9a-fA-F]{4})$'
    hex_literal.test("0xC0DE")      # True
    hex_literal.test("0xZZZZ")      # False

Read the chain top to bottom and it tells you what it accepts.

Patterns you don't have to write
================================

Edify ships 228 ready-made validators. Each is a callable pattern, so checking a
value is a function call:

.. code-block:: python

    from edify.library import email, ipv4, semver

    email("a@b.com")      # True
    semver("1.4.0")       # True
    ipv4("10.0.0.1")      # True
    ipv4("999.1.1.1")     # False — the octet range is enforced

They are assembled from 83 named fragments you can build with too, so a pattern
of your own inherits the same range checks rather than approximating them:

.. code-block:: python

    from edify import Pattern, atoms

    endpoint = (
        Pattern().start_of_input()
        .named_capture("host").use(atoms.ipv4).end()
        .char(":")
        .named_capture("port").use(atoms.port).end()
        .end_of_input()
    )

    endpoint.to_regex().match("10.0.0.1:8080").groupdict()
    # {'host': '10.0.0.1', 'port': '8080'}
    endpoint("10.0.0.1:99999")   # False — 99999 is not a port

Ask a pattern what it means
===========================

Because Edify keeps the structure rather than a string, it can describe a
pattern back to you — in prose, as a diagram, or as an annotated verbose regex:

.. code-block:: python

    from edify import RegexBuilder

    year = RegexBuilder().start_of_input().exactly(4).digit().end_of_input()
    print(year.to_regex().explain())

    # - The text must start with exactly 4 digits (0-9).
    #
    # Text this pattern accepts:
    #     1234

That same structure is what lets Edify warn you at build time about a pattern
shaped for catastrophic backtracking — and the warning names the fix, because
atomic groups and possessive quantifiers are chain methods like everything else.
It is also what lets a pattern round-trip through JSON.

Install
=======

Edify requires **Python 3.11+**:

.. code-block:: bash

    pip install edify

Optional extras add the alternate regex engine and the framework integrations:
``edify[regex]``, ``edify[pydantic]``, ``edify[fastapi]``, ``edify[django]``, or
``edify[all]``.

Also in the box
===============

- **Introspection** — a plain-English explanation, an ASCII or rendered diagram,
  or an annotated ``re.VERBOSE`` form of any pattern.
- **Serialization** — round-trip a pattern through a dict or JSON and keep a
  first-class pattern on the other side, not a flattened string.
- **Integrations** — pydantic, FastAPI, and Django validators from a pattern.
- **Testing helpers** — assert a pattern's contract beside its definition, and
  snapshot what it emits.
- **Reverse parsing** — turn an existing regex string back into a chain and read
  what it does.
- **Unicode-aware classes** — say "any letter" and mean it, in any script, rather
  than settling for ``[a-zA-Z]`` or a ``\w`` that also admits digits.

Documentation
=============

`edify.readthedocs.io <https://edify.readthedocs.io>`_ has the guide, a page for
every validator, and the full API reference. Examples throughout the site are
live — edit the chain and the emitted regex and match results update as you
type, with Edify running in your browser.

License and contributing
========================

Edify is released under the `MIT License
<https://github.com/luciferreeves/edify/blob/main/LICENSE>`_. Contributions are
welcome — see `CONTRIBUTING.rst
<https://github.com/luciferreeves/edify/blob/main/CONTRIBUTING.rst>`_ to get set up.
