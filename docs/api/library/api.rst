API
===

Every validator in the :doc:`API <../../library/api/index>` category.
Each is a callable :class:`~edify.Pattern`: pass a string to get a ``bool``, or
compose it into a larger pattern with :meth:`~edify.RegexBuilder.use`.

Each entry states what the pattern guarantees, shows the chain that builds it, and
ends with the regex it emits. For prose, worked examples, and a live playground, use
the :doc:`library pages <../../library/api/index>`.

.. py:data:: edify.library.atom

   Callable :class:`Pattern` for an Atom feed: a ``<feed`` root element carrying
   the Atom namespace.

   Full description: :doc:`Atom <../../library/api/atom>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      _declaration = Pattern().string("<?xml").zero_or_more().any_char()

      atom = (
          Pattern()
          .start_of_input()
          .zero_or_more()
          .whitespace_char()
          .optional()
          .use(_declaration)
          .string("<feed")
          .zero_or_more()
          .any_char()
          .string("http://www.w3.org/2005/Atom")
          .zero_or_more()
          .any_char()
          .end_of_input()
          .dot_all()
      )

   **Emits** ``^\s*(?:<\?xml.*)?<feed.*http://www\.w3\.org/2005/Atom.*$``

.. py:data:: edify.library.graphql

   Callable :class:`Pattern` for a GraphQL document: an operation, fragment, or
   type-system definition keyword, a comment, or an anonymous selection set.

   Full description: :doc:`GraphQL <../../library/api/graphql>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      _keyword = (
          Pattern()
          .any_of()
          .string("query")
          .string("mutation")
          .string("subscription")
          .string("fragment")
          .string("schema")
          .string("type")
          .string("input")
          .string("interface")
          .string("union")
          .string("enum")
          .string("scalar")
          .string("directive")
          .string("extend")
          .end()
          .any_of()
          .whitespace_char()
          .any_of_chars("{(@")
          .end()
      )

      _anonymous = (
          Pattern()
          .char("{")
          .zero_or_more()
          .whitespace_char()
          .any_of()
          .letter()
          .any_of_chars("_.")
          .end()
          .zero_or_more()
          .any_char()
          .char("}")
      )

      _comment = Pattern().char("#")

      graphql = (
          Pattern()
          .start_of_input()
          .zero_or_more()
          .whitespace_char()
          .any_of()
          .use(_keyword)
          .use(_comment)
          .use(_anonymous)
          .end()
          .zero_or_more()
          .any_char()
          .end_of_input()
          .dot_all()
      )

   **Emits** ``^\s*(?:(?:query|mutation|subscription|fragment|schema|type|input|interface|union|enum|scalar|directive|extend)(?:\s|[{(@])|\#|\{\s*(?:[a-zA-Z]|[_.]).*\}).*$``

.. py:data:: edify.library.hal

   Callable :class:`Pattern` for a hypertext application language document: a
   JSON object carrying a ``_links`` or ``_embedded`` member.

   Full description: :doc:`HAL <../../library/api/hal>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      hal = (
          Pattern()
          .start_of_input()
          .zero_or_more()
          .whitespace_char()
          .char("{")
          .zero_or_more()
          .any_char()
          .char('"')
          .any_of()
          .string("_links")
          .string("_embedded")
          .end()
          .char('"')
          .zero_or_more()
          .whitespace_char()
          .char(":")
          .zero_or_more()
          .any_char()
          .char("}")
          .zero_or_more()
          .whitespace_char()
          .end_of_input()
          .dot_all()
      )

   **Emits** ``^\s*\{.*"(?:_links|_embedded)"\s*:.*\}\s*$``

.. py:data:: edify.library.jsonapi

   Callable :class:`Pattern` for a JSON:API document: a JSON object carrying a
   top-level ``jsonapi``, ``data``, or ``errors`` member.

   Full description: :doc:`JSON:API <../../library/api/jsonapi>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      jsonapi = (
          Pattern()
          .start_of_input()
          .zero_or_more()
          .whitespace_char()
          .char("{")
          .zero_or_more()
          .any_char()
          .char('"')
          .any_of()
          .string("jsonapi")
          .string("data")
          .string("errors")
          .end()
          .char('"')
          .zero_or_more()
          .whitespace_char()
          .char(":")
          .zero_or_more()
          .any_char()
          .char("}")
          .zero_or_more()
          .whitespace_char()
          .end_of_input()
          .dot_all()
      )

   **Emits** ``^\s*\{.*"(?:jsonapi|data|errors)"\s*:.*\}\s*$``

.. py:data:: edify.library.oauth

   Callable :class:`Pattern` for an OAuth 2.0 grant type: a registered value or
   a ``urn:ietf:params:oauth:grant-type:`` extension URN.

   Full description: :doc:`OAuth <../../library/api/oauth>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      _registered = (
          Pattern()
          .any_of()
          .string("authorization_code")
          .string("client_credentials")
          .string("refresh_token")
          .string("password")
          .string("implicit")
          .string("device_code")
          .end()
      )

      _extension = (
          Pattern()
          .string("urn:ietf:params:oauth:grant-type:")
          .one_or_more()
          .any_of()
          .alphanumeric()
          .any_of_chars("-_.")
          .end()
      )

      oauth = Pattern().start_of_input().any_of().use(_extension).use(_registered).end().end_of_input()

   **Emits** ``^(?:urn:ietf:params:oauth:grant\-type:(?:[a-zA-Z0-9]|[-_.])+|(?:authorization_code|client_credentials|refresh_token|password|implicit|device_code))$``

.. py:data:: edify.library.openapi

   Callable :class:`Pattern` for an OpenAPI 3 document: an ``openapi: 3.x``
   declaration in YAML or JSON form.

   Full description: :doc:`OpenAPI <../../library/api/openapi>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      _version = (
          Pattern()
          .char("3")
          .char(".")
          .one_or_more()
          .digit()
          .zero_or_more()
          .any_of()
          .digit()
          .char(".")
          .end()
      )

      _yaml_form = (
          Pattern()
          .string("openapi")
          .zero_or_more()
          .whitespace_char()
          .char(":")
          .zero_or_more()
          .whitespace_char()
          .optional()
          .any_of_chars("\"'")
          .use(_version)
      )

      _json_form = (
          Pattern()
          .char("{")
          .zero_or_more()
          .any_char()
          .char('"')
          .string("openapi")
          .char('"')
          .zero_or_more()
          .whitespace_char()
          .char(":")
          .zero_or_more()
          .whitespace_char()
          .char('"')
          .use(_version)
      )

      openapi = (
          Pattern()
          .start_of_input()
          .zero_or_more()
          .whitespace_char()
          .any_of()
          .use(_json_form)
          .use(_yaml_form)
          .end()
          .zero_or_more()
          .any_char()
          .end_of_input()
          .dot_all()
      )

   **Emits** ``^\s*(?:\{.*"openapi"\s*:\s*"3\.\d+(?:\d|[\.])*|openapi\s*:\s*["']?3\.\d+(?:\d|[\.])*).*$``

.. py:data:: edify.library.openid

   Callable :class:`Pattern` for an OpenID Connect discovery endpoint: a
   ``/.well-known/openid-configuration`` path, with or without an ``https`` origin.

   Full description: :doc:`OpenID Connect <../../library/api/openid>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      _host = (
          Pattern()
          .one_or_more()
          .any_of()
          .alphanumeric()
          .any_of_chars("-.")
          .end()
          .optional()
          .group()
          .char(":")
          .between(1, 5)
          .digit()
          .end()
      )

      _path = Pattern().zero_or_more().any_of().alphanumeric().any_of_chars("-._~/").end()

      openid = (
          Pattern()
          .start_of_input()
          .optional()
          .group()
          .string("https://")
          .use(_host)
          .end()
          .use(_path)
          .string("/.well-known/openid-configuration")
          .optional()
          .char("/")
          .end_of_input()
      )

   **Emits** ``^(?:https://(?:[a-zA-Z0-9]|[-.])+(?::\d{1,5})?)?(?:[a-zA-Z0-9]|[-._~/])*/\.well\-known/openid\-configuration/?$``

.. py:data:: edify.library.rss

   Callable :class:`Pattern` for an RSS feed: an ``<rss`` root element,
   optionally preceded by an XML declaration.

   Full description: :doc:`RSS <../../library/api/rss>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      _declaration = Pattern().string("<?xml").zero_or_more().any_char()

      rss = (
          Pattern()
          .start_of_input()
          .zero_or_more()
          .whitespace_char()
          .optional()
          .use(_declaration)
          .string("<rss")
          .any_of()
          .whitespace_char()
          .char(">")
          .end()
          .zero_or_more()
          .any_char()
          .end_of_input()
          .dot_all()
      )

   **Emits** ``^\s*(?:<\?xml.*)?<rss(?:\s|[>]).*$``

.. py:data:: edify.library.saml

   Callable :class:`Pattern` for a SAML 2.0 message: a protocol or assertion
   element carrying a ``urn:oasis:names:tc:SAML:2.0:`` namespace.

   Full description: :doc:`SAML <../../library/api/saml>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      _declaration = Pattern().string("<?xml").zero_or_more().any_char()

      _prefix = Pattern().one_or_more().any_of().alphanumeric().any_of_chars("-_").end().char(":")

      _element = (
          Pattern()
          .char("<")
          .optional()
          .use(_prefix)
          .any_of()
          .string("Response")
          .string("AuthnRequest")
          .string("LogoutRequest")
          .string("LogoutResponse")
          .string("Assertion")
          .string("EntityDescriptor")
          .end()
          .zero_or_more()
          .any_char()
          .string("urn:oasis:names:tc:SAML:2.0:")
      )

      saml = (
          Pattern()
          .start_of_input()
          .zero_or_more()
          .whitespace_char()
          .optional()
          .use(_declaration)
          .use(_element)
          .zero_or_more()
          .any_char()
          .end_of_input()
          .dot_all()
      )

   **Emits** ``^\s*(?:<\?xml.*)?<(?:(?:[a-zA-Z0-9]|[-_])+:)?(?:Response|AuthnRequest|LogoutRequest|LogoutResponse|Assertion|EntityDescriptor).*urn:oasis:names:tc:SAML:2\.0:.*$``

.. py:data:: edify.library.soap

   Callable :class:`Pattern` for a SOAP 1.1 message: an ``Envelope`` root
   element carrying the SOAP envelope namespace.

   Full description: :doc:`SOAP <../../library/api/soap>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      _declaration = Pattern().string("<?xml").zero_or_more().any_char()

      _prefix = Pattern().one_or_more().any_of().alphanumeric().any_of_chars("-_").end().char(":")

      soap = (
          Pattern()
          .start_of_input()
          .zero_or_more()
          .whitespace_char()
          .optional()
          .use(_declaration)
          .char("<")
          .optional()
          .use(_prefix)
          .string("Envelope")
          .zero_or_more()
          .any_char()
          .string("http://schemas.xmlsoap.org/soap/envelope/")
          .zero_or_more()
          .any_char()
          .end_of_input()
          .dot_all()
      )

   **Emits** ``^\s*(?:<\?xml.*)?<(?:(?:[a-zA-Z0-9]|[-_])+:)?Envelope.*http://schemas\.xmlsoap\.org/soap/envelope/.*$``

.. py:data:: edify.library.swagger

   Callable :class:`Pattern` for a Swagger 2.0 document: a ``swagger: "2.0"``
   declaration in YAML or JSON form.

   Full description: :doc:`Swagger <../../library/api/swagger>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      _yaml_form = (
          Pattern()
          .string("swagger")
          .zero_or_more()
          .whitespace_char()
          .char(":")
          .zero_or_more()
          .whitespace_char()
          .optional()
          .any_of_chars("\"'")
          .string("2.0")
      )

      _json_form = (
          Pattern()
          .char("{")
          .zero_or_more()
          .any_char()
          .char('"')
          .string("swagger")
          .char('"')
          .zero_or_more()
          .whitespace_char()
          .char(":")
          .zero_or_more()
          .whitespace_char()
          .char('"')
          .string("2.0")
      )

      swagger = (
          Pattern()
          .start_of_input()
          .zero_or_more()
          .whitespace_char()
          .any_of()
          .use(_json_form)
          .use(_yaml_form)
          .end()
          .zero_or_more()
          .any_char()
          .end_of_input()
          .dot_all()
      )

   **Emits** ``^\s*(?:\{.*"swagger"\s*:\s*"2\.0|swagger\s*:\s*["']?2\.0).*$``

.. py:data:: edify.library.webhook

   Callable :class:`Pattern` for a webhook callback endpoint: an ``https`` URL
   with a dotted host and a delivery path.

   Full description: :doc:`Webhook <../../library/api/webhook>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      _host = (
          Pattern()
          .one_or_more()
          .any_of()
          .alphanumeric()
          .any_of_chars("-")
          .end()
          .one_or_more()
          .group()
          .char(".")
          .one_or_more()
          .any_of()
          .alphanumeric()
          .any_of_chars("-")
          .end()
          .end()
      )

      _port = Pattern().char(":").between(1, 5).digit()

      _tail = (
          Pattern().char("/").zero_or_more().any_of().alphanumeric().any_of_chars("-._~/%?&=+:@#").end()
      )

      webhook = (
          Pattern()
          .start_of_input()
          .string("https://")
          .use(_host)
          .optional()
          .use(_port)
          .use(_tail)
          .end_of_input()
      )

   **Emits** ``^https://(?:[a-zA-Z0-9]|[-])+(?:\.(?:[a-zA-Z0-9]|[-])+)+(?::\d{1,5})?/(?:[a-zA-Z0-9]|[-._~/%?&=+:@#])*$``

