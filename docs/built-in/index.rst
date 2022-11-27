.. |toggleStart| raw:: html

   <details>
   <summary style="font-size: 1.2rem; font-style: bold; cursor: pointer;">View Supported Locales</summary>

.. |toggleEnd| raw:: html

   </details>


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

.. code-block:: python

    from edify.library import url

    url('example.com', match=['invalid']) # raises ValueError
    url('example.com', match=['no_proto', 'invalid']) # raises ValueError
    url('example.com', match=['no_proto', 1]) # raises TypeError

uuid(uuid: str)
---------------

The ``uuid`` function verifies that a string is a valid UUID. The function takes a ``string`` argument which is supposed to be a valid UUID. The function returns ``True`` if the string is a valid UUID, and ``False`` otherwise.

You can use the ``uuid`` function as follows:

.. code-block:: python

    from edify.library import uuid

    uuid('123e4567-e89b-12d3-a456-426655440000') # returns True
    uuid('123e4567-e') # returns False

zip(zip: str, locale?: str)
---------------------------

The ``zip`` function verifies that a string is a valid ZIP code. The function takes a ``string`` argument which is supposed to be a valid ZIP code. The function returns ``True`` if the string is a valid ZIP code, and ``False`` otherwise.

The ``zip`` function also accepts an optional ``locale`` argument. The ``locale`` argument is a string that you can use to configure what types of ZIP codes the function should match. You can view the ``locale`` argument values below.

|toggleStart|

