Builder
=======

Two classes share the same chain surface.

:class:`~edify.RegexBuilder` is the fluent, immutable builder: every method returns
a **new** builder rather than mutating the receiver, so a partially built chain can
be shared and branched without copying.

:class:`~edify.Pattern` has the same 65 chain methods and adds two things — it is
**callable** as a validator, and it can be embedded in another chain with
:meth:`~edify.RegexBuilder.use`.

.. code-block:: python

   from edify import Pattern, RegexBuilder

   RegexBuilder().exactly(4).digit().to_regex_string()   # '\\d{4}'

   year = Pattern().start_of_input().exactly(4).digit().end_of_input()
   year("2024")   # True — a Pattern is callable

The chain methods are documented by topic:

.. list-table::
   :header-rows: 1
   :widths: 26 74

   * - Topic
     - Methods
   * - :doc:`anchors`
     - ``start_of_input`` ``end_of_input``
   * - :doc:`characters`
     - ``char`` ``string`` ``range`` ``any_of_chars`` ``anything_but_chars``
       ``anything_but_range`` ``anything_but_string``
   * - :doc:`classes`
     - ``digit`` ``letter`` ``word`` ``whitespace_char`` ``alphanumeric``
       ``uppercase`` ``lowercase`` ``any_char`` and their negations
   * - :doc:`quantifiers`
     - ``exactly`` ``between`` ``at_least`` ``at_most`` ``optional``
       ``one_or_more`` ``zero_or_more`` and the lazy variants
   * - :doc:`groups`
     - ``group`` ``any_of`` ``one_of`` ``end``
   * - :doc:`captures`
     - ``capture`` ``named_capture`` ``back_reference`` ``named_back_reference``
   * - :doc:`assertions`
     - ``assert_ahead`` ``assert_behind`` ``assert_not_ahead``
       ``assert_not_behind``
   * - :doc:`flags`
     - ``ignore_case`` ``dot_all`` ``multi_line`` ``verbose`` ``ascii_only``
       ``debug``
   * - :doc:`composition`
     - ``use`` ``subexpression``
   * - :doc:`matching`
     - ``test`` ``match`` ``search`` ``findall`` ``sub``
   * - :doc:`output`
     - ``to_regex`` ``to_regex_string``

The classes
-----------

.. autoclass:: edify.RegexBuilder
   :no-members:

.. autoclass:: edify.Pattern
   :no-members:

Every method below is available on both.
