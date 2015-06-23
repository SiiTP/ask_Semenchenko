# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from ask.models import Tag
import random

lowercase_rus = u'йцукенгшщзфывааоерипролдячсмитьукенгзвапроллдсмиткартинлоестаоие'

def randomWord(length):
    word = ''
    for i in range(length):
        word = word + random.choice(lowercase_rus)
    return word
class Command(BaseCommand):

    def handle(self, *args, **options):
            (amount,) = args
            count = int(amount)
            #EXCEPTIONS
            if count < 1:
                raise ValueError('incorrect parameter')
            #relations_q_t=0
            createdTags=0
            #generate tags
            for i in range(count):
                tag_text = randomWord(random.randint(3,7))
                t = Tag(text=tag_text)
                t.save()
                createdTags += 1
                print('was created : ' + str(createdTags) + ' tags')
            print('was created : ' + str(createdTags) + ' tags')