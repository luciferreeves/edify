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

Factory functions
-----------------

Each builder method has a matching factory function that builds a standalone
:class:`~edify.Pattern`, for a functional composition style (see
:doc:`../guide/composing`).

.. autofunction:: edify.char
.. autofunction:: edify.string
.. autofunction:: edify.chars
.. autofunction:: edify.nonchars
.. autofunction:: edify.range_of
.. autofunction:: edify.nonrange
.. autofunction:: edify.nonstring
.. autofunction:: edify.exactly
.. autofunction:: edify.at_least
.. autofunction:: edify.at_most
.. autofunction:: edify.between
.. autofunction:: edify.between_lazy
.. autofunction:: edify.optional
.. autofunction:: edify.zero_or_more
.. autofunction:: edify.zero_or_more_lazy
.. autofunction:: edify.one_or_more
.. autofunction:: edify.one_or_more_lazy
.. autofunction:: edify.group
.. autofunction:: edify.capture
.. autofunction:: edify.named_capture
.. autofunction:: edify.any_of
.. autofunction:: edify.back_reference
.. autofunction:: edify.named_back_reference
.. autofunction:: edify.assert_ahead
.. autofunction:: edify.assert_not_ahead
.. autofunction:: edify.assert_behind
.. autofunction:: edify.assert_not_behind

Constants
---------

Ready-made single-token :class:`~edify.Pattern` objects. Each is callable as a
one-character validator, composable with ``+`` and ``|``, and usable with
:meth:`~edify.RegexBuilder.use`.

============================  =====================
Constant                      Emits
============================  =====================
``START``                     ``^``
``END``                       ``$``
``WORD_BOUNDARY``             ``\b``
``NON_WORD_BOUNDARY``         ``\B``
``DIGIT``                     ``\d``
``NON_DIGIT``                 ``\D``
``WORD``                      ``\w``
``NON_WORD``                  ``\W``
``WHITESPACE``                ``\s``
``NON_WHITESPACE``            ``\S``
``ANY_CHAR``                  ``.``
``LETTER``                    ``[a-zA-Z]``
``LOWERCASE``                 ``[a-z]``
``UPPERCASE``                 ``[A-Z]``
``ALPHANUMERIC``              ``[a-zA-Z0-9]``
``TAB``                       ``\t``
``NEW_LINE``                  ``\n``
``CARRIAGE_RETURN``           ``\r``
``NULL_BYTE``                 ``\0``
============================  =====================

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

.. autofunction:: edify.serialize.state_to_dict

.. autofunction:: edify.serialize.dict_to_state

.. autodata:: edify.serialize.SCHEMA_VERSION

Validation
----------

.. autofunction:: edify.validate.is_valid_group_name

Testing
-------

.. autofunction:: edify.testing.assert_snapshot

.. autoexception:: edify.testing.SnapshotMismatchError

.. autoexception:: edify.testing.SnapshotMissingError

Errors
------

.. autoexception:: edify.EdifyError

.. autoexception:: edify.EdifySyntaxError
