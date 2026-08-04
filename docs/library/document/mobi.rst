MOBI
====

A `MOBI <https://wiki.mobileread.com/wiki/MOBI>`__ e-book is stored in the old Palm
database container, and its identity sits at a fixed offset rather than the start of
the file: the eight bytes ``BOOKMOBI`` begin at byte 60, after the database name and
attribute fields. **MOBI** checks exactly that position.

The construction is :meth:`~edify.RegexBuilder.exactly`\ ``(60)``
:meth:`~edify.RegexBuilder.any_char` — consuming the header without inspecting it —
then the :meth:`~edify.RegexBuilder.string` literal ``BOOKMOBI``, all under
:meth:`~edify.RegexBuilder.dot_all` so the binary header's newlines are consumed
too.

The type and creator at offset 60
---------------------------------

.. edify-playground::

   from edify.library import mobi

   mobi("X" * 60 + "BOOKMOBI")                 # the marker in position
   mobi("X" * 60 + "BOOKMOBIrest of the book")
   mobi("\x00" * 60 + "BOOKMOBI")              # a realistic binary header

The offset is exact
-------------------

One byte out in either direction and it is not a MOBI file — which is the whole
value of a positioned marker:

.. edify-playground::

   from edify.library import mobi

   mobi("X" * 60 + "BOOKMOBI")   # at offset 60
   mobi("X" * 59 + "BOOKMOBI")   # one byte early
   mobi("X" * 61 + "BOOKMOBI")   # one byte late
   mobi("BOOKMOBI")              # at the start
   mobi("hello")                 # too short to reach the offset

The marker identifies the container; the EXTH metadata and compressed text records
inside are a reader's concern. For the modern e-book format see :doc:`epub`.
