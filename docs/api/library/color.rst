Color
=====

Every validator in the :doc:`color <../../library/color/index>` category. Each is a
callable :class:`~edify.Pattern`: pass a string to get a ``bool``, or compose it into a
larger pattern with :meth:`~edify.RegexBuilder.use`.

For what each one accepts and rejects, with runnable examples, see the
:doc:`library pages <../../library/color/index>`.

.. py:function:: edify.library.color(value: str) -> bool

   Color. See :doc:`../../library/color/color` for the full description.

   Emits ``(?:^\#(?:[0-9A-Fa-f]{3,4}|[0-9A-Fa-f]{6}|[0-9A-Fa-f]{8})$|^rgba?\(\s*\d{1,3}%?\s*,\s*\d{1,3}%?\s*,\s*\d{1,3}%?(?:\s*,\s*(?:\d|[\.])+)?\s*\)$|^hsla?\(\s*\d{1,3}(?:deg)?\s*,\s*\d{1,3}%\s*,\s*\d{1,3}%(?:\s*,\s*(?:\d|[\.])+)?\s*\)$|^[a-zA-Z]{3,20}$)``

.. py:function:: edify.library.filter(value: str) -> bool

   Filter. See :doc:`../../library/color/filter` for the full description.

   Emits ``^(?:blur|brightness|contrast|grayscale|hue\-rotate|invert|opacity|saturate|sepia|drop\-shadow)\([^)]+\)$``

.. py:function:: edify.library.gradient(value: str) -> bool

   Gradient. See :doc:`../../library/color/gradient` for the full description.

   Emits ``^(?:linear|radial|conic)\-gradient\([^()]*(?:\([^()]*\)[^()]*)*\)$``

.. py:function:: edify.library.palette(value: str) -> bool

   Palette. See :doc:`../../library/color/palette` for the full description.

   Emits ``^(?:(?:\#[0-9A-Fa-f]{3,8})|[a-zA-Z]{3,20})(?:\s*,\s*(?:(?:\#[0-9A-Fa-f]{3,8})|[a-zA-Z]{3,20})){1,15}$``

.. py:function:: edify.library.swatch(value: str) -> bool

   Swatch. See :doc:`../../library/color/swatch` for the full description.

   Emits ``^(?:(?:\#[0-9A-Fa-f]{3,8})|[a-zA-Z]{3,20})$``

