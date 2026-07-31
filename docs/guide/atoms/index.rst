Atoms
=====

An **atom** is a named, reusable regex fragment — the smallest meaningful piece of a
pattern. ``edify.atoms`` ships 83 of them: a ``nibble`` is one hex digit, an
``octet`` is a number from 0 to 255, a ``label`` is one DNS name segment.

Atoms are what the :doc:`../../library/index` validators are built from. The
:doc:`../../library/address/ipv4` validator is four ``octet`` atoms joined by dots;
:doc:`../../library/address/ipv6` is ``nibble`` atoms grouped into hex groups. When
you build your own pattern, reach for an atom before writing the character class by
hand.

Atoms are fragments, not validators
-----------------------------------

This is the one thing to understand before using them. A :doc:`../../library/index`
validator is **anchored** — it matches the whole string. An atom is **not**: it is a
fragment meant to sit inside a larger pattern, so calling one directly searches
rather than matching end to end.

.. edify-playground::

   from edify.atoms import slug

   slug("hello-world")        # the whole string is a slug
   slug("xx hello-world xx")  # True as well — it found a slug inside

That second result is the trap. To ask "is this string *exactly* an octet?", compose
the atom into an anchored pattern:

.. edify-playground::

   from edify import Pattern
   from edify.atoms import octet

   exact = Pattern().start_of_input().use(octet).end_of_input()

   exact("200")   # a valid octet
   exact("255")   # the maximum
   exact("256")   # out of range
   exact("x200")  # anchoring rejects the surrounding text

Composing them
--------------

Drop an atom into a chain with :meth:`~edify.RegexBuilder.use`, repeat it with a
quantifier, or join several — exactly as the library validators do:

.. edify-playground::

   from edify import Pattern
   from edify.atoms import octet

   quad = (
       Pattern().start_of_input()
       .use(octet).exactly(3).group().char(".").use(octet).end()
       .end_of_input()
   )

   quad("192.168.0.1")   # four octets
   quad("256.0.0.1")     # the octet range still applies
   quad("1.2.3")         # only three

The eight groups
----------------

.. toctree::
   :hidden:

   network
   numbers
   text
   encodings
   datetime
   web
   finance
   grouping

- :doc:`network` — addresses, hosts, ports, and the pieces they are made of.
- :doc:`numbers` — integers, decimals, bases, and money.
- :doc:`text` — characters, classes, and simple word shapes.
- :doc:`encodings` — base-N alphabets, hashes, and unique identifiers.
- :doc:`datetime` — date, time, and duration components.
- :doc:`web` — HTTP methods and statuses, media types, file names, colours.
- :doc:`finance` — payment and banking fragments, plus version numbers.
- :doc:`grouping` — bracket-delimited spans.
