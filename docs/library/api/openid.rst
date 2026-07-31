OpenID Connect
==============

`OpenID Connect <https://openid.net/developers/how-connect-works/>`__ layers
identity on top of OAuth 2.0, and every provider publishes its configuration at one
well-known location: the path ``/.well-known/openid-configuration``. **OpenID
Connect** matches that discovery endpoint, whether you hold a full URL or only the
path.

The origin is optional, wrapped in an :meth:`~edify.RegexBuilder.optional` group —
``https://`` followed by a dotted host and an optional port. Any path may precede
the well-known suffix, which supports the multi-tenant providers that namespace each
tenant. The scheme is fixed to ``https`` because discovery over plain HTTP is not
permitted.

Full discovery URLs
-------------------

The usual form, with or without a port, and with a tenant path where the provider
uses one:

.. edify-playground::

   from edify.library import openid

   openid("https://accounts.example.com/.well-known/openid-configuration")
   openid("https://id.example.com:8443/.well-known/openid-configuration")
   openid("https://login.example.com/tenant-a/.well-known/openid-configuration")

Bare paths
----------

Handy when the origin is already known and only the path is being routed or
compared:

.. edify-playground::

   from edify.library import openid

   openid("/.well-known/openid-configuration")    # the path alone
   openid("/tenant-a/.well-known/openid-configuration")

Only this endpoint, only over TLS
---------------------------------

A different well-known document, or an ``http`` origin, is not an OpenID Connect
discovery endpoint:

.. edify-playground::

   from edify.library import openid

   openid("/.well-known/openid-configuration")               # the discovery path
   openid("/.well-known/jwks.json")                          # the key set, not discovery
   openid("http://x.example.com/.well-known/openid-configuration")   # discovery requires https

Matching the endpoint says nothing about what the document contains — fetching and
parsing it is a separate step. For the grant types such a document advertises, see
:doc:`oauth`; for the identity assertions of the older federation protocol,
:doc:`saml`.
