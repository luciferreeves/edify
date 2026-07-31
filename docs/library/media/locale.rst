Locale
======

A `locale <https://en.wikipedia.org/wiki/Locale_(computer_software)>`__ identifier
names a language and, optionally, a region, encoding, and variant — ``en``,
``en-US``, ``en_US.UTF-8``. **Locale** matches the POSIX-style form with both
separator conventions.

The construction is a 2–3 letter lowercase language code, an
:meth:`~edify.RegexBuilder.optional` group of ``-`` or ``_`` plus a two-letter
uppercase region, then optional ``.encoding`` and ``@variant`` suffixes.

Language and region
-------------------

Both separators are accepted, since the web uses ``-`` and POSIX uses ``_``:

.. edify-playground::

   from edify.library import locale

   locale("en")            # language only
   locale("en-US")         # web style
   locale("en_US")         # POSIX style
   locale("pt-BR")
   locale("fra")           # a three-letter code

Encoding and variant
--------------------

.. edify-playground::

   from edify.library import locale

   locale("en_US.UTF-8")        # with an encoding
   locale("de_DE.ISO-8859-1")
   locale("sr_RS@latin")        # with a variant

Case and structure are fixed
----------------------------

Language is lowercase, region uppercase — the convention both systems share:

.. edify-playground::

   from edify.library import locale

   locale("en-US")        # correct casing
   locale("EN-us")        # inverted
   locale("english")      # not a code
   locale("zh-Hans-CN")   # a script subtag is BCP 47, not POSIX

The last case is worth noting: full :rfc:`5646` (BCP 47) tags with script subtags —
``zh-Hans-CN`` — are not matched, because this follows the POSIX shape. Use a proper
language-tag parser if you need those.
