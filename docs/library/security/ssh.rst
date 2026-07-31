SSH
===

An `SSH <https://datatracker.ietf.org/doc/html/rfc4253>`__ key appears in two very
different forms: a one-line public key in ``authorized_keys``, and a multi-line
armoured private key. **SSH** accepts both, because both are what you find in a
deployment configuration.

The two are branches of an :func:`~edify.any_of`. The public branch is a key type
from a fixed set — matched with :func:`~edify.any_of` over ``ssh-rsa``,
``ssh-ed25519``, the ECDSA curves, and the security-key variant — then whitespace,
a base64 blob, and an optional comment. The private branch is the
``OPENSSH PRIVATE KEY`` armoured block.

Public keys
-----------

The line you paste into ``authorized_keys``, with or without a trailing comment:

.. edify-playground::

   from edify.library import ssh

   ssh("ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAI me@laptop")   # the modern default
   ssh("ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAAB user@host")
   ssh("ecdsa-sha2-nistp256 AAAAE2VjZHNh key")
   ssh("ssh-ed25519 AAAAC3NzaC1lZDI1NTE5")                   # no comment

Private keys
------------

.. edify-playground::

   from edify.library import ssh

   ssh("-----BEGIN OPENSSH PRIVATE KEY-----\nb3BlbnNzaC1r\n-----END OPENSSH PRIVATE KEY-----")

A known key type is required
----------------------------

The type is drawn from a closed set, so an invented algorithm fails — as does a
blob with no type at all:

.. edify-playground::

   from edify.library import ssh

   ssh("ssh-rsa AAAAB3NzaC1yc2E")   # a known type
   ssh("ssh-foo AAAAB3NzaC1yc2E")   # not a real key type
   ssh("AAAAB3NzaC1yc2E")           # no type prefix
   ssh("ssh-rsa")                   # no key material

Shape is not trust. A well-formed public key says nothing about *whose* key it is —
authorising one means granting access, so verify the fingerprint out of band before
adding it. And a private key should never pass through a validator in the first
place: keep it out of logs, forms, and version control. For the base64 blob alone see
:doc:`../text/base`.
