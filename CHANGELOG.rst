
Changelog
=========
1.1.1 (2026-08-06)
------------------

A documentation release. The package itself is unchanged — every file under
``edify/`` is byte-identical to 1.1.0 — so there is nothing to do on upgrade
unless you read the docs in a browser.

Fixed
~~~~~

* The version switcher now appears on the published documentation. Read the Docs gates its addons event API behind an opt-in ``<meta name="readthedocs-addons-api-version" content="1">`` tag; without it, subscribing to the event throws and the switcher never received the version list (:pr:`326`).
* When the version list cannot be reached, Read the Docs' own flyout stays visible as a fallback. It is now hidden only once our switcher has actually rendered, rather than unconditionally (:pr:`326`).

1.1.0 (2026-08-05)
------------------

Edify 1.1 closes the gaps 1.0 admitted. The ReDoS check recommended two
constructs the builder could not write, so both now exist and work on the
standard library. ``from_regex`` refused character classes the forward builder
writes every day, so it translates them. The Unicode guide named the most common
Unicode bug in a validator and had no API to point at, so there is one. Existing
chains emit exactly what they emitted before; the single behaviour change is in
the :doc:`1.0 → 1.1 guide <upgrading/1.0-to-1.1>`.

Added
~~~~~

* Atomic groups — :meth:`~edify.RegexBuilder.atomic` opens a group that matches as much as it can and then refuses to give any of it back, so the engine cannot backtrack into it (:pr:`318`).
* Possessive quantifiers — ``optional_possessive``, ``zero_or_more_possessive``, ``one_or_more_possessive``, ``at_least_possessive``, ``at_most_possessive``, and ``between_possessive``, each with a factory (:pr:`318`).
* Unicode-aware character classes — ``unicode_letter`` (``\p{L}``), ``unicode_uppercase`` (``\p{Lu}``), ``unicode_lowercase`` (``\p{Ll}``), and ``unicode_alphanumeric`` (``[\p{L}\p{N}]``), which is ``word`` without the underscore. These emit property escapes and compile under ``engine="regex"`` (:pr:`319`).
* A negated multi-member character class — :meth:`~edify.RegexBuilder.anything_but_any_of` opens the negated counterpart of the ``any_of`` frame, so ``[^a-z0-9]`` finally has a chain that builds it. Anything you can build positively, you can now negate (:pr:`315`).
* :meth:`~edify.RegexBuilder.from_regex` translates character classes of any number of members and their negated forms — ``[a-z0-9]``, ``[a-z_]``, ``[^abc]``, ``[^a-z]``, ``[^a-z0-9]`` — plus numbered and named back-references (:pr:`317`).

Fixed
~~~~~

* ``from_regex`` returned a chain that quietly disagreed with its input when a quantified group held more than one element: ``^[a-z]+(?:-[a-z]+)*$`` came back as ``^[a-z]+\-*[a-z]+$``, which matches ``a--b`` and rejects ``x``. The repeat body is now grouped before the quantifier is applied (:pr:`317`).
* ``atoms.ipv6`` rejected compression in the middle of an address — the most common way an IPv6 address is written. It now accepts every ``::``-compressed form, wherever the compressed run falls (:pr:`314`).
* The ``ReDoSWarning`` recommended a possessive quantifier or an atomic group, neither of which the builder could express, and claimed the atomic group needed ``engine='regex'``. It now names :meth:`~edify.RegexBuilder.atomic` and :meth:`~edify.RegexBuilder.one_or_more_possessive`, and no longer fires on a shape built from either — those cannot backtrack (:pr:`318`).
* Every entry in the atoms API reference is now checked against the regex its atom actually emits, so a documented construction cannot drift from the fragment it claims to build (:pr:`320`).

Breaking
~~~~~~~~

* ``atoms.cidr`` range-checks the prefix length, so ``10.0.0.0/33`` no longer matches. The address half is unchanged, and ``edify.library.cidr`` already behaved this way (:pr:`314`). See :ref:`cidr-prefix-range`.

Documentation
~~~~~~~~~~~~~

* :doc:`guide/practice/performance` shows the direct fix for a catastrophic-backtracking shape — the warning, the atomic rewrite, then the warning gone — rather than only advising a bounded quantifier.
* :doc:`guide/builder/quantifiers` places possessive alongside greedy and lazy, so the page answers which of the three you want in a sentence each.
* :doc:`guide/practice/unicode` teaches ``unicode_letter`` where it previously taught a workaround, and its strategy table carries the engine dimension the choice now depends on.
* :doc:`guide/beyond/from-regex` lists the classes and back-references it understands, and states that the emitted text is normalised rather than copied.
* The version switcher is part of the site rather than injected chrome: it sits in the navbar, is built from the same design tokens as the rest of the theme so it follows the light and dark themes, and its list scrolls within the screen it opens on (:pr:`324`).
* The documentation is navigable on a phone. The section links collapse behind a menu button instead of disappearing, the sidebar becomes a control naming the page you are on and opens into a scrollable panel, the footer wraps inside the screen, and a wide table or a playground editor no longer widens the whole page (:pr:`324`).
* A :doc:`1.0 → 1.1 upgrade guide <upgrading/1.0-to-1.1>`.

Tooling and CI
~~~~~~~~~~~~~~

* The install-matrix jobs probe the Unicode classes in both directions: the bare install must raise and name the extra, and the ``edify[regex]`` install must compile and match non-ASCII (:pr:`319`).

1.0.0 (2026-08-04)
------------------

The first stable release. Edify grows from a builder into a full toolkit: a
library of ready-to-call validators, introspection, serialization, framework
integrations, and a closed match API — with the builder itself hardened and its
rough edges filed off, and a documentation site you can run code inside. The
changes worth knowing before you upgrade are below;
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

Documentation
~~~~~~~~~~~~~

* A rebuilt documentation site: a topic-first guide that works through the builder from anchors to lookaround, a page for every one of the 228 validators, and a complete API reference covering the public surface — every method, property, constant, atom, error, and type.
* An in-browser playground. Examples throughout the guide and the library are live: edit the chain and the emitted regex and match results update as you type, with edify itself running in your browser. The :doc:`playground <playground>` page is the same widget at full size.
* Every Python example in the documentation is executed by the test suite and snapshotted against the regex it emits, so a documented pattern cannot drift from what the code produces.
* Method names, constants, and atoms are cross-linked to their reference entries throughout the prose and inside the code samples.

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
