from django.db import models


class Baby(models.Model):
    name = models.CharField(max_length=100, null=True)
    parent = models.ForeignKey(
        'parents.Parent',
        on_delete=models.SET_NULL,
        null=True
    )
