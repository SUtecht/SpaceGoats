from django.db import models
import datetime
from django.utils import timezone
from django import forms
from django.forms.extras.widgets import SelectDateWidget



class Character(models.Model):
    name = models.CharField(max_length=100)
    player = models.ForeignKey('Player')
    server = models.CharField(max_length=100, blank=True)
    bnet = None
    def __unicode__(self):
        return "{} ".format(self.name)

class Player(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254, blank=True)
    def __unicode__(self):
        return "{} ".format(self.name)
    
    
class AttendForm(forms.Form):
    char = forms.ModelChoiceField(Character.objects.all())

        
class Event(models.Model):
    name = models.CharField(max_length=100)
    begin = models.DateField()
    attendees = models.ManyToManyField('Character', blank=True,null=True)
    def __unicode__(self):
        return "{} {}".format( self.name, self.begin)
        
class EventForm(forms.Form):
    name = forms.CharField(max_length=100)
    begin_date = forms.CharField( )	
    
class Rank(models.Model):
    name = models.CharField(max_length=100)
    level = models.IntegerField()
    def __unicode__(self):
        return "{} ".format( self.name)

class Article(models.Model):
    title = models.CharField(max_length=100)
    text  = models.TextField()
    img = models.ImageField(upload_to = "uploads")
    thumb = models.ImageField(upload_to = "uploads", blank=True,null=True)
    author = models.ForeignKey('Player')
    approved = models.CharField(max_length=1)
    def __unicode__(self):
        return "{} by {}  {} ".format( self.title , self.author , self.approved )

class ArticleForm(forms.Form):
    title = forms.CharField(max_length=100)
    text  = forms.CharField(widget=forms.Textarea)
    img = forms.ImageField()
    author = forms.ModelChoiceField(Player.objects.all())
