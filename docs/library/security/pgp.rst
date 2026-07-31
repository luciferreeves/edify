PGP
===

`OpenPGP <https://datatracker.ietf.org/doc/html/rfc9580>`__ armours its data the same
way PEM does, but with its own labels: ``PGP MESSAGE``, ``PGP SIGNATURE``, ``PGP
PUBLIC KEY BLOCK``, and so on. **PGP** matches any of them — the whole family.

The construction is the :meth:`~edify.RegexBuilder.string` literal
``-----BEGIN PGP `` followed by an uppercase label, the armoured body, and the
matching ``-----END PGP `` footer. The body class includes ``:`` so the armour
headers such as ``Version:`` are covered.

Any PGP block
-------------

.. edify-playground::

   from edify.library import pgp

   pgp("-----BEGIN PGP MESSAGE-----\nhQEMA\n-----END PGP MESSAGE-----")
   pgp("-----BEGIN PGP SIGNATURE-----\niQEzBAEBCgAd\n-----END PGP SIGNATURE-----")
   pgp("-----BEGIN PGP PUBLIC KEY BLOCK-----\nmQENBF\n-----END PGP PUBLIC KEY BLOCK-----")
   pgp("-----BEGIN PGP PRIVATE KEY BLOCK-----\nlQOYBF\n-----END PGP PRIVATE KEY BLOCK-----")

PGP labels only
---------------

A PEM certificate uses the same armour syntax but is not an OpenPGP block:

.. edify-playground::

   from edify.library import pgp

   pgp("-----BEGIN PGP MESSAGE-----\nhQEMA\n-----END PGP MESSAGE-----")   # a PGP block
   pgp("-----BEGIN CERTIFICATE-----\nMIIB\n-----END CERTIFICATE-----")     # PEM: see certificate
   pgp("hello")                                                            # not armoured

Matching the armour is not verification: a signature block proves nothing until it
is checked against the signer's public key, and a "signed" message whose signature
you never verify is worth exactly nothing. For key blocks specifically see
:doc:`keyring`; for the PEM family, :doc:`pem`.
