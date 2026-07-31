CSR
===

A `certificate signing request <https://datatracker.ietf.org/doc/html/rfc2986>`__
(:rfc:`2986`) is what you send to a certificate authority: a public key plus the
identity you are claiming, signed with the matching private key. In PEM form it
carries the label ``CERTIFICATE REQUEST``, or ``NEW CERTIFICATE REQUEST`` from older
tooling. **CSR** matches those labels.

The label is an :meth:`~edify.RegexBuilder.optional` ``NEW `` prefix then the
:meth:`~edify.RegexBuilder.string` literal ``CERTIFICATE REQUEST``, wrapped in the
same PEM armouring as :doc:`pem`.

Request blocks
--------------

.. edify-playground::

   from edify.library import csr

   csr("-----BEGIN CERTIFICATE REQUEST-----\nMIIBkTCB+wIJAJ5v\n-----END CERTIFICATE REQUEST-----")
   csr("-----BEGIN NEW CERTIFICATE REQUEST-----\nAA==\n-----END NEW CERTIFICATE REQUEST-----")

Not a certificate
-----------------

The distinction matters: a request is unsigned by any authority, and confusing the
two is a common deployment mistake:

.. edify-playground::

   from edify.library import csr

   csr("-----BEGIN CERTIFICATE REQUEST-----\nMIIB\n-----END CERTIFICATE REQUEST-----")   # a request
   csr("-----BEGIN CERTIFICATE-----\nMIIB\n-----END CERTIFICATE-----")                    # an issued certificate
   csr("hello")                                                                            # not PEM

This confirms the armouring only. Whether the embedded public key is sound, the
subject name is what you intended, or the self-signature verifies are all questions
for a certificate library. For the issued result see :doc:`certificate`.
