Data
====

Every validator in the :doc:`Data <../../library/data/index>` category.
Each is a callable :class:`~edify.Pattern`: pass a string to get a ``bool``, or
compose it into a larger pattern with :meth:`~edify.RegexBuilder.use`.

Each entry states what the pattern guarantees, shows the chain that builds it, and
ends with the regex it emits. For prose, worked examples, and a live playground, use
the :doc:`library pages <../../library/data/index>`.

.. py:data:: edify.library.avro

   Callable :class:`Pattern` for an Avro object-container file (``Obj\x01``
   magic prefix).

   Full description: :doc:`Avro <../../library/data/avro>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      avro = (
          Pattern().start_of_input().string("Obj\x01").zero_or_more().any_char().end_of_input().dot_all()
      )

   **Emits** ``^Obj.*$``

.. py:data:: edify.library.csv

   Callable :class:`Pattern` for comma-separated rows: at least two fields per
   row, with optional double-quoted fields.

   Full description: :doc:`CSV <../../library/data/csv>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      _field = (
          Pattern()
          .any_of()
          .subexpression(Pattern().char('"').zero_or_more().anything_but_chars('"').char('"'))
          .subexpression(Pattern().zero_or_more().anything_but_chars(',"\r\n'))
          .end()
      )

      _row = Pattern().use(_field).one_or_more().group().char(",").use(_field).end()

      csv = (
          Pattern()
          .start_of_input()
          .use(_row)
          .zero_or_more()
          .group()
          .one_or_more()
          .any_of_chars("\r\n")
          .use(_row)
          .end()
          .zero_or_more()
          .any_of_chars("\r\n")
          .end_of_input()
      )

   **Emits** ``^(?:"[^"]*"|[^,"\r\n]*)(?:,(?:"[^"]*"|[^,"\r\n]*))+(?:[\r\n]+(?:"[^"]*"|[^,"\r\n]*)(?:,(?:"[^"]*"|[^,"\r\n]*))+)*[\r\n]*$``

.. py:data:: edify.library.hdf5

   Callable :class:`Pattern` for an HDF5 file (``\x89HDF\r\n\x1a\n`` magic
   prefix).

   Full description: :doc:`HDF5 <../../library/data/hdf5>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      hdf5 = (
          Pattern()
          .start_of_input()
          .string("\x89HDF\r\n\x1a\n")
          .zero_or_more()
          .any_char()
          .end_of_input()
          .dot_all()
      )

   **Emits** ``^HDF\\r\\n\\n.*$``

.. py:data:: edify.library.html

   Callable :class:`Pattern` for an HTML document: a ``<!DOCTYPE`` declaration, a
   leading comment, or an ``<html`` root element.

   Full description: :doc:`HTML <../../library/data/html>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      _doctype = Pattern().string("<!doctype").one_or_more().whitespace_char()

      _root = Pattern().string("<html")

      _comment = Pattern().string("<!--")

      html = (
          Pattern()
          .start_of_input()
          .zero_or_more()
          .whitespace_char()
          .any_of()
          .use(_doctype)
          .use(_comment)
          .use(_root)
          .end()
          .zero_or_more()
          .any_char()
          .end_of_input()
          .dot_all()
          .ignore_case()
      )

   **Emits** ``^\s*(?:<!doctype\s+|<!\-\-|<html).*$``

