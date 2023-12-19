from django.db import models


class Tag(models.Model):
    tags = models.CharField(max_length=255, verbose_name='태그명')

    def __str__(self):
        return self.tags
