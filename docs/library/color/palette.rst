Palette
=======

A `palette <https://www.w3.org/TR/css-color-4/#named-colors>`__ is a comma-separated
list of swatches — the shape a theme file or a chart configuration uses to declare
its colour ramp. **Palette** requires **at least two**
entries, each a hex value or a keyword, which is what distinguishes a palette from a
single :doc:`swatch`.

The construction is a swatch followed by
:meth:`~edify.RegexBuilder.one_or_more` comma-and-swatch groups, with optional
whitespace around each comma.

Lists of colours
----------------

Hex, keywords, and a mix of both:

.. edify-playground::

   from edify.library import palette

   palette("#ff0000, #00ff00, #0000ff")   # a hex ramp
   palette("red, green, blue")            # keywords
   palette("#fff,#000")                   # no spaces
   palette("red, #00ff00")                # mixed

Two or more entries
-------------------

A single colour is a swatch, not a palette:

.. edify-playground::

   from edify.library import palette

   palette("red, blue")   # two entries
   palette("red")         # one entry: use swatch
   palette("#ff0000")     # likewise

Literals only
-------------

Like :doc:`swatch`, entries are hex or keywords — functional notation contains
commas of its own and would make the list ambiguous:

.. edify-playground::

   from edify.library import palette

   palette("red, blue")                       # literals
   palette("rgb(255,0,0), rgb(0,0,255)")      # functional entries
   palette("red,, blue")                      # an empty entry

For one colour see :doc:`swatch`, and for the full notation set, :doc:`color`.
