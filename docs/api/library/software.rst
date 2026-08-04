Software
========

Every validator in the :doc:`Software <../../library/software/index>` category.
Each is a callable :class:`~edify.Pattern`: pass a string to get a ``bool``, or
compose it into a larger pattern with :meth:`~edify.RegexBuilder.use`.

Each entry states what the pattern guarantees, shows the chain that builds it, and
ends with the regex it emits. For prose, worked examples, and a live playground, use
the :doc:`library pages <../../library/software/index>`.

.. py:data:: edify.library.bump

   Callable :class:`Pattern` for a semver bump keyword.

   Full description: :doc:`Bump <../../library/software/bump>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      bump = (
          Pattern()
          .start_of_input()
          .any_of()
          .string("major")
          .string("minor")
          .string("patch")
          .string("premajor")
          .string("preminor")
          .string("prepatch")
          .string("prerelease")
          .string("release")
          .end()
          .end_of_input()
      )

   **Emits** ``^(?:major|minor|patch|premajor|preminor|prepatch|prerelease|release)$``

.. py:data:: edify.library.cargo

   Callable :class:`Pattern` for a Cargo crate identifier.

   Full description: :doc:`Cargo <../../library/software/cargo>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      cargo = (
          Pattern()
          .start_of_input()
          .letter()
          .between(0, 63)
          .any_of()
          .range("a", "z")
          .range("A", "Z")
          .range("0", "9")
          .char("_")
          .char("-")
          .end()
          .optional()
          .group()
          .char("@")
          .one_or_more()
          .digit()
          .between(0, 3)
          .group()
          .char(".")
          .one_or_more()
          .digit()
          .end()
          .optional()
          .group()
          .any_of_chars("-.+")
          .one_or_more()
          .any_of()
          .range("a", "z")
          .range("A", "Z")
          .range("0", "9")
          .char(".")
          .char("-")
          .end()
          .end()
          .end()
          .end_of_input()
      )

   **Emits** ``^[a-zA-Z][a-zA-Z0-9_\-]{0,63}(?:@\d+(?:\.\d+){0,3}(?:[-.+][a-zA-Z0-9\.\-]+)?)?$``

.. py:data:: edify.library.checksum

   Callable :class:`Pattern` for a hex checksum (any common hash width).

   Full description: :doc:`Checksum <../../library/software/checksum>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      checksum = (
          Pattern()
          .start_of_input()
          .between(8, 128)
          .any_of()
          .range("a", "f")
          .range("A", "F")
          .range("0", "9")
          .end()
          .end_of_input()
      )

   **Emits** ``^[a-fA-F0-9]{8,128}$``

.. py:data:: edify.library.component

   Callable :class:`Pattern` for a versioned component identifier ``name@version``.

   Full description: :doc:`Component <../../library/software/component>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      component = (
          Pattern()
          .start_of_input()
          .optional()
          .group()
          .char("@")
          .any_of()
          .range("a", "z")
          .range("0", "9")
          .end()
          .zero_or_more()
          .any_of()
          .range("a", "z")
          .range("0", "9")
          .char("-")
          .end()
          .char("/")
          .end()
          .any_of()
          .range("a", "z")
          .range("0", "9")
          .end()
          .between(0, 213)
          .any_of()
          .range("a", "z")
          .range("0", "9")
          .char(".")
          .char("_")
          .char("-")
          .end()
          .char("@")
          .one_or_more()
          .digit()
          .between(0, 3)
          .group()
          .char(".")
          .one_or_more()
          .digit()
          .end()
          .optional()
          .group()
          .any_of_chars("-.+")
          .one_or_more()
          .any_of()
          .range("a", "z")
          .range("A", "Z")
          .range("0", "9")
          .char(".")
          .char("-")
          .end()
          .end()
          .end_of_input()
      )

   **Emits** ``^(?:@[a-z0-9][a-z0-9\-]*/)?[a-z0-9][a-z0-9\._\-]{0,213}@\d+(?:\.\d+){0,3}(?:[-.+][a-zA-Z0-9\.\-]+)?$``

