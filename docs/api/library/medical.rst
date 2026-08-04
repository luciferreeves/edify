Medical
=======

Every validator in the :doc:`Medical <../../library/medical/index>` category.
Each is a callable :class:`~edify.Pattern`: pass a string to get a ``bool``, or
compose it into a larger pattern with :meth:`~edify.RegexBuilder.use`.

Each entry states what the pattern guarantees, shows the chain that builds it, and
ends with the regex it emits. For prose, worked examples, and a live playground, use
the :doc:`library pages <../../library/medical/index>`.

.. py:data:: edify.library.blood

   Callable :class:`Pattern` for an ABO/Rh blood-type shape.

   Full description: :doc:`Blood <../../library/medical/blood>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      blood = (
          Pattern()
          .start_of_input()
          .group()
          .any_of()
          .string("AB")
          .char("A")
          .char("B")
          .char("O")
          .end()
          .end()
          .any_of_chars("+-")
          .end_of_input()
      )

   **Emits** ``^(?:(?:AB|[ABO]))[+-]$``

.. py:data:: edify.library.dicom

   Callable :class:`Pattern` for a DICOM UID: dotted-integer chain.

   Full description: :doc:`DICOM <../../library/medical/dicom>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      dicom = (
          Pattern()
          .start_of_input()
          .one_or_more()
          .digit()
          .one_or_more()
          .group()
          .char(".")
          .one_or_more()
          .digit()
          .end()
          .end_of_input()
      )

   **Emits** ``^\d+(?:\.\d+)+$``

.. py:data:: edify.library.dosage

   Callable :class:`Pattern` for a pharmaceutical dosage shape:
   digits with optional decimal + unit (``mg``/``g``/``kg``/``ml``/``l``/``mcg``/``iu``)
   and optional per-``kg``/``day``/``dose`` qualifier.

   Full description: :doc:`Dosage <../../library/medical/dosage>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern


      def _unit() -> Pattern:
          return (
              Pattern()
              .any_of()
              .string("mg")
              .char("g")
              .string("kg")
              .string("ml")
              .char("l")
              .string("mcg")
              .string("iu")
              .end()
          )


      dosage = (
          Pattern()
          .start_of_input()
          .one_or_more()
          .digit()
          .optional()
          .group()
          .char(".")
          .one_or_more()
          .digit()
          .end()
          .optional()
          .whitespace_char()
          .subexpression(_unit())
          .optional()
          .group()
          .char("/")
          .any_of()
          .string("kg")
          .string("day")
          .string("dose")
          .end()
          .end()
          .end_of_input()
      )

   **Emits** ``^\d+(?:\.\d+)?\s?(?:mg|kg|ml|mcg|iu|[gl])(?:/(?:kg|day|dose))?$``

.. py:data:: edify.library.medical

   Callable :class:`Pattern` for medical-coding-system codes.

   Full description: :doc:`Medical code <../../library/medical/medical>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern, any_of

      _snomed = Pattern().between(6, 18).digit()
      _icd = (
          Pattern()
          .any_of()
          .range("A", "T")
          .range("V", "Z")
          .end()
          .digit()
          .any_of()
          .range("A", "Z")
          .range("0", "9")
          .end()
          .optional()
          .group()
          .char(".")
          .between(1, 4)
          .any_of()
          .range("A", "Z")
          .range("0", "9")
          .end()
          .end()
      )
      _npi = Pattern().exactly(10).digit()
      _loinc = Pattern().between(1, 7).digit().char("-").digit()

      medical = (
          Pattern().start_of_input().subexpression(any_of(_snomed, _icd, _npi, _loinc)).end_of_input()
      )

   **Emits** ``^(?:\d{6,18}|[A-TV-Z]\d[A-Z0-9](?:\.[A-Z0-9]{1,4})?|\d{10}|\d{1,7}\-\d)$``

