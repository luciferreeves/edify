Integrations
============

Edify patterns drop straight into the frameworks you already use. Each
integration lives behind an optional extra so a plain install stays lean —
install only what you need.

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

   Article(handle="my-post")     # ok
   Article(handle="Not A Slug")  # raises a validation error

The validator returns the value unchanged when it matches and raises
:class:`~edify.integrations.pydantic.PatternDidNotMatchError` otherwise, which
pydantic surfaces as a normal field error.

FastAPI
-------

``pip install edify[fastapi]``

:func:`edify.integrations.fastapi.pattern_path` and
:func:`edify.integrations.fastapi.pattern_query` build FastAPI parameter
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
eight-digit ids reach ``get_order``.

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

   class Product(models.Model):
       code = models.CharField(max_length=8, validators=[pattern_validator(sku)])

Pass ``message`` and ``code`` to customize the error Django raises when the value
doesn't match.

That's the whole guide. From here, browse the :doc:`../library/index` for the
228 ready-made validators, keep the :doc:`../api/index` handy as a reference, or
open the :doc:`../playground` and build something.
