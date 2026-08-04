Filter
======

A `CSS filter <https://www.w3.org/TR/filter-effects-1/>`__ function applies a
graphical effect to an element — blurring it, shifting its hue, adding a shadow.
**Filter** matches a single such call, from the fixed set the specification defines.

The function name is an :func:`~edify.any_of` over the ten filter primitives,
followed by a parenthesised argument. Because the name is drawn from a closed list,
an invented function is rejected — unlike the loosely matched colour keywords in
:doc:`color`.

The filter functions
--------------------

.. edify-playground::

   from edify.library import filter

   filter("blur(4px)")            # length argument
   filter("brightness(150%)")     # percentage
   filter("contrast(2)")          # a plain number
   filter("grayscale(100%)")
   filter("hue-rotate(90deg)")    # an angle
   filter("saturate(150%)")
   filter("sepia(60%)")
   filter("invert(1)")
   filter("opacity(0.5)")

Multi-argument shadows
----------------------

``drop-shadow()`` takes several space-separated values rather than one:

.. edify-playground::

   from edify.library import filter

   filter("drop-shadow(0 0 2px red)")
   filter("drop-shadow(2px 4px 6px rgba(0,0,0,0.4))")

A closed set of names
---------------------

Only the specified primitives match, and the call must be complete:

.. edify-playground::

   from edify.library import filter

   filter("blur(4px)")       # a real primitive
   filter("sharpen(4px)")    # not a CSS filter
   filter("blur")            # no argument
   filter("blur(4px")        # unclosed

It matches the function and its argument shape, not that the units suit the
primitive — ``blur(90deg)`` is well formed but meaningless. For the other CSS
function family see :doc:`gradient`.
