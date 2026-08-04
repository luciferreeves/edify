Printable
=========

**Printable** matches a string with no
`control characters <https://en.wikipedia.org/wiki/Control_character>`__ in it — no
codes in ``0x00``–``0x1F``, and no ``0x7F``. Unlike :doc:`ascii` it places no ceiling
on the character range, so text in any script qualifies as long as every character is
displayable.

The construction uses :meth:`~edify.RegexBuilder.assert_not_ahead`: at each position
it asserts the next character is *not* in the control range, then consumes it with
:meth:`~edify.RegexBuilder.any_char`. Repeating that with
:meth:`~edify.RegexBuilder.one_or_more` covers the whole string.

Any script, any symbol
----------------------

.. edify-playground::

   from edify.library import printable

   printable("Hello, World!")   # ASCII text
   printable("héllo")           # accented letters
   printable("日本語")           # another script
   printable("emoji 🎉")         # symbols
   printable("abc 123")         # spaces are printable

Control codes excluded
----------------------

Tabs, newlines, and the null byte are the characters this rules out — the ones that
corrupt display, logs, and delimited formats:

.. edify-playground::

   from edify.library import printable

   printable("clean text")   # no control codes
   printable("a\tb")         # a tab
   printable("a\nb")         # a newline
   printable("a\x00b")       # a null byte
   printable("")             # empty

This is the right check for text destined for a log line, a CSV cell, or a terminal,
where an embedded newline or escape sequence causes real trouble. For the ASCII-only
range see :doc:`ascii`; to require non-ASCII content, :doc:`unicode`.
