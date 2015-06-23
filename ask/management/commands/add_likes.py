# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from ask.models import Question, Answer, AnswerLikes, QuestionLikes
from django.contrib.auth.models import User
import random
from django.core.exceptions import ObjectDoesNotExist

def questionRatingCounting(questions):
    for q in questions:
        positive = QuestionLikes.objects.filter(question=q, like=True).count()
        #print('to question with id = ' + str(q.id)+ ' was generated ' + str(positive)+ ' positive likes')
        negative = QuestionLikes.objects.filter(question=q, like=False).count()
        #print('to question with id = ' + str(q.id)+ ' was generated ' + str(negative)+ ' negative likes')
        q.rating = positive - negative
        #print('question with id = ' + str(q.id)+ ' has rating ' + str(q.rating))
        q.save()

def answerRatingCounting(answers):
    for a in answers:
        positive = AnswerLikes.objects.filter(answer=a, like=True).count()
        #print('to answer with id = ' + str(a.id)+ ' was generated ' + str(positive)+ ' positive likes')
        negative = AnswerLikes.objects.filter(answer=a, like=False).count()
        #print('to answer with id = ' + str(a.id)+ ' was generated ' + str(negative)+ ' negative likes')
        a.rating = positive - negative
        #print('answer with id = ' + str(a.id)+ ' has rating ' + str(a.rating))
        a.save()

class Command(BaseCommand):

    def handle(self, *args, **options):
        (amount1, amount2) = args
        q_countLikes = int(amount1)
        a_countLikes = int(amount2)
        createdQuestionsLikes = 0
        createdAnswersLikes = 0
        countOfQuestions = Question.objects.count()
        countOfAnswers = Answer.objects.count()
        try:
            users = User.objects.all()
        except ObjectDoesNotExist:
            raise ObjectDoesNotExist("No users")
        if q_countLikes < 1:
            raise ValueError('incorrect parameter 1')
        if a_countLikes < 1:
            raise ValueError('incorrect parameter 2')
        if countOfQuestions == 0:
            raise ValueError('table of questions is empty. You must add questions!')
        if countOfAnswers == 0:
            raise ValueError('table of answers is empty. You must add answers!')
        firstQuestionID = Question.objects.first().id
        lastQuestionID = Question.objects.last().id
        firstAnswerID = Answer.objects.first().id
        lastAnswerID = Answer.objects.last().id
        iter=0
        for u in users:
            for i in range(q_countLikes):
                while True:
                   try:
                       q = Question.objects.get(id=random.randint(firstQuestionID, lastQuestionID))
                       break
                   except ObjectDoesNotExist:
                       continue
                like = bool(random.randint(0,1))
                like_U_Q = QuestionLikes(user=u, question=q, like=like)
                like_U_Q.save()
                createdQuestionsLikes+=1
            for i in range(a_countLikes):
                while True:
                    try:
                        a = Answer.objects.get(id=random.randint(firstAnswerID, lastAnswerID))
                        break
                    except ObjectDoesNotExist:
                        continue
                like = bool(random.randint(0,1))
                like_U_A = AnswerLikes(user=u, answer=a, like=like)
                like_U_A.save()
                createdAnswersLikes+=1
            iter+=1
            print(str(iter) + ' users set likes')
            # positive = QuestionLikes.objects.filter(user=u, like=True).count()
            # print('to user with id = ' + str(u.id)+ ' was generated ' + str(positive)+ ' likes')
            # negative = QuestionLikes.objects.filter(user=u, like=False).count()
            # print('to user with id = ' + str(u.id)+ ' was generated ' + str(negative)+ ' likes')
            # u.rating = positive - negative
            # print('user with id = ' + str(u.id)+ ' has rating ' + str(u.rating))
        questions=Question.objects.all()
        answers=Answer.objects.all()
        questionRatingCounting(questions)
        answerRatingCounting(answers)
        print('==============================================')
        print('was created : ' + str(createdQuestionsLikes) + ' likes User/Question')
        print('was created : ' + str(createdAnswersLikes) + ' likes User/Answer')

