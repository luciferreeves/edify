Cron
====

A `cron expression <https://en.wikipedia.org/wiki/Cron>`__ schedules a recurring job:
five fields for minute, hour, day of month, month, and day of week, each holding a
value, a range, a list, or a step. **Cron** matches that five-field form and the
``@`` shorthands.

The two shapes are branches of an :func:`~edify.any_of`: a shorthand keyword —
``@daily``, ``@hourly``, ``@reboot`` and friends — or five whitespace-separated
fields built from digits and the operators ``*`` ``?`` ``/`` ``,`` ``-``.

Five-field schedules
--------------------

.. edify-playground::

   from edify.library import cron

   cron("* * * * *")        # every minute
   cron("0 9 * * 1-5")      # 9am on weekdays
   cron("*/15 * * * *")     # every fifteen minutes
   cron("0 0 1 * *")        # monthly
   cron("0 9,17 * * *")     # twice a day

Shorthand keywords
------------------

.. edify-playground::

   from edify.library import cron

   cron("@daily")
   cron("@hourly")
   cron("@weekly")
   cron("@reboot")
   cron("@yearly")

The field count is fixed
------------------------

.. edify-playground::

   from edify.library import cron

   cron("* * * * *")      # five fields
   cron("* * * *")        # four
   cron("@invalid")       # not a known shorthand
   cron("every minute")   # prose
   cron("")               # empty

The six-field form some schedulers use — with a leading seconds field — is not
matched, nor are the ``JAN``/``MON`` name abbreviations. Field *values* are not
range-checked either, so ``99 99 * * *`` matches despite being impossible; the
scheduler will reject it.
