PEM
===

`PEM <https://datatracker.ietf.org/doc/html/rfc7468>`__ (:rfc:`7468`) is the
text armouring that wraps binary cryptographic data so it survives email and config
files: a ``-----BEGIN LABEL-----`` header, base64 content, and a matching
``-----END LABEL-----`` footer. **PEM** matches any such block, whatever the label.

The label is an uppercase run allowing spaces — which is how multi-word labels like
``CERTIFICATE REQUEST`` and ``RSA PRIVATE KEY`` are covered. The body is
:meth:`~edify.RegexBuilder.zero_or_more` of base64 characters and whitespace, since
the payload is wrapped across lines.

Any labelled block
------------------

.. edify-playground::

   from edify.library import pem

   pem("-----BEGIN CERTIFICATE-----\nMIIBkTCB+wIJAJ5v\n-----END CERTIFICATE-----")
   pem("-----BEGIN RSA PRIVATE KEY-----\nMIIBOgIBAAJBAK\n-----END RSA PRIVATE KEY-----")
   pem("-----BEGIN EC PARAMETERS-----\nBggqhkjOPQMBBw==\n-----END EC PARAMETERS-----")
   pem("-----BEGIN PUBLIC KEY-----\nMFkwEwYH\n-----END PUBLIC KEY-----")

Both markers are required
-------------------------

A header without its footer is a truncated block, and bare base64 is not armoured
at all:

.. edify-playground::

   from edify.library import pem

   pem("-----BEGIN CERTIFICATE-----\nMIIB\n-----END CERTIFICATE-----")   # complete
   pem("-----BEGIN CERTIFICATE-----")                                     # header only
   pem("MIIBkTCB+wIJ")                                                    # unarmoured base64
   pem("hello")                                                            # not PEM

This matches the armouring, not the payload — the base64 is not decoded, and the
header and footer labels are not compared to each other. For the specific artifacts
see :doc:`certificate`, :doc:`csr`, and :doc:`ssh`; for the binary form,
:doc:`der`.
