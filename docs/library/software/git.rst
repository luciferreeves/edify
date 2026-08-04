Git
===

A `commit hash <https://git-scm.com/book/en/v2/Git-Internals-Git-Objects>`__ names a
commit by the SHA-1 of its content. **Git** matches the full 40-character hash and
the abbreviated forms tools print, from 7 characters up.

The construction is :meth:`~edify.RegexBuilder.between`\ ``(7, 40)`` over an
:meth:`~edify.RegexBuilder.any_of` class of ``0``–``9`` and ``a``–``f``. Lowercase
only, because that is how the hashes are written.

Full and abbreviated
--------------------

.. edify-playground::

   from edify.library import git

   git("a" * 40)                                # a full hash
   git("e83c516")                               # the seven-character short form
   git("e83c5163316f89bfbde7d9ab23ca2e25604af290")
   git("1a2b3c4d")                              # any length in between

Lowercase hex, within range
---------------------------

.. edify-playground::

   from edify.library import git

   git("e83c516")     # valid
   git("E83C516")     # uppercase
   git("e83c51")      # six characters: too short
   git("HEAD")        # a symbolic name: see ref
   git("")            # empty

Two things this cannot tell you: whether the commit exists in your repository, and —
for short forms — whether it is unambiguous, since an abbreviation only identifies a
commit if no other hash shares the prefix. Note also that repositories using SHA-256
object names have 64-character hashes, which exceed this range. For branches and tags
see :doc:`ref`.
