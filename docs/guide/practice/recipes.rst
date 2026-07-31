Recipes
=======

Complete, working patterns for jobs that come up constantly. Each one is a whole
solution — copy it, adjust the parts you need, and read the surrounding prose for
the decision it embodies.

Parse a structured line into fields
-----------------------------------

:meth:`~edify.RegexBuilder.named_capture` gives every part of a match a name, so the
result is a dictionary instead of a tuple of positional groups you have to count.
Named groups survive edits to the pattern; ``m.group(3)`` does not.

.. code-block:: python

   from edify import RegexBuilder

   log_line = (
       RegexBuilder().start_of_input()
       .named_capture("date")
           .exactly(4).digit().char("-").exactly(2).digit().char("-").exactly(2).digit()
       .end()
       .whitespace_char()
       .named_capture("level").one_or_more().range("A", "Z").end()
       .whitespace_char()
       .named_capture("message").one_or_more().any_char().end()
       .end_of_input()
   )

   match = log_line.to_regex().match("2024-05-01 ERROR disk full")
   match.groupdict()
   # {'date': '2024-05-01', 'level': 'ERROR', 'message': 'disk full'}

The emitted regex is ``^(?P<date>\d{4}\-\d{2}\-\d{2})\s(?P<level>[A-Z]+)\s(?P<message>.+)$``.
Note ``range("A", "Z")`` rather than ``letter`` — the level is a fixed vocabulary of
uppercase ASCII, so narrowing is deliberate rather than accidental.

.. edify-playground::
   :tests: 2024-05-01 ERROR disk full|2024-05-01 INFO started|24-5-1 ERROR bad date|2024-05-01 error lowercase

   from edify import RegexBuilder

   RegexBuilder().start_of_input() \
       .named_capture("date") \
           .exactly(4).digit().char("-").exactly(2).digit().char("-").exactly(2).digit() \
       .end() \
       .whitespace_char() \
       .named_capture("level").one_or_more().range("A", "Z").end() \
       .whitespace_char() \
       .named_capture("message").one_or_more().any_char().end() \
       .end_of_input()

Extract every occurrence from a body of text
--------------------------------------------

For extraction you want the *opposite* of a validator: no anchors, so the pattern is
free to match anywhere. :meth:`~edify.Regex.findall` returns the matched strings;
:meth:`~edify.Regex.finditer` returns match objects when you also need positions.

.. code-block:: python

   from edify import RegexBuilder

   hashtag = RegexBuilder().char("#").one_or_more().word().to_regex()

   hashtag.source                                  # '\\#\\w+'
   hashtag.findall("ship #docs and #tests today")  # ['#docs', '#tests']

``word`` here is intentional: hashtags in real text are not ASCII-only, and ``\w``
matches every script. See :doc:`unicode` for when that default is wrong.

.. edify-playground::
   :tests: ship #docs and #tests today|#café|no tags here|#

   from edify import RegexBuilder

   RegexBuilder().char("#").one_or_more().word()

Find repeated words with a back-reference
-----------------------------------------

A back-reference matches *the same text* a earlier group captured — something no
sequence of tokens can express. :meth:`~edify.RegexBuilder.named_back_reference`
refers to a named group, so the intent stays readable:

.. code-block:: python

   from edify import RegexBuilder

   doubled = (
       RegexBuilder().word_boundary()
       .named_capture("w").one_or_more().letter().end()
       .whitespace_char()
       .named_back_reference("w")
       .word_boundary()
       .to_regex()
   )

   doubled.source                            # '\\b(?P<w>[a-zA-Z]+)\\s(?P=w)\\b'
   doubled.sub(r"\g<w>", "this is is fine")  # 'this is fine'

:meth:`~edify.Regex.sub` takes the replacement in Python's own syntax, so
``\g<w>`` puts the single captured word back where the doubled pair was.

.. edify-playground::
   :tests: this is is fine|no repeats here|the the start|is is

   from edify import RegexBuilder

   RegexBuilder().word_boundary() \
       .named_capture("w").one_or_more().letter().end() \
       .whitespace_char() \
       .named_back_reference("w") \
       .word_boundary()

Split on a run of delimiters
----------------------------

:meth:`~edify.Regex.split` breaks a string wherever the pattern matches. Quantifying
the delimiter collapses runs, so empty fields do not appear between adjacent
separators:

.. code-block:: python

   from edify import RegexBuilder

   separators = RegexBuilder().one_or_more().any_of_chars(",;").to_regex()

   separators.source              # '[,;]+'
   separators.split("a,b;;c")     # ['a', 'b', 'c']

Drop the ``one_or_more`` and ``"a,b;;c"`` splits into ``['a', 'b', '', 'c']`` — the
empty string between the two semicolons. Which one you want depends on whether an
empty field is meaningful in your format.

.. edify-playground::
   :tests: a,b;;c|a,,b|abc|,

   from edify import RegexBuilder

   RegexBuilder().one_or_more().any_of_chars(",;")

Build on the library instead of from scratch
--------------------------------------------

An address like ``10.0.0.1:8080`` is two well-specified things joined by a colon.
Rather than re-deriving the octet rules, :meth:`~edify.RegexBuilder.use` drops the
:doc:`../../library/address/ipv4` and :doc:`../../library/address/port` atoms into
your own chain — and captures them under names:

.. code-block:: python

   from edify import RegexBuilder, atoms

   endpoint = (
       RegexBuilder().start_of_input()
       .named_capture("host").use(atoms.ipv4).end()
       .char(":")
       .named_capture("port").use(atoms.port).end()
       .end_of_input()
       .to_regex()
   )

   endpoint.match("10.0.0.1:8080").groupdict()   # {'host': '10.0.0.1', 'port': '8080'}
   endpoint.match("10.0.0.1:99999")              # no match — 99999 exceeds 65535
   endpoint.match("999.1.1.1:80")                # no match — 999 is not an octet

Both atoms carry their real range checks with them: the port branch tops out at
65535, and the octet branch at 255. Writing those by hand is exactly the kind of
detail that gets approximated as ``\d{1,5}`` and then accepts nonsense.

.. edify-playground::
   :tests: 10.0.0.1:8080|127.0.0.1:80|10.0.0.1:99999|999.1.1.1:80

   from edify import RegexBuilder, atoms

   RegexBuilder().start_of_input() \
       .named_capture("host").use(atoms.ipv4).end() \
       .char(":") \
       .named_capture("port").use(atoms.port).end() \
       .end_of_input()

:doc:`../atoms/index` lists every fragment available, and
:doc:`../beyond/composing` covers the composition operators in full.

Where to go next
----------------

- :doc:`performance` — before any of these run against text you do not control.
- :doc:`debugging` — when a recipe almost works.
- :doc:`../../library/index` — 228 validators that already solved the common cases.
