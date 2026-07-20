wallet
======

**Finance** · :doc:`Back to the library <index>`

A crypto wallet address.

.. code-block:: python

   from edify.library import wallet

   wallet('1amAJP1amAJP1amAJP1amAJP1a')   # True

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: 1amAJP1amAJP1amAJP1amAJP1a|bc10a0a0a0a0a0a0a0a0a0a0a0a0a

   from edify.library import wallet
   wallet

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^(?:[13][a-km-zA-HJ-NP-Z1-9]{25,34}|bc1[a-z0-9]{25,89}|0x[a-fA-F0-9]{40}|[LM3][a-km-zA-HJ-NP-Z1-9]{26,33}|D[5-9A-HJ-NP-U][1-9A-HJ-NP-Za-km-z]{32}|X[1-9A-HJ-NP-Za-km-z]{33})$

See the other validators in the :doc:`library <index>`.
