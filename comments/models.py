from django.db import models

class Comment(models.Model):
    author = models.CharField(
        verbose_name="автор",
        max_length=100
    )
    text = models.TextField(
        verbose_name="текст комментария",
        max_length=1000
    )
    likes = models.IntegerField(
        default=0,
        verbose_name="количество лайков"
    )
    dislikes = models.IntegerField(
        default=0,
        verbose_name="количество дизлайков"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="дата создания"
    )
    parent = models.ForeignKey(
        'self', null=True, blank=True, on_delete=models.CASCADE
    )

    def __str__(self):
        return self.text
