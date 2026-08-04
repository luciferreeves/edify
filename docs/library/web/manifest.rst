Manifest
========

A `web app manifest <https://www.w3.org/TR/appmanifest/>`__ is the JSON file that
lets a site be installed like an application — declaring its name, icons, and how it
should launch. **Manifest** looks for a JSON object carrying one of the members that
identify such a file.

The construction is a JSON object whose body contains a quoted key from an
:func:`~edify.any_of` — ``start_url``, ``display``, ``icons``, ``short_name``,
``theme_color`` — followed by a colon, all under
:meth:`~edify.RegexBuilder.dot_all`.

Manifest documents
------------------

.. edify-playground::

   from edify.library import manifest

   manifest('{"short_name": "App", "start_url": "/", "display": "standalone"}')
   manifest('{"icons": [{"src": "/i.png", "sizes": "192x192"}]}')
   manifest('{\n  "name": "My App",\n  "theme_color": "#ffffff"\n}')

A manifest member is required
-----------------------------

Plain JSON without any of those keys is not a manifest:

.. edify-playground::

   from edify.library import manifest

   manifest('{"display": "fullscreen"}')   # a manifest member
   manifest('{"name": "My App"}')          # name alone is not distinctive
   manifest('{"a": 1}')                    # JSON without the manifest keys
   manifest("hello")                       # not JSON

This identifies the document; whether the icons resolve, the ``start_url`` is in
scope, or the manifest meets installability criteria is for a browser to decide. For
general JSON validity see :doc:`../data/json`.
