========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |github-actions| |appveyor| |requires|
        | |codecov|
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|
.. |docs| image:: https://readthedocs.org/projects/edify/badge/?style=flat
    :target: https://edify.readthedocs.io/
    :alt: Documentation Status

.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/luciferreeves/edify?branch=main&svg=true
    :alt: AppVeyor Build Status
    :target: https://ci.appveyor.com/project/luciferreeves/edify

.. |github-actions| image:: https://github.com/luciferreeves/edify/actions/workflows/github-actions.yml/badge.svg
    :alt: GitHub Actions Build Status
    :target: https://github.com/luciferreeves/edify/actions

.. |requires| image:: https://requires.io/github/luciferreeves/edify/requirements.svg?branch=main
    :alt: Requirements Status
    :target: https://requires.io/github/luciferreeves/edify/requirements/?branch=main

.. |codecov| image:: https://codecov.io/gh/luciferreeves/edify/branch/main/graphs/badge.svg?branch=main
    :alt: Coverage Status
    :target: https://codecov.io/github/luciferreeves/edify

.. |version| image:: https://img.shields.io/pypi/v/edify.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/edify

.. |wheel| image:: https://img.shields.io/pypi/wheel/edify.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/project/edify

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/edify.svg
    :alt: Supported versions
    :target: https://pypi.org/project/edify

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/edify.svg
    :alt: Supported implementations
    :target: https://pypi.org/project/edify

.. |commits-since| image:: https://img.shields.io/github/commits-since/luciferreeves/edify/v0.1.0.svg
    :alt: Commits since latest release
    :target: https://github.com/luciferreeves/edify/compare/v0.1.0...main



.. end-badges

Regular Expressions Made Simple

* Free software: Apache Software License 2.0

Installation
============

::

    pip install edify

You can also install the in-development version with::

    pip install https://github.com/luciferreeves/edify/archive/main.zip


Documentation
=============


https://edify.readthedocs.io/


Development
===========

To run all the tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
