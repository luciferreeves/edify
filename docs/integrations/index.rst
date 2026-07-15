Integrations
============

Edify ships lightweight integration modules that let you drop a compiled
:class:`edify.Pattern` into the field-validation layers of the frameworks
most Python teams actually use. Each integration is an opt-in extra —
``pip install edify`` never pulls the framework in, and importing an
integration module never imports the framework at module load time. The
first helper call resolves the framework lazily; when the extra is
missing you get a clean :class:`edify.errors.integration.MissingIntegrationDependencyError`
with the exact install line to run.

Install any one, or all three:

.. code-block:: shell

    pip install 'edify[pydantic]'
    pip install 'edify[fastapi]'
    pip install 'edify[django]'
    pip install 'edify[all]'


Pydantic
--------

.. automodule:: edify.integrations.pydantic
    :members:


FastAPI
-------

.. automodule:: edify.integrations.fastapi
    :members:


Django
------

.. automodule:: edify.integrations.django
    :members:
