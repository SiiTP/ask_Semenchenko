# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from ask.models import Question, Answer, User
import random
from django.core.exceptions import ObjectDoesNotExist

lowercase_rus = u'йцукенгшщзфывааоерипролдячсмитьукенгзвапроллдсмиткартинлоестаоие'

def randomWord(length):
    word = ''
    for i in range(length):
        # print('in random')
        # print(lowercase_rus[1])
        word = word + random.choice(lowercase_rus)
    return word

def randomText(length):
    text = ''
    for i in range(length - 1):
        text = text + randomWord(random.randint(1,9)) + ' '
    text = text + randomWord(random.randint(1,9))
    return text

class Command(BaseCommand):

    def handle(self, *args, **options):
        (amount,) = args
        count = int(amount)
        countOfQuestions = Question.objects.count()
        #EXCEPTIONS
        if count < 1:
            raise ValueError('incorrect parameter')
        if countOfQuestions == 0:
            raise ValueError('table of questions is empty. You must add questions!')

        firstQuestionID = Question.objects.first().id
        lastQuestionID = Question.objects.last().id
        firstUserID = User.objects.first().id
        lastUserID = User.objects.last().id
        createdAnswers=0
        #generate answers
        for i in range(count):
            while True:
                try:
                    q = Question.objects.get(id=random.randint(firstQuestionID , lastQuestionID))
                    break
                except ObjectDoesNotExist:
                    continue

            while True:
                try:
                    u = User.objects.get(id=random.randint(firstUserID + 1, lastUserID)) #without admin user
                    break
                except ObjectDoesNotExist:
                    continue

            a_text = randomText(random.randint(3,30))
            answ = Answer(question = q, text = a_text, author=u, isRight=bool(random.randint(0,1)), rating=0)
            answ.save()
            createdAnswers+=1
            print('was created : ' + str(createdAnswers) + ' answers')
        print('==============================================')
        print('was created : ' + str(createdAnswers) + ' answers')



    # question = models.ForeignKey(Question)
    # text = models.TextField()
    # author = models.ForeignKey(User)
    # createdData = models.DateTimeField(default=timezone.now())
    # isRight = models.BooleanField(default=False)
    # rating = models.IntegerField(default=0)