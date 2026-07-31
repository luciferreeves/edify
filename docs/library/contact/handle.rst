Handle
======

A `handle <https://en.wikipedia.org/wiki/User_(computing)#Username>`__ is the public,
``@``-prefixed name people use to mention each other on social platforms. **Handle** requires the ``@`` and allows 1 to 30 characters of
letters, digits, and underscore after it — a narrower alphabet than
:doc:`username`, which also permits dots and hyphens.

The construction is a literal ``@`` via :meth:`~edify.RegexBuilder.char`, then
:meth:`~edify.RegexBuilder.between`\ ``(1, 30)`` over an
:meth:`~edify.RegexBuilder.any_of` class of alphanumerics and underscore.

With the prefix
---------------

.. edify-playground::

   from edify.library import handle

   handle("@alice")        # a simple handle
   handle("@user_name")    # an underscore
   handle("@a")            # a single character is enough
   handle("@user2024")     # digits

The ``@`` is required
---------------------

That prefix is the whole difference from a username — a bare name is not a handle:

.. edify-playground::

   from edify.library import handle

   handle("@alice")   # prefixed
   handle("alice")    # no prefix
   handle("@")        # nothing after the prefix

Alphabet and length
-------------------

Dots and hyphens are not part of a handle, and 30 characters is the ceiling:

.. edify-playground::

   from edify.library import handle

   handle("@a" + "b" * 29)   # at the maximum
   handle("@a" + "b" * 30)   # too long
   handle("@user.name")      # a dot: see username
   handle("@user-name")      # a hyphen: see username

As with :doc:`username`, look-alike characters make impersonation easy — compare
handles on a normalised form. For the account-name variant see :doc:`username`.
