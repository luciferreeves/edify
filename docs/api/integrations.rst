Integrations
============

Adapters that turn a :class:`~edify.Pattern` into the validator shape a framework
expects. Each lives behind an optional extra, and importing the module without the
framework installed raises :class:`ImportError` at import time.

The pattern stays the single source of truth: you keep
:meth:`~edify.Regex.explain`, the assertions, and the snapshot tests on the edify
side, and the framework gets a native validator it already knows how to report.

For worked examples of each, see :doc:`../guide/beyond/integrations`.

pydantic
--------

``pip install edify[pydantic]``

.. autofunction:: edify.integrations.pydantic.pattern_validator

Attach the returned callable to a field with pydantic's ``AfterValidator``. It
returns the value unchanged when the pattern matches and raises
:class:`~edify.errors.integration.PatternDidNotMatchError` otherwise, which pydantic
folds into its own ``ValidationError``.

FastAPI
-------

``pip install edify[fastapi]``

.. autofunction:: edify.integrations.fastapi.pattern_path

.. autofunction:: edify.integrations.fastapi.pattern_query

Both attach the emitted regex as the parameter's ``pattern`` constraint, so it
lands in the generated OpenAPI schema as well as in validation — the documentation
and the check cannot drift apart, because they are the same value.

Django
------

``pip install edify[django]``

.. autofunction:: edify.integrations.django.pattern_validator

Returns a Django ``RegexValidator`` for a model or form field's ``validators``
list. Because it is a plain ``RegexValidator`` it composes with Django's own
validators, raises the framework's usual ``ValidationError``, and serializes into
migrations like any other.

The default message names the pattern, which suits a developer and not an end
user — pass ``message`` and ``code`` to override it.
