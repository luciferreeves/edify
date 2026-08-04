Introspection
=============

Turn a pattern's elements into a plain-English explanation, a diagram, or an
annotated verbose form. Each function operates on the ``.elements`` of a compiled
:class:`~edify.Regex`; the :class:`~edify.Regex` methods
:meth:`~edify.Regex.explain`, :meth:`~edify.Regex.visualize`, and
:meth:`~edify.Regex.to_verbose_string` wrap them for convenience.

.. autofunction:: edify.introspect.explain_elements

.. autofunction:: edify.introspect.visualize_elements

.. autofunction:: edify.introspect.verbose_elements
