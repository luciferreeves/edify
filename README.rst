========
Edify
========

.. Cover Image
.. image:: https://raw.githubusercontent.com/luciferreeves/edify/main/images/cover.png
    :alt: Cover Image

|

.. image:: https://readthedocs.org/projects/edify/badge/?style=flat&version=latest
    :target: https://edify.readthedocs.io/
    :alt: Documentation Status

.. image:: https://github.com/luciferreeves/edify/actions/workflows/github-actions.yml/badge.svg?branch=main
    :alt: GitHub Actions Build Status
    :target: https://github.com/luciferreeves/edify/actions

.. image:: https://codecov.io/gh/luciferreeves/edify/branch/main/graphs/badge.svg?branch=main
    :alt: Coverage Status
    :target: https://codecov.io/github/luciferreeves/edify

.. .. |version| image:: https://img.shields.io/pypi/v/edify.svg
..     :alt: PyPI Package latest release
..     :target: https://pypi.org/project/edify

.. .. |wheel| image:: https://img.shields.io/pypi/wheel/edify.svg
..     :alt: PyPI Wheel
..     :target: https://pypi.org/project/edify

.. .. |supported-versions| image:: https://img.shields.io/pypi/pyversions/edify.svg
..     :alt: Supported versions
..     :target: https://pypi.org/project/edify

.. .. |supported-implementations| image:: https://img.shields.io/pypi/implementation/edify.svg
..     :alt: Supported implementations
..     :target: https://pypi.org/project/edify

.. .. |commits-since| image:: https://img.shields.io/github/commits-since/luciferreeves/edify/v0.1.0.svg
..     :alt: Commits since latest release
..     :target: https://github.com/luciferreeves/edify/compare/v0.1.0...main



.. end-badges

|

Edify (/ˈɛdɪfaɪ/, "ed-uh-fahy") is a Python library that allows you to easily create regular expressions for matching text in a programmatically-friendly way. It is designed to be used in conjunction with the ``re`` module.

It also allows you to verify a string quickly by providing commonly used regex patterns in its extensive set of built-in patterns. To tap into a pattern, simply import the pattern function from the ``edify.library`` module.

Installation
============

::

    pip install edify

You can also install the in-development version with::

    pip install https://github.com/luciferreeves/edify/archive/main.zip


Why Edify?
===========

Regex is a powerful tool, but its syntax is not very intuitive and can be difficult to build, understand, and use. It gets even more difficult when you have to deal with backtracking, look-ahead, and other features that make regex difficult.

That's where Edify becomes extremely useful. It allows you to create regular expressions in a programmatic way by invoking the ``RegexBuilder`` class [#f1]_. The API uses the `fluent builder pattern <https://en.wikipedia.org/wiki/Fluent_interface>`_, and is completely immutable. It is built to be discoverable and predictable.

- Properties and methods describe what they do in plain English.
- Order matters! Quantifiers are specified before the thing they change, just like in English (e.g. ``RegexBuilder().exactly(5).digit()``).
- If you make a mistake, you'll know how to fix it. Edify will guide you towards a fix if your expression is invalid.
- ``subexpressions`` can be used to create meaningful, reusable components.

Edify turns those complex and unwieldy regexes that appear in code reviews into something that can be read, understood, and **properly reviewed** by your peers - and maintained by anyone!


.. _SuperExpressive: https://github.com/francisrstokes/super-expressive

Quick Start
=============

To get started make sure you have python 3.7 or later installed and then, install Edify from ``pip``::

    pip install edify

Then go on to import the ``RegexBuilder`` class from the ``edify`` module.

Using Pre-Built Patterns
------------------------

The following example recognises and captures any email like ``email@example.com``.

.. code-block:: python


    from edify.library import email

    email_addr = "email@example.com"
    assert email(email_addr) == True


Building Regex Example
----------------------

The following example recognises and captures the value of a 16-bit hexadecimal number like ``0xC0D3``.

.. code-block:: python


    from edify import RegexBuilder

    expr = (
        RegexBuilder()
        .start_of_input()
        .optional().string("0x")
        .capture()
            .exactly(4).any_of()
                .range("A", "F")
                .range("a", "f")
                .range("0", "9")
            .end()
        .end()
        .end_of_input()
        .to_regex()
    )

    """
    Produces the following regular expression:
    re.compile(^(?:0x)?([A-Fa-f0-9]{4})$)
    """

    assert expr.match("0xC0D3")


Documentation
=============

Further API documentation is available on `edify.rftd.io <https://edify.readthedocs.io>`_.

.. rubric:: Footnotes

.. [#f1] ``RegexBuilder`` class based on the `SuperExpressive`_ library.

.. [1]:
