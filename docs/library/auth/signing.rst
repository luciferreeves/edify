Signing key
===========

A signing key is the secret used to produce a
`message authentication code <https://en.wikipedia.org/wiki/Message_authentication_code>`__
or signature — the input to :doc:`hmac`, a webhook signature, or a cookie seal. Because
such keys are usually distributed as base64, **Signing key** matches 32 to 256
characters of letters, digits, ``+``, ``/``, ``=``, ``_``, and ``-``, covering both
base64 alphabets.

The construction is :meth:`~edify.RegexBuilder.between`\ ``(32, 256)`` over an
:meth:`~edify.RegexBuilder.any_of` class. The 32-character floor reflects that a
signing key shorter than that offers too little entropy against offline attack.

Both base64 alphabets
---------------------

Standard base64 with padding, and the URL-safe variant:

.. edify-playground::

   from edify.library import signing

   signing("aGVsbG8gd29ybGQgc2lnbmluZyBrZXkgdmFsdWU=")   # standard, padded
   signing("aGVsbG8td29ybGRfc2lnbmluZy1rZXlfdmFsdWU")    # URL-safe
   signing("A" * 256)                                     # at the maximum

Length bounds
-------------

.. edify-playground::

   from edify.library import signing

   signing("a" * 32)    # at the minimum
   signing("a" * 31)    # too short
   signing("a" * 257)   # too long

Outside the alphabet
--------------------

Spaces and punctuation outside base64 are not part of a key:

.. edify-playground::

   from edify.library import signing

   signing("abcdefghij0123456789abcdefghij12")    # valid
   signing("abcdefghij 123456789abcdefghij12")    # a space
   signing("abcdefghij!123456789abcdefghij12")    # an exclamation mark

A signing key must never leave the server, appear in client code, or be logged —
anyone holding it can forge signatures that verify perfectly. Rotate on exposure,
and prefer separate keys per purpose so one leak does not compromise everything.
For the code produced with it see :doc:`hmac`; for shared secrets generally,
:doc:`secret`.
