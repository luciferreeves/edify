filter
======

**Color** · :doc:`Back to the library <index>`

A CSS filter function.

.. code-block:: python

   from edify.library import filter

   filter('blur(aaa)')   # True

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: blur(aaa)|brightness(aaaa)

   from edify.library import filter
   filter

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^(?:blur|brightness|contrast|grayscale|hue\-rotate|invert|opacity|saturate|sepia|drop\-shadow)\([^)]+\)$

How it reads
------------

.. code-block:: text

   - The text must start with either "blur", "brightness", "contrast", "grayscale", "hue-rotate", "invert", "opacity", "saturate", "sepia", or "drop-shadow".
   - Then the text must have "(".
   - Then the text must have one or more characters NOT from the set ")".
   - Then the text must have ")".

See the other validators in the :doc:`library <index>`.
