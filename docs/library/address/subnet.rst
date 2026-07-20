subnet
======

A dotted-decimal IPv4 subnet mask is four octets, and each octet can only be one
of **nine values** — the bytes whose bits are a run of ones followed by a run of
zeros:

   ``255`` · ``254`` · ``252`` · ``248`` · ``240`` · ``224`` · ``192`` · ``128`` · ``0``

``subnet`` accepts exactly those, joined by dots. Anything else — an ordinary
address byte like ``1`` or ``168`` — is rejected:

.. edify-playground::
   :tests: 255.255.255.0|255.255.0.0|255.255.255.128|0.0.0.0|255.255.255.1|192.168.0.0

   from edify.library import subnet
   subnet

Each octet is an :func:`~edify.any_of` over those nine literals, and ``subnet``
uses four of them, so the emitted pattern just repeats the set four times. It
checks each octet **independently** — it does not verify the mask is *contiguous*,
so a byte-legal but nonsensical mask like ``255.0.255.0`` still matches. When you
want a prefix length rather than a dotted mask, use :doc:`cidr`.
