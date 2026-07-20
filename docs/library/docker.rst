docker
======

**Software** · :doc:`Back to the library <index>`

A Docker image reference.

.. code-block:: python

   from edify.library import docker

   docker('nginx:latest')   # True
   docker('!!')   # False

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: nginx:latest|library/ubuntu:20.04|!!|

   from edify.library import docker
   docker

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^(?:(?:[a-z0-9\.\-]+(?::\d+)?/)?[a-z0-9]+(?:[._-][a-z0-9]+)*)(?:/[a-z0-9]+(?:[._-][a-z0-9]+)*)*(?::[a-zA-Z0-9_][a-zA-Z0-9\._\-]{0,127})?(?:@sha256:[a-f0-9]{64})?$

See the other validators in the :doc:`library <index>`.
