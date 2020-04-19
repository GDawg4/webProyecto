from django.db import models


class Parent(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return 'Este padre se llama', self.name
