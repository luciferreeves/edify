Checksum
========

A `checksum <https://en.wikipedia.org/wiki/Checksum>`__ is the hexadecimal digest
published alongside a download so you can confirm the file arrived intact.
**Checksum** matches 8 to 128 hex digits — CRC32 through SHA-512 — in either case.

The construction is :meth:`~edify.RegexBuilder.between`\ ``(8, 128)`` over an
:meth:`~edify.RegexBuilder.any_of` class of ``0``–``9``, ``a``–``f``, ``A``–``F``.

Digest widths
-------------

.. edify-playground::

   from edify.library import checksum

   checksum("deadbeef")        # 8: CRC32
   checksum("a" * 32)          # MD5 width
   checksum("b" * 40)          # SHA-1 width
   checksum("c" * 64)          # SHA-256 width
   checksum("d" * 128)         # SHA-512 width

Hex in either case
------------------

.. edify-playground::

   from edify.library import checksum

   checksum("DEADBEEF")   # uppercase
   checksum("deadbeef")   # lowercase
   checksum("deadbeeg")   # g is not hex
   checksum("a" * 7)      # too short
   checksum("")           # empty

A checksum confirms *integrity*, not *authenticity*: if an attacker can replace the
file they can usually replace the published checksum too. For real assurance use a
signature (:doc:`../security/signature`) or fetch the digest over a channel the
attacker does not control. For the algorithm-prefixed form see :doc:`digest`.
