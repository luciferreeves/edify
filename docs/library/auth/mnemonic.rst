Mnemonic
========

A `mnemonic phrase <https://github.com/bitcoin/bips/blob/master/bip-0039.mediawiki>`__
encodes a cryptographic seed as ordinary words, so a human can write it down and
type it back. The BIP-39 scheme defines phrases of 12, 15, 18, 21, or 24 words —
**Mnemonic** accepts any length from 12 to 24 words, all lowercase, single-spaced.

The construction is a :meth:`~edify.RegexBuilder.between`\ ``(11, 23)`` group of
"word plus space", followed by a final word with no trailing space — which is how
the count lands between 12 and 24 with exactly one space between each pair.

Phrase lengths
--------------

The 12-word phrase is the common wallet default; 24 words carries the larger seed:

.. edify-playground::

   from edify.library import mnemonic

   mnemonic("legal winner thank year wave sausage worth useful legal winner thank yellow")
   mnemonic("abandon " * 11 + "about")                  # the canonical test vector
   mnemonic("abandon " * 23 + "art")                    # a 24-word phrase

Lowercase, single-spaced
------------------------

The wordlist is lowercase and the separator is exactly one space, so capitalisation
or doubled spacing must be normalised first:

.. edify-playground::

   from edify.library import mnemonic

   mnemonic("abandon " * 11 + "about")            # normalised
   mnemonic("Abandon " * 11 + "about")            # capitalised
   mnemonic("abandon  " * 11 + "about")           # doubled spaces
   mnemonic("abandon-" * 11 + "about")            # hyphen separated

Word count is bounded
---------------------

Fewer than 12 words cannot carry a valid seed, and more than 24 is not a defined
phrase length:

.. edify-playground::

   from edify.library import mnemonic

   mnemonic("abandon " * 11 + "about")   # twelve words
   mnemonic("abandon " * 10 + "about")   # eleven: too few
   mnemonic("abandon " * 24 + "art")     # twenty-five: too many

This counts words; it does not check them against the BIP-39 wordlist or verify the
checksum built into the final word, so an invented phrase of the right length still
matches. A recovery phrase *is* the wallet — never transmit one, log it, or paste it
into a site. For the keys it derives see :doc:`secret`.
