Ratio
=====

**Ratio** matches the colon form of a
`ratio <https://en.wikipedia.org/wiki/Ratio>`__ — ``16:9``, ``4:3``, ``1:1`` — the
notation used for aspect ratios, odds, and proportions.

The construction is :meth:`~edify.RegexBuilder.one_or_more`
:meth:`~edify.RegexBuilder.digit`, a literal ``:``, then digits again. Both sides
are unsigned whole numbers, which is what the notation means.

Two-term ratios
---------------

.. edify-playground::

   from edify.library import ratio

   ratio("16:9")     # a widescreen aspect ratio
   ratio("4:3")      # the older one
   ratio("1:1")      # square
   ratio("21:9")     # ultrawide
   ratio("1:1000")   # any magnitude

Exactly two whole terms
-----------------------

Decimals, signs, and three-term forms are outside the notation:

.. edify-playground::

   from edify.library import ratio

   ratio("16:9")      # valid
   ratio("16/9")      # the slash form: see fraction
   ratio("1.5:1")     # a decimal term
   ratio("-16:9")     # a sign
   ratio("1:2:3")     # three terms
   ratio("")          # empty

As with :doc:`fraction` a zero term is well formed but may be meaningless — ``16:0``
matches. For the slash notation see :doc:`fraction`; for a proportion out of a
hundred, :doc:`percentage`.
