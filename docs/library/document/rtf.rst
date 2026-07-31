RTF
===

`Rich Text Format <https://en.wikipedia.org/wiki/Rich_Text_Format>`__ is plain text
carrying markup as control words, and every RTF document opens with the control word
``{\rtf`` followed by a version digit. **RTF** checks for that prefix.

The construction is the :meth:`~edify.RegexBuilder.string` literal ``{\rtf`` — with
the backslash escaped — then an :meth:`~edify.RegexBuilder.optional`
:meth:`~edify.RegexBuilder.digit`, under :meth:`~edify.RegexBuilder.dot_all` so the
document body may span lines.

The opening control word
------------------------

.. edify-playground::

   from edify.library import rtf

   rtf("{\\rtf1\\ansi Hello}")                  # the usual version 1
   rtf("{\\rtf1\\ansi\\deff0\nsome text\n}")     # spanning lines
   rtf("{\\rtf")                                 # the version digit is optional

The prefix must be exact
------------------------

.. edify-playground::

   from edify.library import rtf

   rtf("{\\rtf1")     # valid
   rtf("{rtf1}")      # missing the backslash
   rtf("\\rtf1")      # missing the brace
   rtf("hello")       # not RTF

RTF is a text format, so this matches its opening rather than a binary signature —
the control-word stream, groups, and destinations are a parser's concern. For the
other portable document format see :doc:`pdf`.
