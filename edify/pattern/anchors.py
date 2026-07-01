"""Pre-built :class:`Pattern` instances for the ``^`` and ``$`` anchors.

These constants exist so the operator algebra reads naturally:

.. code-block:: python

    from edify import END, START, Pattern
    quad_digit = START + Pattern().exactly(4).digit() + END

They are immutable — the underlying ``BuilderState`` never mutates and the
operator overloads always return fresh instances — so importers can share
them freely without worrying about interference between call sites.
"""

from __future__ import annotations

from edify.pattern.composition import Pattern

START: Pattern = Pattern().start_of_input()
END: Pattern = Pattern().end_of_input()
