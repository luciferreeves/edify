Numeric
=======

Every validator in the :doc:`numeric <../../library/numeric/index>` category. Each is a
callable :class:`~edify.Pattern`: pass a string to get a ``bool``, or compose it into a
larger pattern with :meth:`~edify.RegexBuilder.use`.

For what each one accepts and rejects, with runnable examples, see the
:doc:`library pages <../../library/numeric/index>`.

.. py:function:: edify.library.fraction(value: str) -> bool

   Fraction. See :doc:`../../library/numeric/fraction` for the full description.

   Emits ``^\-?(?:\d+\s+)?\d+/\d+$``

.. py:function:: edify.library.hash(value: str) -> bool

   Hash. See :doc:`../../library/numeric/hash` for the full description.

   Emits ``^[a-fA-F0-9]{8,128}$``

.. py:function:: edify.library.integer(value: str) -> bool

   Integer. See :doc:`../../library/numeric/integer` for the full description.

   Emits ``^[+-]?\d+$``

.. py:function:: edify.library.natural(value: str) -> bool

   Natural. See :doc:`../../library/numeric/natural` for the full description.

   Emits ``^[1-9]\d*$``

.. py:function:: edify.library.number(value: str) -> bool

   Number. See :doc:`../../library/numeric/number` for the full description.

   Emits ``^(?:[+-]?\d+|[+-]?\d+\.\d+|[+-]?\.\d+|[+-]?\d+\.\d*[eE][+-]?\d+|[+-]?\d+[eE][+-]?\d+|0[xX][0-9a-fA-F]+|0[oO][0-7]+|0[bB][01]+|[+-]?\d+(?:\.\d+)?[+-]\d+(?:\.\d+)?[jJi])$``

.. py:function:: edify.library.ordinal(value: str) -> bool

   Ordinal. See :doc:`../../library/numeric/ordinal` for the full description.

   Emits ``^\d+(?:(?:st|nd|rd|th))$``

.. py:function:: edify.library.percentage(value: str) -> bool

   Percentage. See :doc:`../../library/numeric/percentage` for the full description.

   Emits ``^\-?\d+(?:\.\d+)?\s?%$``

.. py:function:: edify.library.ratio(value: str) -> bool

   Ratio. See :doc:`../../library/numeric/ratio` for the full description.

   Emits ``^\d+:\d+$``

.. py:function:: edify.library.roman(value: str) -> bool

   Roman. See :doc:`../../library/numeric/roman` for the full description.

   Emits ``^(?=[MDCLXVI]+)M{0,3}(?:(?:CM|CD|D?C{0,3}))(?:(?:XC|XL|L?X{0,3}))(?:(?:IX|IV|V?I{0,3}))$``

.. py:function:: edify.library.scientific(value: str) -> bool

   Scientific. See :doc:`../../library/numeric/scientific` for the full description.

   Emits ``^[+-]?\d+(?:\.\d+)?[eE][+-]?\d+$``

