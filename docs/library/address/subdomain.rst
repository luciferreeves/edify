subdomain
=========

The ``api`` in ``api.example.com`` — a single DNS label, on its own, 2 to 63
characters long.

.. edify-playground::
   :tests: api|my-sub|staging-2|a1|a|-bad|bad-|a.b

   from edify.library import subdomain
   subdomain

**The rules.** A label is letters, digits, and interior hyphens, with an
alphanumeric first *and* last character — so ``-bad`` and ``bad-`` are out, and
requiring both ends is what forces the two-character minimum. A dot makes it two
labels rather than one, so ``a.b`` fails. In edify that is an
:meth:`~edify.RegexBuilder.alphanumeric` character, then
:meth:`~edify.RegexBuilder.between`\ ``(0, 61)`` of a letters/digits/hyphen class,
then another :meth:`~edify.RegexBuilder.alphanumeric` — emitting
``^[a-zA-Z0-9][a-zA-Z0-9\-]{0,61}[a-zA-Z0-9]$``.

For a full dotted name, reach for :doc:`domain` or :doc:`hostname`.
