Pre-Built Pattern API Reference
================================

Edify allows you to verify a string quickly by providing commonly used regex patterns in its extensive set of built-in patterns. To tap into a pattern, simply import the pattern function from the ``edify.library`` module. For example, to verify that a string is a valid email address, you can use the ``email`` pattern. The pattern will return either ``True`` or ``False`` depending on whether the string matches the pattern.

email()
-------

The ``email`` function verifies that a string is a valid email address. The function takes a ``string`` argument which is supposed to be a valid email address. The function returns ``True`` if the string is a valid email address, and ``False`` otherwise.

.. warning::

    The ``email`` function is not a complete email address validator. It only checks that the string is in the correct format. It does not check that the domain name is valid or that the email address actually exists.

To use the ``email`` function, import it from the ``edify.library`` module.

.. code-block:: python

    from edify.library import email

Then, call the ``email`` function with a string argument.

.. code-block:: python

    email('hello@example.com') # returns True
    email('hello') # returns False

phone()
-------

The ``phone`` function verifies that a string is a valid phone number. The function takes a ``string`` argument which is supposed to be a valid phone number. The function returns ``True`` if the string is a valid phone number, and ``False`` otherwise.

.. warning::

    The ``phone`` function is not a complete phone number validator. It only checks that the string is in the correct format. It does not check that the phone number actually exists.

You can use the ``phone`` function as follows:

.. code-block:: python

    from edify.library import phone

    phone('1234567890') # returns True
    phone('123456789') # returns False
    phone('+1 (123) 456-7890') # returns True
    phone('123-456-7890') # returns True
    phone('9012') # returns False
    phone('+1 (615) 243-') # returns False
