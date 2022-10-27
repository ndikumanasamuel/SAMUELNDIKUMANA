from django.db import models


class Words(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=2000)
    image = models.CharField(max_length=2083)
