Number atoms
============

Fourteen fragments for numeric values — whole numbers, decimals, alternative bases,
and money. They are the pieces behind the
:doc:`../../library/numeric/index` validators.

As always, compose them into an anchored pattern rather than calling them directly;
see :doc:`index`.

Whole numbers
-------------

Four atoms cover the integers, and they differ only in what they do about the sign
and about zero:

.. list-table::
   :header-rows: 1
   :widths: 18 22 60

   * - Atom
     - Emits
     - Accepts
   * - ``unsigned``
     - ``\d+``
     - digits only — no sign, leading zeros allowed
   * - ``signed``
     - ``[+-]\d+``
     - a sign is **required**
   * - ``integer``
     - ``[+-]?\d+``
     - sign optional — the general-purpose choice
   * - ``natural``
     - ``[1-9]\d*``
     - 1 upward, no sign, no leading zeros

``natural`` is the one that surprises people: because it starts with ``[1-9]``, it
rejects ``0`` *and* rejects ``007``. That is what makes it right for a quantity or
an identifier where a padded number would be a different value.

.. edify-playground::

   from edify import Pattern
   from edify.atoms import integer, natural, signed, unsigned

   u = Pattern().start_of_input().use(unsigned).end_of_input()
   s = Pattern().start_of_input().use(signed).end_of_input()
   i = Pattern().start_of_input().use(integer).end_of_input()
   n = Pattern().start_of_input().use(natural).end_of_input()

   u("42")      # digits only
   u("007")     # leading zeros are fine here
   u("-42")     # no sign allowed
   s("-42")     # a sign is required
   s("42")      # so a bare number fails
   i("-42")     # either way
   i("42")
   n("42")      # positive, no leading zero
   n("0")       # zero is not natural
   n("007")     # and padding is not either

None of the four accepts a decimal point — ``integer("4.2")`` is False. Reach for
the next section when the value may have a fractional part.

Decimals and exponents
----------------------

``decimal`` is ``\d+\.\d+`` — digits on **both** sides of the point are required,
so ``.5`` and ``3.`` are both rejected along with the bare integer ``3``.

``floatnum`` is the permissive one, accepting an optional sign, an optional
fraction, and an optional exponent in one pattern. ``scientific`` is the same shape
with the exponent made mandatory.

.. edify-playground::

   from edify import Pattern
   from edify.atoms import decimal, floatnum, scientific

   d = Pattern().start_of_input().use(decimal).end_of_input()
   f = Pattern().start_of_input().use(floatnum).end_of_input()
   sci = Pattern().start_of_input().use(scientific).end_of_input()

   d("3.5")       # a fractional part is required
   d("3")         # so an integer fails
   d(".5")        # and so does a bare fraction
   f("3")         # floatnum accepts every float form
   f("+3.5")
   f("1.2e-9")
   sci("1.2e9")   # an exponent is required
   sci("1E9")     # either case of e
   sci("1.2")     # so a plain decimal fails

The three overlap deliberately: every ``decimal`` and every ``scientific`` is also
a ``floatnum``. Pick the narrowest one that describes your field, so the pattern
carries the constraint instead of your validation code.

Other bases
-----------

``hexnum``, ``octnum``, and ``binnum`` match prefixed literals, exactly as a
programming language writes them — and the prefix is required in each case. Both
letter cases of the prefix work, so ``0XFF`` matches as readily as ``0xFF``.

.. edify-playground::

   from edify import Pattern
   from edify.atoms import binnum, hexnum, octnum

   h = Pattern().start_of_input().use(hexnum).end_of_input()
   o = Pattern().start_of_input().use(octnum).end_of_input()
   b = Pattern().start_of_input().use(binnum).end_of_input()

   h("0xFF")      # the 0x prefix is required
   h("0XfF")      # either case, either case of digits
   h("FF")        # a bare hex string is hexstring, not hexnum
   o("0o755")
   b("0b1010")
   b("1010")      # likewise

For a bare run of hex digits with no prefix — a hash, a colour, a byte string —
the atom you want is ``hexstring``, covered in :doc:`encodings`.

Proportions and money
---------------------

``percent`` is a number with a trailing sign, and the fractional part is optional.
``ratio`` is exactly two colon-separated runs of digits, so a three-part ratio like
``16:9:3`` does not match.

``money`` pairs an amount with a three-letter ``currency`` code on **either** side,
with the separating space optional — all four of ``USD 100``, ``USD100``,
``100 USD``, and ``100USD`` match. The code must be uppercase, because ``currency``
is ``[A-Z]{3}``.

.. edify-playground::

   from edify import Pattern
   from edify.atoms import currency, money, percent, ratio

   pc = Pattern().start_of_input().use(percent).end_of_input()
   r = Pattern().start_of_input().use(ratio).end_of_input()
   m = Pattern().start_of_input().use(money).end_of_input()
   c = Pattern().start_of_input().use(currency).end_of_input()

   pc("99.9%")      # the sign is required
   pc("99%")        # the fraction is not
   r("16:9")
   r("16:9:3")      # two parts only
   m("USD 100")     # code first
   m("100 USD")     # or amount first
   m("USD100")      # the space is optional
   c("USD")
   c("usd")         # codes are uppercase

``currency`` checks the *shape* of a code, not that it is a real one — ``XYZ``
matches. If you need the registered set, check the match against a list of codes
after the pattern accepts it.

Next: :doc:`text`.
