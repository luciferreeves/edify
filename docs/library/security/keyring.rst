Keyring
=======

A `keyring <https://www.gnupg.org/gph/en/manual/c235.html>`__ holds OpenPGP keys, and
in armoured form that means a ``PGP PUBLIC KEY BLOCK`` or ``PGP PRIVATE KEY BLOCK``.
**Keyring** narrows :doc:`pgp` to exactly those two labels — the key material,
rather than messages or signatures.

The label is an :func:`~edify.any_of` over ``PUBLIC`` and ``PRIVATE`` followed by the
:meth:`~edify.RegexBuilder.string` literal `` KEY BLOCK``, inside the same armouring
as :doc:`pgp`.

Key blocks
----------

.. edify-playground::

   from edify.library import keyring

   keyring("-----BEGIN PGP PUBLIC KEY BLOCK-----\nmQENBF\n-----END PGP PUBLIC KEY BLOCK-----")
   keyring("-----BEGIN PGP PRIVATE KEY BLOCK-----\nlQOYBF\n-----END PGP PRIVATE KEY BLOCK-----")

Keys, not messages
------------------

This is the distinction from :doc:`pgp`, which accepts the whole family:

.. edify-playground::

   from edify.library import keyring

   keyring("-----BEGIN PGP PUBLIC KEY BLOCK-----\nmQENBF\n-----END PGP PUBLIC KEY BLOCK-----")
   keyring("-----BEGIN PGP MESSAGE-----\nhQEMA\n-----END PGP MESSAGE-----")     # a message
   keyring("-----BEGIN PGP SIGNATURE-----\niQEz\n-----END PGP SIGNATURE-----")  # a signature
   keyring("hello")                                                             # not armoured

A public key block is safe to publish; a private key block is not, and the two differ
by one word in the label. Check *which* you have before storing or transmitting it —
and note that an armoured public key proves nothing about its owner until the
fingerprint is verified. For the broader family see :doc:`pgp`.
