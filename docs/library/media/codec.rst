Codec
=====

A `codec <https://en.wikipedia.org/wiki/Codec>`__ name identifies the algorithm used
to encode audio or video — ``h264``, ``aac``, ``vp9``. **Codec** matches the short
identifier shape these names take.

The construction is a leading :meth:`~edify.RegexBuilder.letter` then
:meth:`~edify.RegexBuilder.between`\ ``(1, 29)`` over an
:meth:`~edify.RegexBuilder.any_of` class of alphanumerics plus ``_``, ``.``, and
``-``. The dot matters: it is what lets the dotted profile strings from the
``codecs`` media-type parameter through.

Codec names
-----------

.. edify-playground::

   from edify.library import codec

   codec("h264")
   codec("aac")
   codec("vp9")
   codec("av1")
   codec("avc1.42E01E")     # a dotted profile string
   codec("mp4a.40.2")

A letter must lead
------------------

.. edify-playground::

   from edify.library import codec

   codec("h264")   # valid
   codec("264")    # starts with a digit
   codec("x")      # too short
   codec("")       # empty

Codec naming is inconsistent across specifications — ``h264``, ``H.264``, and
``avc1`` all name the same thing — so this matches the identifier shape rather than
a registry. For the container's media type see :doc:`mimetype`.
