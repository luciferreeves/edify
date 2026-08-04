API
===

Every validator in the :doc:`api <../../library/api/index>` category. Each is a
callable :class:`~edify.Pattern`: pass a string to get a ``bool``, or compose it into a
larger pattern with :meth:`~edify.RegexBuilder.use`.

For what each one accepts and rejects, with runnable examples, see the
:doc:`library pages <../../library/api/index>`.

.. py:function:: edify.library.atom(value: str) -> bool

   Atom. See :doc:`../../library/api/atom` for the full description.

   Emits ``^\s*(?:<\?xml.*)?<feed.*http://www\.w3\.org/2005/Atom.*$``

.. py:function:: edify.library.graphql(value: str) -> bool

   GraphQL. See :doc:`../../library/api/graphql` for the full description.

   Emits ``^\s*(?:(?:query|mutation|subscription|fragment|schema|type|input|interface|union|enum|scalar|directive|extend)(?:\s|[{(@])|\#|\{\s*(?:[a-zA-Z]|[_.]).*\}).*$``

.. py:function:: edify.library.hal(value: str) -> bool

   HAL. See :doc:`../../library/api/hal` for the full description.

   Emits ``^\s*\{.*"(?:_links|_embedded)"\s*:.*\}\s*$``

.. py:function:: edify.library.jsonapi(value: str) -> bool

   JSON:API. See :doc:`../../library/api/jsonapi` for the full description.

   Emits ``^\s*\{.*"(?:jsonapi|data|errors)"\s*:.*\}\s*$``

.. py:function:: edify.library.oauth(value: str) -> bool

   OAuth. See :doc:`../../library/api/oauth` for the full description.

   Emits ``^(?:urn:ietf:params:oauth:grant\-type:(?:[a-zA-Z0-9]|[-_.])+|(?:authorization_code|client_credentials|refresh_token|password|implicit|device_code))$``

.. py:function:: edify.library.openapi(value: str) -> bool

   OpenAPI. See :doc:`../../library/api/openapi` for the full description.

   Emits ``^\s*(?:\{.*"openapi"\s*:\s*"3\.\d+(?:\d|[\.])*|openapi\s*:\s*["']?3\.\d+(?:\d|[\.])*).*$``

.. py:function:: edify.library.openid(value: str) -> bool

   OpenID Connect. See :doc:`../../library/api/openid` for the full description.

   Emits ``^(?:https://(?:[a-zA-Z0-9]|[-.])+(?::\d{1,5})?)?(?:[a-zA-Z0-9]|[-._~/])*/\.well\-known/openid\-configuration/?$``

.. py:function:: edify.library.rss(value: str) -> bool

   RSS. See :doc:`../../library/api/rss` for the full description.

   Emits ``^\s*(?:<\?xml.*)?<rss(?:\s|[>]).*$``

.. py:function:: edify.library.saml(value: str) -> bool

   SAML. See :doc:`../../library/api/saml` for the full description.

   Emits ``^\s*(?:<\?xml.*)?<(?:(?:[a-zA-Z0-9]|[-_])+:)?(?:Response|AuthnRequest|LogoutRequest|LogoutResponse|Assertion|EntityDescriptor).*urn:oasis:names:tc:SAML:2\.0:.*$``

.. py:function:: edify.library.soap(value: str) -> bool

   SOAP. See :doc:`../../library/api/soap` for the full description.

   Emits ``^\s*(?:<\?xml.*)?<(?:(?:[a-zA-Z0-9]|[-_])+:)?Envelope.*http://schemas\.xmlsoap\.org/soap/envelope/.*$``

.. py:function:: edify.library.swagger(value: str) -> bool

   Swagger. See :doc:`../../library/api/swagger` for the full description.

   Emits ``^\s*(?:\{.*"swagger"\s*:\s*"2\.0|swagger\s*:\s*["']?2\.0).*$``

.. py:function:: edify.library.webhook(value: str) -> bool

   Webhook. See :doc:`../../library/api/webhook` for the full description.

   Emits ``^https://(?:[a-zA-Z0-9]|[-])+(?:\.(?:[a-zA-Z0-9]|[-])+)+(?::\d{1,5})?/(?:[a-zA-Z0-9]|[-._~/%?&=+:@#])*$``

