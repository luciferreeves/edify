url
===

**Address** · :doc:`Back to the library <index>`

An HTTP or HTTPS URL.

.. code-block:: python

   from edify.library import url

   url('https://example.com')   # True
   url('notaurl')   # False

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: https://example.com|http://a.io/path?q=1|notaurl|ftp:/bad

   from edify.library import url
   url

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^(?:https?://)?(?:www\.)?[\-a-zA-Z0-9@:%\._\+\~\#=]{1,256}\.[a-zA-Z0-9\(\)]{1,6}\b[\-a-zA-Z0-9\(\)@:%_\+\.\~\#\?\&/=]*$

See the other validators in the :doc:`library <index>`.
