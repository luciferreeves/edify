Pre-Built Pattern API Reference
================================

Edify allows you to verify a string quickly by providing commonly used regex patterns in its extensive set of built-in patterns. To tap into a pattern, simply import the pattern function from the ``edify.library`` module. For example, to verify that a string is a valid email address, you can use the ``email`` pattern. The pattern will return either ``True`` or ``False`` depending on whether the string matches the pattern.

email(email: str)
-----------------

The ``email`` function verifies that a string is a valid email address. The function takes a ``string`` argument which is supposed to be a valid email address. The function returns ``True`` if the string is a valid email address, and ``False`` otherwise.

.. warning::

    The ``email`` function is not a complete email address validator. It only checks that the string is in the correct format. It does not check that the domain name is valid or that the email address actually exists. This shall also be noted that there are certain trade-offs while validating email addresses using regular expressions. Regular expressions do not serve as a robust solution and should be avoided while validating complex email addresses. To learn more, go to `regular-expressions.info/email.html <https://www.regular-expressions.info/email.html>`_.

To use the ``email`` function, import it from the ``edify.library`` module.

.. code-block:: python

    from edify.library import email

Then, call the ``email`` function with a string argument.

.. code-block:: python

    email('hello@example.com') # returns True
    email('hello') # returns False

email_rfc_5322(email: str)
--------------------------

The ``email_rfc_5322`` function verifies that a string is a valid email address according to the `RFC 5322 <https://tools.ietf.org/html/rfc5322>`_ standard which allows for the most complete validation. Usually, you should not use it because it is an overkill. In most cases apps are not able to handle all emails that this regex allows. The function takes a ``string`` argument which is supposed to be a valid email address. The function returns ``True`` if the string is a valid email address, and ``False`` otherwise.

You can use the ``email_rfc_5322`` function as follows:

.. code-block:: python

    from edify.library import email_rfc_5322

    email_rfc_5322('hello@example.com') # returns True
    email_rfc_5322('hello') # returns False

phone(phone: str)
-----------------

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


ipv4(ip: str)
-------------

The ``ipv4`` function verifies that a string is a valid IPv4 address. The function takes a ``string`` argument which is supposed to be a valid IPv4 address. The function returns ``True`` if the string is a valid IPv4 address, and ``False`` otherwise.

You can use the ``ipv4`` function as follows:

.. code-block:: python

    from edify.library import ipv4

    ipv4('128.128.128.128') # returns True
    ipv4('128.128.128') # returns False


ipv6(ip: str)
-------------

The ``ipv6`` function verifies that a string is a valid IPv6 address. The function takes a ``string`` argument which is supposed to be a valid IPv6 address. The function returns ``True`` if the string is a valid IPv6 address, and ``False`` otherwise.

You can use the ``ipv6`` function as follows:

.. code-block:: python

    from edify.library import ipv6

    ipv6('2001:0db8:85a3:0000:0000:8a2e:0370:7334') # returns True
    ipv6('2001:0db8:85a3:0000:0000:8a2e:0370') # returns False

date(date: str)
---------------

The ``date`` function verifies that a string is a valid date. The function takes a ``string`` argument which is supposed to be a valid date. The function returns ``True`` if the string is a valid date, and ``False`` otherwise.

.. warning::
    The ``date`` function validates the string against a date format (D/M/YYYY or M/D/YYYY). This however does not guarantee that the date would be valid. For example, the string ``31-02-2017`` is a valid date according to the date format, but it is not a valid date.

    While there are some regular expressions that allow more complex date validations, it is usually better to validate dates using special date and time libraries. For example, in Python datetime package can be used for these purposes. In this case, the validation will look like this:

    .. code-block:: python

        from datetime import datetime

        try:
            datetime.strptime('31-02-2017', '%d-%m-%Y')
        except ValueError:
            print('Invalid date')
        else:
            print('Valid date')

You can use the ``date`` function as follows:

.. code-block:: python

    from edify.library import date

    date('31/12/2017') # returns True
    date('31-12-2017') # returns False

iso_date(date: str)
-------------------

The ISO 8061 is an international standard for exchanging and serializing date and time data. The ``iso_date`` function verifies that a string is a valid ISO date. The function takes a ``string`` argument which is supposed to be a valid ISO date. The function returns ``True`` if the string is a valid ISO date, and ``False`` otherwise.

You can use the ``iso_date`` function as follows:

.. code-block:: python

    from edify.library import iso_date

    iso_date('2021-11-04T22:32:47.142354-10:00') # returns True
    iso_date('12/12/2022') # returns False

url(url: str, match?: list)
---------------------------

The ``url`` function verifies that a string is a valid URL. The function takes a ``string`` argument which is supposed to be a valid URL. The function returns ``True`` if the string is a valid URL, and ``False`` otherwise.

.. warning::

    The ``url`` function is not a complete URL validator. It only checks that the string is in the correct format. It does not check that the URL actually exists.

You can use the ``url`` function as follows:

.. code-block:: python

    from edify.library import url

    url('https://example.com') # returns True
    url('example.com') # returns True
    url('example') # returns False

The ``url`` function also accepts an optional ``match`` argument. The ``match`` argument is a list of strings that you can use to configure what types of URLs the function should match. The ``match`` argument can have the following values:

* ``'proto'`` - matches URLs with a protocol (e.g. ``https://example.com`` or ``http://example.com``)
* ``'no_proto'`` - matches URLs without a protocol (e.g. ``example.com``)

By default, the ``url`` function matches both URLs with and without a protocol. You can use the ``match`` argument to configure the function to match only URLs with a protocol or only URLs without a protocol. For example, the following code will match only URLs without a protocol:

.. code-block:: python

    from edify.library import url

    url('example.com', match=['no_proto']) # returns True
    url('https://example.com', match=['no_proto']) # returns False

If you supply an Invalid or empty value in the ``match`` list argument, the function will raise a ``ValueError`` exception. Similarly, if you supply another data type in the ``match`` list argument, the function will raise a ``TypeError`` exception.
