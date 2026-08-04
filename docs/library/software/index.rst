Software
========

Versions, package names, container images, and the identifiers that pin a build.
Each validator is a callable :class:`~edify.Pattern`: import it, call it with a
string, get a ``bool``.

.. code-block:: python

   from edify.library import semver, package, docker

   semver("1.2.3-alpha.1")   # True
   package("@scope/name")    # True
   docker("nginx:1.25")      # True

.. toctree::
   :hidden:

   bump
   cargo
   checksum
   component
   digest
   docker
   git
   image
   makefile
   package
   ref
   semver
   version

Versions
--------

- :doc:`semver` — the strict ``MAJOR.MINOR.PATCH`` contract.
- :doc:`version` — looser dotted versions with an optional ``v`` prefix.
- :doc:`bump` — the name of a release increment.

Packages
--------

- :doc:`package` — a registry package name; :doc:`component` — a name pinned to a
  version.
- :doc:`cargo` — a crate name, optionally versioned.

Containers
----------

- :doc:`docker` and :doc:`image` — an image reference.
- :doc:`digest` — an algorithm-prefixed content digest.

Source control and builds
-------------------------

- :doc:`git` — a commit hash; :doc:`ref` — a branch, tag, or full ref path.
- :doc:`checksum` — a hexadecimal file checksum.
- :doc:`makefile` — a build rule line.
