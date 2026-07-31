Integrations
============

Edify patterns drop straight into the frameworks you already use. Each
integration lives behind an optional extra so a plain install stays lean —
install only what you need.

pydantic
--------

``pip install edify[pydantic]``

``edify.integrations.pydantic.pattern_validator`` turns a ``Pattern`` into a
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
``PatternDidNotMatchError`` otherwise, which pydantic surfaces as a normal field
error alongside any other constraints on the model.

FastAPI
-------

``pip install edify[fastapi]``

``edify.integrations.fastapi.pattern_path`` and ``pattern_query`` build FastAPI
parameter declarations that reject anything the pattern doesn't match — before
your handler runs:

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
eight-digit ids reach ``get_order``. ``pattern_query`` does the same for query
parameters — reach for whichever matches where the value arrives.

Django
------

``pip install edify[django]``

``edify.integrations.django.pattern_validator`` returns a Django
``RegexValidator`` for use in a model or form field's ``validators`` list:

.. code-block:: python

   from django.db import models
   from edify import Pattern
   from edify.integrations.django import pattern_validator

   sku = Pattern().start_of_input().exactly(3).uppercase().char("-").exactly(4).digit().end_of_input()

   class Product(models.Model):
       code = models.CharField(max_length=8, validators=[pattern_validator(sku)])

Because it's a plain ``RegexValidator``, it composes with Django's own
validators and raises the framework's usual ``ValidationError`` when a value
doesn't match — so forms, the admin, and DRF serializers all report it the way
they report everything else.

That's the whole guide. From here, browse the :doc:`../../library/index` for the
228 ready-made validators, keep the :doc:`../../api/index` handy as a reference, or
open the :doc:`../../playground` and build something.
