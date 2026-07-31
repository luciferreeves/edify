Text atoms
==========

Fourteen fragments for characters, classes, and simple word shapes — the pieces
behind the :doc:`../../library/text/index` validators.

Compose them into an anchored pattern rather than calling them directly; see
:doc:`index`.

Single characters
-----------------

``letter``, ``lower``, ``upper``, and ``alnum`` each match exactly one character.
``space`` matches one whitespace character.

.. edify-playground::

   from edify import Pattern
   from edify.atoms import letter, lower, upper, alnum

   one_letter = Pattern().start_of_input().use(letter).end_of_input()
   one_lower = Pattern().start_of_input().use(lower).end_of_input()
   one_upper = Pattern().start_of_input().use(upper).end_of_input()
   one_alnum = Pattern().start_of_input().use(alnum).end_of_input()

   one_letter("a")     # a single letter
   one_letter("ab")    # not two
   one_lower("a")
   one_lower("A")      # case matters
   one_upper("A")
   one_alnum("7")      # digits count as alphanumeric

Runs and ranges
---------------

``word`` matches a run of word characters, ``ascii`` and ``printable`` single
characters within their ranges, and ``line`` everything up to a line break.

.. edify-playground::

   from edify import Pattern
   from edify.atoms import word, printable, line

   w = Pattern().start_of_input().use(word).end_of_input()
   p = Pattern().start_of_input().use(printable).end_of_input()
   ln = Pattern().start_of_input().use(line).end_of_input()

   w("hello_world")    # letters, digits, underscore
   w("hello world")    # a space is not a word character
   p("~")              # inside the printable range
   ln("a whole line")  # anything but a newline

Word shapes
-----------

``slug`` is a lowercase hyphenated identifier; ``quoted`` is a double-quoted span.

.. edify-playground::

   from edify import Pattern
   from edify.atoms import slug, quoted

   s = Pattern().start_of_input().use(slug).end_of_input()
   q = Pattern().start_of_input().use(quoted).end_of_input()

   s("hello-world")
   s("Hello-World")     # slugs are lowercase
   q('"a value"')       # quotes included
   q("a value")         # unquoted

Truthy words
------------

Three atoms cover the ways a boolean is spelled in configuration and data files.
``boolean`` is the widest, accepting on/off as well.

.. edify-playground::

   from edify import Pattern
   from edify.atoms import boolean, truefalse, yesno

   b = Pattern().start_of_input().use(boolean).end_of_input()
   tf = Pattern().start_of_input().use(truefalse).end_of_input()
   yn = Pattern().start_of_input().use(yesno).end_of_input()

   b("true")
   b("on")        # boolean accepts on/off
   tf("on")       # truefalse does not
   tf("TRUE")     # but does accept any case spelling
   yn("y")        # single letters count
   yn("maybe")

Next: :doc:`encodings`.
