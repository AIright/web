# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseNotAllowed, HttpResponseRedirect
from qa.models import Question, Answer
from django.core.paginator import Paginator
from qa.forms import AskForm, AnswerForm
from django.views.decorators.csrf import csrf_protect


def test(request, *args, **kwargs):
    return HttpResponse('OK')


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


@csrf_protect
def one_question(request, question_id):
    question_object = get_object_or_404(Question, id=question_id)
    if request.method == 'GET':
        form = AnswerForm(initial={'question': question_id})
        return render(request, 'html/one_question.html', {
            'question_object': question_object,
            'answers': Answer.objects.filter(question_id=question_id),
            'answer_form': form
        })
    elif request.method == 'POST':
        form = AnswerForm(request.POST)
        print('lol' + form['question'].value())
        if form.is_valid():
            form.save()
            question_object = Question.objects.get(id=form['question'].value())
            url = question_object.get_url()
            return HttpResponseRedirect(url)
    else:
        raise HttpResponseNotAllowed


@csrf_protect
def ask(request):
    if request.method == 'GET':
        return render(request, 'html/ask_form.html', {
            'ask_form': AskForm
        })

    elif request.method == 'POST':
        form = AskForm(request.POST)
        if form.is_valid():
            question = form.save()
            url = question.get_url()
            return HttpResponseRedirect(url)
    else:
        raise HttpResponseNotAllowed
    
    