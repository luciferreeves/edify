YAML
====

A `YAML <https://yaml.org/spec/1.2.2/>`__ document is whitespace-significant, which
makes it impossible to validate fully with a regular expression — but its *opening*
is distinctive. **YAML** recognises the four ways a document can begin: the ``---``
document marker, a ``#`` comment, a ``- `` sequence item, or a ``key:`` mapping
entry.

Those four are the branches of an :func:`~edify.any_of`. The mapping branch is the
subtle one: a key made of word characters, spaces, dots, hyphens, or quotes,
followed by a colon that must itself be followed by whitespace or the end of the
line — the rule that separates ``key: value`` from a bare URL like
``https://example.com``.

Mappings
--------

The most common opening, including nested and quoted keys:

.. edify-playground::

   from edify.library import yaml

   yaml("key: value")
   yaml("name: Ada\nrole: admin")
   yaml("nested:\n  a: 1\n  b: 2")
   yaml('title: "quoted value"')

Sequences, markers, and comments
--------------------------------

A document may start with its list, an explicit start marker, or a comment:

.. edify-playground::

   from edify.library import yaml

   yaml("- one\n- two")           # a sequence
   yaml("---\nkey: value")        # the document marker
   yaml("---")                    # a marker alone
   yaml("# a comment\nkey: v")    # a leading comment

What the opening rules out
--------------------------

A bare scalar or a document in another format does not open like YAML — even though
YAML technically permits a lone scalar, accepting one would make the validator match
nearly any text:

.. edify-playground::

   from edify.library import yaml

   yaml("hello-world")   # a bare scalar
   yaml("42")            # a bare number
   yaml('{"a": 1}')      # JSON flow style is not matched
   yaml("<root/>")       # XML

Because indentation carries meaning in YAML, this checks how a document begins
rather than that its structure is consistent — parse it before trusting it. For the
strict-superset relationship, see :doc:`json`; for the configuration formats that
replaced YAML in some tools, :doc:`toml` and :doc:`ini`.
