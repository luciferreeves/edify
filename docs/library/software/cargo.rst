Cargo
=====

**Cargo** matches a `crate name <https://doc.rust-lang.org/cargo/reference/manifest.html>`__,
optionally pinned to a version — ``serde``, ``serde@1.0.195``. Unlike
:doc:`component`, the version is optional, and unlike :doc:`package` there are no
scopes: the crate registry has a single flat namespace.

The construction is a :meth:`~edify.RegexBuilder.letter`-led name of up to 64
characters over letters, digits, ``_``, and ``-``, then an
:meth:`~edify.RegexBuilder.optional` ``@version`` group.

Crate names
-----------

.. edify-playground::

   from edify.library import cargo

   cargo("serde")
   cargo("tokio_util")      # underscores
   cargo("my-crate")        # hyphens
   cargo("rand")

With a version
--------------

.. edify-playground::

   from edify.library import cargo

   cargo("serde@1.0.195")
   cargo("my-crate@2.0")
   cargo("tokio@1.35.1-rc.1")

A letter must lead
------------------

.. edify-playground::

   from edify.library import cargo

   cargo("serde")      # valid
   cargo("1bad")       # starts with a digit
   cargo("@scope/x")   # crates have no scopes
   cargo("")           # empty

Note that hyphens and underscores are interchangeable at the registry — ``my-crate``
and ``my_crate`` resolve to the same crate — so compare on a normalised form. For
other ecosystems see :doc:`package` and :doc:`component`.
