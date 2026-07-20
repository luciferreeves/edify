domain
======

A DNS domain name is a run of dot-separated **labels** ending in a letters-only
**TLD** — ``example.com``, ``a.b.example.io``. ``domain`` requires that trailing
TLD, which is what separates it from :doc:`hostname` (where a bare ``localhost``
is fine).

.. edify-playground::
   :tests: example.com|a.b.example.io|my-site.org|xn--nxasmq6b.com|example|example.123|-x.com

   from edify.library import domain
   domain

Each label is 1–63 characters of letters, digits, and hyphens, with one rule that
trips people up: a hyphen may sit **inside** a label but not at either end, so
``my-site.org`` is fine while ``-x.com`` and ``x-.com`` are not. The TLD is 2–63
letters (see :doc:`tld`), so ``example`` (no TLD) and ``example.123`` (numeric
TLD) both fail; a Punycode label like ``xn--nxasmq6b.com`` passes, since it is
still letters, digits, and hyphens.

In edify this is a label group repeated with :meth:`~edify.RegexBuilder.one_or_more`,
each followed by a dot, then :meth:`~edify.RegexBuilder.between`\ ``(2, 63)``
letters. For a single label on its own, see :doc:`subdomain`.
