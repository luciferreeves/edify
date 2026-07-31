Digest
======

A `content digest <https://github.com/opencontainers/image-spec/blob/main/descriptor.md#digests>`__
names an artifact by the hash of its bytes — ``sha256:abc123…``. Because the hash is
derived from the content, the reference is immutable: the same digest always means
the same bytes.

The construction is an :func:`~edify.any_of` over the algorithm names — ``sha256``,
``sha512``, ``sha1``, ``md5``, ``blake2b``/``blake2s`` — then a separator and 32 to
128 hex digits. Including the algorithm prefix is what distinguishes a digest from a
bare :doc:`checksum`.

Algorithm and hash
------------------

.. edify-playground::

   from edify.library import digest

   digest("sha256:" + "a" * 64)
   digest("sha512:" + "b" * 128)
   digest("sha1:" + "c" * 40)
   digest("blake2b:" + "d" * 64)

The prefix is required
----------------------

.. edify-playground::

   from edify.library import digest

   digest("sha256:" + "a" * 64)   # prefixed
   digest("a" * 64)               # bare: see checksum
   digest("sha256:")              # no hash
   digest("md9:" + "a" * 32)      # not a known algorithm
   digest("")                     # empty

Note that ``sha1`` and ``md5`` are accepted because they appear in existing
artifacts, not because they are sound — both are broken for security purposes, so
never trust one to establish integrity against a motivated attacker. Prefer
``sha256`` or better. For a bare hash see :doc:`checksum`.
