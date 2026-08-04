Token
=====

An opaque `access token <https://datatracker.ietf.org/doc/html/rfc6749#section-1.4>`__
is a credential with no meaning to the client — it is a handle the server looks up.
**Token** matches 24 to 256 characters of letters, digits, ``-``, ``_``, and ``.``,
which covers both random opaque strings and dotted structured tokens.

The construction is :meth:`~edify.RegexBuilder.between`\ ``(24, 256)`` over an
:meth:`~edify.RegexBuilder.any_of` class. Including ``.`` means a :doc:`jwt` also
satisfies this shape — deliberately, since an access token may be either.

Opaque and structured
---------------------

Random handles, prefixed tokens, and dotted forms all match:

.. edify-playground::

   from edify.library import token

   token("gho_16C7e42F292c6912E7710c838347Ae178B4a")   # a prefixed opaque token
   token("dGhpcy1pcy1hLXRva2VuLXZhbHVl")                # a base64url handle
   token("eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIxIn0.sig")    # a JWT also fits

The permitted alphabet
----------------------

Letters, digits, and the three safe punctuation marks — anything requiring escaping
is out:

.. edify-playground::

   from edify.library import token

   token("abc.def-ghi_jkl012345678901")   # all three marks
   token("abc+def/ghi=012345678901234")   # + / = need escaping
   token("abc def ghi 012345678901234")   # spaces

Length bounds
-------------

Twenty-four characters is the floor for adequate entropy; 256 the practical ceiling
for a header value:

.. edify-playground::

   from edify.library import token

   token("a" * 24)    # at the minimum
   token("a" * 256)   # at the maximum
   token("a" * 23)    # too short
   token("a" * 257)   # too long

An opaque token carries no verifiable structure, so shape is all you can check
locally — validity, scope, and expiry live in the issuing server, and it must be
consulted on every request. For the header wrapping see :doc:`bearer`, for the
long-lived renewal credential :doc:`refresh`, and for signed self-contained tokens
:doc:`jwt`.
