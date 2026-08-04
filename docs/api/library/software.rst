Software
========

Every validator in the :doc:`software <../../library/software/index>` category. Each is a
callable :class:`~edify.Pattern`: pass a string to get a ``bool``, or compose it into a
larger pattern with :meth:`~edify.RegexBuilder.use`.

For what each one accepts and rejects, with runnable examples, see the
:doc:`library pages <../../library/software/index>`.

.. py:function:: edify.library.bump(value: str) -> bool

   Bump. See :doc:`../../library/software/bump` for the full description.

   Emits ``^(?:major|minor|patch|premajor|preminor|prepatch|prerelease|release)$``

.. py:function:: edify.library.cargo(value: str) -> bool

   Cargo. See :doc:`../../library/software/cargo` for the full description.

   Emits ``^[a-zA-Z][a-zA-Z0-9_\-]{0,63}(?:@\d+(?:\.\d+){0,3}(?:[-.+][a-zA-Z0-9\.\-]+)?)?$``

.. py:function:: edify.library.checksum(value: str) -> bool

   Checksum. See :doc:`../../library/software/checksum` for the full description.

   Emits ``^[a-fA-F0-9]{8,128}$``

.. py:function:: edify.library.component(value: str) -> bool

   Component. See :doc:`../../library/software/component` for the full description.

   Emits ``^(?:@[a-z0-9][a-z0-9\-]*/)?[a-z0-9][a-z0-9\._\-]{0,213}@\d+(?:\.\d+){0,3}(?:[-.+][a-zA-Z0-9\.\-]+)?$``

.. py:function:: edify.library.digest(value: str) -> bool

   Digest. See :doc:`../../library/software/digest` for the full description.

   Emits ``^(?:(?:sha256|sha512|sha1|md5|blake2[bs]?))[:-][a-fA-F0-9]{32,128}$``

.. py:function:: edify.library.docker(value: str) -> bool

   Docker. See :doc:`../../library/software/docker` for the full description.

   Emits ``^(?:(?:[a-z0-9\.\-]+(?::\d+)?/)?[a-z0-9]+(?:[._-][a-z0-9]+)*)(?:/[a-z0-9]+(?:[._-][a-z0-9]+)*)*(?::[a-zA-Z0-9_][a-zA-Z0-9\._\-]{0,127})?(?:@sha256:[a-f0-9]{64})?$``

.. py:function:: edify.library.git(value: str) -> bool

   Git. See :doc:`../../library/software/git` for the full description.

   Emits ``^[a-f0-9]{7,40}$``

.. py:function:: edify.library.image(value: str) -> bool

   Image. See :doc:`../../library/software/image` for the full description.

   Emits ``^(?:(?:[a-z0-9\.\-]+(?::\d+)?/)?[a-z0-9]+(?:[._-][a-z0-9]+)*)(?:/[a-z0-9]+(?:[._-][a-z0-9]+)*)*(?::[a-zA-Z0-9_][a-zA-Z0-9\._\-]{0,127})?(?:@sha256:[a-f0-9]{64})?$``

.. py:function:: edify.library.makefile(value: str) -> bool

   Makefile. See :doc:`../../library/software/makefile` for the full description.

   Emits ``^\.?[a-zA-Z][a-zA-Z0-9\._\-]*(?:\s+[a-zA-Z][a-zA-Z0-9\._\-]*)*\s*:.*$``

.. py:function:: edify.library.package(value: str) -> bool

   Package. See :doc:`../../library/software/package` for the full description.

   Emits ``^(?:@[a-z0-9][a-z0-9\-]*/)?[a-z0-9][a-z0-9\._\-]{0,213}$``

.. py:function:: edify.library.ref(value: str) -> bool

   Ref. See :doc:`../../library/software/ref` for the full description.

   Emits ``^(?:[a-f0-9]{7,40}|refs/(?:(?:heads|tags|remotes))/(?:(?!(?:\s|[~^:?*[\\])).)+|(?!(?:\s|[~^:?*[\\/])).(?:(?!(?:\s|[~^:?*[\\])).){0,127})$``

.. py:function:: edify.library.semver(value: str) -> bool

   Semver. See :doc:`../../library/software/semver` for the full description.

   Emits ``^(?P<major>(?:[1-9]\d*|[0]))\.(?P<minor>(?:[1-9]\d*|[0]))\.(?P<patch>(?:[1-9]\d*|[0]))(?:\-(?P<prerelease>(?:[1-9]\d*|\d*[a-zA-Z\-][0-9a-zA-Z\-]*|[0])(?:\.(?:[1-9]\d*|\d*[a-zA-Z\-][0-9a-zA-Z\-]*|[0]))*))?(?:\+(?P<buildmetadata>[0-9a-zA-Z\-]+(?:\.[0-9a-zA-Z\-]+)*))?$``

.. py:function:: edify.library.version(value: str) -> bool

   Version. See :doc:`../../library/software/version` for the full description.

   Emits ``^v?\d+(?:\.\d+){0,3}(?:[-.+][a-zA-Z0-9\.\-]+)?$``

