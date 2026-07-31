ORC
===

`Apache ORC <https://orc.apache.org/specification/>`__ — optimised row columnar — is
the other columnar format in wide analytics use. Its files begin with the three-byte
magic ``ORC``, and **ORC** checks for it.

Like :doc:`parquet` this is a :meth:`~edify.RegexBuilder.string` literal at
:meth:`~edify.RegexBuilder.start_of_input` followed by an unrestricted body under
:meth:`~edify.RegexBuilder.dot_all`, so binary content containing line breaks still
matches.

The magic prefix
----------------

.. edify-playground::

   from edify.library import orc

   orc("ORC")                       # the marker alone
   orc("ORC\x00stripe data")        # a file body
   orc("ORCstripes\nfooter\ntail")  # bytes spanning lines

Exactly those three bytes
-------------------------

.. edify-playground::

   from edify.library import orc

   orc("OR")      # truncated
   orc("orc")     # wrong case
   orc("hello")   # not a signature

The signature identifies the file; the stripe layout, footer, and column statistics
are a reader's concern. For the other columnar format see :doc:`parquet`.
