Image
=====

**Image** matches a `container image reference <https://github.com/opencontainers/distribution-spec>`__
— the same grammar as :doc:`docker`, under the vendor-neutral name. Both accept an
optional registry host, a repository path, and an optional ``:tag``.

The construction is an optional host with an optional ``:port``, then lowercase
repository segments joined by ``/``, then an
:meth:`~edify.RegexBuilder.optional` tag.

Image references
----------------

.. edify-playground::

   from edify.library import image

   image("ubuntu")
   image("ubuntu:22.04")
   image("nginx:latest")
   image("quay.io/org/app:v1.2")     # a registry host
   image("registry.local:5000/app")  # with a port

Lowercase only
--------------

.. edify-playground::

   from edify.library import image

   image("my-app:1.0")   # lowercase
   image("My-App:1.0")   # uppercase is not permitted
   image("")             # empty

A tag can be moved to point at different content, so it is not an identity. When you
need to know exactly which bytes you are running, reference the immutable
:doc:`digest` instead.
