Auth
====

Credentials, tokens, and the secrets behind them. These validators check the
*shape* of a credential — its character set and length — which is what you can
assert without the issuing system. None of them verify a signature, an expiry, or
that a credential was ever issued; treat a match as "well formed", never as
"authentic".

.. code-block:: python

   from edify.library import jwt, otp, apikey

   jwt("eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIxIn0.sig")   # True
   otp("123456")                                      # True
   apikey("sk_live_51H8xQ2eZvKYlo2C0abcdef")          # True

.. toctree::
   :hidden:

   apikey
   bearer
   challenge
   csrf
   hmac
   jwt
   mfa
   mnemonic
   otp
   passkey
   password
   pin
   refresh
   secret
   session
   signing
   sso
   token
   webauthn

Tokens you send
---------------

- :doc:`jwt` — a three-part signed token; :doc:`bearer` — the header that carries one.
- :doc:`token` — a generic opaque access token; :doc:`refresh` — the longer-lived
  token that renews it.
- :doc:`apikey` — a client's long-lived key; :doc:`sso` — a federated sign-on payload.

Human-entered codes
-------------------

- :doc:`otp` and :doc:`mfa` — one-time codes from an app or SMS.
- :doc:`pin` — a numeric personal code; :doc:`password` — a configurable strength policy.
- :doc:`mnemonic` — a recovery phrase of dictionary words.

Keys and secrets
----------------

- :doc:`secret` — a shared secret; :doc:`signing` — a key used to sign payloads.
- :doc:`hmac` — a hexadecimal message authentication code.
- :doc:`passkey` and :doc:`webauthn` — public-key credential identifiers.

Session and request safety
--------------------------

- :doc:`session` — a session identifier; :doc:`csrf` — a per-form request token.
- :doc:`challenge` — a server-issued nonce awaiting a response.
