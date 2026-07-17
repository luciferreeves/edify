============
Contributing
============

Thanks for helping improve Edify. This guide gets you from a fresh clone to a
green pull request.

Setup
=====

Edify uses `uv <https://docs.astral.sh/uv/>`_ for everything. Install it, then
sync the full development environment:

.. code-block:: bash

    git clone https://github.com/luciferreeves/edify
    cd edify
    uv sync --all-groups

That creates ``.venv`` with the library, its optional extras, and every
development tool. Prefix commands with ``uv run`` to use it.

The gate
========

Every change must pass the same checks CI runs. Run them locally before you push:

.. code-block:: bash

    uv run ruff check .            # lint
    uv run ruff format --check .   # formatting
    uv run mypy edify tools        # type-check the library and tooling
    uv run pyright                 # strict type-check (library, tests, tools)
    uv run pytest                  # tests — 100% coverage is required

All of these must be clean. Coverage is enforced at 100%: a line that isn't
exercised by a test through the public API fails the build.

House style
===========

- **No suppressions.** No ``# noqa``, ``# type: ignore``, or ``# pragma`` — if a
  check complains, restructure the code so it doesn't.
- **Single-purpose files with single-word names.** ``edify/builder/anchors.py``,
  not ``edify/builder/anchor_helpers.py``.
- **Tests mirror the source tree** under ``tests/`` and are named ``*.test.py``
  (for example ``tests/builder/anchors.test.py``).
- **Tests exercise the public API.** Reach behavior through the documented
  surface, never by importing private helpers — that's what keeps coverage
  honest.

Public surface and changelog
============================

The exported API is captured in ``tools/surface/.public``. If your change adds,
removes, or alters a public name, regenerate the snapshot and record the change:

.. code-block:: bash

    uv run python tools/surface/surface.py --write

For a **breaking** change, also add a fragment under ``changes/`` describing the
migration (see ``changes/README.rst`` for the format). A CI gate fails any pull
request whose public surface moves without one.

Docs
====

The documentation is a custom Sphinx site in ``docs/``. Build the playground
wheel and serve the site with live reload:

.. code-block:: bash

    uv run python tools/docs/build.py
    uv run --with sphinx-autobuild sphinx-autobuild docs docs/_build/html

Commits and pull requests
=========================

- **Commits** use a single-line, imperative, `conventional-commit
  <https://www.conventionalcommits.org>`_ subject — ``feat(builder): ...``,
  ``fix(compile): ...``, ``docs: ...``. Keep rationale for the pull-request
  description, not the commit body.
- **Pull requests** describe *what changed and why*. Reference the issues they
  close with ``Closes #123`` so they land together.

That's it — open the pull request and the checks will tell you if anything's off.
