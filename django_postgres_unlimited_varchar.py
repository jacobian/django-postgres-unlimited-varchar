__version__ = "1.1.0"

from django.db import models


class UnlimitedCharField(models.CharField):
    def __init__(self, *args, **kwargs):
        # not a typo: we want to skip CharField.__init__ because that adds the max_length validator
        super(models.CharField, self).__init__(*args, **kwargs)

    def check(self, **kwargs):
        # likewise, want to skip CharField.__check__
        return super(models.CharField, self).check(**kwargs)

    def db_type(self, connection):
        return "varchar"
