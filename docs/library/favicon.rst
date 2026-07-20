favicon
=======

**Media** · :doc:`Back to the library <index>`

A favicon file name.

.. code-block:: python

   from edify.library import favicon

   favicon('eoa/oaiu/aiueo/favicon.ico')   # True

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: eoa/oaiu/aiueo/favicon.ico|oaiu/aiueo/iue/ueoa/favicon.png

   from edify.library import favicon
   favicon

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^(?:(?:(?![\0-\x1f/\\]).)+/)*favicon\.(?:(?:ico|png|svg|gif))$

How it reads
------------

.. code-block:: text

   - The text must start with zero or more of one or more of AssertNotAheadElement, then any single character, then "/".
   - Then the text must have "favicon".
   - Then the text must have ".".
   - Then the text must have either "ico", "png", "svg", or "gif".

See the other validators in the :doc:`library <index>`.
