Transport
=========

Vehicle and aircraft identifiers. Each validator is a callable
:class:`~edify.Pattern`: import it, call it with a string, get a ``bool``.

.. code-block:: python

   from edify.library import vehicle, flight, plate

   vehicle("1HGBH41JXMN109186")   # True
   flight("AA100")                # True
   plate("ABC123")                # True

.. toctree::
   :hidden:

   aircraft
   flight
   plate
   vehicle

Road
----

- :doc:`vehicle` — a vehicle identification number.
- :doc:`plate` — a registration plate.

Air
---

- :doc:`aircraft` — an aircraft registration.
- :doc:`flight` — a flight number.
