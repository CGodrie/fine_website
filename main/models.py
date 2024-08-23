from django.db import models
from django.contrib.auth.models import User

class Discussion(models.Model):
    users = models.ManyToManyField(User)

class Message(models.Model):
    discussion = models.ForeignKey(Discussion, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.content}'

    class Meta:
        ordering = ['sent_at']