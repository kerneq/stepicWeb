from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class QuestionManager(models.Manager):
    def new(self):
        return Question.objects.order_by('-added_at')[0]

    def popular(self):
        return Question.objects.order_by('rating')


class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateField(auto_now_add=True)
    rating = models.IntegerField()
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='+')
    likes = models.ManyToManyField(User)
    objects = QuestionManager()


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateField(auto_now_add=True)
    question = models.ForeignKey(Question, on_delete=models.SET_NULL, null=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
