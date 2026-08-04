Ref
===

A `ref <https://git-scm.com/book/en/v2/Git-Internals-Git-References>`__ is any name
that points at a commit — a branch, a tag, a full ``refs/`` path, or a raw hash.
**Ref** accepts all of them, which makes it the validator for a "revision" field
whose form you do not control.

The branches of the :func:`~edify.any_of` are a hex hash as in :doc:`git`, a full
``refs/heads|tags|remotes/…`` path, or a short name. The path and name branches use
:meth:`~edify.RegexBuilder.assert_not_ahead` to exclude the characters git forbids in
a ref: whitespace, ``~``, ``^``, ``:``, ``?``, ``*``, ``[``, and ``\``.

Names and paths
---------------

.. edify-playground::

   from edify.library import ref

   ref("main")                    # a branch name
   ref("v1.0.0")                  # a tag
   ref("feature/new-login")       # a namespaced branch
   ref("refs/heads/main")         # the full path
   ref("refs/tags/v1.0.0")
   ref("refs/remotes/origin/main")

Hashes too
----------

.. edify-playground::

   from edify.library import ref

   ref("e83c516")   # an abbreviated hash
   ref("a" * 40)    # a full hash

Forbidden characters
--------------------

Git rejects these because they carry meaning in revision syntax:

.. edify-playground::

   from edify.library import ref

   ref("main")            # valid
   ref("bad name")        # whitespace
   ref("bad~name")        # ~ selects an ancestor
   ref("bad^name")        # ^ selects a parent
   ref("bad:name")        # : separates a path
   ref("")                # empty

Not every rule is covered — git also forbids a leading dot, a trailing ``.lock``, and
consecutive dots — so ``git check-ref-format`` remains the authority. For hashes
alone see :doc:`git`.
