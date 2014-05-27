from django.db import models
from django.contrib.auth.models import User
from django import forms
from goatnails.db.models import ImageWithThumbsField

class Article(models.Model):
    author = models.ForeignKey(User, related_name='wildstar+')
    title = models.CharField(max_length=50)
    text = models.TextField()
    creation_date = models.DateField(auto_now=True)
    def __unicode__(self):
        return self.title

class ArticleForm(forms.Form):
    title = forms.CharField(max_length=50)
    text  = forms.CharField(widget=forms.Textarea)

class Screenshot(models.Model):
    user = models.ForeignKey(User, related_name='wildstar+')
    caption = models.CharField(max_length=500, blank=True)
    creation_date = models.DateField(auto_now=True)
    image = ImageWithThumbsField(upload_to = "uploads", blank=True,
                                    sizes=((940,528),(200,200)))
    def __unicode__(self):
        return self.caption

class ScreenshotForm(forms.Form):
    caption = forms.CharField(max_length=500)
    img = forms.ImageField()

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)

