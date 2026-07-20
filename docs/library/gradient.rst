gradient
========

**Color** · :doc:`Back to the library <index>`

A CSS gradient function.

.. code-block:: python

   from edify.library import gradient


Edit the string, or the pattern itself:

.. edify-playground::

   from edify.library import gradient
   gradient

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^(?:linear|radial|conic)\-gradient\([^()]*(?:\([^()]*\)[^()]*)*\)$

How it reads
------------

.. code-block:: text

   - The text must start with either "linear", "radial", or "conic".
   - Then the text must have "-gradient(".
   - Then the text must have zero or more characters NOT from the set "()".
   - Then the text must have zero or more of "(", then zero or more characters NOT from the set "()", then ")", then zero or more characters NOT from the set "()".
   - Then the text must have ")".

See the other validators in the :doc:`library <index>`.
