Numeric
=======

Every validator in the :doc:`Numeric <../../library/numeric/index>` category.
Each is a callable :class:`~edify.Pattern`: pass a string to get a ``bool``, or
compose it into a larger pattern with :meth:`~edify.RegexBuilder.use`.

Each entry states what the pattern guarantees, shows the chain that builds it, and
ends with the regex it emits. For prose, worked examples, and a live playground, use
the :doc:`library pages <../../library/numeric/index>`.

.. py:data:: edify.library.fraction

   Callable :class:`Pattern` for a fraction shape:
   ``numerator/denominator`` with optional whole-number prefix.

   Full description: :doc:`Fraction <../../library/numeric/fraction>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      fraction = (
          Pattern()
          .start_of_input()
          .optional()
          .char("-")
          .optional()
          .group()
          .one_or_more()
          .digit()
          .one_or_more()
          .whitespace_char()
          .end()
          .one_or_more()
          .digit()
          .char("/")
          .one_or_more()
          .digit()
          .end_of_input()
      )

   **Emits** ``^\-?(?:\d+\s+)?\d+/\d+$``

.. py:data:: edify.library.hash

   Callable :class:`Pattern` for a hex-hash digest (8-128 hex characters,
   covering CRC-32 through SHA-512).

   Full description: :doc:`Hash <../../library/numeric/hash>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      hash = (
          Pattern()
          .start_of_input()
          .between(8, 128)
          .any_of()
          .range("a", "f")
          .range("A", "F")
          .range("0", "9")
          .end()
          .end_of_input()
      )

   **Emits** ``^[a-fA-F0-9]{8,128}$``

.. py:data:: edify.library.integer

   Callable :class:`Pattern` for a signed decimal integer.

   Full description: :doc:`Integer <../../library/numeric/integer>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      integer = (
          Pattern().start_of_input().optional().any_of_chars("+-").one_or_more().digit().end_of_input()
      )

   **Emits** ``^[+-]?\d+$``

.. py:data:: edify.library.natural

   Callable :class:`Pattern` for a positive integer with no leading zero.

   Full description: :doc:`Natural <../../library/numeric/natural>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      natural = Pattern().start_of_input().range("1", "9").zero_or_more().digit().end_of_input()

   **Emits** ``^[1-9]\d*$``

.. py:data:: edify.library.number

   Callable :class:`Pattern` that accepts numbers in any base or form:
   signed integers, decimals, floats, scientific, hex (``0x``), octal (``0o``),
   binary (``0b``), or complex (``a+bj``).

   Full description: :doc:`Number <../../library/numeric/number>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern, any_of


      def _sign() -> Pattern:
          return Pattern().optional().any_of_chars("+-")


      _int = Pattern().subexpression(_sign()).one_or_more().digit()
      _dec = Pattern().subexpression(_sign()).one_or_more().digit().char(".").one_or_more().digit()
      _ldec = Pattern().subexpression(_sign()).char(".").one_or_more().digit()
      _sci_dec = (
          Pattern()
          .subexpression(_sign())
          .one_or_more()
          .digit()
          .char(".")
          .zero_or_more()
          .digit()
          .any_of_chars("eE")
          .optional()
          .any_of_chars("+-")
          .one_or_more()
          .digit()
      )
      _sci_int = (
          Pattern()
          .subexpression(_sign())
          .one_or_more()
          .digit()
          .any_of_chars("eE")
          .optional()
          .any_of_chars("+-")
          .one_or_more()
          .digit()
      )
      _hex = (
          Pattern()
          .char("0")
          .any_of_chars("xX")
          .one_or_more()
          .any_of()
          .range("0", "9")
          .range("a", "f")
          .range("A", "F")
          .end()
      )
      _oct = Pattern().char("0").any_of_chars("oO").one_or_more().range("0", "7")
      _bin = Pattern().char("0").any_of_chars("bB").one_or_more().any_of_chars("01")
      _complex = (
          Pattern()
          .subexpression(_sign())
          .one_or_more()
          .digit()
          .optional()
          .group()
          .char(".")
          .one_or_more()
          .digit()
          .end()
          .any_of_chars("+-")
          .one_or_more()
          .digit()
          .optional()
          .group()
          .char(".")
          .one_or_more()
          .digit()
          .end()
          .any_of_chars("jJi")
      )

      number = (
          Pattern()
          .start_of_input()
          .subexpression(any_of(_int, _dec, _ldec, _sci_dec, _sci_int, _hex, _oct, _bin, _complex))
          .end_of_input()
      )

   **Emits** ``^(?:[+-]?\d+|[+-]?\d+\.\d+|[+-]?\.\d+|[+-]?\d+\.\d*[eE][+-]?\d+|[+-]?\d+[eE][+-]?\d+|0[xX][0-9a-fA-F]+|0[oO][0-7]+|0[bB][01]+|[+-]?\d+(?:\.\d+)?[+-]\d+(?:\.\d+)?[jJi])$``

.. py:data:: edify.library.ordinal

   Callable :class:`Pattern` for an English ordinal number.

   Full description: :doc:`Ordinal <../../library/numeric/ordinal>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      ordinal = (
          Pattern()
          .start_of_input()
          .one_or_more()
          .digit()
          .group()
          .any_of()
          .string("st")
          .string("nd")
          .string("rd")
          .string("th")
          .end()
          .end()
          .end_of_input()
      )

   **Emits** ``^\d+(?:(?:st|nd|rd|th))$``

