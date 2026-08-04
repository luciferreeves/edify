Script
======

**Script** matches a run of text written in a *single*
`writing system <https://www.unicode.org/standard/supported.html>`__ — Latin, Greek,
Cyrillic, CJK, Arabic, Hebrew, or Devanagari. Its purpose is detecting mixed-script
input, which is the mechanism behind homograph attacks: a domain or username where a
Cyrillic ``а`` stands in for a Latin ``a``.

The seven scripts are the branches of an :func:`~edify.any_of`, each a
:meth:`~edify.RegexBuilder.one_or_more` run over that script's Unicode ranges.
Because each branch must match the whole string, a document mixing two scripts
satisfies none of them.

One script at a time
--------------------

The Latin branch includes the accented Latin-1 and Latin Extended-A ranges, so
European languages qualify:

.. edify-playground::

   from edify.library import script

   script("Hello")       # Latin
   script("naïve")       # Latin with accents
   script("Ελληνικά")    # Greek
   script("Привет")      # Cyrillic
   script("日本語")       # CJK
   script("한국어")       # Hangul
   script("العربية")      # Arabic
   script("עברית")        # Hebrew
   script("हिन्दी")         # Devanagari

Mixing scripts fails
--------------------

This is the check's whole point — a string drawing on two writing systems matches no
single branch:

.. edify-playground::

   from edify.library import script

   script("日本語")        # one script
   script("Hello日本")     # Latin and CJK together
   script("Приvet")       # Cyrillic and Latin together
   script("")             # empty

Note that spaces, digits, and punctuation are not part of any branch, so a sentence
with a space between words will not match — apply this per token rather than to a
whole phrase. A single-script result is not proof of safety either: whole words can
be spoofed within one script. For any-script displayable text see :doc:`printable`.
