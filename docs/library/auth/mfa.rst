MFA code
========

A `multi-factor <https://en.wikipedia.org/wiki/Multi-factor_authentication>`__
verification code is the numeric second factor a user types after their password —
from an authenticator app, an SMS, or a hardware token. **MFA code** matches 6 to 8
decimal digits, the range every mainstream issuer uses.

The construction is :meth:`~edify.RegexBuilder.between`\ ``(6, 8)`` over
:meth:`~edify.RegexBuilder.digit`, anchored at both ends so the whole input must be
the code. It is deliberately narrower than :doc:`otp`, which also accepts
alphanumeric codes.

Digits only
-----------

Six is the common length; seven and eight appear on some hardware tokens:

.. edify-playground::

   from edify.library import mfa

   mfa("123456")     # six digits
   mfa("1234567")    # seven
   mfa("12345678")   # eight
   mfa("000123")     # leading zeros are part of the code

Nothing but digits
------------------

Letters, spaces, and the grouping punctuation some interfaces display are not part
of the value — strip them before validating:

.. edify-playground::

   from edify.library import mfa

   mfa("123456")    # the raw value
   mfa("123 456")   # a display space
   mfa("123-456")   # a display hyphen
   mfa("A1B2C3")    # alphanumeric: use otp
   mfa("12345")     # too short

A matching code proves nothing on its own — it must be checked against the user's
shared secret within its time window, and repeated attempts must be limited, or the
six-digit space is trivially brute-forced. For the alphanumeric variant see
:doc:`otp`.