.. py:data:: edify.library.ini

   Callable :class:`Pattern` for an INI file: a ``[section]`` header, a comment,
   or a ``key=value`` assignment.

   Full description: :doc:`INI <../../library/data/ini>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      _section = Pattern().char("[").one_or_more().anything_but_chars("[]\r\n").char("]")

      _key = (
          Pattern()
          .any_of()
          .alphanumeric()
          .char("_")
          .end()
          .zero_or_more()
          .any_of()
          .alphanumeric()
          .any_of_chars("_.- ")
          .end()
          .any_of_chars("=:")
      )

      _comment = Pattern().any_of_chars(";#")

      ini = (
          Pattern()
          .start_of_input()
          .zero_or_more()
          .whitespace_char()
          .any_of()
          .use(_section)
          .use(_comment)
          .use(_key)
          .end()
          .zero_or_more()
          .any_char()
          .end_of_input()
          .dot_all()
      )

   **Emits** ``^\s*(?:\[[^[\]\r\n]+\]|[;#]|(?:[a-zA-Z0-9]|[_])(?:[a-zA-Z0-9]|[_.\- ])*[=:]).*$``

.. py:data:: edify.library.json

   Callable :class:`Pattern` for a JSON document: an object, array, string,
   number, or literal, with optional surrounding whitespace.

   Full description: :doc:`JSON <../../library/data/json>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      _number = (
          Pattern()
          .optional()
          .char("-")
          .one_or_more()
          .digit()
          .optional()
          .group()
          .char(".")
          .one_or_more()
          .digit()
          .end()
          .optional()
          .group()
          .any_of_chars("eE")
          .optional()
          .any_of_chars("+-")
          .one_or_more()
          .digit()
          .end()
      )

      _object = Pattern().char("{").zero_or_more().any_char().char("}")
      _array = Pattern().char("[").zero_or_more().any_char().char("]")
      _string = Pattern().char('"').zero_or_more().any_char().char('"')

      json = (
          Pattern()
          .start_of_input()
          .zero_or_more()
          .whitespace_char()
          .any_of()
          .use(_object)
          .use(_array)
          .use(_string)
          .string("true")
          .string("false")
          .string("null")
          .use(_number)
          .end()
          .zero_or_more()
          .whitespace_char()
          .end_of_input()
          .dot_all()
      )

   **Emits** ``^\s*(?:\{.*\}|\[.*\]|".*"|true|false|null|\-?\d+(?:\.\d+)?(?:[eE][+-]?\d+)?)\s*$``

.. py:data:: edify.library.msgpack

   Callable :class:`Pattern` for a MessagePack payload whose root is a map or an
   array, identified by its leading type-tag byte.

   Full description: :doc:`MessagePack <../../library/data/msgpack>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      _fixmap = Pattern().range("\x80", "\x8f")
      _fixarray = Pattern().range("\x90", "\x9f")
      _sized = Pattern().any_of_chars("\xdc\xdd\xde\xdf")

      msgpack = (
          Pattern()
          .start_of_input()
          .any_of()
          .use(_fixmap)
          .use(_fixarray)
          .use(_sized)
          .end()
          .one_or_more()
          .any_char()
          .end_of_input()
          .dot_all()
      )

   **Emits** ``^(?:[-]|[-]|[ÜÝÞß]).+$``

.. py:data:: edify.library.orc

   Callable :class:`Pattern` for an Apache ORC file (``ORC`` magic prefix).

   Full description: :doc:`ORC <../../library/data/orc>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      orc = Pattern().start_of_input().string("ORC").zero_or_more().any_char().end_of_input().dot_all()

   **Emits** ``^ORC.*$``

