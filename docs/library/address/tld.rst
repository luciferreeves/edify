tld
===

``tld`` matches a top-level domain: 2 to 63 letters, upper or lower case, like
``com``, ``io``, or ``museum``. It emits ``^[a-zA-Z]{2,63}$`` — nothing more than
:meth:`~edify.RegexBuilder.between`\ ``(2, 63)`` of a
:meth:`~edify.RegexBuilder.letter` class.

.. edify-playground::
   :tests: com|io|museum|COM|zzz|c|c0m|.com

   from edify.library import tld
   tld

It matches the *shape* of a TLD, not the IANA registry, so ``zzz`` passes while a
single letter, a digit, a hyphen, or a leading dot all fail. It is the trailing
component that a full :doc:`domain` requires — and about the only validator in the
library simple enough to fit on one screen.
