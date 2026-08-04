Transport
=========

Every validator in the :doc:`Transport <../../library/transport/index>` category.
Each is a callable :class:`~edify.Pattern`: pass a string to get a ``bool``, or
compose it into a larger pattern with :meth:`~edify.RegexBuilder.use`.

Each entry states what the pattern guarantees, shows the chain that builds it, and
ends with the regex it emits. For prose, worked examples, and a live playground, use
the :doc:`library pages <../../library/transport/index>`.

.. py:data:: edify.library.aircraft

   Callable :class:`Pattern` for an aircraft-registration mark.

   Full description: :doc:`Aircraft <../../library/transport/aircraft>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      aircraft = (
          Pattern()
          .start_of_input()
          .between(1, 2)
          .uppercase()
          .optional()
          .char("-")
          .between(1, 5)
          .any_of()
          .range("A", "Z")
          .range("0", "9")
          .end()
          .end_of_input()
      )

   **Emits** ``^[A-Z]{1,2}\-?[A-Z0-9]{1,5}$``

.. py:data:: edify.library.flight

   Callable :class:`Pattern` for an IATA/ICAO flight-number shape.

   Full description: :doc:`Flight <../../library/transport/flight>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      flight = (
          Pattern()
          .start_of_input()
          .exactly(2)
          .uppercase()
          .between(1, 4)
          .digit()
          .optional()
          .uppercase()
          .end_of_input()
      )

   **Emits** ``^[A-Z]{2}\d{1,4}[A-Z]?$``

.. py:data:: edify.library.plate

   Callable :class:`Pattern` for a vehicle license-plate shape.

   Full description: :doc:`Plate <../../library/transport/plate>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      plate = (
          Pattern()
          .start_of_input()
          .between(1, 3)
          .any_of()
          .range("A", "Z")
          .range("0", "9")
          .end()
          .optional()
          .any_of_chars("- ")
          .between(1, 4)
          .any_of()
          .range("A", "Z")
          .range("0", "9")
          .end()
          .end_of_input()
      )

   **Emits** ``^[A-Z0-9]{1,3}[- ]?[A-Z0-9]{1,4}$``

.. py:data:: edify.library.vehicle

   Callable :class:`Pattern` for a permissive transport-vehicle identifier.

   Full description: :doc:`Vehicle <../../library/transport/vehicle>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      vehicle = (
          Pattern()
          .start_of_input()
          .any_of()
          .range("A", "Z")
          .range("0", "9")
          .end()
          .between(3, 17)
          .any_of()
          .range("A", "Z")
          .range("0", "9")
          .char("-")
          .char(" ")
          .end()
          .end_of_input()
      )

   **Emits** ``^[A-Z0-9][A-Z0-9\- ]{3,17}$``

