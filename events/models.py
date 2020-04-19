from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=80, null=True, blank=False)
    notes = models.CharField(max_length=500)
    date = models.DateTimeField
    baby = models.ForeignKey(
        'babies.Baby',
        on_delete=models.SET_NULL,
        null=True
    )
