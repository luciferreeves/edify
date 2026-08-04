OAuth
=====

An `OAuth 2.0 <https://oauth.net/2/>`__ client tells the token endpoint *how* it is
authenticating by sending a ``grant_type`` parameter, and **OAuth** validates that
value. :rfc:`6749` defines a handful of names, later specifications add more, and
anyone may define their own using a URN — so the validator accepts both the
registered words and the extension form.

The two families are the branches of an :func:`~edify.any_of`. Registered grants
are matched with :meth:`~edify.RegexBuilder.string` alternatives; extension grants
are the ``urn:ietf:params:oauth:grant-type:`` prefix followed by a name. The
extension branch is tried first so a URN is never partly matched.

Registered grant types
----------------------

The values defined by the core specification and its companions:

.. edify-playground::

   from edify.library import oauth

   oauth("authorization_code")   # the standard web-app flow
   oauth("client_credentials")   # machine-to-machine
   oauth("refresh_token")        # exchanging a refresh token
   oauth("password")             # the legacy direct-credentials grant
   oauth("implicit")             # the deprecated browser flow

Extension grants
----------------

Anything registered as a URN — device authorisation, token exchange, JWT bearer,
and any private extension:

.. edify-playground::

   from edify.library import oauth

   oauth("urn:ietf:params:oauth:grant-type:device_code")
   oauth("urn:ietf:params:oauth:grant-type:token-exchange")
   oauth("urn:ietf:params:oauth:grant-type:jwt-bearer")

Exact values only
-----------------

Grant types are case-sensitive and carry no surrounding syntax, so the parameter
name, an uppercase spelling, or an unknown bare word all fail:

.. edify-playground::

   from edify.library import oauth

   oauth("authorization_code")       # the registered spelling
   oauth("AUTHORIZATION_CODE")       # grant types are lowercase
   oauth("grant_type")               # that is the parameter name
   oauth("magic_link")               # unregistered, and not a URN

It validates the grant-type value alone — not the token request around it, and not
the token that comes back. For the discovery document that advertises which grants
a server supports, see :doc:`openid`.
