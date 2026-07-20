path
====

:doc:`Library <../index>` › :doc:`Address <index>` › **path**

``path`` matches a filesystem path shape in three families: POSIX, Windows
drive-letter, and UNC. It is deliberately permissive — it matches the *form* of a
path, not whether it exists.

.. code-block:: python

   from edify.library import path

   path("/usr/local/bin")   # True

POSIX paths
-----------

An optional ``/``, ``./``, or ``../`` prefix, then one or more ``/``-separated
segments — absolute or relative, with any depth of ``../``:

.. code-block:: python

   path("/usr/local/bin")   # True — absolute
   path("relative/dir")     # True — relative
   path("./config.yaml")    # True — dot-relative
   path("../../up/two")     # True — parent-relative

Windows drive paths
-------------------

A drive letter, a colon, and backslash-separated segments:

.. code-block:: python

   path("C:\\Windows\\System32")   # True
   path("D:\\data\\file.txt")      # True

UNC shares
----------

A ``\\server\share`` path, with optional further segments:

.. code-block:: python

   path("\\\\server\\share")           # True
   path("\\\\nas\\media\\movies")      # True

Deliberately permissive
-----------------------

Within a segment, ``path`` allows spaces and most punctuation — so it matches the
messy real-world names filesystems accept. The only string it rejects outright is
the empty one (and, on the POSIX side, control characters inside a segment):

.. code-block:: python

   path("my documents/report v2.txt")   # True — spaces are fine
   path("")                              # False — the empty string

Because it is so permissive it does not distinguish a path from arbitrary text
with slashes; reach for it when you want the *shape*, not strict validation.

Try it
------

.. edify-playground::
   :tests: /usr/local/bin|relative/dir|./config.yaml|../../up/two|C:\Windows\System32

   from edify.library import path
   path
