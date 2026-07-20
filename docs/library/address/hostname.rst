hostname
========

``hostname`` is :doc:`domain`'s more relaxed sibling. It follows RFC 1123 and
differs in two ways: a **bare single label** such as ``localhost`` is valid, and
there is **no letters-only TLD** requirement. So the names you meet on a LAN —
``localhost``, ``gateway``, ``db.internal`` — all pass.

.. edify-playground::
   :tests: example.com|localhost|db.internal|host-1|-bad|a b|a..b

   from edify.library import hostname
   hostname

The label rules are the same as a domain's — letters, digits, interior hyphens —
so ``-bad`` (leading hyphen) and ``a..b`` (empty label) still fail. What is unique
to ``hostname`` is a pair of length limits enforced at once: a leading
:meth:`~edify.RegexBuilder.assert_ahead` caps the *whole* name at 253 characters,
while each label is capped at 63. A single 253-character label is therefore
rejected — the length has to be spread across labels:

.. code-block:: python

   hostname("a" * 63)            # True  — a label at its 63-char maximum
   hostname("a" * 64)            # False — that label is one character too long
   hostname("a" * 63 + ".com")   # True  — 63-char label, then a short one

For a name that must end in a real TLD, use :doc:`domain`; for a single label,
:doc:`subdomain`; for a ``host:port`` pair, :doc:`socket`.
