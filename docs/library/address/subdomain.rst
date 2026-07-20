subdomain
=========

:doc:`Library <../index>` › :doc:`Address <index>` › **subdomain**

``subdomain`` matches a **single** DNS label — the ``api`` in
``api.example.com`` — not a dotted name.

.. code-block:: python

   from edify.library import subdomain

   subdomain("api")   # True

A single label
--------------

Letters and digits, with hyphens allowed only in the interior. The first and last
characters must be alphanumeric:

.. code-block:: python

   subdomain("api")        # True
   subdomain("my-sub")     # True — interior hyphen
   subdomain("staging-2")  # True — digits and hyphen
   subdomain("a1")         # True — the two-character minimum

Length is 2 to 63
-----------------

Because the pattern anchors on a first *and* a last alphanumeric character, the
minimum length is **two**; the maximum is **63**:

.. code-block:: python

   subdomain("a1")          # True  — two characters
   subdomain("a")           # False — a single character can't satisfy first + last
   subdomain("a" * 63)      # True  — at the 63-character maximum
   subdomain("a" * 64)      # False — one over the maximum

What it rejects
---------------

.. code-block:: python

   subdomain("-bad")   # False — can't start with a hyphen
   subdomain("bad-")   # False — can't end with a hyphen
   subdomain("a.b")    # False — a dot makes it two labels, not one
   subdomain("a b")    # False — no spaces

For a full dotted name use :doc:`domain` or :doc:`hostname`.

Pattern
-------

.. code-block:: text

   ^[a-zA-Z0-9][a-zA-Z0-9\-]{0,61}[a-zA-Z0-9]$
