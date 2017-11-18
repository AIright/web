# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User


"""
Question - вопрос
title - заголовок вопроса
text - полный текст вопроса
added_at - дата добавления вопроса
rating - рейтинг вопроса (число)
author - автор вопроса
likes - список пользователей, поставивших "лайк"
"""


class QuestionManager(models.Manager):
    def new(self):
        from django.db import connection
        return Question.object.order_by('date')[0:5].get()

    def popular(self):
        return Question.object.order_by('rating')


class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField(blank=True, auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, blank=True, related_name='user_id')
    objects = QuestionManager()


"""
Answer - ответ
text - текст ответа
added_at - дата добавления ответа
question - вопрос, к которому относится ответ
author - автор ответа
"""


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(auto_now=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)






