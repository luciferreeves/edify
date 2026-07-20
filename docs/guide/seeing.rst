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

Plain-English explanation
-------------------------

:meth:`~edify.Regex.explain` describes the pattern in words, and even shows a few
strings it would accept:

.. code-block:: python

   print(rx.explain())

.. code-block:: text

   - The text must start with exactly 4 digits (0-9).

   Text this pattern accepts:
       1234
       2345
       3456

ASCII diagram
-------------

:meth:`~edify.Regex.visualize` draws a railroad diagram — great for dropping into
a terminal, a comment, or a code review:

.. code-block:: python

   print(rx.visualize())

.. code-block:: text

   +-------+   +------------------+   +----------+   +----------------+   +-----+
   | START |-->| text starts here |-->| 4 digits |-->| text ends here |-->| END |
   +-------+   +------------------+   +----------+   +----------------+   +-----+

For a polished vector diagram, render it through Graphviz (install it with
``pip install edify[graphviz]``):

.. code-block:: python

   svg = rx.visualize(format="svg", engine="graphviz")

Annotated regex
---------------

:meth:`~edify.Regex.to_verbose_string` emits the raw pattern in ``re.VERBOSE``
form — each token on its own line with a comment — so you can see exactly how
your chain maps to regex syntax:

.. code-block:: python

   print(rx.to_verbose_string())

.. code-block:: text

   ^                       # start of input
   \d{4}                   # exactly 4
   $                       # end of input

Working from raw elements
-------------------------

Under those methods sit three functions that operate on a pattern's
``.elements`` directly. Reach for them when you have elements in hand — for
example straight from :meth:`~edify.RegexBuilder.from_regex` — rather than a
compiled :class:`~edify.Regex`:

.. code-block:: python

   from edify.introspect import explain_elements, visualize_elements, verbose_elements

   elements = rx.elements
   explain_elements(elements)
   visualize_elements(elements, format="svg", engine="graphviz")
   verbose_elements(elements)

Because these work on any pattern's elements, they pair beautifully with
:doc:`from-regex`: parse a mystery regex, compile it, and ask edify to explain or
draw it.

.. code-block:: python

   from edify import RegexBuilder
   from edify.introspect import explain_elements

   mystery = RegexBuilder.from_regex(r"(?P<area>\d{3})-(?P<line>\d{4})").to_regex()
   print(explain_elements(mystery.elements))

Next: :doc:`serialization`, on saving and loading patterns as portable data.
