# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from ask.models import Question, Tag
from django.contrib.auth.models import User
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
        createdQuestions = 0
        createdRelations_q_t = 0
        (amount,) = args
        count = int(amount)
        countOfUsers = User.objects.count()
        countOfTags = Tag.objects.count()
        if count < 1:
            raise ValueError('incorrect parameter')
        if countOfUsers < 2:
            raise ValueError('table of users is empty. You must add users!')
        if countOfTags < 1:
            raise ValueError('table of tags is empty. You must add tags!')

        firstUser = User.objects.first().id
        lastUser = User.objects.last().id

        #generate questions
        for i in range(count):
            while True:
                try:
                    u = User.objects.get(id=random.randint(firstUser + 1, lastUser)) #without admin user
                    # print('user was founded : ' + str(u.id))
                    break
                except ObjectDoesNotExist:
                    continue

            title = randomText(random.randint(1, 4)) + '?'
            text = randomText(random.randint(5, 30)) + '?'
            q = Question(title=title, text=text, user=u, rating=0)
            firstTagID = Tag.objects.first().id
            lastTagID = Tag.objects.last().id
            amountTags = random.randint(1,5)
            q.save()
            for i in range(amountTags):
                while True:
                     try:
                         t = Tag.objects.get(id=random.randint(firstTagID, lastTagID))
                         #print('question was founded : ' + str(q.id))
                         break
                     except ObjectDoesNotExist:
                         #print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!incorrect question was generated')
                         continue
                q.tags.add(t)
                createdRelations_q_t+=1
                q.save()
            createdQuestions+=1
            print('was created : ' + str(createdQuestions) + ' questions')
        print('==============================================')
        print('was created : ' + str(createdQuestions) + ' questions')
        print('was created : ' + str(createdRelations_q_t) + ' relations question_tag')

