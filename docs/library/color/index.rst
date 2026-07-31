Color
=====

CSS colour values and the constructs built from them — single colours, gradients,
filter functions, and lists of swatches. Each validator is a callable
:class:`~edify.Pattern`: import it, call it with a string, get a ``bool``.

.. code-block:: python

   from edify.library import color, gradient, filter

   color("#ff8800")                          # True
   gradient("linear-gradient(red, blue)")    # True
   filter("blur(4px)")                       # True

.. toctree::
   :hidden:

   color
   filter
   gradient
   palette
   swatch

Single colours
--------------

- :doc:`color` — a hex, ``rgb()``, or ``hsl()`` value.
- :doc:`swatch` — one hex value or a named colour.

Collections and functions
-------------------------

- :doc:`palette` — a comma-separated list of swatches.
- :doc:`gradient` — a ``linear-``, ``radial-``, or ``conic-gradient()``.
- :doc:`filter` — a CSS filter function such as ``blur()`` or ``saturate()``.
