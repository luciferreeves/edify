Email
=====

**Email** matches an email address the way a form should: a local part, an ``@``,
and a **dotted** domain. It is the practical subset of :rfc:`5322` — the grammar
people actually type — and it is the one to reach for in a sign-up form.

The local part is :meth:`~edify.RegexBuilder.one_or_more` dot-separated runs of the
characters :rfc:`5322` permits unquoted, including the ``+`` used for tagged
addresses. The domain side
requires at least one dot, which is the deliberate difference from the full grammar:
a bare ``a@b`` is legal by specification but is never a deliverable public address.

Everyday addresses
------------------

.. edify-playground::

   from edify.library import email

   email("first.last@example.com")     # a dotted local part
   email("user+tag@example.com")       # plus-addressing
   email("a@b.com")                    # the shortest practical form
   email("name@example.co.uk")         # a multi-label domain

The domain must be dotted
-------------------------

This is the rule that separates this validator from :doc:`email_rfc_5322`:

.. edify-playground::

   from edify.library import email

   email("a@b.com")   # dotted domain
   email("a@b")       # legal by RFC, but not deliverable
   email("no-at.com") # no @ at all

Structural rejections
---------------------

Spaces, doubled dots, and a missing side all fail:

.. edify-playground::

   from edify.library import email

   email("user@example.com")    # valid
   email("a b@c.com")           # a space
   email("a..b@c.com")          # consecutive dots
   email("@example.com")        # no local part
   email("")                    # empty

No pattern can tell you an address exists or accepts mail — only sending to it can,
which is why a confirmation link beats a stricter regex. Validate loosely here, then
verify by delivery. For the complete grammar including quoted local parts see
:doc:`email_rfc_5322`.
