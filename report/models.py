from django.db import models

from board.models import Board
from user.models import User


class Report(models.Model):
    reporter = models.ForeignKey(User, on_delete=models.CASCADE)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)

    def __str__(self):
        return f"Report #{self.id} - {self.reporter.username} on {self.board.title}"