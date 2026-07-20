Serialization
=============

Round-trip a pattern through plain data. The :class:`~edify.Pattern` methods
``to_dict`` / ``from_dict`` / ``to_json`` / ``from_json`` are built on these
functions; reach for them directly when you need finer control over a single
element or a whole builder state.

.. autofunction:: edify.serialize.element_to_dict

.. autofunction:: edify.serialize.dict_to_element

.. autofunction:: edify.serialize.state_to_dict

.. autofunction:: edify.serialize.dict_to_state

.. autodata:: edify.serialize.SCHEMA_VERSION
