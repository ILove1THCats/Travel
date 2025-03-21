from django.db import models

class Location(models.Model):
    name = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
    description = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=255, blank=True, null=True) # Thêm danh mục

    def __str__(self):
        return self.name