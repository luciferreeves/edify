Network atoms
=============

Seventeen fragments for addresses, hosts, and the pieces they are assembled from.
These are the atoms the :doc:`../../library/address/index` validators are built out
of — ``octet`` appears in :doc:`../../library/address/ipv4`, ``nibble`` in
:doc:`../../library/address/ipv6`, ``label`` in
:doc:`../../library/address/domain`.

Remember that atoms are unanchored: compose them with
:meth:`~edify.RegexBuilder.use` inside an anchored pattern rather than calling them
directly. See :doc:`index` for why.

The building blocks
-------------------

``nibble`` is a single hex digit and ``octet`` a number from 0 to 255 — the two
smallest network atoms, and the ones most worth knowing. ``label`` is one DNS name
segment: alphanumeric at both ends, hyphens allowed inside, up to 63 characters.

``octet`` is worth reading closely, because it shows how a numeric range is done
properly. It emits ``(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]\d|\d)`` — five disjoint
branches covering 0–255 with no overlap, so exactly one can ever apply. The lazy
approximation ``\d{1,3}`` would accept ``999``.

.. edify-playground::

   from edify import Pattern
   from edify.atoms import label, nibble, octet

   hex_digit = Pattern().start_of_input().use(nibble).end_of_input()
   number = Pattern().start_of_input().use(octet).end_of_input()
   segment = Pattern().start_of_input().use(label).end_of_input()

   hex_digit("f")        # one hex digit
   hex_digit("g")        # not hex
   number("255")         # the top of the range
   number("256")         # out of range
   segment("my-host")    # interior hyphens are fine
   segment("-bad")       # but not at the edges

Whole addresses
---------------

``ipv4``, ``ipv6``, ``cidr``, and ``mac`` are complete address fragments, ready to
embed in a larger pattern — a log-line parser, say, where the address is surrounded
by other text.

``ipv4`` is four ``octet`` branches joined by dots, so it carries the full range
check. ``mac`` accepts either separator, colon or hyphen, but requires one — a bare
twelve-hex-digit string does not match.

.. edify-playground::

   from edify import Pattern
   from edify.atoms import cidr, ipv4, mac

   v4 = Pattern().start_of_input().use(ipv4).end_of_input()
   block = Pattern().start_of_input().use(cidr).end_of_input()
   hardware = Pattern().start_of_input().use(mac).end_of_input()

   v4("192.168.0.1")
   v4("999.1.1.1")                # the octet range is enforced
   block("10.0.0.0/8")
   block("10.0.0.0/33")           # so is the prefix length
   hardware("00:1A:2B:3C:4D:5E")  # colons
   hardware("00-1A-2B-3C-4D-5E")  # or hyphens
   hardware("001A2B3C4D5E")       # but a separator is required

``cidr`` range-checks both halves: the address through ``octet``, and the prefix
length to ``0``-``32``.

``ipv6`` accepts the full eight-group form and every ``::``-compressed form,
wherever the compressed run falls:

.. edify-playground::

   from edify import Pattern
   from edify.atoms import ipv6

   v6 = Pattern().start_of_input().use(ipv6).end_of_input()

   v6("2001:db8:0:0:0:0:0:1")   # the full eight-group form
   v6("2001:db8::1")            # compressed in the middle
   v6("2001:db8::")             # compressed at the end
   v6("::1")                    # compressed at the start
   v6("::")                     # the unspecified address
   v6("1::2::3")                # but only one run may be compressed

The library validators still go further. :doc:`../../library/address/ipv6` also
accepts zone identifiers (``fe80::1%eth0``), the IPv4-mapped form
(``::ffff:192.168.0.1``), and the hybrid IPv4-suffix form — reach for it when your
input may carry any of those. The atoms are fragments for embedding, not
replacements for the validators.

Hosts and names
---------------

``hostname`` is a full dotted name — one or more ``label`` segments joined by dots,
so the per-label rules apply throughout. ``tld`` is the trailing letters-only
component, two to sixty-three characters. ``port`` range-checks 0–65535 the same
way ``octet`` checks 0–255, with disjoint branches rather than ``\d{1,5}``.

.. edify-playground::

   from edify import Pattern
   from edify.atoms import hostname, port, tld

   host = Pattern().start_of_input().use(hostname).end_of_input()
   suffix = Pattern().start_of_input().use(tld).end_of_input()
   number = Pattern().start_of_input().use(port).end_of_input()

   host("db.internal")
   host("localhost")    # a single label is a valid hostname
   host("-bad.com")     # label rules apply to every segment
   suffix("com")
   suffix("c0m")        # digits are not a TLD
   number("65535")      # the maximum
   number("65536")      # past it

Locators
--------

``uri`` and ``url`` match whole locators, and they differ in more than name.
``uri`` is a generic scheme followed by a non-space remainder, so it accepts
``mailto:`` and ``urn:`` as readily as ``https://``. ``url`` is specifically
``https?://`` — it will not match an FTP or mailto locator.

.. edify-playground::

   from edify import Pattern
   from edify.atoms import uri, url

   locator = Pattern().start_of_input().use(uri).end_of_input()
   web = Pattern().start_of_input().use(url).end_of_input()

   locator("mailto:me@example.dev")   # any scheme
   locator("urn:isbn:0451450523")
   web("https://example.dev/page")    # http and https only
   web("ftp://example.dev")           # not other schemes
   web("example.dev")                 # the scheme is required

Both stop at whitespace, which is what makes them usable for extracting a locator
from running text. Neither validates the structure after the scheme — for that,
:doc:`../../library/address/url` and :doc:`../../library/address/uri`.

Schemes, mail, and people
-------------------------

``scheme`` and ``protocol`` both match the leading part of a locator, and choosing
between them is a real decision. ``protocol`` is a **closed set** — ``https``,
``http``, ``ftps``, ``ftp``, ``wss``, ``ws``, ``ssh``, ``git``, ``file`` — while
``scheme`` accepts any letter-led scheme shape at all.

``email`` is a whole address in its permissive form; ``localpart`` is just the part
before the ``@``, capped at 64 characters; ``username`` is a 3–30 character handle
of letters, digits, dots, hyphens, and underscores.

.. edify-playground::

   from edify import Pattern
   from edify.atoms import email, localpart, protocol, scheme, username

   s = Pattern().start_of_input().use(scheme).end_of_input()
   p = Pattern().start_of_input().use(protocol).end_of_input()
   e = Pattern().start_of_input().use(email).end_of_input()
   local = Pattern().start_of_input().use(localpart).end_of_input()
   user = Pattern().start_of_input().use(username).end_of_input()

   s("https")           # any scheme shape
   s("gopher")          # including ones protocol does not list
   p("https")           # one of a known set
   p("gopher")          # not in the set
   e("a@b.com")
   local("first.last")
   user("alice")
   user("ab")           # three characters minimum

Use ``protocol`` when you are deciding what your code will *do* with a locator,
and ``scheme`` when you are only parsing. A closed set that silently grows is a
security problem; a closed set that rejects something you meant to support is a
bug you will notice immediately.

Next: :doc:`numbers`.
