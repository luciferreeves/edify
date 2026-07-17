Seeing your pattern
===================

A pattern you can read is good; a pattern you can *see* is better. Edify can turn
any pattern into a plain-English explanation, a diagram, or an annotated regex —
all from the compiled pattern's elements.

Each tool takes the ``.elements`` of a compiled :class:`~edify.Regex`:

.. code-block:: python

   from edify import RegexBuilder

   rx = RegexBuilder().start_of_input().exactly(4).digit().end_of_input().to_regex()
   elements = rx.elements

Plain-English explanation
-------------------------

:func:`edify.introspect.explain_elements` describes the pattern in words, and
even shows a few strings it would accept:

.. code-block:: python

   from edify.introspect import explain_elements

   print(explain_elements(elements))

.. code-block:: text

   - The text must start with exactly 4 digits (0-9).

   Text this pattern accepts:
       1234
       2345
       3456

ASCII diagram
-------------

:func:`edify.introspect.visualize_elements` draws a railroad diagram — great for
dropping into a terminal, a comment, or a code review:

.. code-block:: python

   from edify.introspect import visualize_elements

   print(visualize_elements(elements))

.. code-block:: text

   +-------+   +------------------+   +----------+   +----------------+   +-----+
   | START |-->| text starts here |-->| 4 digits |-->| text ends here |-->| END |
   +-------+   +------------------+   +----------+   +----------------+   +-----+

For a polished vector diagram, render it through Graphviz (install it with
``pip install edify[introspect]``):

.. code-block:: python

   svg = visualize_elements(elements, format="svg", engine="graphviz")

Annotated regex
---------------

:func:`edify.introspect.verbose_elements` emits the raw pattern in
``re.VERBOSE`` form — each token on its own line with a comment — so you can see
exactly how your chain maps to regex syntax:

.. code-block:: python

   from edify.introspect import verbose_elements

   print(verbose_elements(elements))

.. code-block:: text

   ^                       # start of input
   \d{4}                   # exactly 4
   $                       # end of input

Because these work on any compiled pattern, they pair beautifully with
:doc:`from-regex`: parse a mystery regex, compile it, and ask edify to explain or
draw it.

Next: :doc:`serialization`, on saving and loading patterns as portable data.
