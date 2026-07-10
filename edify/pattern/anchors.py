"""Pre-built :class:`Pattern` instances for the ``^`` and ``$`` anchors.

.. code-block:: python

    from edify import END, START, Pattern
    quad_digit = START + Pattern().exactly(4).digit() + END
"""

from __future__ import annotations

from edify.pattern.composition import Pattern

START: Pattern = Pattern().start_of_input()
END: Pattern = Pattern().end_of_input()
