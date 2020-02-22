# -*- coding: utf-8 -*-
import logging
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseBadRequest, HttpResponseNotAllowed, HttpResponseRedirect
from .models import Publication, Comment
from django.core.paginator import Paginator
from .forms import PublicationForm, CommentForm, LoginForm, SignupForm
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login


logger = logging.getLogger(__name__)


def test(request, *args, **kwargs):
    return HttpResponse('OK')


# Return login page if request method is GET
# Authorization as user if POST
def login_page(request):
    if request.method == 'GET':
        return render(request, 'login_page.html', {
            'login_form': LoginForm,
            'message': ''
        })
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
        else:
            raise HttpResponseBadRequest

        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/popular')
        else:
            return render(request, 'login_page.html', {
                'login_form': LoginForm,
                'message': 'Invalid login/password'
            })
    else:
        raise HttpResponseNotAllowed


# Return signup page if request method is GET
# Create new user, authorize as new user, redirect on the main page
def signup_page(request):
    if request.method == 'GET':
        return render(request, 'signup_page.html', {
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
                return HttpResponseRedirect('/login')
            except:
                message = 'Already in use'
                return render(request, 'signup_page.html', {
                    'signup_form': SignupForm,
                    'message': message
                })
        else:
            message = 'Invalid login/password/email'
            return render(request, 'signup_page.html', {
                'signup_form': SignupForm,
                'message': message
            })
    else:
        raise HttpResponseNotAllowed


# Return last requests with Publication model method 'new()'
# paginator is used with 10 items on the page
def last_requests(request):
    page = request.GET.get('page', 1)
    try:
        int(page)
        publications = Publication.objects.new()
        limit = request.GET.get('limit', 10)
        paginator = Paginator(publications, limit)
        paginator.baseurl = '?page='
        page = paginator.page(page)
        return render(request, 'last_requests.html', {
            'publications': page.object_list,
            'paginator': paginator, 'page': page,
        })
    except:
        raise Http404


# Return popular requests with Publication model method 'popular()'
# paginator is used with 10 items on the page
def popular_requests(request):
    page = request.GET.get('page', 1)
    try:
        page = int(page)
        publications = Publication.objects.popular()
        limit = request.GET.get('limit', 10)
        paginator = Paginator(publications, limit)
        paginator.baseurl = '?page='
        page = paginator.page(page)
        return render(request, 'popular_requests.html', {
            'publications': page.object_list,
            'paginator': paginator, 'page': page,
        })                                                            
    except:
        raise Http404


# Return publications page with comments if GET method is used
# Add publication and redirect on publication page with that comment if
# POST method is used
@csrf_protect
def one_publication(request, publication_id):
    publication_object = get_object_or_404(Publication, id=publication_id)
    if request.method == 'GET':
        return render(request, 'one_publication.html', {
            'publication_object': publication_object,
            'comments': Comment.objects.filter(publication_id=publication_id),
            'comment_form': CommentForm(initial={'publication': publication_id})
        })
    elif request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form._author = request.user
            form.save()
            publication_object = Publication.objects.get(id=publication_id)
            url = publication_object.get_url()
            return HttpResponseRedirect(url)
        else:
            return render(request, 'one_publication.html', {
                'publication_object': publication_object,
                'comments': Comment.objects.filter(publication_id=publication_id),
                'comment_form': CommentForm(initial={'publication': publication_id})
            })
    else:
        raise HttpResponseNotAllowed


# Return page with publication create page if GET
# Add publication and redirect on the page with that publication
@csrf_protect
def publish(request):
    if request.method == 'GET':
        return render(request, 'create_publication_form.html', {
            'publication_form': PublicationForm
        })

    elif request.method == 'POST':
        form = PublicationForm(request.POST)
        if form.is_valid():
            form._author = request.user
            publication = form.save()
            url = publication.get_url()
            return HttpResponseRedirect(url)
    else:
        raise HttpResponseNotAllowed
