Quantifiers
===========

Quantifiers come **before** the token they repeat, so the chain reads the way you
say it out loud: ``.exactly(3).digit()`` is *exactly three digits*.

The lazy variants stop at the first match that satisfies the pattern rather than
consuming as much as possible.

.. automethod:: edify.RegexBuilder.exactly

.. automethod:: edify.RegexBuilder.between

.. automethod:: edify.RegexBuilder.at_least

.. automethod:: edify.RegexBuilder.at_most

.. automethod:: edify.RegexBuilder.optional

.. automethod:: edify.RegexBuilder.one_or_more

.. automethod:: edify.RegexBuilder.zero_or_more

.. automethod:: edify.RegexBuilder.between_lazy

.. automethod:: edify.RegexBuilder.one_or_more_lazy

.. automethod:: edify.RegexBuilder.zero_or_more_lazy
