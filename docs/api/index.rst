API reference
=============

The complete public surface, generated from the source. For a guided tour start
with the :doc:`../guide/index`; for the ready-made validators see the
:doc:`../library/index`.

The builder
-----------

.. autoclass:: edify.RegexBuilder
   :members:
   :undoc-members:

.. autoclass:: edify.Pattern
   :members:
   :undoc-members:

Results
-------

.. autoclass:: edify.Regex
   :members:

.. autoclass:: edify.result.Match
   :members:

.. autoclass:: edify.result.NamedCaptures
   :members:

Introspection
-------------

.. autofunction:: edify.introspect.explain_elements

.. autofunction:: edify.introspect.visualize_elements

.. autofunction:: edify.introspect.verbose_elements

Serialization
-------------

.. autofunction:: edify.serialize.element_to_dict

.. autofunction:: edify.serialize.dict_to_element

.. autodata:: edify.serialize.SCHEMA_VERSION

Testing
-------

.. autofunction:: edify.testing.assert_snapshot

.. autoexception:: edify.testing.SnapshotMismatchError

.. autoexception:: edify.testing.SnapshotMissingError

Errors
------

.. autoexception:: edify.EdifyError

.. autoexception:: edify.EdifySyntaxError
