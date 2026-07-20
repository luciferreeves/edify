path
====

:doc:`Library <../index>` › :doc:`Address <index>` › **path**

``path`` matches a filesystem path shape — POSIX absolute or relative, a Windows
drive-letter path, or a UNC share.

.. code-block:: python

   from edify.library import path

   path("/usr/local/bin")      # True — POSIX absolute
   path("relative/dir")        # True — POSIX relative
   path("./config")            # True — dot-relative
   path("C:\\Windows\\System") # True — Windows drive
   path("\\\\server\\share")   # True — UNC

What it matches
---------------

- **POSIX**: an optional ``/``, ``./`` or ``../`` prefix, then one or more
  ``/``-separated segments.
- **Windows**: a ``C:\`` drive letter followed by backslash-separated segments.
- **UNC**: a ``\\server\share`` path.
- Anchored at both ends.

This validator is **deliberately permissive** — it matches the *shape* of a path,
so spaces and most punctuation are allowed inside segments. The only thing it
rejects outright is the empty string (and, on the POSIX side, control characters
inside a segment). It does not check that the path exists or is reachable.

Try it
------

.. edify-playground::
   :tests: /usr/local/bin|relative/dir|./config|C:\Windows\System|../up

   from edify.library import path
   path
