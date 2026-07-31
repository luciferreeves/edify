Package
=======

**Package** matches a `registry package name <https://docs.npmjs.com/package-name-guidelines>`__
— a plain name such as ``lodash``, or a scoped one such as ``@babel/core``.

The construction is an :meth:`~edify.RegexBuilder.optional` ``@scope/`` prefix, then
a name that must start with a lowercase alphanumeric and may continue with ``.``,
``_``, and ``-`` up to the registry's 214-character limit.

Plain and scoped names
----------------------

.. edify-playground::

   from edify.library import package

   package("lodash")
   package("my-package")
   package("@babel/core")        # a scope
   package("@my-org/utils")
   package("some.package_name")  # dots and underscores

Lowercase, alphanumeric-led
---------------------------

Registries fold case, so a name with capitals is not canonical:

.. edify-playground::

   from edify.library import package

   package("my-package")   # canonical
   package("My-Package")   # uppercase
   package("-leading")     # must start alphanumeric
   package("")             # empty

Matching says nothing about availability — a name may be taken, deprecated, or
deliberately squatted. Be wary of near-miss names when installing: typosquatting
relies on a package that is perfectly well formed. For a name pinned to a version see
:doc:`component`; for the crate ecosystem, :doc:`cargo`.
