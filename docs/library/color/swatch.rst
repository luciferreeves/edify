Swatch
======

A swatch is a single colour chip — the kind stored in a
`design token <https://www.w3.org/community/design-tokens/>`__ or a theme file. **Swatch** is deliberately narrower than :doc:`color`: it accepts a hex value
or a bare keyword, but not the functional ``rgb()`` and ``hsl()`` notations, because
a stored swatch is normally one flat literal.

The two forms are branches of an :func:`~edify.any_of`: ``#`` followed by 3 to 8 hex
digits, or a run of 3–20 letters via :meth:`~edify.RegexBuilder.between`.

Hex and keyword
---------------

.. edify-playground::

   from edify.library import swatch

   swatch("#fff")        # shorthand hex
   swatch("#ff8800")     # full hex
   swatch("#ff8800cc")   # hex with alpha
   swatch("red")         # a keyword
   swatch("teal")        # another keyword

No functional notation
----------------------

This is what separates a swatch from a general colour value:

.. edify-playground::

   from edify.library import swatch

   swatch("#ff8800")               # a literal
   swatch("rgb(255,136,0)")        # functional: use color
   swatch("hsl(30,100%,50%)")      # functional: use color
   swatch("#gg0000")               # not hex

As with :doc:`color`, the keyword branch matches letter-shaped words rather than the
named-colour list. For several swatches at once see :doc:`palette`.
