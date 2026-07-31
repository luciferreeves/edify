DER
===

`DER <https://www.itu.int/rec/T-REC-X.690/en>`__ is the binary encoding beneath PEM:
where :doc:`pem` is base64 text, DER is the raw bytes. Every certificate, key, and
request is a DER ``SEQUENCE``, which begins with the tag byte ``0x30`` followed by a
length. **DER** matches that opening.

The tag is a :meth:`~edify.RegexBuilder.char` literal; the length is an
:func:`~edify.any_of` of two forms — a short form, one byte below ``0x80`` giving the
length directly, or a long form, ``0x81``–``0x84`` saying how many bytes of length
follow. Everything after runs under :meth:`~edify.RegexBuilder.dot_all`.

Short and long lengths
----------------------

.. edify-playground::

   from edify.library import der

   der("\x30\x0d\x06\x09")           # short form: a 13-byte sequence
   der("\x30\x82\x01\x0a\x02\x82")   # long form: two length bytes follow
   der("\x30\x81\xff" + "\x00" * 4)  # long form with one length byte

The SEQUENCE tag is required
----------------------------

A different tag byte is a different ASN.1 type, and text is not DER at all:

.. edify-playground::

   from edify.library import der

   der("\x30\x82\x01\x0a")   # a SEQUENCE
   der("\x31\x82\x01\x0a")   # 0x31 is a SET
   der("hello")              # text
   der("")                   # empty

This checks the outermost tag and length shape — it does not walk the structure,
confirm the declared length matches the data, or tell you which artifact the
sequence encodes. For the text armouring of the same bytes see :doc:`pem`; for
certificates in either encoding, :doc:`x509`.
