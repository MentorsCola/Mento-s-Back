from django.db import models


class Tag(models.Model):
    tag_content = models.CharField("Tag Content", max_length=255, unique=True)

    def __str__(self):
        return self.tag_content