from django.db import models
from django.contrib.auth.models import User
from django import forms
from goatnails.db.models import ImageWithThumbsField


class Character(models.Model):
    name = models.CharField(max_length=100)
    player = models.ForeignKey(User)
    server = models.CharField(max_length=100, blank=True)
    class_name = models.CharField(max_length=15)
    ilvl = models.IntegerField()
    level = models.IntegerField()
    def __unicode__(self):
        return "{} ".format(self.name)

class Player(models.Model):
    user = models.OneToOneField(User)
    main = models.ForeignKey('Character', related_name='main_character')
    def __unicode__(self):
        return "{} ".format(self.user.username)

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)

class NewUserForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)
    email = forms.CharField(max_length=100)
    secret_word = forms.CharField(max_length=100)
    character = forms.CharField(max_length=100)
    server = forms.CharField(max_length=100, initial='Auchindoun')
    
class NewCharacterForm(forms.Form):
    name = forms.CharField(max_length=100)
    server = forms.CharField(max_length=100, initial='Auchindoun')

class AttendForm(forms.Form):
    char = forms.ModelChoiceField(Character.objects.all())
        
class Event(models.Model):
    name = models.CharField(max_length=100)
    begin = models.DateTimeField()
    def __unicode__(self):
        return "{} {}".format( self.name, self.begin)

class Event_Attendee(models.Model):
    event = models.ForeignKey('Event')
    character =  models.ForeignKey('Character')
    role = models.ForeignKey('Role')
    class Meta :
        unique_together = (('event', 'character'),)

        
class EventForm(forms.Form):
    name = forms.CharField(max_length=100)
    begin_date = forms.CharField( ) 
    
class Role(models.Model):
    name = models.CharField(max_length=10)
    img = models.ImageField(upload_to = "uploads")
    def __unicode__(self):
        return "{} ".format(self.name)
  
class AttendForm(forms.Form):
    role = forms.ModelChoiceField(Role.objects.all())
    def __init__(self, user, *args, **kwargs):
        super(AttendForm, self).__init__(*args, **kwargs)
        self.fields['char'] = forms.ChoiceField(choices=[ (o.id, str(o)) for o in Character.objects.filter(player=user)])

  
class Rank(models.Model):
    name = models.CharField(max_length=100)
    level = models.IntegerField()
    def __unicode__(self):
        return "{} ".format( self.name)

class Article(models.Model):
    title = models.CharField(max_length=100)
    text  = models.TextField()
    # img = models.ImageField(upload_to = "uploads")
    img = ImageWithThumbsField(upload_to = "uploads", 
                               sizes=((128,128), (200,200)))
    author = models.ForeignKey(User)
    approved = models.BooleanField(default=False)
    creation_date = models.DateField()
    def __unicode__(self):
        return "{} by {}  {} ".format( self.title , self.author , self.approved )

class ArticleForm(forms.Form):
    title = forms.CharField(max_length=100)
    text  = forms.CharField(widget=forms.Textarea)
    img = forms.ImageField()
    
class Goat_of_the_Week(models.Model):
    name =  models.ForeignKey('Character')
    creation_date = models.DateField()
    img = ImageWithThumbsField(upload_to = "uploads", 
                               sizes=((128,128), (200,200)))
    desc = models.TextField()
    
class Goat_of_the_Week_Form(forms.Form):
    name = forms.ModelChoiceField(Character.objects.all())
    img = forms.ImageField()
    desc  = forms.CharField(widget=forms.Textarea)

