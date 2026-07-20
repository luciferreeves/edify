tld
===

``tld`` matches a top-level domain — 2 to 63 letters, like ``com``, ``io``, or
``museum``. It is the trailing component :doc:`domain` requires.

Under the hood it is simply :meth:`~edify.RegexBuilder.between`\ ``(2, 63)`` of a
:meth:`~edify.RegexBuilder.letter` class, anchored with
:meth:`~edify.RegexBuilder.start_of_input` / :meth:`~edify.RegexBuilder.end_of_input`:

.. code-block:: python

   from edify import Pattern

   tld = Pattern().start_of_input().between(2, 63).letter().end_of_input()

which emits:

.. code-block:: text

   ^[a-zA-Z]{2,63}$

Two to sixty-three letters
--------------------------

From the shortest country codes to the long branded and legacy TLDs. Case does
not matter, mirroring DNS case-insensitivity; a single letter is too short, and
digits, hyphens, or a leading dot all fail:

.. code-block:: python

   tld("io")       # True — two-letter minimum
   tld("com")      # True
   tld("museum")   # True — a long gTLD
   tld("COM")      # True — case-insensitive
   tld("c")        # False — a single letter is too short
   tld("c0m")      # False — letters only, no digits
   tld(".com")     # False — the leading dot is not part of the TLD

.. edify-playground::
   :tests: io|com|museum|COM|c|c0m|.com

   from edify.library import tld
   tld

Shape, not registry
-------------------

``tld`` matches the *form* of a TLD — it does not consult the IANA list, so an
unregistered string of letters still passes:

.. code-block:: python

   tld("zzz")   # True — well-formed, though not a real TLD

.. edify-playground::
   :tests: dev|app|zzz|co-op

   from edify.library import tld
   tld

Notes
-----

- ``tld`` is the trailing component of a full :doc:`domain`.
