Blood
=====

**Blood** matches an `ABO and Rh blood type <https://en.wikipedia.org/wiki/Blood_type>`__
— a group of ``A``, ``B``, ``AB``, or ``O``, followed by an Rh sign.

The construction is an :func:`~edify.any_of` over the four groups — with ``AB``
listed first so it is matched before the single letters — then an
:meth:`~edify.RegexBuilder.any_of_chars` over ``+`` and ``-``.

The eight types
---------------

.. edify-playground::

   from edify.library import blood

   blood("A+")
   blood("A-")
   blood("B+")
   blood("AB+")   # the universal recipient
   blood("O-")    # the universal donor

Group and sign are both required
--------------------------------

.. edify-playground::

   from edify.library import blood

   blood("O-")     # complete
   blood("O")      # no Rh sign
   blood("X+")     # not a blood group
   blood("a+")     # groups are uppercase
   blood("AB")     # no sign
   blood("")       # empty

Only the eight ABO/Rh combinations are covered — the other blood-group systems
(Kell, Duffy, and the rest) that matter for transfusion compatibility are not
represented here. A blood type is also protected health information: validate it
where you must, and never treat a shape check as clinical verification.
