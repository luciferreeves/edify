interval
========

**Temporal** · :doc:`Back to the library <index>`

A time interval.

.. code-block:: python

   from edify.library import interval

   interval('2345-23-23t23:23/Po')   # True

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: 2345-23-23t23:23/Po

   from edify.library import interval
   interval

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^\d{4}\-\d{2}\-\d{2}[Tt ]\d{2}:\d{2}(?::\d{2}(?:\.\d+)?)?(?:(?:[+-]\d{2}:?\d{2}|[Zz]))?/(?:\d{4}\-\d{2}\-\d{2}[Tt ]\d{2}:\d{2}(?::\d{2}(?:\.\d+)?)?(?:(?:[+-]\d{2}:?\d{2}|[Zz]))?|P(?=.)(?:\d+(?:\.\d+)?Y)?(?:\d+(?:\.\d+)?M)?(?:\d+(?:\.\d+)?W)?(?:\d+(?:\.\d+)?D)?(?:T(?=\d)(?:\d+(?:\.\d+)?H)?(?:\d+(?:\.\d+)?M)?(?:\d+(?:\.\d+)?S)?)?)$

See the other validators in the :doc:`library <index>`.
