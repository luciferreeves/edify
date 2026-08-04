UUID
====

A `UUID <https://datatracker.ietf.org/doc/html/rfc9562>`__ is a 128-bit identifier
written as five hyphenated hex groups. **UUID** is stricter than a plain hex check:
it validates the **version** and **variant** bits that :rfc:`9562` defines, so a
random hex string of the right shape is rejected.

The version nibble — the first character of the third group — is constrained with a
:meth:`~edify.RegexBuilder.range` to ``0``–``5``, and the variant nibble at the start
of the fourth group to an :meth:`~edify.RegexBuilder.any_of_chars` set of ``8``,
``9``, ``a``, ``b``. Lowercase only.

Real UUIDs
----------

.. edify-playground::

   from edify.library import uuid

   uuid("550e8400-e29b-41d4-a716-446655440000")   # version 4
   uuid("6ba7b810-9dad-11d1-80b4-00c04fd430c8")   # version 1, time-based
   uuid("00000000-0000-0000-0000-000000000000")   # the nil UUID

Version and variant are checked
-------------------------------

This is what separates it from a hex-shaped string:

.. edify-playground::

   from edify.library import uuid

   uuid("550e8400-e29b-41d4-a716-446655440000")   # version 4, variant a
   uuid("550e8400-e29b-71d4-a716-446655440000")   # version 7 is not accepted
   uuid("550e8400-e29b-41d4-c716-446655440000")   # c is not a valid variant

Lowercase and hyphenated
------------------------

.. edify-playground::

   from edify.library import uuid

   uuid("550e8400-e29b-41d4-a716-446655440000")   # canonical
   uuid("550E8400-E29B-41D4-A716-446655440000")   # uppercase
   uuid("550e8400e29b41d4a716446655440000")       # no hyphens
   uuid("")                                        # empty

Note the version ceiling: UUIDv6, v7, and v8 were added by :rfc:`9562` and are
**not** matched, so a v7 identifier — increasingly common because it sorts by time —
will fail. Use :doc:`guid` for a laxer check. A valid UUID is also not a secret: v1
encodes a timestamp and MAC address, so prefer v4 where unpredictability matters.
