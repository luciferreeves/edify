Contact
=======

Ways to reach a person — email addresses, telephone numbers, handles, and postal
addresses. Each validator is a callable :class:`~edify.Pattern`: import it, call it
with a string, get a ``bool``.

.. code-block:: python

   from edify.library import email, phone, handle

   email("first.last@example.com")   # True
   phone("+1 555 123 4567")          # True
   handle("@alice")                  # True

.. toctree::
   :hidden:

   address
   email
   email_rfc_5322
   fax
   handle
   pager
   phone
   username

Electronic mail
---------------

- :doc:`email` — the practical address shape you should validate against.
- :doc:`email_rfc_5322` — the full grammar, including quoted local parts.

Telephone
---------

- :doc:`phone` — international and national number shapes.
- :doc:`fax` — the same, for a fax line; :doc:`pager` — a numeric pager code.

Names and addresses
-------------------

- :doc:`username` — an account name; :doc:`handle` — an ``@``-prefixed public handle.
- :doc:`address` — a street address beginning with a building number.
