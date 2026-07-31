HDF5
====

`HDF5 <https://docs.hdfgroup.org/hdf5/develop/_s_p_e_c.html>`__ is the container
format behind much scientific and numerical data. Its files open with an eight-byte
signature chosen to survive mangling in transit: ``\x89HDF\r\n\x1a\n``. The high-bit
byte detects seven-bit-stripping transfers, the ``\r\n`` pair detects line-ending
translation, and the ``\x1a`` stops the file printing to a terminal. **HDF5** checks
for all eight bytes.

The signature is one :meth:`~edify.RegexBuilder.string` literal at
:meth:`~edify.RegexBuilder.start_of_input`; the rest of the file is matched under
:meth:`~edify.RegexBuilder.dot_all`, which is essential here because the signature
itself contains newlines.

The file signature
------------------

.. edify-playground::

   from edify.library import hdf5

   hdf5("\x89HDF\r\n\x1a\n")                      # the signature alone
   hdf5("\x89HDF\r\n\x1a\nsuperblock\nmore")      # a file body

Every byte is required
----------------------

A partial signature does not match — which is the point of a marker designed to
detect corruption:

.. edify-playground::

   from edify.library import hdf5

   hdf5("\x89HDF")   # truncated
   hdf5("HDF")       # missing the guard byte
   hdf5("hello")     # not a signature

The signature identifies the container; groups, datasets, and the superblock are a
library's concern. For other scientific and analytics containers see :doc:`parquet`,
:doc:`orc`, and :doc:`avro`.
