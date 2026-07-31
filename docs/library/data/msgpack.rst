MessagePack
===========

`MessagePack <https://msgpack.org/>`__ is a binary serialisation format with no file
magic — every value is simply prefixed by a type-tag byte. That leaves one reliable
check: whether the payload's *root* is a map or an array, which is what almost every
encoded document is. **MessagePack** matches those root tags.

The tags are the branches of an :func:`~edify.any_of`: the fixmap range
``0x80``–``0x8f`` and fixarray range ``0x90``–``0x9f``, written with
:meth:`~edify.RegexBuilder.range`, plus the four sized forms ``0xdc``–``0xdf`` for
collections too large for a fixed tag. At least one further byte must follow, and
:meth:`~edify.RegexBuilder.dot_all` allows arbitrary binary content.

Fixed-size roots
----------------

Small maps and arrays encode their length into the tag byte itself:

.. edify-playground::

   from edify.library import msgpack

   msgpack("\x82\xa1a\x01")   # a two-entry map
   msgpack("\x90\x01")        # an array tag
   msgpack("\x81\xa1k\xa1v")  # a one-entry map

Sized roots
-----------

Larger collections use an explicit length prefix:

.. edify-playground::

   from edify.library import msgpack

   msgpack("\xdc\x00\x02x")   # array 16
   msgpack("\xde\x00\x01y")   # map 16

Scalars and text are not matched
--------------------------------

A payload whose root is a plain integer or string carries a different tag, and text
in another format is not MessagePack at all:

.. edify-playground::

   from edify.library import msgpack

   msgpack("\x01")      # an integer root
   msgpack('{"a":1}')   # JSON text
   msgpack("hello")     # plain text

Because the format has no signature, this is a root-type check rather than proof the
payload decodes — only a decoder can confirm that. For the self-describing
alternative see :doc:`avro`, and for the text format MessagePack mirrors,
:doc:`json`.