.. py:data:: edify.library.percentage

   Callable :class:`Pattern` for a percentage value: signed number optionally
   with a decimal part and a trailing ``%``.

   Full description: :doc:`Percentage <../../library/numeric/percentage>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      percentage = (
          Pattern()
          .start_of_input()
          .optional()
          .char("-")
          .one_or_more()
          .digit()
          .optional()
          .group()
          .char(".")
          .one_or_more()
          .digit()
          .end()
          .optional()
          .whitespace_char()
          .char("%")
          .end_of_input()
      )

   **Emits** ``^\-?\d+(?:\.\d+)?\s?%$``

.. py:data:: edify.library.ratio

   Callable :class:`Pattern` for a ratio shape: ``digits:digits``.

   Full description: :doc:`Ratio <../../library/numeric/ratio>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      ratio = (
          Pattern().start_of_input().one_or_more().digit().char(":").one_or_more().digit().end_of_input()
      )

   **Emits** ``^\d+:\d+$``

.. py:data:: edify.library.roman

   Callable :class:`Pattern` for a Roman-numeral value 1-3999.

   Full description: :doc:`Roman <../../library/numeric/roman>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      roman = (
          Pattern()
          .start_of_input()
          .assert_ahead()
          .one_or_more()
          .any_of_chars("MDCLXVI")
          .end()
          .between(0, 3)
          .char("M")
          .group()
          .any_of()
          .string("CM")
          .string("CD")
          .subexpression(Pattern().optional().char("D").between(0, 3).char("C"))
          .end()
          .end()
          .group()
          .any_of()
          .string("XC")
          .string("XL")
          .subexpression(Pattern().optional().char("L").between(0, 3).char("X"))
          .end()
          .end()
          .group()
          .any_of()
          .string("IX")
          .string("IV")
          .subexpression(Pattern().optional().char("V").between(0, 3).char("I"))
          .end()
          .end()
          .end_of_input()
      )

   **Emits** ``^(?=[MDCLXVI]+)M{0,3}(?:(?:CM|CD|D?C{0,3}))(?:(?:XC|XL|L?X{0,3}))(?:(?:IX|IV|V?I{0,3}))$``

.. py:data:: edify.library.scientific

   Callable :class:`Pattern` for scientific-notation shape.

   Full description: :doc:`Scientific <../../library/numeric/scientific>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      scientific = (
          Pattern()
          .start_of_input()
          .optional()
          .any_of_chars("+-")
          .one_or_more()
          .digit()
          .optional()
          .group()
          .char(".")
          .one_or_more()
          .digit()
          .end()
          .any_of_chars("eE")
          .optional()
          .any_of_chars("+-")
          .one_or_more()
          .digit()
          .end_of_input()
      )

   **Emits** ``^[+-]?\d+(?:\.\d+)?[eE][+-]?\d+$``

