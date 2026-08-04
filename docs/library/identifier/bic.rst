BIC
===

A `BIC <https://www.iso.org/standard/60390.html>`__ — also called a SWIFT code —
identifies a bank: four letters for the institution, two for the country, two for the
location, and optionally three more for a branch. **BIC** matches both the 8- and
11-character forms.

The construction is four :meth:`~edify.RegexBuilder.uppercase` characters, two more
for the country, two alphanumerics for the location, then an
:meth:`~edify.RegexBuilder.optional` three-character branch code.

Institution codes
-----------------

.. edify-playground::

   from edify.library import bic

   bic("DEUTDEFF")       # Deutsche Bank, Frankfurt
   bic("DEUTDEFF500")    # with a branch code
   bic("NEDSZAJJ")       # South Africa
   bic("CHASUS33")       # a location code with digits

Structure is fixed
------------------

Eight or eleven characters — never ten, never nine:

.. edify-playground::

   from edify.library import bic

   bic("DEUTDEFF")      # eight
   bic("DEUTDEFF500")   # eleven
   bic("DEUTDEFF5")     # nine
   bic("DEUT1EFF")      # the country code must be letters
   bic("deutdeff")      # lowercase
   bic("")              # empty

A BIC has no check digit, so the shape is genuinely all you can verify offline —
whether a code is registered requires the SWIFT directory. For the account number it
accompanies see :doc:`iban`.
