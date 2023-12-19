from django.db import models
from django.contrib.auth.models import User

from Mentos import settings
from board.models import Board


class Report(models.Model):
    reporter = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)

    def __str__(self):
        return f"Report #{self.id} - {self.reporter.username} on {self.board.title}"