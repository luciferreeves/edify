shebang
=======

**Media** · :doc:`Back to the library <index>`

A script shebang line.

.. code-block:: python

   from edify.library import shebang

   shebang('#!/usr/bin/env   aA0')   # True

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: #!/usr/bin/env   aA0|#!/sbin/A0._

   from edify.library import shebang
   shebang

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^\#!/(?:usr/)?(?:(?:bin|sbin|local))/(?:env\s+)?[a-zA-Z0-9\._\+/\-]+$

How it reads
------------

.. code-block:: text

   - The text must start with "#!/".
   - Optional: "usr/".
   - Then the text must have either "bin", "sbin", or "local".
   - Then the text must have "/".
   - Optional: "env", then one or more whitespace characters (space, tab, newline, etc.).
   - Then the text must have one or more of either one character from "a" through "z", one character from "A" through "Z", one character from "0" through "9", ".", "_", "+", "/", or "-".

See the other validators in the :doc:`library <index>`.
