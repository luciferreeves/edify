
Changelog
=========
0.3.0 (unreleased)
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
