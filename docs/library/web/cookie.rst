Cookie
======

An HTTP `cookie <https://datatracker.ietf.org/doc/html/rfc6265>`__ (:rfc:`6265`) is a
``name=value`` pair. **Cookie** matches that single pair — the name from the token
alphabet, then ``=``, then a value that runs up to the first semicolon or space.

The name is :meth:`~edify.RegexBuilder.one_or_more` of letters, digits, ``_``, and
``-``. The value uses :meth:`~edify.RegexBuilder.assert_not_ahead` over whitespace
and ``;`` — consuming any character that is not a delimiter, which is precisely where
a cookie value ends.

Name and value
--------------

.. edify-playground::

   from edify.library import cookie

   cookie("sessionid=abc123")        # a session cookie
   cookie("theme=dark")              # a preference
   cookie("_ga=GA1.2.123456789")     # an underscore-led name
   cookie("csrf-token=aBcDeF")       # a hyphen in the name

One pair, without attributes
----------------------------

This is the important limitation: a ``Set-Cookie`` header appends attributes after
the pair, and those are *not* part of what this matches. Split them off first:

.. edify-playground::

   from edify.library import cookie

   cookie("sessionid=abc123")                    # the pair alone
   cookie("sessionid=abc123; Path=/; HttpOnly")  # with attributes
   cookie("name=value; Secure")                  # likewise
   cookie("noequals")                            # no separator
   cookie("")                                    # empty

Validating the pair says nothing about the cookie's safety. The protections that
matter — ``HttpOnly``, ``Secure``, ``SameSite`` — live in the attributes this
deliberately excludes, and a session identifier in the value should also satisfy
:doc:`../auth/session`.
