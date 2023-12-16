from django.db import models

from comment.models import Comment
from nicknames.models import Nicknames
from user.models import User


class Board(models.Model):  # 제목, 작성자, 내용, 작성일, 마지막 수정일
    id = models.AutoField(primary_key=True)
    title = models.CharField("제목", max_length=50, null=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='boards')
    content = models.TextField("내용", null=False)
    dt_created = models.DateTimeField("작성일", auto_now_add=True, null=False)
    dt_modified = models.DateTimeField("수정일", auto_now=True, null=False)
    nickname_author = models.ForeignKey(Nicknames, on_delete=models.CASCADE)
    comments = models.ManyToManyField(Comment, null=True)

    def __str__(self):
        return self.title

    def likes_count(self):
        return self.likes.count()
