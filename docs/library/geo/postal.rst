Postal
======

**Postal** matches a `postal code <https://en.wikipedia.org/wiki/Postal_code>`__ from
any of several national systems — the US, UK, Canada, the Netherlands, Japan, and the
common continental five-digit form. It is the validator for an address form that
accepts international addresses.

The national layouts are the branches of an :func:`~edify.any_of`, each spelling out
that country's letter-and-digit arrangement: the UK's ``SW1A 1AA``, Canada's
alternating ``K1A 0B1``, the Dutch ``1234 AB``, Japan's ``100-0001``, and the plain
digit runs.

National formats
----------------

.. edify-playground::

   from edify.library import postal

   postal("12345")        # United States
   postal("12345-6789")   # US ZIP+4
   postal("SW1A 1AA")     # United Kingdom
   postal("K1A 0B1")      # Canada
   postal("1234 AB")      # Netherlands
   postal("100-0001")     # Japan
   postal("75001")        # France

Not any string
--------------

.. edify-playground::

   from edify.library import postal

   postal("12345")    # a recognised format
   postal("abc")      # letters alone
   postal("")         # empty

Two caveats. Accepting many formats means a code valid in one country may be accepted
for another — the pattern cannot tell which country an address is in, so pair it with
the country field. And matching the shape does not mean the code exists; only a
postal database can confirm that. For US codes specifically see
:doc:`../address/zip_code`.
