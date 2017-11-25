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
from django.core import validators


class AskForm(forms.Form):
    title = forms.CharField(label='title', max_length=255)
    text = forms.CharField(label='question', widget=forms.Textarea)

    def clean_text(self):
        text = self.cleaned_data['text']
        # some validation logic
        return text

    def save(self):
        question = Question(**self.cleaned_data)
        question.save()
        return question


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['text', 'question']

    def clean_text(self):
        text = self.cleaned_data['text']
        # some validation logic
        return text

    def save(self):
        answer = Answer(**self.cleaned_data)
        answer.save()
        return answer

