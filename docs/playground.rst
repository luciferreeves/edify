Playground
==========

Build a pattern and watch the regex — and the matches — update as you type. This
runs real Edify in your browser; nothing is sent anywhere.

.. edify-playground::

   Pattern().start_of_input().exactly(4).digit().end_of_input()

Edit the chain on the left. The emitted regex appears below it, and the test
strings on the right light up green when they match. Autocomplete offers every
builder method as you type — start with ``Pattern().`` and explore.
