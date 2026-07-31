Extension
=========

**Extension** matches a `file extension <https://en.wikipedia.org/wiki/Filename_extension>`__
on its own — a leading dot followed by 1 to 10 alphanumeric characters.

The construction is :meth:`~edify.RegexBuilder.char`\ ``(".")`` then
:meth:`~edify.RegexBuilder.between`\ ``(1, 10)`` over an
:meth:`~edify.RegexBuilder.any_of` alphanumeric class, anchored end to end.

Extensions
----------

.. edify-playground::

   from edify.library import extension

   extension(".txt")
   extension(".pdf")
   extension(".mp4")
   extension(".JPEG")     # case is not constrained
   extension(".7z")       # digits are fine

The dot is required
-------------------

.. edify-playground::

   from edify.library import extension

   extension(".txt")     # with the dot
   extension("txt")      # without
   extension(".")        # no characters
   extension(".tar.gz")  # a compound suffix is two extensions
   extension(".c++")     # punctuation is not alphanumeric

Note that ``.tar.gz`` is not matched: it is two extensions, and the *file* extension
is ``.gz``. Split on the last dot before validating. Extensions imply a format but do
not prove one — check the content signature for that, as the
:doc:`../document/index` validators do. For a whole name see :doc:`filename`.
