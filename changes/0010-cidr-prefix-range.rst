[change]
anchor = cidr-prefix-range
heading = atoms.cidr range-checks the prefix length
before = atoms.cidr  ->  "10.0.0.0/33" matches
after = atoms.cidr  ->  "10.0.0.0/33" does not match
context = The prefix length is validated against the range 0-32 instead of being
    matched as one or two digits, so /33 through /99 no longer match. The address
    half is unchanged, and edify.library.cidr already behaved this way. If you
    relied on the looser shape, match the prefix yourself with an explicit
    quantifier after the address.