.. list-table::
  :header-rows: 1

  * - Country
    - Locale

  * - Afghanistan
    - AF

  * - Albania
    - AL

  * - Algeria
    - DZ

  * - American Samoa
    - AS

  * - Andorra
    - AD

  * - Angola
    - AO

  * - Anguilla
    - AI

  * - Antigua and Barbuda
    - AG

  * - Argentina
    - AR

  * - Armenia
    - AM

  * - Aruba
    - AW

  * - Australia
    - AU

  * - Austria
    - AT

  * - Azerbaijan
    - AZ

  * - Bahamas
    - BS

  * - Bahrain
    - BH

  * - Bangladesh
    - BD

  * - Barbados
    - BB

  * - Belarus
    - BY

  * - Belgium
    - BE

  * - Belize
    - BZ

  * - Benin
    - BJ

  * - Bermuda
    - BM

  * - Bhutan
    - BT

  * - Bolivia
    - BO

  * - Bonaire
    - BQ

  * - Bosnia and Herzegovina
    - BA

  * - Botswana
    - BW

  * - Brazil
    - BR

  * - Brunei
    - BN

  * - Bulgaria
    - BG

  * - Burkina Faso
    - BF

  * - Burundi
    - BI

  * - Cambodia
    - KH

  * - Cameroon
    - CM

  * - Canada
    - CA

  * - Canary Islands
    - CI

  * - Cape Verde
    - CV

  * - Cayman Islands
    - KY

  * - Central African Republic
    - CF

  * - Chad
    - TD

  * - Channel Islands
    - CI

  * - Chile
    - CL

  * - China, People's Republic
    - CN

  * - Colombia
    - CO

  * - Comoros
    - KM

  * - Congo
    - CG

  * - Congo, The Democratic Republic of
    - CD

  * - Cook Islands
    - CK

  * - Costa Rica
    - CR

  * - Côte d'Ivoire
    - CI

  * - Croatia
    - HR

  * - Cuba
    - CU

  * - Curacao
    - CW

  * - Cyprus
    - CY

  * - Czech Republic
    - CZ

  * - Denmark
    - DK

  * - Djibouti
    - DJ

  * - Dominica
    - DM

  * - Dominican Republic
    - DO

  * - East Timor
    - TL

  * - Ecuador
    - EC

  * - Egypt
    - EG

  * - El Salvador
    - SV

  * - Eritrea
    - ER

  * - Estonia
    - EE

  * - Ethiopia
    - ET

  * - Falkland Islands
    - FK

  * - Faroe Islands
    - FO

  * - Fiji
    - FJ

  * - Finland
    - FI

  * - France
    - FR

  * - French Polynesia
    - PF

  * - Gabon
    - GA

  * - Gambia
    - GM

  * - Georgia
    - GE

  * - Germany
    - DE

  * - Ghana
    - GH

  * - Gibraltar
    - GI

  * - Greece
    - GR

  * - Greenland
    - GL

  * - Grenada
    - GD

  * - Guadeloupe
    - GP

  * - Guam
    - GU

  * - Guatemala
    - GT

  * - Guernsey
    - GG

  * - Guinea-Bissau
    - GW

  * - Guinea-Equatorial
    - GQ

  * - Guinea Republic
    - GN

  * - Guyana (British)
    - GY

  * - Guyana (French)
    - GF

  * - Haiti
    - HT

  * - Honduras
    - HN

  * - Hong Kong
    - HK

  * - Hungary
    - HU

  * - Iceland
    - IS

  * - India
    - IN

  * - Indonesia
    - ID

  * - Iran
    - IR

  * - Iraq
    - IQ

  * - Ireland, Republic of
    - IE

  * - Islas Malvinas
    - FK

  * - Israel
    - IL

  * - Italy
    - IT

  * - Ivory Coast
    - CI

  * - Jamaica
    - JM

  * - Japan
    - JP

  * - Jersey
    - JE

  * - Jordan
    - JO

  * - Kazakhstan
    - KZ

  * - Kenya
    - KE

  * - Kiribati
    - KI

  * - Korea, Republic of
    - KR

  * - Korea, The D.P.R of
    - KP

  * - Kosovo
    - XK

  * - Kuwait
    - KW

  * - Kyrgyzstan
    - KG

  * - Laos
    - LA

  * - Latvia
    - LV

  * - Lebanon
    - LB

  * - Lesotho
    - LS

  * - Liberia
    - LR

  * - Libya
    - LY

  * - Liechtenstein
    - LI

  * - Lithuania
    - LT

  * - Luxembourg
    - LU

  * - Macau
    - MO

  * - Macedonia, Republic of
    - MK

  * - Madagascar
    - MG

  * - Malawi
    - MW

  * - Malaysia
    - MY

  * - Maldives
    - MV

  * - Mali
    - ML

  * - Malta
    - MT

  * - Marshall Islands
    - MH

  * - Martinique
    - MQ

  * - Mauritania
    - MR

  * - Mauritius
    - MU

  * - Mayotte
    - YT

  * - Mexico
    - MX

  * - Moldova, Republic of
    - MD

  * - Monaco
    - MC

  * - Mongolia
    - MN

  * - Montenegro
    - ME

  * - Montserrat
    - MS

  * - Morocco
    - MA

  * - Mozambique
    - MZ

  * - Myanmar
    - MM

  * - Namibia
    - NA

  * - Nauru
    - NR

  * - Nepal
    - NP

  * - Netherlands
    - NL

  * - New Caledonia
    - NC

  * - New Zealand
    - NZ

  * - Nicaragua
    - NI

  * - Niger
    - NE

  * - Nigeria
    - NG

  * - Niue
    - NU

  * - Northern Mariana Islands
    - MP

  * - Norway
    - NO

  * - Oman
    - OM

  * - Pakistan
    - PK

  * - Palau
    - PW

  * - Panama
    - PA

  * - Papua New Guinea
    - PG

  * - Paraguay
    - PY

  * - Peru
    - PE

  * - Philippines
    - PH

  * - Poland
    - PL

  * - Portugal
    - PT

  * - Puerto Rico
    - PR

  * - Qatar
    - QA

  * - Réunion
    - RE

  * - Romania
    - RO

  * - Russian Federation
    - RU

  * - Rwanda
    - RW

  * - Saipan
    - MP

  * - Samoa
    - WS

  * - Sao Tome and Principe
    - ST

  * - Saudi Arabia
    - SA

  * - Senegal
    - SN

  * - Serbia
    - RS

  * - Seychelles
    - SC

  * - Sierra Leone
    - SL

  * - Singapore
    - SG

  * - Slovakia
    - SK

  * - Slovenia
    - SI

  * - Solomon Islands
    - SB

  * - Somalia
    - SO

  * - South Africa
    - ZA

  * - South Sudan
    - SS

  * - Spain
    - ES

  * - Sri Lanka
    - LK

  * - St. Barthélemy
    - BL

  * - St. Croix
    - VI

  * - St. Eustatius
    - SE

  * - St. Helena
    - SH

  * - St. John
    - AG

  * - St. Kitts and Nevis
    - KN

  * - St. Lucia
    - LC

  * - St. Maarten
    - SX

  * - St. Thomas
    - VI

  * - St. Vincent and the Grenadines
    - VC

  * - Sudan
    - SD

  * - Suriname
    - SR

  * - Swaziland
    - SZ

  * - Sweden
    - SE

  * - Switzerland
    - CH

  * - Syria
    - SY

  * - Tahiti
    - PF

  * - Taiwan
    - TW

  * - Tanzania
    - TZ

  * - Thailand
    - TH

  * - Togo
    - TG

  * - Tonga
    - TO

  * - Tortola
    - VG

  * - Trinidad and Tobago
    - TT

  * - Tunisia
    - TN

  * - Turkey
    - TR

  * - Turkmenistan
    - TM

  * - Turks and Caicos Islands
    - TC

  * - Tuvalu
    - TV

  * - Uganda
    - UG

  * - Ukraine
    - UA

  * - United Arab Emirates
    - AE

  * - United Kingdom
    - GB

  * - United States of America
    - US

  * - Uruguay
    - UY

  * - Uzbekistan
    - UZ

  * - Vanuatu
    - VU

  * - Venezuela
    - VE

  * - Vietnam
    - VN

  * - Virgin Islands (British)
    - VG

  * - Virgin Islands (US)
    - VI

  * - Yemen
    - YE

  * - Zambia
    - ZM

  * - Zimbabwe
    - ZW

