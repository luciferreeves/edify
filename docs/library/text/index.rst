Text
====

Character-class and string-shape checks — the building blocks you reach for when
validating a field that is "just letters" or "just digits", plus the encoding and
script-aware checks. Each validator is a callable :class:`~edify.Pattern`: import
it, call it with a string, get a ``bool``.

.. code-block:: python

   from edify.library import slug, alpha, emoji

   slug("hello-world")   # True
   alpha("Hello")        # True
   emoji("🎉")            # True

.. toctree::
   :hidden:

   alpha
   alphanumeric
   ascii
   base
   emoji
   numeric
   printable
   script
   slug
   unicode
   word

Character classes
-----------------

- :doc:`alpha` — letters only; :doc:`numeric` — digits only.
- :doc:`alphanumeric` — letters and digits; :doc:`word` — those plus underscore.

Encoding and range
------------------

- :doc:`ascii` — printable ASCII; :doc:`printable` — no control codes, any script.
- :doc:`unicode` — a string that actually uses characters beyond ASCII.
- :doc:`base` — a base16/32/58/64 encoded payload.

Scripts and symbols
-------------------

- :doc:`script` — a run of text in a single writing system.
- :doc:`emoji` — one or more emoji characters.

Identifiers
-----------

- :doc:`slug` — a lowercase, hyphen-separated URL segment.
