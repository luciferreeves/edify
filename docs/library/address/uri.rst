uri
===

:doc:`Library <../index>` › :doc:`Address <index>` › **uri**

``uri`` matches the generic URI shape — a scheme, a colon, and a non-empty
remainder. Unlike :doc:`url`, it accepts *any* scheme, not just HTTP.

.. code-block:: python

   from edify.library import uri

   uri("mailto:jane@example.com")   # True

Any scheme
----------

The scheme starts with a letter and may contain letters, digits, ``+``, ``.``,
and ``-``; after the ``:`` comes any run of non-whitespace. That covers the whole
family of URI schemes:

.. code-block:: python

   uri("https://example.com")        # True — web
   uri("mailto:jane@example.com")    # True — email
   uri("tel:+15551234567")           # True — telephone
   uri("urn:isbn:0451450523")        # True — a URN
   uri("ftp://host/file.txt")        # True — file transfer

What it rejects
---------------

.. code-block:: python

   uri("no scheme")     # False — there is no scheme + colon
   uri("ht tp://x")     # False — a space breaks the scheme
   uri("http:")         # False — the part after the colon is empty

For the narrower HTTP/HTTPS web-URL shape — with an optional scheme, a ``www.``
prefix, and a validated short TLD — use :doc:`url`.

Try it
------

.. edify-playground::
   :tests: https://example.com|mailto:jane@example.com|tel:+15551234567|urn:isbn:0451450523|no scheme

   from edify.library import uri
   uri
