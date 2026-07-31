Grouping atoms
==============

Three fragments matching a bracket-delimited span: ``braces`` for ``{…}``,
``brackets`` for ``[…]``, and ``parens`` for ``(…)``.

Compose them into an anchored pattern rather than calling them directly; see
:doc:`index`.

Delimited spans
---------------

Each matches an opening delimiter, any content that is not the closing delimiter,
and the close:

.. edify-playground::

   from edify import Pattern
   from edify.atoms import braces, brackets, parens

   b = Pattern().start_of_input().use(braces).end_of_input()
   sq = Pattern().start_of_input().use(brackets).end_of_input()
   p = Pattern().start_of_input().use(parens).end_of_input()

   b("{value}")
   b("{}")            # an empty span is fine
   sq("[1, 2, 3]")
   p("(a + b)")
   p("(unclosed")     # both delimiters are required

They do not nest
----------------

This is the limitation to know. Because the content is "anything but the closing
delimiter", the span ends at the **first** close — so a nested pair does not match
as a whole:

.. edify-playground::

   from edify import Pattern
   from edify.atoms import braces

   b = Pattern().start_of_input().use(braces).end_of_input()

   b("{outer}")            # a flat span
   b("{outer {inner}}")    # the span ends at the first }, so anchoring fails

That is not a defect in the atom — matching balanced, arbitrarily nested delimiters
is beyond what a regular expression can express at all. When you need to handle
nesting, parse rather than match.

Used unanchored, though, they are exactly right for pulling the first delimited span
out of a longer string — a template placeholder, a bracketed log field, a
parenthesised aside.

That is the last of the atom groups. Back to :doc:`index`, or on to
:doc:`../beyond/composing` for the other ways to build patterns from parts.
