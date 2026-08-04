HAL
===

`HAL <https://datatracker.ietf.org/doc/html/draft-kelly-json-hal-08>`__ — the hypertext application
language — is a convention for making JSON responses navigable. A HAL document is
an ordinary JSON object with two reserved members: ``_links``, holding the URIs
related to this resource, and ``_embedded``, holding whole resources inlined to save
a round trip. **HAL** looks for either.

The shape is a JSON object whose body contains one of those quoted keys followed by
a colon, matched with :meth:`~edify.RegexBuilder.any_of` over the two names. The
document must open with ``{`` and close with ``}``, and
:meth:`~edify.RegexBuilder.dot_all` lets the body span as many lines as a real
response needs.

Linked resources
----------------

The ``_links`` member is what makes a response HAL — it carries at minimum the
``self`` relation:

.. edify-playground::

   from edify.library import hal

   hal('{"_links": {"self": {"href": "/orders/1"}}}')
   hal('{"total": 2, "_links": {"self": {"href": "/orders"}}}')
   hal('{\n  "_links": {\n    "next": {"href": "/orders?page=2"}\n  }\n}')

Embedded resources
------------------

A collection response usually inlines its members under ``_embedded`` instead of
making the client fetch each one:

.. edify-playground::

   from edify.library import hal

   hal('{"_embedded": {"orders": []}}')
   hal('{"_links": {"self": {"href": "/o"}}, "_embedded": {"orders": []}}')

Plain JSON is not HAL
---------------------

Without one of the reserved members a document is just JSON — correct, but not
navigable, and not HAL:

.. edify-playground::

   from edify.library import hal

   hal('{"id": 1, "_links": {}}')      # one reserved member is enough
   hal('{"id": 1, "total": 9.99}')   # valid JSON, no HAL members
   hal("{}")                         # an empty object
   hal("hello-world")                # not JSON at all

It confirms the HAL members are present, not that every link object carries a valid
``href``. For the other common hypermedia convention see :doc:`jsonapi`; for plain
document validity, :doc:`../data/json`.
