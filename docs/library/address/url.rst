url
===

:doc:`Library <../index>` › :doc:`Address <index>` › **url**

``url`` matches a permissive HTTP/HTTPS web-URL shape: an optional
``http[s]://`` scheme, an optional ``www.`` prefix, a dotted host with a 1–6
character TLD, and an optional path/query tail.

.. code-block:: python

   from edify.library import url

   url("https://example.com")        # True
   url("http://a.io/path?q=1")       # True
   url("www.example.com")            # True — scheme optional
   url("notaurl")                    # False — no dotted host
   url("ftp://x")                    # False — HTTP/HTTPS only

What it matches
---------------

- An **optional** ``http://`` or ``https://`` scheme.
- An **optional** ``www.`` host prefix.
- A dot-separated authority ending in a **1–6 character** alphanumeric TLD.
- An **optional path, query, and fragment** tail after the host.
- Anchored at both ends.

It does **not** guarantee reachability, TLS validity, or DNS resolution, and it
does **not** match non-HTTP schemes such as ``ftp:``, ``mailto:``, or ``file:`` —
for those, or for the generic ``scheme:path`` shape, use :doc:`uri`. The pattern
is deliberately permissive rather than a full RFC 3986 grammar.

Try it
------

.. edify-playground::
   :tests: https://example.com|http://a.io/path?q=1|www.example.com|example.com/x|notaurl|ftp://x

   from edify.library import url
   url

Pattern
-------

.. code-block:: text

   ^(?:https?://)?(?:www\.)?[\-a-zA-Z0-9@:%\._\+\~\#=]{1,256}\.[a-zA-Z0-9\(\)]{1,6}\b[\-a-zA-Z0-9\(\)@:%_\+\.\~\#\?\&/=]*$
