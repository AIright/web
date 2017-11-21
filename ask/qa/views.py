# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse, Http404
from qa.models import Question, Answer
from django.core.paginator import Paginator
import re


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


def one_question(request):
    a = re.split('/', request.get_full_path())
    question_object = get_object_or_404(Question, id=a[2])
    return render(request, 'html/one_question.html', {
        'question_object': question_object,
        'answers': Answer.objects.filter(question_id=a[2])
        })
    
    