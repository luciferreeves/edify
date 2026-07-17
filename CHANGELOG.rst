
Changelog
=========
1.0.0 (2026-07-17)
------------------

The first stable release. Edify grows from a builder into a full toolkit: a
library of ready-to-call validators, introspection, serialization, framework
integrations, and a closed match API — with the builder itself hardened and its
rough edges filed off. The changes worth knowing before you upgrade are below;
the :doc:`0.3 → 1.0 guide <upgrading/0.3-to-1.0>` walks each one with
before/after code.

Added
~~~~~

* A library of 228 ready-to-call validators — email, URL, semver, IBAN, phone, postal, and hundreds more — each a callable :class:`~edify.Pattern` organised into topical categories. See :ref:`validators-callable`.
* Five closed match verbs on every builder — ``test``, ``match``, ``search``, ``findall``, and ``sub`` — returning edify result wrappers. See :ref:`closed-match-verbs`.
* :meth:`~edify.RegexBuilder.to_regex` accepts inline flags and an ``engine`` argument, compiling against an alternate backend when one is installed. See :ref:`engine-kwarg`.
* Builders compare by emitted pattern: two chains that describe the same regex are equal. See :ref:`builder-equality`.
* Introspection: render any pattern as a plain-English explanation, an ASCII or graph diagram, or an annotated ``re.VERBOSE`` form.
* Serialization: round-trip a pattern through a dict or JSON.
* Framework integrations shipped as opt-in extras — ``edify[pydantic]``, ``edify[fastapi]``, and ``edify[django]``.

Breaking
~~~~~~~~

* Python 3.11 or newer is required (:pr:`64`). See :ref:`python-floor`.
* Relicensed from Apache-2.0 to the `MIT License <https://github.com/luciferreeves/edify/blob/main/LICENSE>`_. No API change. See :ref:`license-mit`.
* Invalid patterns raise an annotated error at the call site instead of emitting a subtly wrong regex. See :ref:`silent-failure-raises`.
* Terminal methods return a :class:`~edify.result.Regex` wrapper rather than a bare :class:`re.Pattern`. See :ref:`regex-wrapper-return`.
* :meth:`~edify.RegexBuilder.to_regex_string` returns the emitted source exactly as written into the pattern. See :ref:`to-regex-string-output`.
* Named back-references resolve by name and named groups read off ``.captures``. See :ref:`named-backref-return`.
* Character-class escaping is minimal and correct: only the metacharacters that need escaping inside a class are escaped. See :ref:`char-class-escape`.
* The validator library is organised into categories, and a handful of import paths moved with it. See :ref:`library-reorg` and :ref:`moved-import-paths`.

Tooling and CI
~~~~~~~~~~~~~~

* Dropped the macOS and Windows runners from the CI matrix; Linux-only from here on. Edify is a pure-Python wheel with no platform-specific code, so the multi-OS jobs were buying ~zero signal and produced false negatives (:pr:`60`).
* Bumped the minimum ``virtualenv`` floor for the CI bootstrap to ``>=21.4.2`` (:pr:`56`, :pr:`58`).

0.3.0 (2026-04-29)
------------------

A maintenance release: Edify is dragged out of 2022 and back into modern shape. No new patterns or builder API. The minimum supported Python rises to 3.8.

Breaking
~~~~~~~~

* Dropped support for Python 3.7. Edify now requires Python 3.8 or newer (:pr:`32`).

Added
~~~~~

* Support for Python 3.12, 3.13, and 3.14, with the matrix and Read the Docs build configuration updated to match (:pr:`31`).

Tooling and CI
~~~~~~~~~~~~~~

* Bumped GitHub Actions to current major versions: ``actions/checkout@v5``, ``actions/setup-python@v5``, ``github/codeql-action@v3``. All workflow jobs now run on the Node 20 runtime instead of the deprecated Node 16. ``pypa/gh-action-pypi-publish`` SHA refreshed to ``v1.14.0`` (:pr:`35`).
* PyPy CI matrix moved off the EOL ``pypy-3.8`` line to the maintained ``pypy-3.10`` and ``pypy-3.11`` (:pr:`37`).
* ``.pre-commit-config.yaml`` modernised: every hook pinned to an immutable tag instead of a floating branch ref, dead repo URLs corrected (``gitlab.com/pycqa/flake8`` → ``github.com/PyCQA/flake8``, ``timothycrosley/isort`` → ``PyCQA/isort``), and ``psf/black`` swapped for the upstream-recommended ``psf/black-pre-commit-mirror`` (:pr:`33`).

Dependencies
~~~~~~~~~~~~

* Bumped minimum versions: ``setuptools >=75.0``, ``pip >=26.0.1``, ``virtualenv >=21.3.0``, ``six >=1.17.0``, ``sphinx >=7.4.7`` (:pr:`25`, :pr:`26`, :pr:`27`, :pr:`28`, :pr:`29`).

Repository infrastructure
~~~~~~~~~~~~~~~~~~~~~~~~~

* Added ``.github/CODEOWNERS`` and ``natsuoto`` to ``AUTHORS.rst`` for the new agent-driven contribution flow (:pr:`39`).
* Locked ``main``: 1 approving code-owner review required, 31 status-check contexts required (the full matrix), linear history enforced, no force pushes or deletions, applies to administrators.
* Repo-level ``allow_auto_merge`` enabled — PRs auto-merge once review and CI gates pass.

Housekeeping
~~~~~~~~~~~~

* Dropped a dead ``py37``/``pypy37`` exclusion from the cookiecutter Jinja template and refreshed the docs copyright year (:pr:`43`).
* Updated author website URL in ``AUTHORS.rst`` and ``.cookiecutterrc`` (:pr:`41`).
* Removed all cookiecutter regeneration scaffolding — ``.cookiecutterrc``, ``ci/bootstrap.py``, and ``ci/templates/`` (containing dead AppVeyor config and a workflow template that lagged the live one) — along with the ``[testenv:bootstrap]`` env, related ``MANIFEST.in`` / ``setup.cfg`` / ``.pre-commit-config.yaml`` exclusions, and the dead Python 3.7 branch in ``tests.local.sh``. The local-test script's per-version ``if/elif`` chain is now a single programmatic ``tox -e py$VERSION`` lookup, which adapts automatically when Python versions are added or removed from the matrix (:pr:`47`).

0.2.2 (2022-12-22)
------------------
* Added Support for Python 3.11
* Added more RegexBuilder Examples
* Fixed Documentation Typos

0.2.1 (2022-11-27)
------------------

* This is a Quick Fix Release to fix the incomplete release of 0.2.0. The release was intended to drop support for 3.6, but the metadata was not updated to reflect this. This release fixes that. v0.2.0 remains available on PyPI, but is incompatible with Python 3.6. Using it with other versions of Python is not a problem. Other than the metadata, the two releases are identical.

0.2.0 (2022-11-27)
------------------
This is a minor release with a few new built-in validators along with some small changes and bug fixes.

Validators added:
~~~~~~~~~~~~~~~~~
* URL Validator
* UUID Validator
* GUID Validator
* SSN Validator
* Mac Address (IEEE 802) Validator
* Zip Code Validator
* Password Validator

Documentation:
~~~~~~~~~~~~~~

* Added documentation for new validators
* Add warning for trade-offs in email regex validation

Bug Fixes:
~~~~~~~~~~

* Fixed Phone pattern failing for service numbers and 4 digit numbers (See `#16 <https://github.com/luciferreeves/edify/issues/16>`_ for more information)


0.1.0 (2022-09-10)
------------------

* First release on PyPI.
