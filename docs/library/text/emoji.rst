Emoji
=====

**Emoji** matches a string made entirely of
`emoji <https://unicode.org/emoji/charts/full-emoji-list.html>`__ characters — the
check for a reaction field, a status icon, or a tag that should hold symbols and
nothing else.

The construction is :meth:`~edify.RegexBuilder.one_or_more` over an
:meth:`~edify.RegexBuilder.any_of` covering two Unicode spans: the main
``U+1F300``–``U+1FAFF`` emoji planes, and the ``U+2600``–``U+27BF`` block that holds
the older symbols such as ☀ and ➿.

Emoji strings
-------------

.. edify-playground::

   from edify.library import emoji

   emoji("🎉")       # a single emoji
   emoji("🎉🎊")      # several in a row
   emoji("☀")        # an older symbol block character
   emoji("🚀🌕")      # any combination

Emoji only
----------

Mixing text or spaces in fails — the whole string must be symbols:

.. edify-playground::

   from edify.library import emoji

   emoji("🎉🎊")      # all emoji
   emoji("🎉 a")     # a space and a letter
   emoji("abc")      # plain text
   emoji("")         # empty

The two ranges cover the emoji in everyday use, but not every sequence Unicode
defines: flags, skin-tone modifiers, and zero-width-joiner families (such as 👨‍👩‍👧) are
built from characters outside these blocks and will not match. For general non-ASCII
text see :doc:`unicode`.
