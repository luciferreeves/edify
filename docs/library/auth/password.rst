Password
========

**Password** is the one validator in the library that is not a regular expression.
Counting character classes and comparing thresholds is not something a pattern can
do cleanly, so it is a :class:`~edify.Pattern` subclass with its own ``__call__`` —
which is why reading its emitted regex shows an empty pattern. Call it instead.

Its default policy follows the shape most services use: 8 to 64 characters, with at
least one uppercase letter, one lowercase letter, one digit, and one special
character from ``!@#$%^&*()_+-=[]{}|;':",./<>?``. Every threshold is also
overridable per call.

The default policy
------------------

All four classes must be present, and the length must fall in range:

.. edify-playground::

   from edify.library import password

   password("Str0ng!Pass")    # all four classes
   password("passw0rd!")      # no uppercase
   password("PASSW0RD!")      # no lowercase
   password("StrongPass!")    # no digit
   password("Str0ngPass")     # no special character
   password("Ab1!")           # shorter than eight

Tightening the policy
---------------------

Any threshold can be raised for a single call, which is how you apply a stricter
rule to administrators or to a password-change form:

.. edify-playground::

   from edify.library import password

   password("Str0ng!Pass", min_length=12)               # too short under the stricter rule
   password("Much-L0nger!Passphrase", min_length=12)    # long enough
   password("Str0ng!Pass", min_special=2)               # only one special character
   password("Str0ng!!Pass", min_special=2)              # two now

Relaxing it, and custom specials
--------------------------------

Thresholds can be lowered too, and the set of characters that counts as "special"
is replaceable — useful when a downstream system rejects some punctuation:

.. edify-playground::

   from edify.library import password

   password("simplepass", min_upper=0, min_digit=0, min_special=0)
   password("Pass#word1", special_chars="#")     # only # counts as special
   password("Pass!word1", special_chars="#")     # ! no longer counts

Counting character classes is a weak measure of strength: ``Password1!`` satisfies
every default threshold and is among the most breached passwords in existence. This
enforces a policy, not safety — pair it with a breached-password check, allow long
passphrases, and always store a slow hash rather than the value itself. For short
numeric secrets see :doc:`pin`; for recovery phrases, :doc:`mnemonic`.
