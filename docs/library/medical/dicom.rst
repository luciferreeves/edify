DICOM
=====

A `DICOM <https://www.dicomstandard.org/>`__ unique identifier names a study, series,
or instance in medical imaging. It is an ISO object identifier: dot-separated numeric
components, such as ``1.2.840.10008.1.1``. **DICOM** matches that structure.

The construction is :meth:`~edify.RegexBuilder.one_or_more`
:meth:`~edify.RegexBuilder.digit`, then
:meth:`~edify.RegexBuilder.one_or_more` groups of ``.`` plus more digits — so at
least two components are required.

Object identifiers
------------------

.. edify-playground::

   from edify.library import dicom

   dicom("1.2.840.10008.1.1")          # a standard SOP class
   dicom("1.2.840.113619.2.55.3.123")  # a vendor identifier
   dicom("1.2.3")                       # a short identifier
   dicom("2.16.840.1.113883")           # an HL7 arc

Digits and dots
---------------

.. edify-playground::

   from edify.library import dicom

   dicom("1.2.3")     # valid
   dicom("1")         # a single component
   dicom("1.2.a")     # a letter
   dicom("1..2")      # an empty component
   dicom("")          # empty

The standard also caps a UID at 64 characters and forbids a leading zero in a
component — neither is enforced here. Identifiers in imaging data are frequently
patient-linked, so treat them as sensitive.
