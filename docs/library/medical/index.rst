Medical
=======

Clinical codes and identifiers. Each validator is a callable
:class:`~edify.Pattern`: import it, call it with a string, get a ``bool``.

Health data is among the most sensitive a system can hold, and these validators check
*shape* only. A match never means a code is clinically correct, current, or safe to
act on — and validating a value is not a reason to store it.

.. code-block:: python

   from edify.library import blood, medical, dosage

   blood("AB+")        # True
   medical("J45.909")  # True
   dosage("500mg")     # True

.. toctree::
   :hidden:

   blood
   dicom
   dosage
   medical

Codes
-----

- :doc:`medical` — a diagnosis or procedure code.
- :doc:`blood` — an ABO/Rh blood type.

Clinical data
-------------

- :doc:`dosage` — a medication amount with units.
- :doc:`dicom` — a DICOM unique identifier.
