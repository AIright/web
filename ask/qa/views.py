# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseNotAllowed, HttpResponseRedirect
from qa.models import Question, Answer
from django.core.paginator import Paginator
from qa.forms import AskForm, AnswerForm, LoginForm, SignupForm
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login


def test(request, *args, **kwargs):
    return HttpResponse('OK')


# Return login page if request method is GET
# Authorization as user if POST
def login_page(request):
    if request.method == 'GET':
        return render(request, 'html/login_page.html', {
            'login_form': LoginForm,
            'message': ''
        })
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            return render(request, 'html/login_page.html', {
                'login_form': LoginForm,
                'message': 'Invalid login/password'
            })
    else:
        raise HttpResponseNotAllowed


# Return signup page if request method is GET
# Create new user, authorize as new user, redirect on the main page
def signup_page(request):
    if request.method == 'GET':
        return render(request, 'html/signup_page.html', {
            'signup_form': SignupForm,
            'message': ''
        })
    elif request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            try:
                form.save()
                user = authenticate(request, username=username, password=password)
                login(request, user)
                return HttpResponseRedirect('/')
            except:
                message = 'Already in use'
                return render(request, 'html/signup_page.html', {
                    'signup_form': SignupForm,
                    'message': message
                })
        else:
            message = 'Invalid login/password/email'
            return render(request, 'html/signup_page.html', {
                'signup_form': SignupForm,
                'message': message
            })
    else:
        raise HttpResponseNotAllowed


# Return last requests with Question model method 'new()'
# paginator is used with 10 items on the page
def last_requests(request):
    page = request.GET.get('page', 1)
    try:
        int(page)
        questions = Question.objects.new()
        limit = request.GET.get('limit', 10)
        paginator = Paginator(questions, limit)
        paginator.baseurl = '?page='
        page = paginator.page(page)
        return render(request, 'html/last_requests.html', {
            'questions': page.object_list,
            'paginator': paginator, 'page': page,
        })
    except:
        raise Http404


# Return popular requests with Question model method 'popular()'
# paginator is used with 10 items on the page
def popular_requests(request):
    page = request.GET.get('page', 1)
    try:
        int(page)
        questions = Question.objects.popular()
        limit = request.GET.get('limit', 10)
        paginator = Paginator(questions, limit)
        paginator.baseurl = '?page='
        page = paginator.page(page)
        return render(request, 'html/popular_requests.html', {
            'questions': page.object_list,
            'paginator': paginator, 'page': page,
        })                                                            
    except:
        raise Http404


# Return question page with answers if GET method is used
# Add question and redirect on question page with that answer if
# POST method is used
@csrf_protect
def one_question(request, question_id):
    question_object = get_object_or_404(Question, id=question_id)
    if request.method == 'GET':
        return render(request, 'html/one_question.html', {
            'question_object': question_object,
            'answers': Answer.objects.filter(question_id=question_id),
            'answer_form': AnswerForm(initial={'question': question_id})
        })
    elif request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            form._author = request.user
            form.save()
            question_object = Question.objects.get(id=form['question'].value())
            url = question_object.get_url()
            return HttpResponseRedirect(url)
        else:
            return render(request, 'html/one_question.html', {
                'question_object': question_object,
                'answers': Answer.objects.filter(question_id=question_id),
                'answer_form': AnswerForm(initial={'question': question_id})
            })
    else:
        raise HttpResponseNotAllowed


# Return page with question create page if GET
# Add question and redirect on the page with that question
@csrf_protect
def ask(request):
    if request.method == 'GET':
        return render(request, 'html/ask_form.html', {
            'ask_form': AskForm
        })

    elif request.method == 'POST':
        form = AskForm(request.POST)
        if form.is_valid():
            form._author = request.user
            question = form.save()
            url = question.get_url()
            return HttpResponseRedirect(url)
    else:
        raise HttpResponseNotAllowed
