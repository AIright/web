"""
AskForm - форма добавления вопроса
title - поле заголовка
text - поле текста вопроса

AnswerForm - форма добавления ответа
text - поле текста ответа
question - поле для связи с вопросом
"""

from django import forms
from qa.models import Question, Answer
from django.contrib.auth.models import User


class SignupForm(forms.Form):
    username = forms.CharField(label='username', max_length=32)
    email = forms.EmailField(label='email', required=True)
    password = forms.CharField(label='password', widget=forms.PasswordInput)

    def save(self):
        user = User.objects.create_user(**self.cleaned_data)
        user = user.save()
        return user


class LoginForm(forms.Form):
    username = forms.CharField(max_length=32, required=True)
    password = forms.CharField(widget=forms.PasswordInput)


class AskForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'text']
        _author = ''

    def clean_text(self):
        text = self.cleaned_data['text']
        # some validation logic
        return text

    def save(self):
        self.cleaned_data['author'] = self._author
        question = Question(**self.cleaned_data)
        question.save()
        return question


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['text', 'question']
        _author = ''

    def clean_text(self):
        text = self.cleaned_data['text']
        # some validation logic
        return text

    def save(self):
        self.cleaned_data['author'] = self._author
        answer = Answer(**self.cleaned_data)
        answer.save()
        return answer

