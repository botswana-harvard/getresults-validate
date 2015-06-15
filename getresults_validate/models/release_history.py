from django.db import models

from simple_history.models import HistoricalRecords

from edc_base.model.models import BaseUuidModel


class ReleaseHistory(BaseUuidModel):

    order_identifier = models.CharField(
        max_length=25)

    validation_reference = models.CharField(
        max_length=25)

    reference_range = models.CharField(
        max_length=25)

    grading = models.CharField(
        max_length=25,
        null=True)

    panel_name = models.CharField(
        max_length=25)

    release_datetime = models.DateTimeField()

    operator = models.CharField(
        max_length=25)

    history = HistoricalRecords()

    def __str__(self):
        return '{}: {}'.format(self.utestid_name, self.validation_reference)

    class Meta:
        app_label = 'getresults_validate'
        db_table = 'getresults_releasehistory'
