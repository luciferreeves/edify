
Changelog
=========

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
