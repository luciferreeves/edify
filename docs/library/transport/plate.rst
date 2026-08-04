Plate
=====

A `registration plate <https://en.wikipedia.org/wiki/Vehicle_registration_plate>`__
number identifies a vehicle within a jurisdiction. Formats vary enormously between
countries, so **Plate** matches the common shape: one to three characters, an
optional separator, then one to four more.

The construction is :meth:`~edify.RegexBuilder.between`\ ``(1, 3)`` uppercase
alphanumerics, an :meth:`~edify.RegexBuilder.optional` hyphen or space, then
:meth:`~edify.RegexBuilder.between`\ ``(1, 4)`` more.

Plate formats
-------------

.. edify-playground::

   from edify.library import plate

   plate("ABC123")     # a common US format
   plate("ABC-123")    # with a hyphen
   plate("AB 1234")    # with a space
   plate("123ABCD")
   plate("XYZ 999")

Uppercase, two groups
---------------------

.. edify-playground::

   from edify.library import plate

   plate("ABC123")     # valid
   plate("abc123")     # lowercase
   plate("AB-12-CD")   # three groups
   plate("")           # empty

The three-group forms used across much of Europe — ``AB-12-CD`` — are **not**
matched, so this suits single-jurisdiction data rather than international input.
Plates are also reassigned over time and are not unique across jurisdictions: the
:doc:`vehicle` identification number is the stable identifier.
