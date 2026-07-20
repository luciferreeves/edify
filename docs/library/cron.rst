cron
====

**Temporal** · :doc:`Back to the library <index>`

A cron schedule expression.

.. code-block:: python

   from edify.library import cron

   cron('*/5 * * * *')   # True
   cron('nope')   # False

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: */5 * * * *|0 0 * * 1|@daily|nope|99 99

   from edify.library import cron
   cron

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^(?:@(?:(?:annually|yearly|monthly|weekly|daily|hourly|reboot))|(?:[\*\?0-9/,\-]+\s+){4,5}[\*\?0-9/,\-]+)$

How it reads
------------

.. code-block:: text

   - The text must start with either "@", then either "annually", "yearly", "monthly", "weekly", "daily", "hourly", or "reboot" or between 4 and 5 of one or more of either "*", "?", one character from "0" through "9", "/", ",", or "-", then one or more whitespace characters (space, tab, newline, etc.), then one or more of either "*", "?", one character from "0" through "9", "/", ",", or "-".

See the other validators in the :doc:`library <index>`.
