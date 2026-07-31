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

.. edify-playground::

   from edify import Pattern
   from edify.atoms import nibble, octet, label

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

.. edify-playground::

   from edify import Pattern
   from edify.atoms import ipv4, ipv6, cidr, mac

   v4 = Pattern().start_of_input().use(ipv4).end_of_input()
   v6 = Pattern().start_of_input().use(ipv6).end_of_input()
   block = Pattern().start_of_input().use(cidr).end_of_input()
   hardware = Pattern().start_of_input().use(mac).end_of_input()

   v4("192.168.0.1")
   v4("999.1.1.1")
   v6("2001:db8::1")
   block("10.0.0.0/8")
   hardware("00:1A:2B:3C:4D:5E")

Hosts and names
---------------

``hostname`` is a full dotted name, ``tld`` the trailing letters-only component, and
``label`` a single segment. ``port`` range-checks 0–65535.

.. edify-playground::

   from edify import Pattern
   from edify.atoms import hostname, tld, port

   host = Pattern().start_of_input().use(hostname).end_of_input()
   suffix = Pattern().start_of_input().use(tld).end_of_input()
   number = Pattern().start_of_input().use(port).end_of_input()

   host("db.internal")
   host("localhost")
   suffix("com")
   suffix("c0m")        # digits are not a TLD
   number("65535")      # the maximum
   number("65536")      # past it

Locators and mail
-----------------

``uri`` and ``url`` match whole locators; ``scheme`` and ``protocol`` match just the
leading part. ``email``, ``localpart``, and ``username`` cover addressing people.

.. edify-playground::

   from edify import Pattern
   from edify.atoms import scheme, protocol, email, localpart, username

   s = Pattern().start_of_input().use(scheme).end_of_input()
   p = Pattern().start_of_input().use(protocol).end_of_input()
   e = Pattern().start_of_input().use(email).end_of_input()
   local = Pattern().start_of_input().use(localpart).end_of_input()
   user = Pattern().start_of_input().use(username).end_of_input()

   s("https")           # any scheme shape
   p("https")           # one of a known set
   p("gopher")          # not in the set
   e("a@b.com")
   local("first.last")
   user("alice")

The ``protocol`` atom is a closed set — ``https``, ``http``, ``ftps``, ``ftp``,
``wss``, ``ws``, ``ssh``, ``git``, ``file`` — while ``scheme`` accepts any
letter-led scheme shape. Reach for whichever matches your intent.

Next: :doc:`numbers`.
