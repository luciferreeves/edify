path
====

``path`` recognises three families of filesystem path and is deliberately
permissive within each — it matches the *shape* of a path, not whether the file
exists. The only thing it rejects outright is the empty string.

.. edify-playground::
   :tests: /usr/local/bin|relative/dir|./config.yaml|../../up/two|C:\Windows\System32|\\server\share

   from edify.library import path
   path

POSIX
   An optional ``/``, ``./``, or ``../`` prefix, then slash-separated segments —
   absolute (``/usr/local/bin``), relative (``relative/dir``), or parent-relative
   to any depth (``../../up/two``). Spaces and most punctuation are fine inside a
   segment, so ``my documents/report v2.txt`` matches.

Windows
   A drive letter, a colon, and backslash segments — ``C:\Windows\System32``,
   ``D:\data\file.txt``.

UNC
   A ``\\server\share`` network path, with optional further segments.

The three are an :func:`~edify.any_of`, anchored at both ends. Because it is so
permissive, ``path`` won't distinguish a real path from arbitrary slashed text —
reach for it when you want the shape, not strict validation.
