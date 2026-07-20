subnet
======

**Address** · :doc:`Back to the library <index>`

A subnet mask or prefix.

.. code-block:: python

   from edify.library import subnet

   subnet('255.255.255.255')   # True

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: 255.255.255.255|254.254.254.254

   from edify.library import subnet
   subnet

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^(?:255|254|252|248|240|224|192|128|[0])\.(?:255|254|252|248|240|224|192|128|[0])\.(?:255|254|252|248|240|224|192|128|[0])\.(?:255|254|252|248|240|224|192|128|[0])$

How it reads
------------

.. code-block:: text

   - The text must start with either "255", "254", "252", "248", "240", "224", "192", "128", or "0".
   - Then the text must have ".".
   - Then the text must have either "255", "254", "252", "248", "240", "224", "192", "128", or "0".
   - Then the text must have ".".
   - Then the text must have either "255", "254", "252", "248", "240", "224", "192", "128", or "0".
   - Then the text must have ".".
   - Then the text must have either "255", "254", "252", "248", "240", "224", "192", "128", or "0".

See the other validators in the :doc:`library <index>`.
