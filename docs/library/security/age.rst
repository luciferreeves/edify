Age
===

`age <https://age-encryption.org/>`__ is a modern file-encryption tool built around
two short, human-copyable key strings: a **recipient** you encrypt to, written
``age1…``, and an **identity** you decrypt with, written ``AGE-SECRET-KEY-1…``.
**Age** matches either.

The two are branches of an :func:`~edify.any_of`. The recipient is the ``age1``
prefix then 8–128 lowercase Bech32 characters; the identity is the
``AGE-SECRET-KEY-1`` prefix then uppercase characters — the case difference is
deliberate in the format, making a secret visually obvious.

Recipients and identities
-------------------------

.. edify-playground::

   from edify.library import age

   age("age1ql3z7hjy54pw3hyww5ayyfg7zqgvc7w3j2elw8zmrj2kg5sfn9aqmcac8p")   # a recipient
   age("AGE-SECRET-KEY-1QWERTYUIOPASDFGHJKLZXCVBNM234567")                 # an identity

The prefix and case are exact
-----------------------------

.. edify-playground::

   from edify.library import age

   age("age1ql3z7hjy54pw3hyww5ayyfg7zqgvc7w3j2elw8")   # a valid recipient
   age("age1UPPERCASEISNOTBECH32CHARSET")              # recipients are lowercase
   age("age1")                                          # no key material
   age("AGE-SECRET-KEY-")                               # no key material
   age("hello")                                         # not an age key

An identity is a secret: if one reaches a validator via a form or a log line, it has
already been exposed. Bech32 carries a checksum that this pattern does not verify —
a typo'd key can match here and still fail to decrypt. For other key formats see
:doc:`ssh` and :doc:`pgp`.
