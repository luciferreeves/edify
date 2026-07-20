subdomain
=========

``subdomain`` matches a single DNS label on its own — the ``api`` in
``api.example.com``, not a dotted name. It is the building block a
:doc:`domain` and a :doc:`hostname` are made of, validated in isolation.

.. edify-playground::
   :tests: api|my-sub|staging-2|a1|a|-bad|bad-|a.b|has space

   from edify.library import subdomain
   subdomain

**Letters, digits, and interior hyphens.** The body of a label can mix
alphanumerics and hyphens, which is why ``my-sub`` and ``staging-2`` are fine:

.. code-block:: python

   subdomain("api")        # True
   subdomain("my-sub")     # True — interior hyphen
   subdomain("staging-2")  # True — digits and a hyphen

**The ends must be alphanumeric.** A label may not begin or end with a hyphen —
this is the rule that keeps ``-bad`` and ``bad-`` out — and requiring a first
*and* a last alphanumeric character means the minimum length is **two**, not one:

.. code-block:: python

   subdomain("a1")   # True  — two characters, the minimum
   subdomain("a")    # False — a single char can't be both first and last
   subdomain("-bad") # False — leading hyphen
   subdomain("bad-") # False — trailing hyphen

**It is one label, so no dots.** A dot would make it two labels, which is a job
for :doc:`domain`:

.. code-block:: python

   subdomain("a.b")        # False — that's two labels
   subdomain("has space")  # False — no spaces

The maximum length is 63. In edify the label is an
:meth:`~edify.RegexBuilder.alphanumeric` character, then
:meth:`~edify.RegexBuilder.between`\ ``(0, 61)`` of a letters/digits/hyphen class,
then a final :meth:`~edify.RegexBuilder.alphanumeric` — emitting
``^[a-zA-Z0-9][a-zA-Z0-9\-]{0,61}[a-zA-Z0-9]$``.
