from django.db import models
from nicknames.models import Nicknames
from tag.models import Tag
from user.models import User


class Board(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField("제목", max_length=50, null=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='boards')
    content = models.TextField("내용", null=False)
    dt_created = models.DateTimeField("작성일", auto_now_add=True, null=False)
    dt_modified = models.DateTimeField("수정일", auto_now=True, null=False)
    nickname_author = models.ForeignKey(Nicknames, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, related_name='boards', blank=True)

    def __str__(self):
        return self.title

    def likes_count(self):
        return self.likes.count()