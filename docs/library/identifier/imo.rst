IMO
===

An `IMO number <https://www.imo.org/en/OurWork/MSAS/Pages/IMO-identification-number-scheme.aspx>`__
identifies a ship for its entire life — it never changes, even when the vessel is
sold, renamed, or reflagged. It is the literal ``IMO`` followed by seven digits, and
**IMO** matches that.

The construction is the :meth:`~edify.RegexBuilder.string` literal ``IMO`` then
:meth:`~edify.RegexBuilder.exactly`\ ``(7)`` :meth:`~edify.RegexBuilder.digit`.

Ship identifiers
----------------

.. edify-playground::

   from edify.library import imo

   imo("IMO9074729")   # Oasis of the Seas
   imo("IMO1234567")
   imo("IMO0000001")

The prefix is required
----------------------

.. edify-playground::

   from edify.library import imo

   imo("IMO9074729")   # prefixed
   imo("9074729")      # bare digits
   imo("imo9074729")   # lowercase prefix
   imo("IMO 9074729")  # a space after the prefix
   imo("IMO907472")    # six digits
   imo("")             # empty

The seventh digit is a weighted check digit that this cannot compute. Because an IMO
number is permanent while the ship's name, flag, and :doc:`mmsi` all change, it is
the reliable key for vessel records.
