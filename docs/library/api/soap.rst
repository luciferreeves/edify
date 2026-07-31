SOAP
====

A `SOAP <https://www.w3.org/TR/2000/NOTE-SOAP-20000508/>`__ message is an XML
document whose root element is an ``Envelope`` bound to the SOAP namespace. That
pairing is the whole test: the element name alone is too common to be meaningful, so
**SOAP** requires the ``http://schemas.xmlsoap.org/soap/envelope/`` namespace to
appear as well.

An XML declaration may come first and is wrapped in
:meth:`~edify.RegexBuilder.optional`. The element may carry any namespace prefix —
``soap:``, ``soapenv:``, or none at all — so the prefix is an optional group of
name characters ending in a colon.

Prefixed and unprefixed envelopes
---------------------------------

The prefix is a local choice; what matters is the namespace it is bound to:

.. edify-playground::

   from edify.library import soap

   soap('<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"><soap:Body/></soap:Envelope>')
   soap('<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"/>')
   soap('<Envelope xmlns="http://schemas.xmlsoap.org/soap/envelope/"/>')

With an XML declaration
-----------------------

Most SOAP on the wire is a complete XML document, declaration and all:

.. edify-playground::

   from edify.library import soap

   soap('<?xml version="1.0" encoding="UTF-8"?>\n<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">\n  <soap:Body/>\n</soap:Envelope>')

The namespace is required
-------------------------

An ``Envelope`` element without the SOAP namespace is just XML that happens to share
a tag name:

.. edify-playground::

   from edify.library import soap

   soap("<Envelope/>")                       # no namespace
   soap('<Envelope xmlns="urn:other"/>')     # the wrong namespace
   soap("hello-world")                        # not XML

It recognises a SOAP 1.1 envelope; it does not check the header and body structure,
the fault format, or the 1.2 namespace. For plain XML validity see
:doc:`../data/xml`, and for the identity assertions often carried inside a SOAP
header, :doc:`saml`.
