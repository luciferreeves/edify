Roman
=====

**Roman** matches a `Roman numeral <https://en.wikipedia.org/wiki/Roman_numerals>`__
from I to MMMCMXCIX — 1 to 3999, the range the standard letters can express without
the overline notation for thousands.

The construction reads the numeral place by place, exactly as the system works:
thousands as :meth:`~edify.RegexBuilder.between`\ ``(0, 3)`` ``M``, then hundreds,
tens, and units, each an :func:`~edify.any_of` of the subtractive pair (``CM``,
``CD``), the optional five-letter with up to three ones, or nothing. A leading
:meth:`~edify.RegexBuilder.assert_ahead` requires at least one numeral letter, so
the empty string does not slip through an all-optional pattern.

Numerals across the range
-------------------------

.. edify-playground::

   from edify.library import roman

   roman("I")            # one
   roman("IV")           # subtractive four
   roman("XIV")          # fourteen
   roman("MMXXIV")       # 2024
   roman("MMMCMXCIX")    # 3999, the maximum

Subtractive notation is enforced
--------------------------------

Four is ``IV``, not ``IIII`` — the pattern encodes the rule rather than accepting
any run of letters:

.. edify-playground::

   from edify.library import roman

   roman("IV")       # correct
   roman("IIII")     # four ones
   roman("VX")       # not a valid subtractive pair
   roman("IC")       # ninety-nine is XCIX

Uppercase only, and non-empty
-----------------------------

.. edify-playground::

   from edify.library import roman

   roman("XIV")   # uppercase
   roman("xiv")   # lowercase
   roman("")      # empty
   roman("ABC")   # not numeral letters

Values above 3999 need the overline notation, which has no plain-text form and is
not matched here. For the Arabic value see :doc:`integer`.
