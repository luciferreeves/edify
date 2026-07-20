duration
========

**Temporal** · :doc:`Back to the library <index>`

An ISO 8601 duration.

.. code-block:: python

   from edify.library import duration

   duration('P1Y2M10D')   # True
   duration('1 hour')   # False

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: P1Y2M10D|PT1H30M|P3D|1 hour|abc

   from edify.library import duration
   duration

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^P(?=.)(?:\d+(?:\.\d+)?Y)?(?:\d+(?:\.\d+)?M)?(?:\d+(?:\.\d+)?W)?(?:\d+(?:\.\d+)?D)?(?:T(?=\d)(?:\d+(?:\.\d+)?H)?(?:\d+(?:\.\d+)?M)?(?:\d+(?:\.\d+)?S)?)?$

See the other validators in the :doc:`library <index>`.
