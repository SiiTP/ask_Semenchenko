# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from ask.models import UserProfile
from django.contrib.auth.models import User
import random

lowercase_rus = u'йцукенгшщзфывааоерипролдячсмитьукенгзвапроллдсмиткартинлоестаоие'

def randomWord(length):
    word = ''
    for i in range(length):
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
        createdProfiles = 0
        (amount,) = args
        count = int(amount)
        #EXCEPTIONS
        if count < 1:
            raise ValueError('incorrect parameter')
        # generate users
        for i in range(count):
            nick = randomWord(random.randint(4,9))
            is_act = random.randint(0,1)
            fName = randomWord(random.randint(4,8))
            lName = randomWord(random.randint(6,10))
            u = User(username = nick, password = '', is_active = bool(is_act), first_name = fName, last_name = lName)
            u.save()
            u_p = UserProfile(user=u, rating=random.randint(-100,100), avatar='ivan.jpeg')
            u_p.save()
            createdProfiles += 1
        print('==============================================')
        print('was created : ' + str(createdProfiles) + ' users')