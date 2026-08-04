Plus code
=========

An `Open Location Code <https://maps.google.com/pluscodes/>`__ — a "plus code" —
encodes a position as a short string with a ``+`` before the last few characters. It
was designed for places without street addresses. **Plus code** matches that format.

The construction is 2 to 8 characters of the code alphabet, a literal ``+``, then 2
or 3 more, with an :meth:`~edify.RegexBuilder.optional` locality suffix. The alphabet
is a restricted set of 20 digits and consonants — vowels are excluded so that codes
cannot accidentally spell words.

Full and short codes
--------------------

.. edify-playground::

   from edify.library import plus

   plus("849VCWC8+R9")      # a full code
   plus("8FVC9G8F+6W")
   plus("CWC8+R9")          # a shortened code
   plus("849VCWC8+R9X")     # extra precision

With a locality
---------------

A shortened code is paired with a town name to disambiguate it:

.. edify-playground::

   from edify.library import plus

   plus("CWC8+R9 Mountain View")
   plus("9G8F+6W Zurich")

The restricted alphabet
-----------------------

.. edify-playground::

   from edify.library import plus

   plus("849VCWC8+R9")   # valid characters
   plus("849AEIOU+R9")   # vowels are excluded
   plus("849VCWC8")      # no plus sign
   plus("")              # empty

A shortened code is only meaningful with its locality — on its own it repeats every
few hundred kilometres. This validator does not check the code's internal
consistency, so decode it to confirm it names a real position.
