Subdomain
=========

**Subdomain** matches a single DNS label on its own — the ``api`` in
``api.example.com``, not a dotted name. It is the building block a :doc:`domain` and a
:doc:`hostname` are made of (:rfc:`1035`), validated in isolation.

That "first and last character must be alphanumeric" rule is written straight into
the shape: an :meth:`~edify.RegexBuilder.alphanumeric` character, then
:meth:`~edify.RegexBuilder.between`\ ``(0, 61)`` of a letters/digits/hyphen
:meth:`~edify.RegexBuilder.any_of` class, then a closing
:meth:`~edify.RegexBuilder.alphanumeric`.

The character set
-----------------

The body of a label is letters, digits, and hyphens, which is why ``my-sub`` and
``staging-2`` both pass:

.. edify-playground::

   from edify.library import subdomain

   subdomain("api")         # a plain label
   subdomain("my-sub")      # interior hyphen
   subdomain("staging-2")   # digits and a hyphen
   subdomain("has space")   # no spaces

The ends, and the length
------------------------

A label may not begin or end with a hyphen — the rule that keeps ``-bad`` and ``bad-``
out. Requiring a first *and* a last alphanumeric character means the minimum length is
**two**, not one; the maximum is 63:

.. edify-playground::

   from edify.library import subdomain

   subdomain("a1")      # two characters, the minimum
   subdomain("a")       # a single char can't be both first and last
   subdomain("-bad")    # leading hyphen
   subdomain("bad-")    # trailing hyphen

One label — no dots
-------------------

A dot would make it two labels, which is a job for :doc:`domain`:

.. edify-playground::

   from edify.library import subdomain

   subdomain("internal")   # still one label
   subdomain("a.b")        # that's two labels

For a full dotted name ending in a :doc:`tld`, use :doc:`domain`; to allow a bare
single label as a host, :doc:`hostname`.
