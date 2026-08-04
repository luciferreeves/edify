Email (RFC 5322)
================

**Email (RFC 5322)** implements the mailbox grammar from :rfc:`5322` proper —
including the two forms almost no everyday address uses: a **quoted local part**,
and a **domain literal** holding an IP address instead of a name.

The local part is an :func:`~edify.any_of` of a dot-atom or a quoted string; the
domain side is an :func:`~edify.any_of` of dotted labels or a bracketed literal.
Where :doc:`email` stops at what people type, this covers what the specification
permits.

Quoted local parts
------------------

Wrapping the local part in quotes lets it hold characters a dot-atom cannot:

.. edify-playground::

   from edify.library import email_rfc_5322

   email_rfc_5322('"quoted"@example.com')      # a quoted local part
   email_rfc_5322('"very.unusual"@example.com')
   email_rfc_5322("plain@example.com")          # dot-atoms still work

Domain literals
---------------

An address may point at an IP address directly, in brackets:

.. edify-playground::

   from edify.library import email_rfc_5322

   email_rfc_5322("user@[192.168.0.1]")   # an IPv4 domain literal
   email_rfc_5322("user@example.com")     # a normal domain

Still anchored and structural
-----------------------------

The grammar is broader, not looser — a missing side or a doubled dot fails here
just as it does in :doc:`email`:

.. edify-playground::

   from edify.library import email_rfc_5322

   email_rfc_5322("user@example.com")   # valid
   email_rfc_5322("a..b@c.com")         # consecutive dots
   email_rfc_5322("@example.com")       # no local part
   email_rfc_5322("")                   # empty

Two caveats. The display-name form ``Name <user@example.com>`` is a *header* field,
not a mailbox, and is not matched here. And accepting the exotic forms is rarely
what a sign-up form wants — a quoted local part is far more likely to be a mistake
or an injection attempt than a real address, so prefer :doc:`email` for user input
and keep this for parsing existing mail data.
