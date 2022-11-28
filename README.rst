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

.. image:: https://img.shields.io/pypi/v/edify.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/edify

.. image:: https://img.shields.io/pypi/wheel/edify.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/project/edify

.. image:: https://img.shields.io/pypi/pyversions/edify.svg
    :alt: Supported versions
    :target: https://pypi.org/project/edify

.. image:: https://img.shields.io/pypi/implementation/edify.svg
    :alt: Supported implementations
    :target: https://pypi.org/project/edify

.. image:: https://img.shields.io/github/commits-since/luciferreeves/edify/v0.2.1.svg
    :alt: Commits since latest release
    :target: https://github.com/luciferreeves/edify/compare/v0.2.1...main



.. end-badges

|

Edify (/ˈɛdɪfaɪ/, "ed-uh-fahy") is a Python library that allows you to easily create regular expressions for matching text in a programmatically-friendly way. It is designed to be used in conjunction with the ``re`` module.

It also allows you to verify a string quickly by providing commonly used regex patterns in its extensive set of built-in patterns. To tap into a pattern, simply import the pattern function from the ``edify.library`` module.

Quick Start
=============

To get started make sure you have python 3.7 or later installed and then, install Edify from ``pip``:

.. code-block:: bash

    pip install edify

You can also install the in-development version with:

.. code-block:: bash

    pip install https://github.com/luciferreeves/edify/archive/main.zip

Then go on to import the ``RegexBuilder`` class from the ``edify`` module.

Using Pre-Built Patterns
------------------------

The following example recognises and captures any email like ``email@example.com``.

.. code-block:: python


    from edify.library import email

    email_addr = "email@example.com"
    assert email(email_addr) == True


Building Regex Example: Validating 16-bit Hexadecimal Number
------------------------------------------------------------

The following example recognises and captures the value of a 16-bit hexadecimal number like ``0xC0D3``.

.. code-block:: python


    from edify import RegexBuilder

    expr = (
        RegexBuilder()
        .start_of_input()
        .optional().string("0x")                # match an optional "0x" string
        .capture()
            .exactly(4).any_of()                # let x = any characters between (a-f, A-F, and 0-9)
                .range("A", "F")                # now capture exactly 4 such groups of "x"
                .range("a", "f")                # this will give the match for the number like "C0D3"
                .range("0", "9")                # which when combined with "0x" becomes a 16-bit hexadecimal number
            .end()
        .end()
        .end_of_input()
        .to_regex()                             # used to convert to `re` compatible form
    )

    """
    Produces the following regular expression:
    re.compile(^(?:0x)?([A-Fa-f0-9]{4})$)
    
    Using `to_regex_string()` instead of `to_regex()` at the end
    will give the compiled regex string.
    """

    assert expr.match("0xC0D3")
    
Building Regex Example: Validating Signed Integer
-------------------------------------------------

The following example recognises and checks if a number is a valid signed integer or not (eg. ``-45`` or ``+45``).

.. code-block:: python


    from edify import RegexBuilder

    # expression for matching any signed integer. compiles to '^[\+\-]{1}\d+$'
    expr = (
        RegexBuilder()
            .start_of_input()
                .exactly(1).any_of()            # capture either '+' or '-', exactly once
                    .char('+')
                    .char('-')
                .end()
                .one_or_more().digit()          # capture any number of digits
            .end_of_input()
        .to_regex()
    )

    if expr.match('-69'):
        print("Matched")                        # prints matched
    
Building Regex Example: Simple URL Validator
--------------------------------------------

The following example checks if a string is a valid url in the form of ``https://www.example.com/path/to/file.ext``


.. code-block:: python


    from edify import RegexBuilder

    # expression for validating URLs
    validate_urls = (
        RegexBuilder()
            .optional().string('http://')       # look for an optional "http://"
            .optional().string('https://')      # or "https://"
            .one_or_more().any_of()             # let x = any characters between (a-z, 0-9, '-', and '.')
                .range('a', 'z')                # now capture one or more groups of "x"
                .range('0', '9')                # essentially capturing all url patterns in the form of
                .any_of_chars('.-')             # xxx.yyyyyyy.abra-cadabra.com
            .end()
            .at_least(2).any_of()               # this is to make sure we get at least 2 characters in
                .range('a', 'z')                # the end of the string, which would be our domain
            .end()
            .zero_or_more().any_of()
                .range('a', 'z')                # same logic as capturing the url in step 1, but now
                .range('0', '9')                # we are essentially looking for an optional path
                .any_of_chars('/.-_%')          # and we add some more characters supported in path
            .end()
        )

    # compiles to '^(?:http://)?(?:https://)?([a-z0-9\\.]+[a-z]{2,}[a-z0-9/\\.\\-_%]*)$'
    expr = (
        RegexBuilder()
            .ignore_case()                      # case does not matter
            .subexpression(validate_urls)       # directly writing the subexpression works too
        .to_regex()                             # convert to regex finally
    )


    if expr.match('https://SOMETHING.www.exam-ple.com/path/to/file.txt'):
        print("Matched")                        # prints matched


Building Regex Example: Simple Password Validator
-------------------------------------------------
The regular expression below cheks that a password:

* Has minimum 8 characters in length.
* At least one uppercase English letter. 
* At least one lowercase English letter.
* At least one digit. 
* At least one special character from ``#?!@$%^&*-``.

.. code-block:: python

    from edify import RegexBuilder

    # expression for validating passwords - complies to '^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$'
    expr = (
        RegexBuilder()
            .start_of_input()   # asserts position at start of a line
                .assert_ahead() # positive look ahead
                    # matches any character in range 'A' to 'Z' zero and unlimited times,
                    # as few times as possible, expanding as needed (lazy) - matching at least 1 uppercase character
                    .zero_or_more_lazy().any_char().range('A', 'Z')  
                .end()
                .assert_ahead()
                     # at least 1 lowercase character
                    .zero_or_more_lazy().any_char().range('a', 'z')
                .end()
                .assert_ahead()
                    # at least 1 number
                    .zero_or_more_lazy().any_char().range('0', '9') 
                .end()
                .assert_ahead()
                    # at least 1 special character present in the list
                    .zero_or_more_lazy().any_char().any_of_chars('#?!@$%^&*-')   
                .end()
                .at_least(8).any_char() # must be at least 8 characters long
        .end_of_input()
        .to_regex()
    )

    if expr.match('-Secr3t!'):
      print("Matched")  # prints matched


Further Documentation
---------------------

Further API documentation is available on `edify.rftd.io <https://edify.readthedocs.io>`_.

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

.. [1]:

License & Contributing
======================

This project is licensed under `Apache Software License 2.0 <https://github.com/luciferreeves/edify/blob/main/LICENSE>`_. See `Contributing Guidelines <https://github.com/luciferreeves/edify/blob/main/CONTRIBUTING.rst>`_ for information on how to contribute to this project.

Contributors
------------
.. image:: https://contrib.rocks/image?repo=luciferreeves/edify


.. rubric:: Footnotes

.. [#f1] ``RegexBuilder`` class based on the `SuperExpressive`_ library.
