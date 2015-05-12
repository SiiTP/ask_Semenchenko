from django.db import models
from django.contrib.auth.models import User
import datetime

class Question(models.Model):
    title = models.TextField()
    text = models.TextField()
    user = models.ForeignKey(User)
    createdDate = models.DateTimeField(default=datetime.datetime.now)




    def __unicode__(self):
        return self.title

class Answer(models.Model):
    question = models.ForeignKey(Question)
    text = models.TextField()