Quantifiers
===========

A quantifier says *how many* of the next token to match. Remember the one habit
from :doc:`thinking-in-edify`: the quantifier comes **before** the token it
governs.

Fixed counts
------------

.. code-block:: python

   from edify import RegexBuilder as R

   R().exactly(3).digit().to_regex_string()      # '\\d{3}'      exactly three
   R().at_least(2).digit().to_regex_string()     # '\\d{2,}'     two or more
   R().at_most(4).digit().to_regex_string()      # '\\d{0,4}'    up to four
   R().between(2, 5).digit().to_regex_string()   # '\\d{2,5}'    two to five

Open-ended counts
-----------------

The three classic quantifiers have plain-English names:

.. code-block:: python

   R().optional().char("s").to_regex_string()    # 's?'    zero or one
   R().zero_or_more().digit().to_regex_string()  # '\\d*'  zero or more
   R().one_or_more().digit().to_regex_string()   # '\\d+'  one or more

Greedy vs lazy
--------------

By default a quantifier is **greedy** — it matches as much as it can, then gives
characters back only if the rest of the pattern needs them. The ``_lazy``
variants flip that: they match as *little* as possible and expand only when
forced. Every open-ended and range quantifier has a lazy twin:

.. code-block:: python

   R().one_or_more_lazy().digit().to_regex_string()    # '\\d+?'
   R().zero_or_more_lazy().digit().to_regex_string()   # '\\d*?'
   R().between_lazy(2, 5).digit().to_regex_string()    # '\\d{2,5}?'

The difference matters the moment you match between two delimiters. Greedy runs
to the *last* delimiter; lazy stops at the *first*:

.. code-block:: python

   greedy = R().char("<").one_or_more().any_char().char(">").to_regex()
   lazy = R().char("<").one_or_more_lazy().any_char().char(">").to_regex()

   greedy.search("<a><b>").group()   # '<a><b>'  — grabbed everything
   lazy.search("<a><b>").group()     # '<a>'     — stopped at the first '>'

Reach for lazy when you want the *smallest* match; leave it greedy otherwise.

Quantifying a group
-------------------

A quantifier before a group repeats the entire group — see :doc:`groups` for the
grouping tokens:

.. code-block:: python

   R().one_or_more().group().digit().char("-").end().to_regex_string()
   # '(?:\\d\\-)+'   — one or more "digit-dash" units

Next: :doc:`groups`, for grouping and alternation.
