CSRF token
==========

A `cross-site request forgery <https://owasp.org/www-community/attacks/csrf>`__
token is the unpredictable value a server embeds in a form and checks on submission,
proving the request came from its own page rather than an attacker's. Because it
must resist guessing, it is issued longer than a session handle: **CSRF token**
matches 32 to 128 characters of letters, digits, ``-``, and ``_``.

The construction is :meth:`~edify.RegexBuilder.between`\ ``(32, 128)`` over an
:meth:`~edify.RegexBuilder.any_of` class — the same URL-safe alphabet as
:doc:`session`, but with double the minimum length.

Framework formats
-----------------

Base64url and hex tokens both fit:

.. edify-playground::

   from edify.library import csrf

   csrf("kbyuFDidLLm280jXFEHRpQIXPCX2XmvW")           # a 32-character token
   csrf("Nn9Iv-yq_3xQ7ZwR2tKpLmXcVbNaSdFgHjKl")       # URL-safe characters
   csrf("a" * 128)                                     # at the maximum

Longer than a session handle
----------------------------

Thirty-two characters is the floor — anything shorter is inside brute-force range
for an attacker who can retry:

.. edify-playground::

   from edify.library import csrf

   csrf("a" * 32)    # at the minimum
   csrf("a" * 31)    # too short
   csrf("a" * 129)   # too long

Outside the alphabet
--------------------

Tokens travel in form fields and headers, so escaping-free characters only:

.. edify-playground::

   from edify.library import csrf

   csrf("abcdefghij0123456789abcdefghij12")   # valid
   csrf("abcdefghij+123456789abcdefghij12")   # + needs escaping in a form body
   csrf("abcdefghij 123456789abcdefghij12")   # a space

Shape is the least important property of a CSRF token — what matters is that it is
unpredictable, bound to the user's session, and compared in constant time on every
state-changing request. This validator cannot check any of that. Pair the token with
``SameSite`` cookies rather than relying on either alone. For the session it is bound
to see :doc:`session`.
