Data
====

Every validator in the :doc:`data <../../library/data/index>` category. Each is a
callable :class:`~edify.Pattern`: pass a string to get a ``bool``, or compose it into a
larger pattern with :meth:`~edify.RegexBuilder.use`.

For what each one accepts and rejects, with runnable examples, see the
:doc:`library pages <../../library/data/index>`.

.. py:function:: edify.library.avro(value: str) -> bool

   Avro. See :doc:`../../library/data/avro` for the full description.

   Emits ``^Obj.*$``

.. py:function:: edify.library.csv(value: str) -> bool

   CSV. See :doc:`../../library/data/csv` for the full description.

   Emits ``^(?:"[^"]*"|[^,"\r\n]*)(?:,(?:"[^"]*"|[^,"\r\n]*))+(?:[\r\n]+(?:"[^"]*"|[^,"\r\n]*)(?:,(?:"[^"]*"|[^,"\r\n]*))+)*[\r\n]*$``

.. py:function:: edify.library.hdf5(value: str) -> bool

   HDF5. See :doc:`../../library/data/hdf5` for the full description.

   Emits ``^HDF\\r\\n\\n.*$``

.. py:function:: edify.library.html(value: str) -> bool

   HTML. See :doc:`../../library/data/html` for the full description.

   Emits ``^\s*(?:<!doctype\s+|<!\-\-|<html).*$``

.. py:function:: edify.library.ini(value: str) -> bool

   INI. See :doc:`../../library/data/ini` for the full description.

   Emits ``^\s*(?:\[[^[\]\r\n]+\]|[;#]|(?:[a-zA-Z0-9]|[_])(?:[a-zA-Z0-9]|[_.\- ])*[=:]).*$``

.. py:function:: edify.library.json(value: str) -> bool

   JSON. See :doc:`../../library/data/json` for the full description.

   Emits ``^\s*(?:\{.*\}|\[.*\]|".*"|true|false|null|\-?\d+(?:\.\d+)?(?:[eE][+-]?\d+)?)\s*$``

.. py:function:: edify.library.msgpack(value: str) -> bool

   MessagePack. See :doc:`../../library/data/msgpack` for the full description.

   Emits ``^(?:[-]|[-]|[ÜÝÞß]).+$``

.. py:function:: edify.library.orc(value: str) -> bool

   ORC. See :doc:`../../library/data/orc` for the full description.

   Emits ``^ORC.*$``

.. py:function:: edify.library.parquet(value: str) -> bool

   Parquet. See :doc:`../../library/data/parquet` for the full description.

   Emits ``^PAR1.*$``

.. py:function:: edify.library.protobuf(value: str) -> bool

   Protocol Buffers. See :doc:`../../library/data/protobuf` for the full description.

   Emits ``^\s*(?:syntax\s*=\s*["']proto\d|//|(?:package|import|message|service|enum)\s+).*$``

.. py:function:: edify.library.toml(value: str) -> bool

   TOML. See :doc:`../../library/data/toml` for the full description.

   Emits ``^\s*(?:\[\[?[^[\]\r\n]+\]\]?|\#|(?:[a-zA-Z0-9]|[_\-"'])(?:[a-zA-Z0-9]|[_.\-"'])*\s*=).*$``

.. py:function:: edify.library.tsv(value: str) -> bool

   TSV. See :doc:`../../library/data/tsv` for the full description.

   Emits ``^[^\t\r\n]*(?:\t[^\t\r\n]*)+(?:[\r\n]+[^\t\r\n]*(?:\t[^\t\r\n]*)+)*[\r\n]*$``

.. py:function:: edify.library.xml(value: str) -> bool

   XML. See :doc:`../../library/data/xml` for the full description.

   Emits ``^\s*(?:<\?xml.*|<(?:[a-zA-Z]|[_])(?:[a-zA-Z0-9]|[._\-:])*.*)$``

.. py:function:: edify.library.yaml(value: str) -> bool

   YAML. See :doc:`../../library/data/yaml` for the full description.

   Emits ``^\s*(?:\-\-\-|\#|\- |(?:[a-zA-Z0-9]|[_"'])(?:[a-zA-Z0-9]|[_.\- "'])*:(?:\s|)).*$``

