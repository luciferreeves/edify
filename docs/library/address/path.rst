path
====

``path`` recognises three families of filesystem path — POSIX, Windows, and UNC —
and is deliberately permissive within each: it matches the *shape* of a path, not
whether the file exists. The only string it rejects outright is the empty one.

POSIX paths
-----------

An optional ``/``, ``./``, or ``../`` prefix, then slash-separated segments —
absolute, relative, or parent-relative to any depth. Spaces and most punctuation
are fine inside a segment:

.. code-block:: python

   path("/usr/local/bin")               # True — absolute
   path("relative/dir")                 # True — relative
   path("./config.yaml")                # True — dot-relative
   path("../../up/two")                 # True — parent-relative
   path("my documents/report v2.txt")   # True — spaces are allowed

.. edify-playground::
   :tests: /usr/local/bin|relative/dir|./config.yaml|../../up/two|my documents/report.txt

   from edify.library import path
   path

Windows and UNC paths
---------------------

A drive letter with backslash segments, or a ``\\server\share`` UNC path:

.. code-block:: python

   path("C:\\Windows\\System32")   # True — drive path
   path("D:\\data\\file.txt")      # True
   path("\\\\server\\share")       # True — UNC share
   path("\\\\nas\\media\\movies")  # True

.. edify-playground::
   :tests: C:\Windows\System32|D:\data\file.txt|\\server\share|\\nas\media\movies

   from edify.library import path
   path

The three families are an :func:`~edify.any_of`, anchored at both ends. Because it
is so permissive — only the empty string, and POSIX control characters inside a
segment, are rejected — ``path`` won't distinguish a real path from arbitrary
slashed text. Reach for it when you want the shape, not strict validation.
