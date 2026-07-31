Hostname
========

**Hostname** is :doc:`domain`'s more relaxed sibling (:rfc:`1123`, tightening the
older :rfc:`952`). It differs in two ways that matter: a **bare single label** is
valid, and there is **no letters-only TLD** requirement.

Structurally it is a :doc:`label <../../guide/composing>` — an
:meth:`~edify.RegexBuilder.alphanumeric` start and end around up to 61 interior
letters/digits/hyphens — repeated with :meth:`~edify.RegexBuilder.zero_or_more`
dot-prefixed labels, behind a leading :meth:`~edify.RegexBuilder.assert_ahead` that
caps the whole name at 253 characters.

Single labels are allowed
-------------------------

Unlike a domain, a hostname can be one label with no dot and no TLD — the names you
meet on a LAN — as well as dotted names:

.. edify-playground::

   from edify.library import hostname

   hostname("localhost")     # the classic single label
   hostname("gateway")       # any LAN name
   hostname("db.internal")   # dotted names work too
   hostname("example.com")   # so do public ones

Same label rules as a domain
----------------------------

Letters, digits, and interior hyphens only, so a leading hyphen or an empty label
between two dots still fails:

.. edify-playground::

   from edify.library import hostname

   hostname("host-1")   # interior hyphen
   hostname("-bad")     # leading hyphen
   hostname("a b")      # no spaces
   hostname("a..b")     # empty label

Two length limits at once
-------------------------

This is what is unique to **Hostname**: the leading
:meth:`~edify.RegexBuilder.assert_ahead` caps the *whole* name at 253 characters,
while each label is capped at 63. So a single 253-character label is rejected — the
length has to be spread across labels:

.. edify-playground::

   from edify.library import hostname

   hostname("a" * 63)            # a label at its 63-char maximum
   hostname("a" * 64)            # that label is one over
   hostname("a" * 63 + ".com")   # 63-char label, then a short one

For a name that must end in a real :doc:`tld`, use :doc:`domain`; for a single label on
its own, :doc:`subdomain`; for a ``host:port`` pair, :doc:`socket`.
