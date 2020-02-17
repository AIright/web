"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from blog import views

urlpatterns = (
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.last_requests, name='last_requests'),
    url(r'^login/', views.login_page, name='login'),
    url(r'^signup/', views.signup_page, name='signup'),
    url(r'^question/(?P<question_id>[0-9]+)', views.one_question, name='question'),
    url(r'^ask/', views.ask),
    url(r'^popular/', views.popular_requests),
    url(r'^new/', views.test, name='new')
)
