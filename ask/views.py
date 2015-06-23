# -*- coding: utf-8 -*-
from django.http import HttpResponse, Http404
from django.shortcuts import render
from ask.models import *
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def getDataForQuestions(questions):
    data = {}
    i = 1
    for q in questions:
        answers = Answer.objects.filter(question_id=q.id).count()
        mas = {'question': q, 'tags': q.tags.all(), 'answers': answers}
        data[i] = mas
        i+=1
    return data



def hello(request):
    # render(request,'picture.html',{})
    return HttpResponse("Hello world! from views.py")

def postget(request):
    outp = """
        <form action = "/postget/" method="post">
            <label for="hello">Say hello!!!: </label>
			<input id="hello" type="str" name="hello" value=""><br>
        	<button type="submit">
				OK
			</button>
	    </form>
		%s
		"""
    if request.method == 'POST':
        param = request.POST['hello']
        outp = outp % ("You said :  " + str(param) + '\n')
        return HttpResponse(outp)
    return HttpResponse(outp)

def myHello(request):
    if request.method == 'GET':
        param = request.GET.get('param')
        return HttpResponse("Get " + str(param))

def main(request):
    typeOfSorting=''
    pageNumb = 1
    if request.method == 'GET':
        if 'page' in request.GET:
            pageNumb = request.GET['page']
        else:
            pageNumb = 1
        try:
            typeOfSorting = request.GET['sort']
        except:
            typeOfSorting = 'new'
        try:
            questionsBuf=Question.objects.all().order_by('title')
        except:
            raise Http404

        title='default'
        questionsBuf2 = questionsBuf
        if typeOfSorting=='best':
            questionsBuf2 = questionsBuf.order_by('-rating')
            title='Best questions'
        if typeOfSorting=='new':
            questionsBuf2 = questionsBuf.order_by('-createdDate')
            title='New questions'

        p=Paginator(questionsBuf2, 10)
        try:
            questions=p.page(pageNumb)
        except PageNotAnInteger:
            questions=p.page(1)
        except EmptyPage:
            questions=p.page(p.num_pages)

        data=getDataForQuestions(questions)
        context = {
            'questions': questions,
            'data': data,
            'title': title,
            'sort': typeOfSorting
        }
        return render(request, 'main.html', context)


def ask(request):
    return render(request, 'ask.html', {})


def question(request, pk):
    try:
        question = Question.objects.filter(id=pk).get()
        tags = question.tags.all()

    except ObjectDoesNotExist:
        raise Http404
    try:
        answersAll = Answer.objects.filter(question=question).order_by('-rating')
    except ObjectDoesNotExist:
        raise Http404
    try:
        pageNumb=request.GET['page']
    except:
        pageNumb=1
    p=Paginator(answersAll, 5)
    answers=p.page(pageNumb)
    context = {
        'question': question,
        'answers': answers,
        'tags': tags
    }
    return render(request, 'question.html', context)

def tag(request, tagID):
    try:
        tag=Tag.objects.get(id=tagID)
    except:
        raise Http404
    try:
        page = request.GET['page']
    except:
        page=1
    questionsBuf = tag.question_set.all().order_by('-rating')
    p = Paginator(questionsBuf, 3)
    try:
        questions = p.page(page)
    except PageNotAnInteger:
        questions=p.page(1)
    except EmptyPage:
        questions=p.page(p.num_pages)
    title = "Tag : " + tag.text
    data=getDataForQuestions(questions)
    context = {
            'questions': questions,
            'data': data,
            'title': title,
            'tagID': tagID
        }
    return render(request, 'main_tag.html', context)

def login(request):
    return render(request, 'login.html', {})

def register(request):
    return render(request, 'register.html', {})

def image(request):
    return render(request, 'image.html', {})