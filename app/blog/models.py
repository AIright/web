# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class PublicationManager(models.Manager):
    def new(self):
        return self.order_by('-added_at')

    def popular(self):
        return self.order_by('-rating')


class Publication(models.Model):
    """
    Publication:
    title - title content
    text - content of publication
    added_at - last update date
    rating - number of users who rated post
    author - user who published
    likes - users who rated
    """
    title = models.CharField(max_length=255)
    text = models.TextField(blank=True)
    added_at = models.DateTimeField(blank=True, auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    likes = models.ManyToManyField(User, blank=True, related_name='user_id')
    objects = PublicationManager()

    def __str__(self):
        return str(self.id)

    def get_url(self):
        return reverse('publication', kwargs={'publication_id': self.id})


class Comment(models.Model):
    """
    Answer:
    text - content
    added_at - last update
    publication - related publication
    author - user who posted the answer
    """
    text = models.TextField()
    added_at = models.DateTimeField(auto_now=True)
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    objects = models.Manager()
