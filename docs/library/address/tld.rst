tld
===

:doc:`Library <../index>` › :doc:`Address <index>` › **tld**

``tld`` matches a top-level domain — 2 to 63 letters. It is the trailing
component :doc:`domain` requires.

.. code-block:: python

   from edify.library import tld

   tld("com")   # True

Two to sixty-three letters
--------------------------

From the shortest country codes to the long branded and legacy TLDs:

.. code-block:: python

   tld("io")       # True — two-letter minimum
   tld("com")      # True
   tld("dev")      # True
   tld("museum")   # True — a long gTLD
   tld("c")        # False — a single letter is too short

Case does not matter
--------------------

Upper, lower, and mixed case all match, mirroring DNS case-insensitivity:

.. code-block:: python

   tld("com")   # True
   tld("COM")   # True
   tld("Dev")   # True

Shape, not registry
-------------------

``tld`` matches the *form* of a TLD — it does not consult the IANA list, so an
unregistered string of letters still passes:

.. code-block:: python

   tld("zzz")   # True — well-formed, though not a real TLD

What it rejects
---------------

.. code-block:: python

   tld("c0m")    # False — letters only, no digits
   tld("co-op")  # False — no hyphens
   tld(".com")   # False — the leading dot is not part of the TLD

Pattern
-------

.. code-block:: text

   ^[a-zA-Z]{2,63}$
