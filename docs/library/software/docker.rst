Docker
======

**Docker** matches a `container image reference <https://github.com/opencontainers/distribution-spec>`__
— an optional registry host, a repository path, and an optional ``:tag``. It is the
string you hand to a ``pull`` command.

The construction is an :meth:`~edify.RegexBuilder.optional` host with an optional
``:port``, then lowercase path segments joined by ``/``, and an optional tag. The
lowercase restriction is part of the specification, not a stylistic choice.

Image references
----------------

.. edify-playground::

   from edify.library import docker

   docker("nginx")                          # an official image
   docker("nginx:1.25")                     # with a tag
   docker("library/nginx:latest")           # with a namespace
   docker("docker.io/library/nginx:1.25")   # fully qualified
   docker("ghcr.io/owner/app:v2")           # another registry
   docker("localhost:5000/my-app:dev")      # a registry with a port

Lowercase only
--------------

.. edify-playground::

   from edify.library import docker

   docker("my-app:1.0")   # lowercase
   docker("My-App:1.0")   # uppercase is not permitted
   docker("")             # empty

An untagged reference implicitly means ``:latest``, which is a moving target — pin a
tag, or better a :doc:`digest`, for anything reproducible. This validator and
:doc:`image` accept the same references; use whichever name reads better where you
are.
