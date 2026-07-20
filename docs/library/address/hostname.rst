hostname
========

:doc:`Library <../index>` › :doc:`Address <index>` › **hostname**

``hostname`` matches an RFC 1123 hostname. It is close to :doc:`domain`, with two
differences: a bare single label is valid, and there is no letters-only TLD
requirement.

.. code-block:: python

   from edify.library import hostname

   hostname("db-01.internal")   # True

One or more labels
------------------

Labels of letters, digits, and interior hyphens, joined by dots — each 1–63
characters:

.. code-block:: python

   hostname("example.com")     # True
   hostname("db.internal")     # True
   hostname("host-1")          # True — a hyphen and a digit
   hostname("x-.com")          # False — a label can't end with a hyphen

Single labels are allowed
-------------------------

Unlike :doc:`domain`, ``hostname`` accepts a lone label with no dot and no TLD —
the names you meet on a LAN:

.. code-block:: python

   hostname("localhost")   # True
   hostname("gateway")     # True
   hostname("printer")     # True

Two length limits
-----------------

Two caps apply at once: a leading assertion holds the **whole name to 1–253
characters** (the DNS limit), and **each label** is at most **63** characters. So
a single 253-character label is rejected — the length has to be spread across
labels:

.. code-block:: python

   hostname("a" * 63)            # True  — a label at its 63-char maximum
   hostname("a" * 64)            # False — that label is one character too long
   hostname("a" * 63 + ".com")   # True  — 63-char label, then a short one

What it rejects
---------------

.. code-block:: python

   hostname("-bad")    # False — can't start with a hyphen
   hostname("a b")     # False — no spaces
   hostname("a..b")    # False — an empty label between dots

For a ``host:port`` pair use :doc:`socket`; for a name that must end in a real
TLD, :doc:`domain`.

Try it
------

.. edify-playground::
   :tests: example.com|localhost|host-1|db.internal|-bad|a b

   from edify.library import hostname
   hostname
