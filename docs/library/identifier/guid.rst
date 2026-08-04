GUID
====

A `GUID <https://learn.microsoft.com/en-us/dotnet/api/system.guid>`__ is the same
128-bit value as a :doc:`uuid`, written the way Microsoft platforms write it: often
wrapped in braces, and in either case. **GUID** is the lenient counterpart —
five hex groups of the right widths, with no version or variant check.

The construction is an :meth:`~edify.RegexBuilder.optional` ``{``, the five hex
groups joined by hyphens, and a matching optional ``}``. Hex digits in either case.

Braced and bare
---------------

.. edify-playground::

   from edify.library import guid

   guid("550e8400-e29b-41d4-a716-446655440000")     # bare
   guid("{550e8400-e29b-41d4-a716-446655440000}")   # braced, as a registry value
   guid("550E8400-E29B-41D4-A716-446655440000")     # uppercase

Any version or variant
----------------------

Values that :doc:`uuid` rejects are accepted here, which is the point of having both:

.. edify-playground::

   from edify.library import guid

   guid("550e8400-e29b-71d4-a716-446655440000")   # version 7
   guid("550e8400-e29b-41d4-c716-446655440000")   # a non-standard variant

The group widths are fixed
--------------------------

.. edify-playground::

   from edify.library import guid

   guid("550e8400-e29b-41d4-a716-446655440000")   # 8-4-4-4-12
   guid("550e8400e29b41d4a716446655440000")       # no hyphens
   guid("550e840-e29b-41d4-a716-446655440000")    # a short first group
   guid("")                                        # empty

Use this when consuming identifiers from mixed sources — including the newer UUID
versions — and :doc:`uuid` when you want the specification enforced.