.. py:data:: edify.library.digest

   Callable :class:`Pattern` for a content-addressable digest.

   Full description: :doc:`Digest <../../library/software/digest>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      digest = (
          Pattern()
          .start_of_input()
          .group()
          .any_of()
          .string("sha256")
          .string("sha512")
          .string("sha1")
          .string("md5")
          .subexpression(Pattern().string("blake2").optional().any_of_chars("bs"))
          .end()
          .end()
          .any_of_chars(":-")
          .between(32, 128)
          .any_of()
          .range("a", "f")
          .range("A", "F")
          .range("0", "9")
          .end()
          .end_of_input()
      )

   **Emits** ``^(?:(?:sha256|sha512|sha1|md5|blake2[bs]?))[:-][a-fA-F0-9]{32,128}$``

.. py:data:: edify.library.docker

   Callable :class:`Pattern` for a docker image reference.

   Full description: :doc:`Docker <../../library/software/docker>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      docker = (
          Pattern()
          .start_of_input()
          .group()
          .optional()
          .group()
          .one_or_more()
          .any_of()
          .range("a", "z")
          .range("0", "9")
          .char(".")
          .char("-")
          .end()
          .optional()
          .group()
          .char(":")
          .one_or_more()
          .digit()
          .end()
          .char("/")
          .end()
          .one_or_more()
          .any_of()
          .range("a", "z")
          .range("0", "9")
          .end()
          .zero_or_more()
          .group()
          .any_of_chars("._-")
          .one_or_more()
          .any_of()
          .range("a", "z")
          .range("0", "9")
          .end()
          .end()
          .end()
          .zero_or_more()
          .group()
          .char("/")
          .one_or_more()
          .any_of()
          .range("a", "z")
          .range("0", "9")
          .end()
          .zero_or_more()
          .group()
          .any_of_chars("._-")
          .one_or_more()
          .any_of()
          .range("a", "z")
          .range("0", "9")
          .end()
          .end()
          .end()
          .optional()
          .group()
          .char(":")
          .any_of()
          .range("a", "z")
          .range("A", "Z")
          .range("0", "9")
          .char("_")
          .end()
          .between(0, 127)
          .any_of()
          .range("a", "z")
          .range("A", "Z")
          .range("0", "9")
          .char(".")
          .char("_")
          .char("-")
          .end()
          .end()
          .optional()
          .group()
          .string("@sha256:")
          .exactly(64)
          .any_of()
          .range("a", "f")
          .range("0", "9")
          .end()
          .end()
          .end_of_input()
      )

   **Emits** ``^(?:(?:[a-z0-9\.\-]+(?::\d+)?/)?[a-z0-9]+(?:[._-][a-z0-9]+)*)(?:/[a-z0-9]+(?:[._-][a-z0-9]+)*)*(?::[a-zA-Z0-9_][a-zA-Z0-9\._\-]{0,127})?(?:@sha256:[a-f0-9]{64})?$``

