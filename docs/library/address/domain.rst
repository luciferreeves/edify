domain
======

A DNS domain name is a run of dot-separated **labels** ending in a letters-only
**TLD** — ``example.com``, ``a.b.example.io``. That trailing TLD is what
distinguishes ``domain`` from :doc:`hostname`, where a bare ``localhost`` is
allowed.

.. edify-playground::
   :tests: example.com|a.b.example.io|my-site.org|xn--nxasmq6b.com|example|example.123|-x.com|x-.com

   from edify.library import domain
   domain

**Labels.** One or more, joined by dots. Each label is 1–63 characters of letters,
digits, and hyphens, and you can stack as many as you like. A Punycode (IDNA)
label such as ``xn--nxasmq6b`` is just letters, digits, and hyphens, so it passes:

.. code-block:: python

   domain("example.com")        # True — one label + TLD
   domain("a.b.example.io")     # True — several labels deep
   domain("xn--nxasmq6b.com")   # True — a Punycode label

**Hyphens are interior only.** A label may contain hyphens but may not begin or
end with one — the rule that most often surprises people:

.. code-block:: python

   domain("my-site.org")   # True  — interior hyphen
   domain("-x.com")        # False — label starts with a hyphen
   domain("x-.com")        # False — label ends with a hyphen

**The TLD is letters only.** The final component must be a :doc:`tld` of 2–63
letters, so a name with no TLD or a numeric one fails:

.. code-block:: python

   domain("example")       # False — no TLD
   domain("example.123")   # False — a TLD is letters only

In edify this is a label group repeated with :meth:`~edify.RegexBuilder.one_or_more`,
each followed by a dot, then :meth:`~edify.RegexBuilder.between`\ ``(2, 63)``
letters. For a name that may be a bare single label, use :doc:`hostname`; for one
label on its own, :doc:`subdomain`.
