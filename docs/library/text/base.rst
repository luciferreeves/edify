Base
====

**Base** matches a payload encoded in one of the common
`base-N <https://datatracker.ietf.org/doc/html/rfc4648>`__ alphabets (:rfc:`4648`):
base16, base32, base58, base64, or base64url. It is the check for "this field holds
encoded bytes" when you do not yet know which encoding produced it.

The five alphabets are the branches of an :func:`~edify.any_of`, tried in order:
hexadecimal, base32 with optional ``=`` padding, base58, standard base64 with
padding, and the URL-safe base64 variant. Because the alphabets overlap, a short
string may satisfy several — the first matching branch decides.

The five alphabets
------------------

.. edify-playground::

   from edify.library import base

   base("deadbeef")                                       # base16
   base("JBSWY3DPEB")                                     # base32
   base("1BvBMSEYstWetqTFn5Au4m4GFg7xJaNVN2")             # base58
   base("SGVsbG8gV29ybGQ=")                               # base64 with padding
   base("abc-def_ghi")                                    # base64url

Padding
-------

Base32 and base64 permit trailing ``=`` characters; the URL-safe form drops them:

.. edify-playground::

   from edify.library import base

   base("SGVsbG8=")     # padded
   base("SGVsbG8")      # unpadded
   base("JBSWY3DP===")  # base32 padding

Outside every alphabet
----------------------

Spaces and punctuation belong to no base-N alphabet:

.. edify-playground::

   from edify.library import base

   base("deadbeef")      # valid
   base("hello world")   # a space
   base("!!!")           # punctuation
   base("")              # empty

Matching tells you the characters *could* be base-N, not that the payload decodes —
length constraints and padding correctness are a decoder's job, and the overlap
between alphabets means a match does not identify which encoding was used. For hex
digests specifically see :doc:`../numeric/hash`.
