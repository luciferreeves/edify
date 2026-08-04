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

.. image:: https://img.shields.io/pypi/v/edify.svg
    :target: https://pypi.org/project/edify
    :alt: PyPI

.. image:: https://img.shields.io/pypi/pyversions/edify.svg
    :target: https://pypi.org/project/edify
    :alt: Python versions

.. image:: https://img.shields.io/badge/license-MIT-blue.svg
    :target: https://github.com/luciferreeves/edify/blob/main/LICENSE
    :alt: MIT License

.. end-badges

|

**Edify builds regular expressions you can actually read.** It's a fluent,
immutable regex builder for Python: you describe a pattern step by step in plain
English, and Edify hands you a compiled regex — one your teammates can review in
a pull request instead of squinting at.

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

Read the chain top to bottom and it says what it does. The quantity comes before
the thing it counts (*exactly four* of a hex digit), every step returns a new
builder so nothing you build ever mutates something you built earlier, and if you
make a mistake Edify raises an error that points at the fix.

Install
=======

Edify requires **Python 3.11+**:

.. code-block:: bash

    pip install edify

Optional extras add the third-party regex engine and the framework integrations:
``edify[regex]``, ``edify[pydantic]``, ``edify[fastapi]``, ``edify[django]``, or
``edify[all]``.

Batteries included
==================

Beyond the builder, Edify ships:

- **228 ready-made validators** — email, URL, semver, IBAN, phone, postal, and
  hundreds more. Each is a callable pattern: ``from edify.library import email``
  then ``email("a@b.com")`` returns ``True``.
- **Introspection** — turn any pattern into a plain-English explanation, an ASCII
  or Graphviz diagram, or an annotated ``re.VERBOSE`` form.
- **Serialization** — round-trip a pattern through a dict or JSON.
- **Integrations** — first-class pydantic, FastAPI, and Django support.

Documentation
=============

The full guide, the searchable library, an interactive in-browser playground,
and the API reference live at `edify.readthedocs.io <https://edify.readthedocs.io>`_.

License and contributing
========================

Edify is released under the `MIT License
<https://github.com/luciferreeves/edify/blob/main/LICENSE>`_. Contributions are
welcome — see `CONTRIBUTING.rst
<https://github.com/luciferreeves/edify/blob/main/CONTRIBUTING.rst>`_ to get set up.