.. py:data:: edify.library.git

   Callable :class:`Pattern` for a git commit SHA (7-40 hex characters).

   Full description: :doc:`Git <../../library/software/git>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      git = (
          Pattern()
          .start_of_input()
          .between(7, 40)
          .any_of()
          .range("a", "f")
          .range("0", "9")
          .end()
          .end_of_input()
      )

   **Emits** ``^[a-f0-9]{7,40}$``

.. py:data:: edify.library.image

   Callable :class:`Pattern` for a image image reference.

   Full description: :doc:`Image <../../library/software/image>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      image = (
          Pattern()
          .start_of_input()
          .group()
          .optional()
          .group()
          .one_or_more()
          .any_of()
          .range("a", "z")
          .range("0", "9")
          .char(".")
          .char("-")
          .end()
          .optional()
          .group()
          .char(":")
          .one_or_more()
          .digit()
          .end()
          .char("/")
          .end()
          .one_or_more()
          .any_of()
          .range("a", "z")
          .range("0", "9")
          .end()
          .zero_or_more()
          .group()
          .any_of_chars("._-")
          .one_or_more()
          .any_of()
          .range("a", "z")
          .range("0", "9")
          .end()
          .end()
          .end()
          .zero_or_more()
          .group()
          .char("/")
          .one_or_more()
          .any_of()
          .range("a", "z")
          .range("0", "9")
          .end()
          .zero_or_more()
          .group()
          .any_of_chars("._-")
          .one_or_more()
          .any_of()
          .range("a", "z")
          .range("0", "9")
          .end()
          .end()
          .end()
          .optional()
          .group()
          .char(":")
          .any_of()
          .range("a", "z")
          .range("A", "Z")
          .range("0", "9")
          .char("_")
          .end()
          .between(0, 127)
          .any_of()
          .range("a", "z")
          .range("A", "Z")
          .range("0", "9")
          .char(".")
          .char("_")
          .char("-")
          .end()
          .end()
          .optional()
          .group()
          .string("@sha256:")
          .exactly(64)
          .any_of()
          .range("a", "f")
          .range("0", "9")
          .end()
          .end()
          .end_of_input()
      )

   **Emits** ``^(?:(?:[a-z0-9\.\-]+(?::\d+)?/)?[a-z0-9]+(?:[._-][a-z0-9]+)*)(?:/[a-z0-9]+(?:[._-][a-z0-9]+)*)*(?::[a-zA-Z0-9_][a-zA-Z0-9\._\-]{0,127})?(?:@sha256:[a-f0-9]{64})?$``

.. py:data:: edify.library.makefile

   Callable :class:`Pattern` for a Makefile-target declaration line.

   Full description: :doc:`Makefile <../../library/software/makefile>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      makefile = (
          Pattern()
          .start_of_input()
          .optional()
          .char(".")
          .letter()
          .zero_or_more()
          .any_of()
          .range("a", "z")
          .range("A", "Z")
          .range("0", "9")
          .char(".")
          .char("_")
          .char("-")
          .end()
          .zero_or_more()
          .group()
          .one_or_more()
          .whitespace_char()
          .letter()
          .zero_or_more()
          .any_of()
          .range("a", "z")
          .range("A", "Z")
          .range("0", "9")
          .char(".")
          .char("_")
          .char("-")
          .end()
          .end()
          .zero_or_more()
          .whitespace_char()
          .char(":")
          .zero_or_more()
          .any_char()
          .end_of_input()
      )

   **Emits** ``^\.?[a-zA-Z][a-zA-Z0-9\._\-]*(?:\s+[a-zA-Z][a-zA-Z0-9\._\-]*)*\s*:.*$``

.. py:data:: edify.library.package

   Callable :class:`Pattern` for an npm/pypi-style package identifier.

   Full description: :doc:`Package <../../library/software/package>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      package = (
          Pattern()
          .start_of_input()
          .optional()
          .group()
          .char("@")
          .any_of()
          .range("a", "z")
          .range("0", "9")
          .end()
          .zero_or_more()
          .any_of()
          .range("a", "z")
          .range("0", "9")
          .char("-")
          .end()
          .char("/")
          .end()
          .any_of()
          .range("a", "z")
          .range("0", "9")
          .end()
          .between(0, 213)
          .any_of()
          .range("a", "z")
          .range("0", "9")
          .char(".")
          .char("_")
          .char("-")
          .end()
          .end_of_input()
      )

   **Emits** ``^(?:@[a-z0-9][a-z0-9\-]*/)?[a-z0-9][a-z0-9\._\-]{0,213}$``

