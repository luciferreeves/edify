Crypto
======

**Crypto** matches a `cryptocurrency ticker <https://en.wikipedia.org/wiki/Cryptocurrency>`__
— the short uppercase symbol an exchange lists an asset under: ``BTC``, ``ETH``,
``USDT``.

The construction is :meth:`~edify.RegexBuilder.between`\ ``(3, 10)`` over an
:meth:`~edify.RegexBuilder.any_of` class of uppercase letters and digits. The range
is wider than the three letters of :doc:`currency`, since crypto tickers are not
standardised.

Asset tickers
-------------

.. edify-playground::

   from edify.library import crypto

   crypto("BTC")
   crypto("ETH")
   crypto("USDT")
   crypto("SHIB")
   crypto("1INCH")   # digits appear in some tickers

Uppercase, three to ten
-----------------------

.. edify-playground::

   from edify.library import crypto

   crypto("BTC")       # canonical
   crypto("bitcoin")   # a name, not a ticker
   crypto("btc")       # lowercase
   crypto("BT")        # too short
   crypto("")          # empty

Crypto tickers have no registry, so collisions are common and a ticker does not
identify an asset unambiguously — several unrelated tokens share popular symbols, and
that ambiguity is actively exploited. Identify an asset by its contract address (see
:doc:`wallet`) rather than its ticker. For national currencies see :doc:`currency`.
