from django.db import models


class delo(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(null=True, blank=True)
    time = models.DateTimeField(null=True)
    importance = models.SmallIntegerField(null=True)

# Create your models here.
