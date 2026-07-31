SAML
====

`SAML 2.0 <https://docs.oasis-open.org/security/saml/v2.0/>`__ is the XML standard
behind most enterprise single sign-on. Its messages are recognised by two things
together: a known root element — a protocol message such as ``Response`` or
``AuthnRequest``, an ``Assertion``, or an ``EntityDescriptor`` from a metadata
document — and one of the ``urn:oasis:names:tc:SAML:2.0:`` namespaces. **SAML**
requires both.

The element name is an :meth:`~edify.RegexBuilder.any_of` over those roots, behind an
optional namespace prefix, and the namespace URN must appear somewhere in the
attributes that follow. An XML declaration may precede it.

Protocol messages
-----------------

The requests and responses exchanged during a sign-on:

.. edify-playground::

   from edify.library import saml

   saml('<samlp:Response xmlns:samlp="urn:oasis:names:tc:SAML:2.0:protocol"/>')
   saml('<samlp:AuthnRequest xmlns:samlp="urn:oasis:names:tc:SAML:2.0:protocol" ID="a1"/>')
   saml('<samlp:LogoutRequest xmlns:samlp="urn:oasis:names:tc:SAML:2.0:protocol"/>')

Assertions and metadata
-----------------------

The assertion carrying the identity claims, and the metadata describing a party:

.. edify-playground::

   from edify.library import saml

   saml('<Assertion xmlns="urn:oasis:names:tc:SAML:2.0:assertion"/>')
   saml('<?xml version="1.0"?>\n<EntityDescriptor xmlns="urn:oasis:names:tc:SAML:2.0:metadata" entityID="x"/>')

Both parts are required
-----------------------

A matching element without the SAML namespace, or the wrong root entirely, is
rejected — which is what stops an unrelated ``<Response>`` from passing:

.. edify-playground::

   from edify.library import saml

   saml('<Response xmlns="urn:oasis:names:tc:SAML:2.0:protocol"/>')   # element + namespace
   saml("<Response/>")                              # no SAML namespace
   saml('<Response xmlns="urn:other"/>')            # the wrong namespace
   saml("hello-world")                               # not XML

It identifies the message; it does not verify the signature, the assertion
conditions, or the audience — those need a full SAML implementation, and the
signature check in particular must never be skipped. For the modern alternative see
:doc:`openid`.
