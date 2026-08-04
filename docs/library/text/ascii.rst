ASCII
=====

**ASCII** matches a string made entirely of printable
`ASCII <https://en.wikipedia.org/wiki/ASCII>`__ characters — the range ``0x20``
(space) through ``0x7E`` (tilde). It is the check for a field that must survive
systems with no Unicode support.

The construction is :meth:`~edify.RegexBuilder.one_or_more` of a
:meth:`~edify.RegexBuilder.range` from space to tilde, anchored end to end. That
range deliberately excludes the control codes below ``0x20`` and the delete
character at ``0x7F``.

The printable range
-------------------

Letters, digits, punctuation, and the space all qualify:

.. edify-playground::

   from edify.library import ascii

   ascii("Hello, World!")   # letters, punctuation, space
   ascii("abc 123")         # digits
   ascii("!@#$%^&*()")      # symbols
   ascii("~")               # the top of the range

Outside the range
-----------------

Anything beyond ``0x7E`` — accented letters, other scripts, emoji — and every
control code are excluded:

.. edify-playground::

   from edify.library import ascii

   ascii("plain text")   # in range
   ascii("héllo")        # é is beyond 0x7E
   ascii("日本語")        # another script
   ascii("a\tb")         # a tab is a control code
   ascii("")             # empty

Note the space *is* included, so this accepts multi-word text. For a check that
allows any script but still bars control codes see :doc:`printable`; for one that
requires non-ASCII, :doc:`unicode`.
