from django.db import models
from django.utils import timezone


class Notice(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to="news/images/", null=True)
    url = models.URLField(blank=True)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.title}"
