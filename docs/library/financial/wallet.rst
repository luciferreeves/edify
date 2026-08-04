Wallet
======

**Wallet** matches a `cryptocurrency address <https://en.wikipedia.org/wiki/Cryptocurrency_wallet>`__
across the common chains: legacy and SegWit Bitcoin, and the 20-byte hex addresses
used by Ethereum and compatible chains.

The forms are the branches of an :func:`~edify.any_of`: a Base58Check address
starting ``1`` or ``3``, a Bech32 address starting ``bc1``, or ``0x`` followed by 40
hex characters. The Base58 alphabet deliberately omits ``0``, ``O``, ``I``, and ``l``
because they are easily confused by eye.

Bitcoin addresses
-----------------

.. edify-playground::

   from edify.library import wallet

   wallet("1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa")   # legacy P2PKH
   wallet("3J98t1WpEZ73CNmQviecrnyiWrnqRhWNLy")   # P2SH
   wallet("bc1qar0srrr7xfkvy5l643lydnw9re59gtzzwf5mdq")   # native SegWit

Ethereum-style addresses
------------------------

.. edify-playground::

   from edify.library import wallet

   wallet("0x" + "a" * 40)
   wallet("0x71C7656EC7ab88b098defB751B7401B5f6d8976F")   # mixed-case checksum form

Malformed addresses
-------------------

.. edify-playground::

   from edify.library import wallet

   wallet("0x" + "a" * 40)   # correct length
   wallet("0x" + "a" * 39)   # one character short
   wallet("0" + "a" * 40)    # no 0x prefix
   wallet("")                # empty

This is the highest-stakes caveat in the library: cryptocurrency transfers are
irreversible, and every one of these formats carries a checksum that a pattern cannot
verify — a mistyped address can match here and send funds nowhere recoverable. Always
validate the Base58Check or Bech32 checksum, and for Ethereum verify the
`EIP-55 <https://eips.ethereum.org/EIPS/eip-55>`__ mixed-case checksum, before
sending anything.
