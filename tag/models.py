from django.db import models

from board.models import Board


class Tag(models.Model):
    id = models.AutoField(primary_key=True)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    tag_content = models.TextField("tag", null=False)

    def __str__(self):
        return self.tag_content
