Certificate
===========

A `certificate <https://datatracker.ietf.org/doc/html/rfc5280>`__ (:rfc:`5280`) binds
a public key to an identity, and in PEM form it carries the label ``CERTIFICATE`` —
or ``TRUSTED CERTIFICATE`` in an OpenSSL trust store. **Certificate** narrows
:doc:`pem` to exactly those labels.

The label is an :meth:`~edify.RegexBuilder.optional` ``TRUSTED `` prefix followed by
the :meth:`~edify.RegexBuilder.string` literal ``CERTIFICATE``; the body is the same
base64-and-whitespace run as :doc:`pem`.

Certificate blocks
------------------

.. edify-playground::

   from edify.library import certificate

   certificate("-----BEGIN CERTIFICATE-----\nMIIBkTCB+wIJAJ5v\n-----END CERTIFICATE-----")
   certificate("-----BEGIN TRUSTED CERTIFICATE-----\nAA==\n-----END TRUSTED CERTIFICATE-----")

Only certificate labels
-----------------------

A private key or a signing request is a PEM block but not a certificate:

.. edify-playground::

   from edify.library import certificate

   certificate("-----BEGIN CERTIFICATE-----\nMIIB\n-----END CERTIFICATE-----")   # a certificate
   certificate("-----BEGIN RSA PRIVATE KEY-----\nMIIB\n-----END RSA PRIVATE KEY-----")  # a key
   certificate("-----BEGIN CERTIFICATE REQUEST-----\nMIIB\n-----END CERTIFICATE REQUEST-----")  # a request
   certificate("hello")                                                            # not PEM

Matching says nothing about validity — not the signature, the issuer chain, the
expiry, or the hostname it covers. Every one of those must be checked by a TLS
library before the certificate is trusted. A certificate file may also hold a chain
of several blocks; this matches a single one. For the request form see :doc:`csr`;
for the binary encoding, :doc:`x509`.
