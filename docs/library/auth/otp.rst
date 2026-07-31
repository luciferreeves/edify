OTP
===

A `one-time password <https://datatracker.ietf.org/doc/html/rfc6238>`__ is the short
code an authenticator app or SMS delivers. The time-based algorithm (:rfc:`6238`)
and its counter-based predecessor (:rfc:`4226`) both produce digits, but many
providers issue alphanumeric codes instead — so **OTP** accepts either, 6 to 8
characters long.

The two forms are branches of an :func:`~edify.any_of`, each separately anchored:
all :meth:`~edify.RegexBuilder.digit` for the standard case, or all uppercase
letters and digits for the alphanumeric case. Mixed case is not accepted, because
codes are displayed in one case for transcription.

Numeric codes
-------------

The six-digit code is near-universal; some issuers use seven or eight:

.. edify-playground::

   from edify.library import otp

   otp("123456")     # the common six-digit code
   otp("1234567")    # seven digits
   otp("12345678")   # eight digits
   otp("000000")     # leading zeros are significant

Alphanumeric codes
------------------

Uppercase letters and digits, for issuers that use a larger alphabet:

.. edify-playground::

   from edify.library import otp

   otp("A1B2C3")     # uppercase alphanumeric
   otp("ZZZZ99")     # all letters and digits
   otp("a1b2c3")     # lowercase is not accepted

Length is strict
----------------

Shorter than six or longer than eight is not a one-time code, and separators are
never part of the value:

.. edify-playground::

   from edify.library import otp

   otp("123456")      # in range
   otp("12345")       # too short
   otp("123456789")   # too long
   otp("123 456")     # a space is not part of the code

Codes are single-use and time-limited: a well-formed code may still be expired,
already spent, or meant for another account. Verify it against the issuing secret,
and rate-limit attempts. For the same code in a two-factor flow see :doc:`mfa`; for
a numeric personal code, :doc:`pin`.
