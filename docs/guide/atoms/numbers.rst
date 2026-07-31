Number atoms
============

Fourteen fragments for numeric values — whole numbers, decimals, alternative bases,
and money. They are the pieces behind the
:doc:`../../library/numeric/index` validators.

As always, compose them into an anchored pattern rather than calling them directly;
see :doc:`index`.

Whole numbers
-------------

``unsigned`` is bare digits, ``signed`` requires a sign, ``integer`` makes the sign
optional, and ``natural`` excludes zero and leading zeros.

.. edify-playground::

   from edify import Pattern
   from edify.atoms import unsigned, signed, integer, natural

   u = Pattern().start_of_input().use(unsigned).end_of_input()
   s = Pattern().start_of_input().use(signed).end_of_input()
   i = Pattern().start_of_input().use(integer).end_of_input()
   n = Pattern().start_of_input().use(natural).end_of_input()

   u("42")      # digits only
   u("-42")     # no sign allowed
   s("-42")     # a sign is required
   s("42")      # so a bare number fails
   i("-42")     # either way
   i("42")
   n("42")      # positive, no leading zero
   n("0")       # zero is not natural

Decimals and exponents
----------------------

``decimal`` requires a fractional part, ``floatnum`` accepts any of the float forms,
and ``scientific`` requires an exponent.

.. edify-playground::

   from edify import Pattern
   from edify.atoms import decimal, floatnum, scientific

   d = Pattern().start_of_input().use(decimal).end_of_input()
   f = Pattern().start_of_input().use(floatnum).end_of_input()
   sci = Pattern().start_of_input().use(scientific).end_of_input()

   d("3.5")       # a fractional part is required
   d("3")         # so an integer fails
   f("3")         # floatnum accepts both
   f("1.2e-9")
   sci("1.2e9")   # an exponent is required
   sci("1.2")     # so a plain decimal fails

Other bases
-----------

``hexnum``, ``octnum``, and ``binnum`` match prefixed literals, exactly as a
programming language writes them.

.. edify-playground::

   from edify import Pattern
   from edify.atoms import hexnum, octnum, binnum

   h = Pattern().start_of_input().use(hexnum).end_of_input()
   o = Pattern().start_of_input().use(octnum).end_of_input()
   b = Pattern().start_of_input().use(binnum).end_of_input()

   h("0xFF")      # the 0x prefix is required
   h("FF")        # a bare hex string is hexstring, not hexnum
   o("0o755")
   b("0b1010")
   b("1010")      # likewise

Proportions and money
---------------------

``percent`` and ``ratio`` express relationships; ``money`` pairs an amount with a
``currency`` code on either side.

.. edify-playground::

   from edify import Pattern
   from edify.atoms import percent, ratio, money, currency

   pc = Pattern().start_of_input().use(percent).end_of_input()
   r = Pattern().start_of_input().use(ratio).end_of_input()
   m = Pattern().start_of_input().use(money).end_of_input()
   c = Pattern().start_of_input().use(currency).end_of_input()

   pc("99.9%")      # the sign is required
   r("16:9")
   m("USD 100")     # code first
   m("100 USD")     # or amount first
   c("USD")
   c("usd")         # codes are uppercase

Next: :doc:`text`.
