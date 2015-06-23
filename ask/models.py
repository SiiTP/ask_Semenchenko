# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Tag(models.Model):
    text = models.TextField()

    def __unicode__(self):
        return self.text


class Question(models.Model):
    title = models.TextField()
    text = models.TextField()
    user = models.ForeignKey(User)
    rating = models.IntegerField(default=0)
    createdDate = models.DateTimeField(default=timezone.now())
    tags = models.ManyToManyField(Tag)

    def __unicode__(self):
        return self.title

class Answer(models.Model):
    question = models.ForeignKey(Question)
    text = models.TextField()
    author = models.ForeignKey(User)
    createdData = models.DateTimeField(default=timezone.now())
    isRight = models.BooleanField(default=False)
    rating = models.IntegerField(default=0)

    def __unicode__(self):
        return self.text

class UserProfile (models.Model):
    user = models.OneToOneField(User)
    rating = models.IntegerField(default=0)
    avatar = models.ImageField(upload_to='/uploads/avatars/')

class QuestionLikes(models.Model):
    user = models.ForeignKey(User)
    question = models.ForeignKey(Question)
    like = models.BooleanField(default=True) # 1 - like; 0 - dislike

class AnswerLikes(models.Model):
    user = models.ForeignKey(User)
    answer = models.ForeignKey(Answer)
    like = models.BooleanField(default=True) # 1 - like; 0 - dislike
