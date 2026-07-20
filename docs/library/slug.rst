slug
====

**Text** · :doc:`Back to the library <index>`

A URL slug such as ``my-post-title``.

.. code-block:: python

   from edify.library import slug

   slug('my-post')   # True
   slug('Not A Slug')   # False

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: my-post|hello-world-2|Not A Slug|with space

   from edify.library import slug
   slug

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^[a-z0-9]+(?:\-[a-z0-9]+)*$

How it reads
------------

.. code-block:: text

   - The text must start with one or more of either one character from "a" through "z" or one character from "0" through "9".
   - Then the text must have zero or more of "-", then one or more of either one character from "a" through "z" or one character from "0" through "9".

See the other validators in the :doc:`library <index>`.
