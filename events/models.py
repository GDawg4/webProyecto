from django.db import models
import datetime

class Event(models.Model):
    title = models.CharField(max_length=80, null=True, blank=False)
    notes = models.CharField(max_length=500)
    date = datetime.datetime.now()
    baby = models.ForeignKey(
        'babies.Baby',
        related_name='events',
        on_delete=models.SET_NULL,
        null=True
    )

    def __str__(self):
        return 'This event is from {},it started {} and has {} title with {} notes'.\
            format(self.baby.name, self.date, self.title, self.notes)
