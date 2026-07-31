API key
=======

An `API key <https://en.wikipedia.org/wiki/Application_programming_interface_key>`__
is a long-lived credential a client sends to identify itself. There is no standard
format — every provider invents its own — but the shape is consistent: a long,
URL-safe, opaque string. **API key** matches 20 to 128 characters of letters,
digits, ``-``, and ``_``.

The construction is :meth:`~edify.RegexBuilder.between`\ ``(20, 128)`` over an
:meth:`~edify.RegexBuilder.any_of` class of alphanumerics plus the two URL-safe
punctuation marks, anchored end to end. The 20-character floor is what separates a
key from an ordinary identifier.

Provider formats
----------------

Prefixed keys, raw random strings, and underscore-separated forms all fit:

.. edify-playground::

   from edify.library import apikey

   apikey("sk_live_51H8xQ2eZvKYlo2C0abcdef")     # a prefixed secret key
   apikey("AIzaSyD-abc123DEF456ghi789JKL")       # a raw provider key
   apikey("key-0123456789abcdef0123")            # hyphen separated

URL-safe characters only
------------------------

Keys travel in headers and query strings, so characters needing escaping are not
part of the alphabet:

.. edify-playground::

   from edify.library import apikey

   apikey("abcdefghij0123456789")     # the minimum length
   apikey("abcdefghij+123456789/")    # + and / need escaping
   apikey("abcdefghij 0123456789")    # a space
   apikey("abcdefghij.0123456789")    # a dot: see token

Length bounds
-------------

Under 20 characters there is not enough entropy to be a key; over 128 it is
something else:

.. edify-playground::

   from edify.library import apikey

   apikey("a" * 20)    # at the minimum
   apikey("a" * 128)   # at the maximum
   apikey("a" * 19)    # too short
   apikey("a" * 129)   # too long

Shape tells you nothing about validity — a matching key may be revoked, expired, or
belong to another tenant, so always check it against your store. Keys are bearer
credentials: transmit them only over TLS, never place them in a URL path that lands
in logs, and rotate them on exposure. For per-request tokens see :doc:`token`.
