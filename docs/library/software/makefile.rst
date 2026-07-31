Makefile
========

A `makefile <https://www.gnu.org/software/make/manual/make.html>`__ rule names a
target, a colon, and the prerequisites it depends on — ``build: deps``. **Makefile**
matches that rule line.

The construction is an :meth:`~edify.RegexBuilder.optional` leading ``.`` for special
targets such as ``.PHONY``, a :meth:`~edify.RegexBuilder.letter`-led target name,
then :meth:`~edify.RegexBuilder.zero_or_more` further whitespace-separated targets,
optional whitespace, and the ``:``.

Rule lines
----------

.. edify-playground::

   from edify.library import makefile

   makefile("all:")                    # a target with no prerequisites
   makefile("build: deps")             # one prerequisite
   makefile("test: build lint")        # several
   makefile(".PHONY: all clean")       # a special target
   makefile("install : build")         # space before the colon

The colon is required
---------------------

A recipe line — the tab-indented command under a rule — is not a rule:

.. edify-playground::

   from edify.library import makefile

   makefile("build: deps")   # a rule
   makefile("\tgcc -o x x.c")  # a recipe line
   makefile("build")          # no colon
   makefile("")               # empty

This matches the rule header only. Variable assignments, conditionals, and the
tab-versus-spaces requirement for recipe lines — the classic makefile error — are
outside its scope.
