Finance
=======

Every validator in the :doc:`Finance <../../library/financial/index>` category.
Each is a callable :class:`~edify.Pattern`: pass a string to get a ``bool``, or
compose it into a larger pattern with :meth:`~edify.RegexBuilder.use`.

Each entry states what the pattern guarantees, shows the chain that builds it, and
ends with the regex it emits. For prose, worked examples, and a live playground, use
the :doc:`library pages <../../library/financial/index>`.

.. py:data:: edify.library.card

   Callable :class:`Pattern` for credit-card number shape:
   groups of 4 digits with optional dash/space separators, 13-19 digits total.

   Full description: :doc:`Card <../../library/financial/card>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      card = (
          Pattern()
          .start_of_input()
          .exactly(4)
          .digit()
          .optional()
          .any_of_chars("- ")
          .exactly(4)
          .digit()
          .optional()
          .any_of_chars("- ")
          .exactly(4)
          .digit()
          .optional()
          .any_of_chars("- ")
          .between(1, 7)
          .digit()
          .end_of_input()
      )

   **Emits** ``^\d{4}[- ]?\d{4}[- ]?\d{4}[- ]?\d{1,7}$``

.. py:data:: edify.library.crypto

   Callable :class:`Pattern` for a cryptocurrency ticker shape:
   3-10 uppercase-alphanumeric characters (``BTC``, ``ETH``, ``USDT``, ``SHIB``, …).

   Full description: :doc:`Crypto <../../library/financial/crypto>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      crypto = (
          Pattern()
          .start_of_input()
          .between(3, 10)
          .any_of()
          .range("A", "Z")
          .range("0", "9")
          .end()
          .end_of_input()
      )

   **Emits** ``^[A-Z0-9]{3,10}$``

.. py:data:: edify.library.currency

   Callable :class:`Pattern` for the ISO 4217 currency-code shape:
   3 uppercase letters (``USD``, ``EUR``, ``JPY``, …).

   Full description: :doc:`Currency <../../library/financial/currency>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      currency = Pattern().start_of_input().exactly(3).any_of().range("A", "Z").end().end_of_input()

   **Emits** ``^[A-Z]{3}$``

.. py:data:: edify.library.routing

   Callable :class:`Pattern` for a US ABA routing number (9 digits).

   Full description: :doc:`Routing <../../library/financial/routing>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      routing = Pattern().start_of_input().exactly(9).digit().end_of_input()

   **Emits** ``^\d{9}$``

.. py:data:: edify.library.sortcode

   Callable :class:`Pattern` for a UK sort code.

   Full description: :doc:`Sort code <../../library/financial/sortcode>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern, any_of

      _dashed = (
          Pattern()
          .start_of_input()
          .exactly(2)
          .digit()
          .char("-")
          .exactly(2)
          .digit()
          .char("-")
          .exactly(2)
          .digit()
          .end_of_input()
      )
      _solid = Pattern().start_of_input().exactly(6).digit().end_of_input()

      sortcode = any_of(_dashed, _solid)

   **Emits** ``(?:^\d{2}\-\d{2}\-\d{2}$|^\d{6}$)``

.. py:data:: edify.library.vat

   Callable :class:`Pattern` for a VAT identification number.

   Full description: :doc:`VAT <../../library/financial/vat>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      vat = Pattern().start_of_input().exactly(2).uppercase().between(6, 12).digit().end_of_input()

   **Emits** ``^[A-Z]{2}\d{6,12}$``

.. py:data:: edify.library.wallet

   Callable :class:`Pattern` for cryptocurrency-wallet address shapes:
   Bitcoin (legacy, SegWit, Bech32), Ethereum, Litecoin, Dogecoin, Dash.

   Full description: :doc:`Wallet <../../library/financial/wallet>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern, any_of

      _bitcoin_legacy = (
          Pattern()
          .any_of_chars("13")
          .between(25, 34)
          .any_of()
          .range("a", "k")
          .range("m", "z")
          .range("A", "H")
          .range("J", "N")
          .range("P", "Z")
          .range("1", "9")
          .end()
      )

      _bitcoin_bech32 = (
          Pattern().string("bc1").between(25, 89).any_of().range("a", "z").range("0", "9").end()
      )

      _ethereum = (
          Pattern()
          .string("0x")
          .exactly(40)
          .any_of()
          .range("a", "f")
          .range("A", "F")
          .range("0", "9")
          .end()
      )

      _litecoin = (
          Pattern()
          .any_of_chars("LM3")
          .between(26, 33)
          .any_of()
          .range("a", "k")
          .range("m", "z")
          .range("A", "H")
          .range("J", "N")
          .range("P", "Z")
          .range("1", "9")
          .end()
      )

      _dogecoin = (
          Pattern()
          .char("D")
          .any_of()
          .range("5", "9")
          .range("A", "H")
          .range("J", "N")
          .range("P", "U")
          .end()
          .exactly(32)
          .any_of()
          .range("1", "9")
          .range("A", "H")
          .range("J", "N")
          .range("P", "Z")
          .range("a", "k")
          .range("m", "z")
          .end()
      )

      _dash = (
          Pattern()
          .char("X")
          .exactly(33)
          .any_of()
          .range("1", "9")
          .range("A", "H")
          .range("J", "N")
          .range("P", "Z")
          .range("a", "k")
          .range("m", "z")
          .end()
      )

      wallet = (
          Pattern()
          .start_of_input()
          .subexpression(any_of(_bitcoin_legacy, _bitcoin_bech32, _ethereum, _litecoin, _dogecoin, _dash))
          .end_of_input()
      )

      del _bitcoin_legacy, _bitcoin_bech32, _ethereum, _litecoin, _dogecoin, _dash

   **Emits** ``^(?:[13][a-km-zA-HJ-NP-Z1-9]{25,34}|bc1[a-z0-9]{25,89}|0x[a-fA-F0-9]{40}|[LM3][a-km-zA-HJ-NP-Z1-9]{26,33}|D[5-9A-HJ-NP-U][1-9A-HJ-NP-Za-km-z]{32}|X[1-9A-HJ-NP-Za-km-z]{33})$``

