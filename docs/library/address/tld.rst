tld
===

``tld`` matches a top-level domain — the ``com`` in ``example.com``. The grammar
is small (2 to 63 letters) but there are three things worth being precise about:
how long it can be, which characters count, and the fact that it checks the shape
rather than the registry.

.. edify-playground::
   :tests: io|com|museum|COM|Dev|zzz|c|c0m|co-op|.com

   from edify.library import tld
   tld

**Length — two to sixty-three.** Two letters at the short end (country codes like
``io`` and ``uk``), up to 63 at the long end (legacy and branded gTLDs). A single
letter is below the minimum:

.. code-block:: python

   tld("io")       # True  — the two-letter minimum
   tld("museum")   # True  — a long gTLD
   tld("c")        # False — one letter is too short

**Case doesn't matter.** DNS is case-insensitive, and so is ``tld`` — upper,
lower, and mixed all match, which is why you never have to normalise before
checking:

.. code-block:: python

   tld("com")   # True
   tld("COM")   # True
   tld("Dev")   # True

**Letters only.** No digits, no hyphens, no dots — the leading dot of ``.com`` is
punctuation in a domain, not part of the TLD:

.. code-block:: python

   tld("c0m")     # False — digits
   tld("co-op")   # False — hyphens
   tld(".com")    # False — the leading dot

Note that it matches the *form* of a TLD, not the IANA list, so an unregistered
string of letters like ``zzz`` still passes. Under the hood it is just
:meth:`~edify.RegexBuilder.between`\ ``(2, 63)`` of a
:meth:`~edify.RegexBuilder.letter` class — ``^[a-zA-Z]{2,63}$`` — and it is the
trailing component that a full :doc:`domain` requires.
