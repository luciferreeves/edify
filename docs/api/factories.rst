Factory functions
=================

Each builder method has a matching factory function that builds a standalone
:class:`~edify.Pattern`, for a functional composition style (see
:doc:`../guide/composing`).

Characters and literals
-----------------------

.. autofunction:: edify.char
.. autofunction:: edify.string
.. autofunction:: edify.chars
.. autofunction:: edify.nonchars
.. autofunction:: edify.range_of
.. autofunction:: edify.nonrange
.. autofunction:: edify.nonstring

Quantifiers
-----------

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

Groups, captures, and alternation
---------------------------------

.. autofunction:: edify.group
.. autofunction:: edify.capture
.. autofunction:: edify.named_capture
.. autofunction:: edify.any_of
.. autofunction:: edify.back_reference
.. autofunction:: edify.named_back_reference

Lookaround
----------

.. autofunction:: edify.assert_ahead
.. autofunction:: edify.assert_not_ahead
.. autofunction:: edify.assert_behind
.. autofunction:: edify.assert_not_behind
