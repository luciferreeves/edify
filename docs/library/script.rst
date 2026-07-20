script
======

**Text** · :doc:`Back to the library <index>`

A writing-script run.

.. code-block:: python

   from edify.library import script


Edit the string, or the pattern itself:

.. edify-playground::

   from edify.library import script
   script

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^(?:[A-Za-zÀ-ɏ]+|[Ѐ-ӿ]+|[Ͱ-Ͽ]+|[一-鿿぀-ヿ가-힯]+|[؀-ۿ]+|[֐-׿]+|[ऀ-ॿ]+)$

See the other validators in the :doc:`library <index>`.
