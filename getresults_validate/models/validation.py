from uuid import uuid4

from django.db import models

from edc_base.model.models import BaseUuidModel, HistoricalRecords

from ..choices import VALIDATION_OPTIONS


class Validation(BaseUuidModel):
    """Model to track validtion reference per result item in a result."""

    order_identifier = models.CharField(
        max_length=25)

    panel_name = models.CharField(
        max_length=25)

    utestid_name = models.CharField(
        max_length=25,
        null=True)

    validation_reference = models.CharField(
        max_length=36,
        default=uuid4)

    validation = models.CharField(
        max_length=25,
        choices=VALIDATION_OPTIONS)

    validation_comment = models.CharField(
        max_length=25,
        null=True)

    validation_datetime = models.DateTimeField()

    operator = models.CharField(
        max_length=25)

    history = HistoricalRecords()

    def __str__(self):
        return '{}: {}'.format(self.utestid_name, self.validation_reference)

    class Meta:
        app_label = 'getresults_validate'
        db_table = 'getresults_validation'
