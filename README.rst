A tiny app adding support unlimited ``varchar`` fields (no specified max length) in Django/Postgres.

Usage::

    from django.db import models
    from django_postgres_unlimited_varchar import UnlimitedCharField

    class Person(models.Model):
        name = UnlimitedCharField()
        ...

Why?

Out of the box, Django has two fields for text:

* ``CharField``, which is for single-line text, and has a required maximum length (the ``max_length`` argument). In the database, this creates a field of type ``varchar(LENGTH)``.
* ``TextField``, which is for multi-line text, and has no maximum length. In the database, this creates a field of type ``text``.

Clearly missing is a third type: single-line, no max length. Postgres supports this as the ``varchar`` type (note the lack of a length).

This field adds that type. AFAIK there isn't any performance hit in using this, so it's suitable for any situation where there isn't a clear required max length.
