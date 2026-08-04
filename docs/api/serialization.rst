Serialization
=============

Round-trip a pattern through plain data. What travels is the element tree, not a
regex string, so a reconstructed pattern can still be explained, visualized,
extended, and re-emitted for a different engine.

Pattern methods
---------------

The everyday surface. Each is built on the module-level functions below.

.. automethod:: edify.Pattern.to_dict

.. automethod:: edify.Pattern.from_dict

.. automethod:: edify.Pattern.to_json

.. automethod:: edify.Pattern.from_json

Module functions
----------------

Reach for these directly when you need finer control over a single element or a
whole builder state.

.. autofunction:: edify.serialize.element_to_dict

.. autofunction:: edify.serialize.dict_to_element

.. autofunction:: edify.serialize.state_to_dict

.. autofunction:: edify.serialize.dict_to_state

.. autodata:: edify.serialize.SCHEMA_VERSION
