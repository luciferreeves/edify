Gradient
========

A `CSS gradient <https://www.w3.org/TR/css-images-3/#gradients>`__ is an image
function — ``linear-gradient()``, ``radial-gradient()``, or ``conic-gradient()`` —
whose arguments describe direction and colour stops. **Gradient** matches the
function call, including the nested parentheses that appear when a stop is written
in functional colour notation.

The keyword is an :func:`~edify.any_of` over the three types, followed by
``-gradient(``. The argument list allows one level of nested parentheses, which is
what lets ``rgba(...)`` stops sit inside without ending the call early.

The three types
---------------

.. edify-playground::

   from edify.library import gradient

   gradient("linear-gradient(red, blue)")
   gradient("radial-gradient(circle, #fff, #000)")
   gradient("conic-gradient(from 0deg, red, blue)")
   gradient("linear-gradient(to right, red 0%, blue 100%)")

Nested colour functions
-----------------------

A stop written as ``rgba()`` or ``hsl()`` nests one level deep, and the pattern
tracks it:

.. edify-playground::

   from edify.library import gradient

   gradient("linear-gradient(rgba(255,0,0,0.5), blue)")
   gradient("radial-gradient(hsl(30,100%,50%), #000)")

The call must be complete
-------------------------

An unclosed call or a bare keyword is not a gradient, and a plain colour belongs to
:doc:`color`:

.. edify-playground::

   from edify.library import gradient

   gradient("linear-gradient(red, blue)")   # complete
   gradient("linear-gradient(red, blue")    # unclosed
   gradient("linear-gradient")              # no arguments
   gradient("red")                          # a plain colour

It matches the function's shape rather than validating the stops, angles, or units
inside it. For individual colours see :doc:`color`, and for the other CSS function
family, :doc:`filter`.
