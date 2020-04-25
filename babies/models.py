from django.db import models


class Baby(models.Model):
    name = models.CharField(max_length=100, null=True)
    parent = models.ForeignKey(
        'parents.Parent',
        related_name='babies',
        on_delete=models.CASCADE,
        #null=True
    )

    def __str__(self):
        return 'This child is named {} and its parent is {}'.format(self.name, self.parent.name)
