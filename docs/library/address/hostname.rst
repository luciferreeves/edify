hostname
========

``hostname`` is :doc:`domain`'s more relaxed sibling. It follows RFC 1123, and
differs in two ways that matter: a **bare single label** is valid, and there is
**no letters-only TLD** requirement.

.. edify-playground::
   :tests: example.com|localhost|gateway|db.internal|host-1|-bad|a b|a..b

   from edify.library import hostname
   hostname

**Single labels are allowed.** Unlike a domain, a hostname can be one label with
no dot and no TLD — the names you meet on a LAN:

.. code-block:: python

   hostname("localhost")     # True
   hostname("gateway")       # True
   hostname("db.internal")   # True — and dotted names work too

**Same label rules as a domain.** Letters, digits, and interior hyphens, so a
leading hyphen or an empty label between two dots still fails:

.. code-block:: python

   hostname("host-1")   # True
   hostname("-bad")     # False — leading hyphen
   hostname("a..b")     # False — empty label

**Two length limits at once.** This is what is unique to ``hostname``: a leading
:meth:`~edify.RegexBuilder.assert_ahead` caps the *whole* name at 253 characters,
while each label is capped at 63. So a single 253-character label is rejected — the
length has to be spread across labels:

.. code-block:: python

   hostname("a" * 63)            # True  — a label at its 63-char maximum
   hostname("a" * 64)            # False — that label is one over
   hostname("a" * 63 + ".com")   # True  — 63-char label, then a short one

For a name that must end in a real TLD, use :doc:`domain`; for a single label,
:doc:`subdomain`; for a ``host:port`` pair, :doc:`socket`.