.. py:data:: edify.library.ref

   Callable :class:`Pattern` for a git ref: SHA, ``refs/heads/…``, or bare branch/tag name.

   Full description: :doc:`Ref <../../library/software/ref>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern, any_of


      def _forbidden() -> Pattern:
          return (
              Pattern()
              .assert_not_ahead()
              .any_of()
              .whitespace_char()
              .any_of_chars("~^:?*[\\")
              .end()
              .end()
              .any_char()
          )


      def _forbidden_incl_slash() -> Pattern:
          return (
              Pattern()
              .assert_not_ahead()
              .any_of()
              .whitespace_char()
              .any_of_chars("~^:?*[\\/")
              .end()
              .end()
              .any_char()
          )


      _sha = Pattern().between(7, 40).any_of().range("a", "f").range("0", "9").end()
      _refs = (
          Pattern()
          .string("refs/")
          .group()
          .any_of()
          .string("heads")
          .string("tags")
          .string("remotes")
          .end()
          .end()
          .char("/")
          .one_or_more()
          .subexpression(_forbidden())
      )
      _bare = Pattern().subexpression(_forbidden_incl_slash()).between(0, 127).subexpression(_forbidden())

      ref = Pattern().start_of_input().subexpression(any_of(_sha, _refs, _bare)).end_of_input()

   **Emits** ``^(?:[a-f0-9]{7,40}|refs/(?:(?:heads|tags|remotes))/(?:(?!(?:\s|[~^:?*[\\])).)+|(?!(?:\s|[~^:?*[\\/])).(?:(?!(?:\s|[~^:?*[\\])).){0,127})$``

.. py:data:: edify.library.semver

   Callable :class:`Pattern` for SemVer 2.0.0 versions.

   Full description: :doc:`Semver <../../library/software/semver>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern, any_of


      def _positive() -> Pattern:
          return any_of(
              Pattern().char("0"),
              Pattern().range("1", "9").zero_or_more().digit(),
          )


      def _pre_id() -> Pattern:
          return any_of(
              Pattern().char("0"),
              Pattern().range("1", "9").zero_or_more().digit(),
              (
                  Pattern()
                  .zero_or_more()
                  .digit()
                  .any_of()
                  .range("a", "z")
                  .range("A", "Z")
                  .char("-")
                  .end()
                  .zero_or_more()
                  .any_of()
                  .range("0", "9")
                  .range("a", "z")
                  .range("A", "Z")
                  .char("-")
                  .end()
              ),
          )


      semver = (
          Pattern()
          .start_of_input()
          .named_capture("major")
          .subexpression(_positive())
          .end()
          .char(".")
          .named_capture("minor")
          .subexpression(_positive())
          .end()
          .char(".")
          .named_capture("patch")
          .subexpression(_positive())
          .end()
          .optional()
          .group()
          .char("-")
          .named_capture("prerelease")
          .subexpression(_pre_id())
          .zero_or_more()
          .group()
          .char(".")
          .subexpression(_pre_id())
          .end()
          .end()
          .end()
          .optional()
          .group()
          .char("+")
          .named_capture("buildmetadata")
          .one_or_more()
          .any_of()
          .range("0", "9")
          .range("a", "z")
          .range("A", "Z")
          .char("-")
          .end()
          .zero_or_more()
          .group()
          .char(".")
          .one_or_more()
          .any_of()
          .range("0", "9")
          .range("a", "z")
          .range("A", "Z")
          .char("-")
          .end()
          .end()
          .end()
          .end()
          .end_of_input()
      )

   **Emits** ``^(?P<major>(?:[1-9]\d*|[0]))\.(?P<minor>(?:[1-9]\d*|[0]))\.(?P<patch>(?:[1-9]\d*|[0]))(?:\-(?P<prerelease>(?:[1-9]\d*|\d*[a-zA-Z\-][0-9a-zA-Z\-]*|[0])(?:\.(?:[1-9]\d*|\d*[a-zA-Z\-][0-9a-zA-Z\-]*|[0]))*))?(?:\+(?P<buildmetadata>[0-9a-zA-Z\-]+(?:\.[0-9a-zA-Z\-]+)*))?$``

.. py:data:: edify.library.version

   Callable :class:`Pattern` for a permissive dotted version string.

   Full description: :doc:`Version <../../library/software/version>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      version = (
          Pattern()
          .start_of_input()
          .optional()
          .char("v")
          .one_or_more()
          .digit()
          .between(0, 3)
          .group()
          .char(".")
          .one_or_more()
          .digit()
          .end()
          .optional()
          .group()
          .any_of_chars("-.+")
          .one_or_more()
          .any_of()
          .range("a", "z")
          .range("A", "Z")
          .range("0", "9")
          .char(".")
          .char("-")
          .end()
          .end()
          .end_of_input()
      )

   **Emits** ``^v?\d+(?:\.\d+){0,3}(?:[-.+][a-zA-Z0-9\.\-]+)?$``

