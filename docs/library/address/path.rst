path
====

.. edify-validator:: path

``path`` matches a filesystem path shape in three families — POSIX, Windows
drive-letter, and UNC. It is deliberately permissive: it matches the *form* of a
path, not whether it exists.

Under the hood it is an :func:`~edify.any_of` of those three shapes, anchored with
:meth:`~edify.RegexBuilder.start_of_input` / :meth:`~edify.RegexBuilder.end_of_input`.
The POSIX branch allows an optional ``/``, ``./``, or ``../`` prefix followed by
slash-separated segments; the Windows branch a drive letter and backslash
segments; the UNC branch a ``\\server\share``:

.. code-block:: python

   from edify import Pattern, any_of

   path = (
       Pattern().start_of_input()
       .use(any_of(posix_path, windows_path, unc_path))
       .end_of_input()
   )

POSIX paths
-----------

An optional ``/``, ``./``, or ``../`` prefix, then one or more slash-separated
segments — absolute or relative, with any depth of ``../``:

.. code-block:: python

   path("/usr/local/bin")   # True — absolute
   path("relative/dir")     # True — relative
   path("./config.yaml")    # True — dot-relative
   path("../../up/two")     # True — parent-relative

.. edify-playground::
   :tests: /usr/local/bin|relative/dir|./config.yaml|../../up/two

   from edify.library import path
   path

Windows and UNC paths
---------------------

A drive letter with backslash segments, or a ``\\server\share`` UNC path:

.. code-block:: python

   path("C:\\Windows\\System32")   # True — drive path
   path("D:\\data\\file.txt")      # True
   path("\\\\server\\share")       # True — UNC share

.. edify-playground::
   :tests: C:\Windows\System32|D:\data\file.txt|\\server\share

   from edify.library import path
   path

Deliberately permissive
-----------------------

Within a segment, ``path`` allows spaces and most punctuation, so it matches the
messy real-world names filesystems accept. The only string it rejects outright is
the empty one (and, on the POSIX side, control characters inside a segment):

.. code-block:: python

   path("my documents/report v2.txt")   # True — spaces are fine
   path("")                              # False — the empty string

.. edify-playground::
   :tests: my documents/report v2.txt|/etc/hosts|src/main.py

   from edify.library import path
   path

Notes
-----

- Because it is so permissive, ``path`` does not distinguish a path from arbitrary
  text with slashes; reach for it when you want the *shape*, not strict validation.