|toggleEnd|

By default, the ``zip`` function matches ZIP codes for "US". Here's an example of how to use the ``zip`` function to match ZIP codes:

.. code-block:: python

    from edify.library import zip

    zip('12345') # returns True
    zip('1234') # returns False
    zip('12345', locale='US') # returns True
    zip('12345-1234') # returns True
    zip('12345-1234', locale='US') # returns True
    zip('123456', locale='IN') # returns True

If you supply an Invalid or empty value in the ``locale`` argument, the function will raise a ``ValueError`` exception. Similarly, if you supply another data type in the ``locale`` argument, the function will raise a ``TypeError`` exception.


guid(guid: str)
---------------

The ``guid`` function validates a GUID (Globally Unique Identifier) string. The function returns ``True`` if the string is a valid GUID, and ``False`` otherwise.

Here's an example of how to use the ``guid`` function:

.. code-block:: python

    from edify.library import guid

    guid('6ba7b810-9dad-11d1-80b4-00c04fd430c8') # returns True
    guid('{51d52cf1-83c9-4f02-b117-703ecb728b74}') # returns True
    guid('{51d52cf1-83c9-4f02-b117-703ecb728-b74}') # returns False

password(password: str, min_length?: int, max_length?: int, min_upper?: int, min_lower?: int, min_digit?: int, min_special?: int, special_chars?: str)
------------------------------------------------------------------------------------------------------------------------------------------------------------

The ``password`` function validates a password string. The function returns ``True`` if the string is a valid password, and ``False`` otherwise.

The ``password`` function takes the following arguments:

  * ``password``: The password string to validate.
  * ``min_length``: The minimum length of the password. The default value is 8.
  * ``max_length``: The maximum length of the password. The default value is 64.
  * ``min_upper``: The minimum number of uppercase characters in the password. The default value is 1.
  * ``min_lower``: The minimum number of lowercase characters in the password. The default value is 1.
  * ``min_digit``: The minimum number of digits in the password. The default value is 1.
  * ``min_special``: The minimum number of special characters in the password. The default value is 1.
  * ``special_chars``: The special characters to use in the password. The default value is ``!@#$%^&*()_+-=[]{}|;':\",./<>?``.

Here's an example of how to use the ``password`` function:

.. code-block:: python

    from edify.library import password

    password('password') # returns False
    password("Password123!") # returns True
    password("Password123!", max_length=8) # returns False
    password("Password123!", min_upper=2) # returns False
    password("password", min_upper=0, min_digit=0, min_special=0) # returns True
    password("pass@#1", min_special=1, special_chars="!", min_digit=0, min_upper=0, min_length=4) # returns False

ssn(ssn: str)
-------------

The ``ssn`` function validates a Social Security Number (SSN) string. The function returns ``True`` if the string is a valid SSN, and ``False`` otherwise.

Here's an example of how to use the ``ssn`` function:

.. code-block:: python

    from edify.library import ssn

    ssn('123-45-6789') # returns True
    ssn('123-45-678') # returns False
    ssn('123-45-67890') # returns False


mac(mac: str)
-------------

The ``mac`` function validates a MAC address (IEEE 802) string. The function returns ``True`` if the string is a valid MAC address, and ``False`` otherwise.

Here's an example of how to use the ``mac`` function:

.. code-block:: python

    from edify.library import mac

    mac('00:00:00:00:00:00') # returns True
    mac('00:00:00:00:00:0') # returns False
    mac('00:00:00:00:00:000') # returns False
