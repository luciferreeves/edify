Integrations
============

Edify patterns drop straight into the frameworks you already use. Each
integration lives behind an optional extra so a plain install stays lean —
install only what you need.

All three follow the same idea: the pattern stays the single source of truth, and
the adapter translates it into whatever shape the framework expects. You keep
``explain()``, the assertions, and the snapshot tests on the edify side; the
framework gets a native validator it already knows how to report.

pydantic
--------

``pip install edify[pydantic]``

:func:`edify.integrations.pydantic.pattern_validator` turns a ``Pattern`` into a
validator you can attach to a field with pydantic's ``AfterValidator``:

.. code-block:: python

   from typing import Annotated
   from pydantic import BaseModel, AfterValidator
   from edify import Pattern
   from edify.integrations.pydantic import pattern_validator

   slug = Pattern().start_of_input().one_or_more().any_of().range("a", "z").char("-").end().end_of_input()

   class Article(BaseModel):
       handle: Annotated[str, AfterValidator(pattern_validator(slug))]

   from pydantic import ValidationError

   Article(handle="my-post")     # ok

   try:
       Article(handle="Not A Slug")
   except ValidationError as problem:
       print(problem)          # pydantic surfaces it as a normal field error

The validator returns the value unchanged when it matches and raises
``PatternDidNotMatchError`` otherwise, quoting both the value and the emitted
regex so the failure is self-explanatory in a log:

.. code-block:: text

   input 'Not A Slug' does not match the pattern with source '^[a-z\-]+$';
   adjust the value to match the pattern or select a pattern that accepts it.

Pydantic catches that and folds it into its own ``ValidationError`` alongside any
other constraints on the model, so the field reports the way every other field
does.

.. edify-playground::
   :tests: my-post|another-one|Not A Slug|my_post

   from edify import Pattern

   Pattern().start_of_input() \
       .one_or_more().any_of().range("a", "z").char("-").end() \
       .end_of_input()

FastAPI
-------

``pip install edify[fastapi]``

:func:`edify.integrations.fastapi.pattern_path` and
:func:`~edify.integrations.fastapi.pattern_query` build FastAPI parameter
declarations that reject anything the pattern doesn't match — before your handler
runs:

.. code-block:: python

   from fastapi import FastAPI
   from edify import Pattern
   from edify.integrations.fastapi import pattern_path

   app = FastAPI()
   order_id = Pattern().start_of_input().exactly(8).digit().end_of_input()

   @app.get("/orders/{oid}")
   def get_order(oid: str = pattern_path(order_id, description="8-digit order id")):
       return {"order": oid}

A request to ``/orders/abc`` is rejected with a 422 automatically; only
eight-digit ids reach ``get_order``. The emitted regex is attached as the
parameter's ``pattern`` constraint, which means it also lands in the generated
OpenAPI schema — your API documentation and your validation cannot drift apart,
because they are the same object.

``pattern_query`` does the same for query parameters and adds a ``default``: pass
one and the parameter becomes optional, omit it and the parameter is required.

.. code-block:: python

   from edify import Pattern
   from edify.integrations.fastapi import pattern_query

   order_id = Pattern().start_of_input().exactly(8).digit().end_of_input()

   required = pattern_query(order_id, description="filter by order id")
   optional = pattern_query(order_id, default="00000000", description="filter by order id")

.. edify-playground::
   :tests: 12345678|00000000|1234567|abcdefgh

   from edify import Pattern

   Pattern().start_of_input() \
       .exactly(8).digit() \
       .end_of_input()

Django
------

``pip install edify[django]``

:func:`edify.integrations.django.pattern_validator` returns a Django
``RegexValidator`` for use in a model or form field's ``validators`` list:

.. code-block:: python

   from django.db import models
   from edify import Pattern
   from edify.integrations.django import pattern_validator

   sku = Pattern().start_of_input().exactly(3).uppercase().char("-").exactly(4).digit().end_of_input()

   code = models.CharField(max_length=8, validators=[pattern_validator(sku)])

The validator is callable on its own, which is the easiest way to see what it
does:

.. code-block:: python

   from django.core.exceptions import ValidationError
   from edify import Pattern
   from edify.integrations.django import pattern_validator

   sku = Pattern().start_of_input().exactly(3).uppercase().char("-").exactly(4).digit().end_of_input()
   validate_sku = pattern_validator(sku)

   validate_sku("ABC-1234")          # passes, returns None

   try:
       validate_sku("nope")
   except ValidationError as problem:
       print(problem.messages)       # ['value does not match ^[A-Z]{3}\\-\\d{4}$']

The default message names the pattern, which is right for a developer and wrong
for an end user — so ``message`` and ``code`` are there to override it. The
``code`` is what your form templates and DRF error handlers branch on:

.. code-block:: python

   from django.core.exceptions import ValidationError
   from edify import Pattern
   from edify.integrations.django import pattern_validator

   sku_shape = Pattern().start_of_input().exactly(3).uppercase().char("-").exactly(4).digit().end_of_input()
   check_sku = pattern_validator(
       sku_shape,
       message="Enter a SKU like ABC-1234.",
       code="bad_sku",
   )

   try:
       check_sku("nope")
   except ValidationError as problem:
       print(problem.messages, problem.code)   # ['Enter a SKU like ABC-1234.'] bad_sku

Because it's a plain ``RegexValidator``, it composes with Django's own
validators and raises the framework's usual ``ValidationError`` when a value
doesn't match — so forms, the admin, and DRF serializers all report it the way
they report everything else. It also survives ``makemigrations``: the validator is
serialized into the migration like any other.

.. edify-playground::
   :tests: ABC-1234|XYZ-0000|abc-1234|ABC-123

   from edify import Pattern

   Pattern().start_of_input() \
       .exactly(3).uppercase().char("-").exactly(4).digit() \
       .end_of_input()

Choosing a pattern to hand over
-------------------------------

Two rules apply to every integration.

**Anchor it.** All three adapters ultimately hand the emitted regex to a matcher
that may use search semantics. An unanchored pattern will accept a value that
merely *contains* something valid. Every example above starts with
``start_of_input`` and ends with ``end_of_input`` for that reason.

**Bound it.** These patterns run against request data, which is exactly the
untrusted input :doc:`../practice/performance` is about. Prefer
``between(1, 64)`` over ``one_or_more`` when a field has a real maximum length,
and let the ``ReDoSWarning`` catch the shape it can.

The :doc:`../../library/index` validators are already anchored and bounded, so
handing one of those to a framework needs nothing extra.

Next: :doc:`../practice/index`, on what happens when these patterns meet real
input at scale.
