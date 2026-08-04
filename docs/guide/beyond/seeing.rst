Seeing your pattern
===================

A pattern you can read is good; a pattern you can *see* is better. Edify can turn
any compiled pattern into a plain-English explanation, a diagram, or an annotated
regex — three views onto the same expression.

Every compiled :class:`~edify.Regex` carries these as methods, so the common case
is a single call:

.. code-block:: python

   from edify import RegexBuilder

   rx = RegexBuilder().start_of_input().exactly(4).digit().end_of_input().to_regex()

   rx.explain()             # a plain-English description
   rx.visualize()           # an ASCII railroad diagram
   rx.to_verbose_string()   # the annotated re.VERBOSE form

They are all derived from the element tree, not from parsing the regex string —
which is why the descriptions know the difference between ``exactly(4)`` and a
literal ``{4}`` you typed by hand.

Plain-English explanation
-------------------------

:meth:`~edify.Regex.explain` describes the pattern in words, and then shows a few
strings it would accept — generated from the pattern itself, so they cannot be
out of date:

.. code-block:: python

   from edify import RegexBuilder

   rx = RegexBuilder().start_of_input().exactly(4).digit().to_regex()

   print(rx.explain())

.. code-block:: text

   - The text must start with exactly 4 digits (0-9).

   Text this pattern accepts:
       1234
       2345
       3456

The prose follows the structure of the chain, one bullet per top-level element,
and it collapses alternation into the way you would say it out loud:

.. code-block:: python

   from edify import RegexBuilder

   animal = (
       RegexBuilder().start_of_input()
       .any_of().string("cat").string("dog").end()
       .end_of_input()
       .to_regex()
   )
   print(animal.explain())

.. code-block:: text

   - The text must start with either "cat" or "dog".

   Text this pattern accepts:
       cat
       dog

Those sample strings make ``explain`` the fastest sanity check there is: if the
accepted examples are not what you expected, stop and fix the chain. See
:doc:`../practice/debugging` for the rest of that workflow.

.. edify-playground::
   :tests: cat|dog|cats|bird

   from edify import RegexBuilder

   RegexBuilder().start_of_input() \
       .any_of().string("cat").string("dog").end() \
       .end_of_input()

ASCII diagram
-------------

:meth:`~edify.Regex.visualize` draws a railroad diagram — good for dropping into
a terminal, a comment, or a code review:

.. code-block:: python

   from edify import RegexBuilder

   rx = RegexBuilder().start_of_input().exactly(4).digit().to_regex()

   print(rx.visualize())

.. code-block:: text

      +-------+   +------------------+   +----------+   +-----+
      | START |-->| text starts here |-->| 4 digits |-->| END |
      +-------+   +------------------+   +----------+   +-----+

Branching is where the diagram earns its keep. An alternation becomes parallel
tracks, so you can see at a glance which paths exist and where they rejoin:

.. code-block:: python

   from edify import RegexBuilder

   animal = (
       RegexBuilder().start_of_input()
       .any_of().string("cat").string("dog").end()
       .end_of_input()
       .to_regex()
   )
   print(animal.visualize())

.. code-block:: text

                                              +-------+
                                         +--->| "cat" |----+
                                         |    +-------+    |
                                         |                 |
      +-------+   +------------------+   |    +-------+    |   +----------------+   +-----+
      | START |-->| text starts here |-->+--->| "dog" |----+-->| text ends here |-->| END |
      +-------+   +------------------+        +-------+        +----------------+   +-----+

For a polished vector diagram, render it through Graphviz (install it with
``pip install edify[graphviz]``):

.. code-block:: python

   from edify import RegexBuilder

   rx = RegexBuilder().start_of_input().exactly(4).digit().to_regex()

   svg = rx.visualize(format="svg", engine="graphviz")

The ``engine`` argument selects the renderer and ``format`` the output; the
default pair is ``ascii``/``ascii``, which needs no extra dependency at all.

Annotated regex
---------------

:meth:`~edify.Regex.to_verbose_string` emits the raw pattern in ``re.VERBOSE``
form — each token on its own line with a comment — so you can see exactly how
your chain maps to regex syntax:

.. code-block:: python

   from edify import RegexBuilder

   rx = RegexBuilder().start_of_input().exactly(4).digit().to_regex()

   print(rx.to_verbose_string())

.. code-block:: text

   ^                       # start of input
   \d{4}                   # exactly 4
   $                       # end of input

Nesting is indented, and groups get an opening and closing comment naming them —
which makes this the view to reach for when a capture is landing in the wrong
place:

.. code-block:: text

   (?P<area>               # begin group named "area"
     \d{3}                 # exactly 3
   )                       # end group named "area"
   \-                      # literal "\-"
   (?P<line>               # begin group named "line"
     \d{4}                 # exactly 4
   )                       # end group named "line"

.. edify-playground::
   :tests: 123-1234|1234-123|123 1234|abc-defg

   from edify import RegexBuilder

   RegexBuilder().start_of_input() \
       .named_capture("area").exactly(3).digit().end() \
       .char("-") \
       .named_capture("line").exactly(4).digit().end() \
       .end_of_input()

Working from raw elements
-------------------------

Under those methods sit three functions that operate on a pattern's
``.elements`` directly. Reach for them when you have elements in hand — for
example straight from :meth:`~edify.RegexBuilder.from_regex` — rather than a
compiled :class:`~edify.Regex`:

.. code-block:: python

   from edify import RegexBuilder
   from edify.introspect import explain_elements, verbose_elements, visualize_elements

   rx = RegexBuilder().start_of_input().exactly(4).digit().to_regex()

   elements = rx.elements
   explain_elements(elements)
   verbose_elements(elements)
   visualize_elements(elements, format="svg", engine="graphviz")

Because these work on any pattern's elements, they pair with :doc:`from-regex`:
parse a mystery regex, compile it, and ask edify to explain or draw it. This is
the fastest way to understand a regex you inherited:

.. code-block:: python

   from edify import RegexBuilder
   from edify.introspect import explain_elements

   mystery = RegexBuilder.from_regex(r"(?P<area>\d{3})-(?P<line>\d{4})").to_regex()
   print(explain_elements(mystery.elements))

.. code-block:: text

   - The text must contain exactly 3 digits (0-9).
   - Then the text must have "-".
   - Then the text must have exactly 4 digits (0-9).

   Text this pattern accepts:
       123-1234
       234-2345
       345-3456

Which view to use
-----------------

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Reach for
     - When you want to know
   * - ``explain()``
     - What the pattern *means*, and what it accepts.
   * - ``visualize()``
     - What paths exist through it — branches, loops, optional parts.
   * - ``to_verbose_string()``
     - How your chain maps to regex syntax, token by token.

All three are plain text, so any of them can go into a snapshot test and become a
tripwire for unintended change — see :doc:`testing`.

Next: :doc:`serialization`, on saving and loading patterns as portable data.
