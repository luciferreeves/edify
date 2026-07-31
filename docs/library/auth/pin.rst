PIN
===

A `personal identification number <https://en.wikipedia.org/wiki/Personal_identification_number>`__
is a short numeric secret — four digits on a bank card, longer on a phone or SIM.
**PIN** matches 4 to 12 digits.

The construction is :meth:`~edify.RegexBuilder.between`\ ``(4, 12)`` over
:meth:`~edify.RegexBuilder.digit`, anchored end to end. The lower bound is the
banking minimum; the upper bound covers the longer device passcodes.

The usual lengths
-----------------

.. edify-playground::

   from edify.library import pin

   pin("1234")           # the card standard
   pin("0000")           # leading zeros count
   pin("123456")         # a six-digit device code
   pin("123456789012")   # the twelve-digit maximum

Digits only, within range
-------------------------

Three digits is below every issuer's minimum, thirteen is past the maximum, and a
PIN never contains letters or separators:

.. edify-playground::

   from edify.library import pin

   pin("1234")            # in range
   pin("123")             # too short
   pin("1234567890123")   # too long
   pin("12a4")            # not a digit
   pin("12 34")           # a space

Shape is not strength: ``1234`` and ``0000`` match here and are among the most
guessed codes in existence. Enforce a blocklist of common sequences, and never log
or transmit a PIN in the clear. For app-generated codes see :doc:`otp` and
:doc:`mfa`; for full password policies, :doc:`password`.