.. py:data:: edify.library.parquet

   Callable :class:`Pattern` for an Apache Parquet file (``PAR1`` magic prefix).

   Full description: :doc:`Parquet <../../library/data/parquet>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      parquet = (
          Pattern().start_of_input().string("PAR1").zero_or_more().any_char().end_of_input().dot_all()
      )

   **Emits** ``^PAR1.*$``

.. py:data:: edify.library.protobuf

   Callable :class:`Pattern` for a protocol-buffer schema: a ``syntax``
   declaration, a comment, or a ``package``/``import``/``message``/``service``/
   ``enum`` keyword.

   Full description: :doc:`Protocol Buffers <../../library/data/protobuf>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      _syntax = (
          Pattern()
          .string("syntax")
          .zero_or_more()
          .whitespace_char()
          .char("=")
          .zero_or_more()
          .whitespace_char()
          .any_of_chars("\"'")
          .string("proto")
          .digit()
      )

      _declaration = (
          Pattern()
          .any_of()
          .string("package")
          .string("import")
          .string("message")
          .string("service")
          .string("enum")
          .end()
          .one_or_more()
          .whitespace_char()
      )

      _comment = Pattern().string("//")

      protobuf = (
          Pattern()
          .start_of_input()
          .zero_or_more()
          .whitespace_char()
          .any_of()
          .use(_syntax)
          .use(_comment)
          .use(_declaration)
          .end()
          .zero_or_more()
          .any_char()
          .end_of_input()
          .dot_all()
      )

   **Emits** ``^\s*(?:syntax\s*=\s*["']proto\d|//|(?:package|import|message|service|enum)\s+).*$``

.. py:data:: edify.library.toml

   Callable :class:`Pattern` for a TOML document: a ``[table]`` header, a
   comment, or a ``key =`` assignment.

   Full description: :doc:`TOML <../../library/data/toml>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      _table = (
          Pattern()
          .char("[")
          .optional()
          .char("[")
          .one_or_more()
          .anything_but_chars("[]\r\n")
          .char("]")
          .optional()
          .char("]")
      )

      _key = (
          Pattern()
          .any_of()
          .alphanumeric()
          .any_of_chars("_-\"'")
          .end()
          .zero_or_more()
          .any_of()
          .alphanumeric()
          .any_of_chars("_.-\"'")
          .end()
          .zero_or_more()
          .whitespace_char()
          .char("=")
      )

      _comment = Pattern().char("#")

      toml = (
          Pattern()
          .start_of_input()
          .zero_or_more()
          .whitespace_char()
          .any_of()
          .use(_table)
          .use(_comment)
          .use(_key)
          .end()
          .zero_or_more()
          .any_char()
          .end_of_input()
          .dot_all()
      )

   **Emits** ``^\s*(?:\[\[?[^[\]\r\n]+\]\]?|\#|(?:[a-zA-Z0-9]|[_\-"'])(?:[a-zA-Z0-9]|[_.\-"'])*\s*=).*$``

.. py:data:: edify.library.tsv

   Callable :class:`Pattern` for tab-separated rows: at least two tab-delimited
   fields per row.

   Full description: :doc:`TSV <../../library/data/tsv>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      _field = Pattern().zero_or_more().anything_but_chars("\t\r\n")

      _row = Pattern().use(_field).one_or_more().group().tab().use(_field).end()

      tsv = (
          Pattern()
          .start_of_input()
          .use(_row)
          .zero_or_more()
          .group()
          .one_or_more()
          .any_of_chars("\r\n")
          .use(_row)
          .end()
          .zero_or_more()
          .any_of_chars("\r\n")
          .end_of_input()
      )

   **Emits** ``^[^\t\r\n]*(?:\t[^\t\r\n]*)+(?:[\r\n]+[^\t\r\n]*(?:\t[^\t\r\n]*)+)*[\r\n]*$``

.. py:data:: edify.library.xml

   Callable :class:`Pattern` for an XML document: an ``<?xml`` declaration or a
   root element tag.

   Full description: :doc:`XML <../../library/data/xml>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      _declaration = Pattern().string("<?xml").zero_or_more().any_char()

      _element = (
          Pattern()
          .char("<")
          .any_of()
          .letter()
          .char("_")
          .end()
          .zero_or_more()
          .any_of()
          .alphanumeric()
          .any_of_chars("._-:")
          .end()
          .zero_or_more()
          .any_char()
      )

      xml = (
          Pattern()
          .start_of_input()
          .zero_or_more()
          .whitespace_char()
          .any_of()
          .use(_declaration)
          .use(_element)
          .end()
          .end_of_input()
          .dot_all()
      )

   **Emits** ``^\s*(?:<\?xml.*|<(?:[a-zA-Z]|[_])(?:[a-zA-Z0-9]|[._\-:])*.*)$``

.. py:data:: edify.library.yaml

   Callable :class:`Pattern` for a YAML document: a ``---`` marker, a comment, a
   ``- `` sequence item, or a ``key:`` mapping.

   Full description: :doc:`YAML <../../library/data/yaml>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      _key = (
          Pattern()
          .any_of()
          .alphanumeric()
          .any_of_chars("_\"'")
          .end()
          .zero_or_more()
          .any_of()
          .alphanumeric()
          .any_of_chars("_.- \"'")
          .end()
          .char(":")
          .any_of()
          .whitespace_char()
          .end_of_input()
          .end()
      )

      _item = Pattern().string("- ")
      _marker = Pattern().string("---")
      _comment = Pattern().char("#")

      yaml = (
          Pattern()
          .start_of_input()
          .zero_or_more()
          .whitespace_char()
          .any_of()
          .use(_marker)
          .use(_comment)
          .use(_item)
          .use(_key)
          .end()
          .zero_or_more()
          .any_char()
          .end_of_input()
          .dot_all()
      )

   **Emits** ``^\s*(?:\-\-\-|\#|\- |(?:[a-zA-Z0-9]|[_"'])(?:[a-zA-Z0-9]|[_.\- "'])*:(?:\s|)).*$``

