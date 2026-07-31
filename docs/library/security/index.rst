Security
========

Cryptographic artifacts — the armoured blocks, binary encodings, and key formats you
find in a certificate store or a deployment secret. Each validator is a callable
:class:`~edify.Pattern`: import it, call it with a string, get a ``bool``.

Matching any of these confirms an artifact's *shape*. None of them verify a
signature, a trust chain, or an expiry date — a well-formed certificate from an
attacker looks exactly like a real one, so parse and verify before trusting.

.. code-block:: python

   from edify.library import pem, ssh, nonce

   pem("-----BEGIN CERTIFICATE-----\nMIIB\n-----END CERTIFICATE-----")   # True
   ssh("ssh-ed25519 AAAAC3NzaC1lZDI1NTE5 me")                            # True
   nonce("Y2hhbGxlbmdlLXZhbHVl")                                          # True

.. toctree::
   :hidden:

   age
   certificate
   csr
   der
   keyring
   nonce
   pem
   pgp
   signature
   ssh
   x509

Armoured blocks
---------------

- :doc:`pem` — any ``-----BEGIN LABEL-----`` block.
- :doc:`certificate` — a PEM certificate; :doc:`csr` — a signing request.
- :doc:`pgp` — any OpenPGP block; :doc:`keyring` — a PGP key block.

Binary encodings
----------------

- :doc:`der` — a DER ``SEQUENCE``; :doc:`x509` — a certificate in either encoding.

Keys and values
---------------

- :doc:`ssh` — an SSH public-key line or private-key block.
- :doc:`age` — an age recipient or identity.
- :doc:`nonce` — a single-use value; :doc:`signature` — a base64 signature.
