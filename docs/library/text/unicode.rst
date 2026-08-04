Unicode
=======

**Unicode** matches a control-code-free string that *actually uses*
`Unicode <https://home.unicode.org/>`__ beyond ASCII — at least one character above
``0x7F``. It answers a different question from :doc:`printable`: not "is this
displayable?" but "does this need more than ASCII?"

The construction pairs the control-code exclusion of :doc:`printable` with a leading
:meth:`~edify.RegexBuilder.assert_ahead`. The lookahead scans for one character in
the range ``0x80`` upward, and only if it finds one does the rest of the pattern
consume the string.

Text that needs Unicode
-----------------------

.. edify-playground::

   from edify.library import unicode

   unicode("héllo")      # an accented letter
   unicode("日本語")      # a non-Latin script
   unicode("naïve")      # a single accent is enough
   unicode("emoji 🎉")    # a symbol beyond ASCII

Pure ASCII does not qualify
---------------------------

This is the distinguishing rule — plain ASCII is well-formed text, but it is not
*Unicode-requiring* text:

.. edify-playground::

   from edify.library import unicode

   unicode("héllo")     # has a non-ASCII character
   unicode("Hello!")    # pure ASCII
   unicode("abc 123")   # pure ASCII

Control codes still excluded
----------------------------

.. edify-playground::

   from edify.library import unicode

   unicode("日本語")      # clean
   unicode("日本\t語")    # a tab
   unicode("")           # empty

Use this to detect fields that will break an ASCII-only downstream system, or to
confirm a transliteration actually happened. For "displayable in any script" see
:doc:`printable`; for a single writing system, :doc:`script`.
