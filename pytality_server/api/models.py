from django.contrib.postgres.fields import JSONField
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models import TextField, CharField, IntegerField, BooleanField


class Snippet(models.Model):
    incorrect_code = TextField(null=False, blank=False)
    correct_code = TextField(null=False, blank=False)
    task_title = CharField(null=False, max_length=256)
    time_to_solve = IntegerField(null=False,
                                 default=5,
                                 validators=[MinValueValidator(1),
                                             MaxValueValidator(30)])
    input_schema = JSONField(null=True)
    used_in_current_rotation = BooleanField(default=False, null=False)
