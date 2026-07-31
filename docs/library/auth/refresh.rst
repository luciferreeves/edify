Refresh token
=============

A `refresh token <https://datatracker.ietf.org/doc/html/rfc6749#section-1.5>`__
outlives the short-lived access token it renews, so it is issued longer and from a
wider alphabet. **Refresh token** matches 32 to 512 characters of letters, digits,
and the punctuation ``.`` ``_`` ``-`` ``~`` ``+`` ``/`` ``=`` — the union of the
URL-safe and standard base64 sets, because providers differ.

The construction is :meth:`~edify.RegexBuilder.between`\ ``(32, 512)`` over an
:meth:`~edify.RegexBuilder.any_of` class. The 32-character floor is double
:doc:`token`'s, reflecting the higher value of a credential that mints new access
tokens.

Provider formats
----------------

Both base64 alphabets, with or without padding:

.. edify-playground::

   from edify.library import refresh

   refresh("1//0eXaMPle-refresh_token.value~here+more/data=")   # mixed alphabet
   refresh("v1.MRefreshTokenValueGoesHere0123456789")           # a dotted form
   refresh("a" * 512)                                           # at the maximum

Length bounds
-------------

.. edify-playground::

   from edify.library import refresh

   refresh("a" * 32)    # at the minimum
   refresh("a" * 31)    # too short
   refresh("a" * 513)   # too long

Outside the alphabet
--------------------

Spaces and characters that would need escaping in a form body are not part of a
refresh token:

.. edify-playground::

   from edify.library import refresh

   refresh("abcdefghij0123456789abcdefghij12")    # valid
   refresh("abcdefghij 123456789abcdefghij12")    # a space
   refresh("abcdefghij#123456789abcdefghij12")    # a fragment marker

A refresh token is the most valuable credential in an OAuth flow — it survives
access-token expiry, so treat leakage as a full compromise. Store it server-side or
in secure storage, rotate on every use, and revoke the whole chain if one is
replayed. For the access token it renews see :doc:`token`.
