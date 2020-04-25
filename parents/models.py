from django.db import models


class Parent(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return 'This parent is named {}'.format(self.name)
