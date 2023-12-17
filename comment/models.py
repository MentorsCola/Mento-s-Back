from django.db import models
from nicknames.models import Nicknames


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    board = models.ForeignKey('board.Board', on_delete=models.CASCADE, related_name='comments', null=True)
    content = models.TextField("댓글 내용", null=False)
    nickname_commend = models.ForeignKey(Nicknames, on_delete=models.CASCADE)

    def __str__(self):
        return f"Comment #{self.id} for Board #{self.board_id}"