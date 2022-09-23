from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=300, null=True, blank=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['complete']
