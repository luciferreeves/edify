Flags
=====

Flags in Edify are same as the flags in ``re`` module. Edify supports the following flags:
    - ``A``: ASCII (standard ASCII) character
    - ``D``: DEBUG, returns ``re.DEBUG``
    - ``I``: Ignore Case
    - ``M``: Multi Line
    - ``S``: Dot All
    - ``X``: Verbose

To learn more about the flags, please refer to the ``re`` module documentation. If you wish to use the ``/g`` or any other unsupported flag, you can use the ``re.search`` or ``re.match`` methods, according to your needs. If you need to support extra flags, you can try looking at the `regex <https://pypi.python.org/pypi/regex>`_ package. To get started, import the ``RegexBuilder`` class::

    from edify import RegexBuilder


ASCII Only Matching
--------------------

Make ``\w``, ``\W``, ``\b``, ``\B``, ``\d``, ``\D``, ``\s``, and ``\S`` perform ASCII-only matching instead of full Unicode matching. This is only meaningful for Unicode patterns, and is ignored for byte patterns. Corresponds to the inline flag ``(?a)``.

Example
^^^^^^^

.. code-block:: python

    # returns re.compile('hello', re.ASCII)
    expr = RegexBuilder().ascii_only().string('hello').to_regex()

Display Debug Information
-------------------------
Display debug information about compiled expression. No corresponding inline flag.

Example
^^^^^^^

.. code-block:: python

    # returns re.compile('hello', re.DEBUG)
    expr = RegexBuilder().debug().string('hello').to_regex()


Ignore Case
------------
Perform case-insensitive matching; expressions like ``[A-Z]`` will also match lowercase letters. Full Unicode matching (such as ``Ü`` matching ``ü``) also works unless the ``re.ASCII`` flag is used to disable non-ASCII matches. Corresponds to the inline flag ``(?i)``.

Example
^^^^^^^

.. code-block:: python

    # returns re.compile('hello', re.IGNORECASE)
    expr = RegexBuilder().ignore_case().string('hello').to_regex()


Multi Line
----------
When specified, the pattern character ``'^'`` matches at the beginning of the string and at the beginning of each line (immediately following each newline); and the pattern character ``'$'`` matches at the end of the string and at the end of each line (immediately preceding each newline). By default, ``'^'`` matches only at the beginning of the string, and ``'$'`` only at the end of the string and immediately before the newline (if any) at the end of the string. Corresponds to the inline flag ``(?m)``.


Example
^^^^^^^

.. code-block:: python

    # returns re.compile('hello', re.MULTILINE)
    expr = RegexBuilder().multi_line().string('hello').to_regex()


Dot All
-------

Make the ``'.'`` special character match any character at all, including a newline; without this flag, ``'.'`` will match anything *except* a newline. Corresponds to the inline flag ``(?s)``.


Example
^^^^^^^

.. code-block:: python

    # returns re.compile('hello', re.DOTALL)
    expr = RegexBuilder().dot_all().string('hello').to_regex()


Verbose
-------
This workd same as the ``re.VERBOSE`` flag, which allows you to write regular expressions that look nicer and are more readable by allowing you to visually separate logical sections of the pattern and add comments. However, this flag is basically rendered useless with Edify, but it is still available for use to keep the API consistent with the ``re`` module. Corresponds to the inline flag ``(?x)``.


Example
^^^^^^^

.. code-block:: python

    # returns re.compile('hello', re.VERBOSE)
    expr = RegexBuilder().verbose().string('hello').to_regex()
