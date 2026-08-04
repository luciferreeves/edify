TLD
===

**TLD** matches a top-level domain — the ``com`` in ``example.com``, or any of the
`IANA-registered <https://www.iana.org/domains/root/db>`__ endings. It is the smallest
grammar in the library: a single :meth:`~edify.RegexBuilder.between`\ ``(2, 63)`` over
a :meth:`~edify.RegexBuilder.letter` class, anchored end to end with
:meth:`~edify.RegexBuilder.start_of_input` / :meth:`~edify.RegexBuilder.end_of_input`.

Length — two to sixty-three
---------------------------

Two letters at the short end (country codes like ``io`` and ``uk``), up to 63 at the
long end (the legacy and branded gTLDs). A single letter is below the minimum:

.. edify-playground::

   from edify.library import tld

   tld("io")       # the two-letter minimum
   tld("uk")       # a country code
   tld("museum")   # a long gTLD
   tld("c")        # one letter is too short

Case-insensitive
----------------

DNS is case-insensitive, and so is **TLD** — upper, lower, and mixed all match, so you
never have to normalise before checking:

.. edify-playground::

   from edify.library import tld

   tld("com")   # lowercase
   tld("COM")   # uppercase
   tld("Dev")   # mixed case

Letters only, and only the shape
--------------------------------

No digits, no hyphens, no dots — the leading dot of ``.com`` is punctuation in a
domain, not part of the TLD. And it matches the *form* of a TLD, not the IANA
registry, so an unregistered string of letters still passes:

.. edify-playground::

   from edify.library import tld

   tld("zzz")     # well-formed, though not a real TLD
   tld("c0m")     # digits
   tld("co-op")   # hyphens
   tld(".com")    # the leading dot

**TLD** is the trailing component that a full :doc:`domain` requires; for a single
label anywhere in a name, see :doc:`subdomain`.
