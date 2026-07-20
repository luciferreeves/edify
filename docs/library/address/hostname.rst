hostname
========

.. edify-validator:: hostname

``hostname`` matches an RFC 1123 hostname. It is close to :doc:`domain`, with two
differences: a bare single label such as ``localhost`` is valid, and there is no
letters-only TLD requirement.

Under the hood a leading :meth:`~edify.RegexBuilder.assert_ahead` caps the whole
name at 1–253 characters, then a label (alphanumeric, up to 61 interior
letters/digits/hyphens, alphanumeric) is followed by
:meth:`~edify.RegexBuilder.zero_or_more` dot-prefixed labels — all anchored with
:meth:`~edify.RegexBuilder.start_of_input` / :meth:`~edify.RegexBuilder.end_of_input`:

.. code-block:: python

   from edify import Pattern

   hostname = (
       Pattern().start_of_input()
       .assert_ahead().between(1, 253).any_char().end()
       .use(label).zero_or_more().group().char(".").use(label).end()
       .end_of_input()
   )

Single labels are allowed
-------------------------

Unlike :doc:`domain`, ``hostname`` accepts a lone label with no dot and no TLD —
the names you meet on a LAN — as well as dotted names:

.. code-block:: python

   hostname("localhost")     # True — a single label is fine
   hostname("db.internal")   # True
   hostname("host-1")        # True — a hyphen and a digit
   hostname("-bad")          # False — can't start with a hyphen
   hostname("a b")           # False — no spaces

.. edify-playground::
   :tests: localhost|db.internal|host-1|-bad|a b

   from edify.library import hostname
   hostname

Two length limits
-----------------

Two caps apply at once: the leading assertion holds the whole name to 253
characters, and each label to 63. So a single 253-character label is rejected —
the length has to be spread across labels:

.. code-block:: python

   hostname("a" * 63)            # True  — a label at its 63-char maximum
   hostname("a" * 64)            # False — that label is one character too long
   hostname("a" * 63 + ".com")   # True  — 63-char label, then a short one

.. edify-playground::
   :tests: gateway|printer.local|a.very.long.but.valid.internal.hostname

   from edify.library import hostname
   hostname

Notes
-----

- For a name that must end in a real TLD use :doc:`domain`; for a single label on
  its own, :doc:`subdomain`; for a ``host:port`` pair, :doc:`socket`.
