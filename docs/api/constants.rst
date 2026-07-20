Constants
=========

Ready-made single-token :class:`~edify.Pattern` objects. Each is callable as a
one-character validator, composable with ``+`` and ``|``, and usable with
:meth:`~edify.RegexBuilder.use`.

.. code-block:: python

   from edify import DIGIT, LETTER, START, END

   DIGIT("5")                        # True
   (START + DIGIT + END).to_regex_string()   # '^\\d$'

Anchors
-------

============================  =====================
Constant                      Emits
============================  =====================
``START``                     ``^``
``END``                       ``$``
``WORD_BOUNDARY``             ``\b``
``NON_WORD_BOUNDARY``         ``\B``
============================  =====================

Character classes
-----------------

============================  =====================
Constant                      Emits
============================  =====================
``DIGIT``                     ``\d``
``NON_DIGIT``                 ``\D``
``WORD``                      ``\w``
``NON_WORD``                  ``\W``
``WHITESPACE``                ``\s``
``NON_WHITESPACE``            ``\S``
``ANY_CHAR``                  ``.``
``LETTER``                    ``[a-zA-Z]``
``LOWERCASE``                 ``[a-z]``
``UPPERCASE``                 ``[A-Z]``
``ALPHANUMERIC``              ``[a-zA-Z0-9]``
============================  =====================

Whitespace and control
----------------------

============================  =====================
Constant                      Emits
============================  =====================
``TAB``                       ``\t``
``NEW_LINE``                  ``\n``
``CARRIAGE_RETURN``           ``\r``
``NULL_BYTE``                 ``\0``
============================  =====================
