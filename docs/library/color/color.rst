Color
=====

A `CSS colour <https://www.w3.org/TR/css-color-4/>`__ can be written four ways, and
**Color** accepts all of them: a hex value, an ``rgb()``/``rgba()`` call, an
``hsl()``/``hsla()`` call, or a bare keyword such as ``red``.

The four forms are the branches of an :func:`~edify.any_of`, each separately
anchored. The hex branch allows the 3-, 4-, 6-, and 8-digit widths — the short forms
being shorthand, the 4- and 8-digit ones carrying alpha. The functional branches
allow optional percentages and an optional trailing alpha component.

Hex values
----------

All four widths, in either case:

.. edify-playground::

   from edify.library import color

   color("#fff")        # the three-digit shorthand
   color("#ff8800")     # the full six-digit form
   color("#ff8800cc")   # eight digits: with alpha
   color("#FF8800")     # uppercase hex
   color("#gg0000")     # g is not a hex digit

Functional notation
-------------------

``rgb()`` and ``hsl()``, with or without their alpha variants:

.. edify-playground::

   from edify.library import color

   color("rgb(255,136,0)")            # channel values
   color("rgba(255,136,0,0.5)")       # with alpha
   color("hsl(30,100%,50%)")          # hue, saturation, lightness
   color("hsla(30,100%,50%,0.5)")     # with alpha
   color("rgb(255, 136, 0)")          # spaces around commas are fine

Keywords are matched loosely
----------------------------

The keyword branch accepts any run of 3–20 letters rather than checking the named
colour list, so an invented word passes. If that matters, compare against the
keyword list yourself:

.. edify-playground::

   from edify.library import color

   color("red")          # a real keyword
   color("rebeccapurple")  # a longer keyword
   color("notacolor")    # not a real colour, but letter-shaped

Because the keyword branch is permissive and the numeric branches do not range-check
their channels, this validates notation rather than colour validity — ``rgb(999,0,0)``
is well formed but out of gamut. For a single hex-or-keyword value see :doc:`swatch`;
for a list, :doc:`palette`.
