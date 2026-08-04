Color
=====

Every validator in the :doc:`Color <../../library/color/index>` category.
Each is a callable :class:`~edify.Pattern`: pass a string to get a ``bool``, or
compose it into a larger pattern with :meth:`~edify.RegexBuilder.use`.

Each entry states what the pattern guarantees, shows the chain that builds it, and
ends with the regex it emits. For prose, worked examples, and a live playground, use
the :doc:`library pages <../../library/color/index>`.

.. py:data:: edify.library.color

   Callable :class:`Pattern` for any common CSS colour shape.

   Full description: :doc:`Color <../../library/color/color>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern, any_of

      color = any_of(
          Pattern()
          .start_of_input()
          .char("#")
          .any_of()
          .between(3, 4)
          .any_of()
          .range("0", "9")
          .range("A", "F")
          .range("a", "f")
          .end()
          .exactly(6)
          .any_of()
          .range("0", "9")
          .range("A", "F")
          .range("a", "f")
          .end()
          .exactly(8)
          .any_of()
          .range("0", "9")
          .range("A", "F")
          .range("a", "f")
          .end()
          .end()
          .end_of_input(),
          Pattern()
          .start_of_input()
          .string("rgb")
          .optional()
          .char("a")
          .char("(")
          .zero_or_more()
          .whitespace_char()
          .between(1, 3)
          .digit()
          .optional()
          .char("%")
          .zero_or_more()
          .whitespace_char()
          .char(",")
          .zero_or_more()
          .whitespace_char()
          .between(1, 3)
          .digit()
          .optional()
          .char("%")
          .zero_or_more()
          .whitespace_char()
          .char(",")
          .zero_or_more()
          .whitespace_char()
          .between(1, 3)
          .digit()
          .optional()
          .char("%")
          .optional()
          .group()
          .zero_or_more()
          .whitespace_char()
          .char(",")
          .zero_or_more()
          .whitespace_char()
          .one_or_more()
          .any_of()
          .digit()
          .char(".")
          .end()
          .end()
          .zero_or_more()
          .whitespace_char()
          .char(")")
          .end_of_input(),
          Pattern()
          .start_of_input()
          .string("hsl")
          .optional()
          .char("a")
          .char("(")
          .zero_or_more()
          .whitespace_char()
          .between(1, 3)
          .digit()
          .optional()
          .group()
          .string("deg")
          .end()
          .zero_or_more()
          .whitespace_char()
          .char(",")
          .zero_or_more()
          .whitespace_char()
          .between(1, 3)
          .digit()
          .char("%")
          .zero_or_more()
          .whitespace_char()
          .char(",")
          .zero_or_more()
          .whitespace_char()
          .between(1, 3)
          .digit()
          .char("%")
          .optional()
          .group()
          .zero_or_more()
          .whitespace_char()
          .char(",")
          .zero_or_more()
          .whitespace_char()
          .one_or_more()
          .any_of()
          .digit()
          .char(".")
          .end()
          .end()
          .zero_or_more()
          .whitespace_char()
          .char(")")
          .end_of_input(),
          Pattern().start_of_input().between(3, 20).letter().end_of_input(),
      )

   **Emits** ``(?:^\#(?:[0-9A-Fa-f]{3,4}|[0-9A-Fa-f]{6}|[0-9A-Fa-f]{8})$|^rgba?\(\s*\d{1,3}%?\s*,\s*\d{1,3}%?\s*,\s*\d{1,3}%?(?:\s*,\s*(?:\d|[\.])+)?\s*\)$|^hsla?\(\s*\d{1,3}(?:deg)?\s*,\s*\d{1,3}%\s*,\s*\d{1,3}%(?:\s*,\s*(?:\d|[\.])+)?\s*\)$|^[a-zA-Z]{3,20}$)``

.. py:data:: edify.library.filter

   Callable :class:`Pattern` for a CSS filter function call.

   Full description: :doc:`Filter <../../library/color/filter>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      filter = (
          Pattern()
          .start_of_input()
          .any_of(
              "blur",
              "brightness",
              "contrast",
              "grayscale",
              "hue-rotate",
              "invert",
              "opacity",
              "saturate",
              "sepia",
              "drop-shadow",
          )
          .char("(")
          .one_or_more()
          .anything_but_chars(")")
          .char(")")
          .end_of_input()
      )

   **Emits** ``^(?:blur|brightness|contrast|grayscale|hue\-rotate|invert|opacity|saturate|sepia|drop\-shadow)\([^)]+\)$``

.. py:data:: edify.library.gradient

   Callable :class:`Pattern` for a CSS gradient function call.

   Full description: :doc:`Gradient <../../library/color/gradient>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      gradient = (
          Pattern()
          .start_of_input()
          .any_of("linear", "radial", "conic")
          .string("-gradient(")
          .zero_or_more()
          .anything_but_chars("()")
          .zero_or_more()
          .group()
          .char("(")
          .zero_or_more()
          .anything_but_chars("()")
          .char(")")
          .zero_or_more()
          .anything_but_chars("()")
          .end()
          .char(")")
          .end_of_input()
      )

   **Emits** ``^(?:linear|radial|conic)\-gradient\([^()]*(?:\([^()]*\)[^()]*)*\)$``

.. py:data:: edify.library.palette

   Callable :class:`Pattern` for a comma-separated list of 2-16 colours.

   Full description: :doc:`Palette <../../library/color/palette>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      palette = (
          Pattern()
          .start_of_input()
          .any_of()
          .group()
          .char("#")
          .between(3, 8)
          .any_of()
          .range("0", "9")
          .range("A", "F")
          .range("a", "f")
          .end()
          .end()
          .between(3, 20)
          .letter()
          .end()
          .between(1, 15)
          .group()
          .zero_or_more()
          .whitespace_char()
          .char(",")
          .zero_or_more()
          .whitespace_char()
          .any_of()
          .group()
          .char("#")
          .between(3, 8)
          .any_of()
          .range("0", "9")
          .range("A", "F")
          .range("a", "f")
          .end()
          .end()
          .between(3, 20)
          .letter()
          .end()
          .end()
          .end_of_input()
      )

   **Emits** ``^(?:(?:\#[0-9A-Fa-f]{3,8})|[a-zA-Z]{3,20})(?:\s*,\s*(?:(?:\#[0-9A-Fa-f]{3,8})|[a-zA-Z]{3,20})){1,15}$``

.. py:data:: edify.library.swatch

   Callable :class:`Pattern` for a single hex colour or CSS named colour.

   Full description: :doc:`Swatch <../../library/color/swatch>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      swatch = (
          Pattern()
          .start_of_input()
          .any_of()
          .group()
          .char("#")
          .between(3, 8)
          .any_of()
          .range("0", "9")
          .range("A", "F")
          .range("a", "f")
          .end()
          .end()
          .between(3, 20)
          .letter()
          .end()
          .end_of_input()
      )

   **Emits** ``^(?:(?:\#[0-9A-Fa-f]{3,8})|[a-zA-Z]{3,20})$``

