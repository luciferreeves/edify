path
====

**Address** · :doc:`Back to the library <index>`

A URL or filesystem path.

.. code-block:: python

   from edify.library import path

   path('/aaa/aaaaaaaaa/')   # True

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: /aaa/aaaaaaaaa/|o:\aaaaaaaaa\aaaaaaa\

   from edify.library import path
   path

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^(?:(?:(?:(?:\./)|(?:(?:\.\./)+)|[/]))?(?:[^\0\r\n/]+/?)+|[a-zA-Z]:\\(?:[^\\/:*?"<>|\r\n]+\\?)+|\\\\[^\\/:*?"<>|\r\n]+\\[^\\/:*?"<>|\r\n]+(?:\\[^\\/:*?"<>|\r\n]*)*)$

See the other validators in the :doc:`library <index>`.
