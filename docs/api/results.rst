Results
=======

Terminal builder methods return these wrappers. :class:`~edify.Regex` is a
compiled pattern that forwards the whole standard-library surface and adds
introspection; :class:`~edify.result.Match` and
:class:`~edify.result.NamedCaptures` wrap a match.

Regex
-----

.. autoclass:: edify.Regex
   :members:

Match
-----

.. autoclass:: edify.result.Match
   :members:

NamedCaptures
-------------

.. autoclass:: edify.result.NamedCaptures
   :members:
